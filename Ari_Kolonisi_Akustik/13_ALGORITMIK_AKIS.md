# Algoritmik Akış (Kaba Kod)

Kodlar yöntemi anlatan taslaktır. Pencere uzunlukları ve bant seçimi Faz A'da veriye bakılarak kesinleşecektir.

## A1. Özellik çıkarımı

```
GİRDİ: ses_kaydı (fs = 16 kHz), çevre_kaydı
pencere = 5 s;  adım = 5 s
HER pencere w İÇİN:
    X     = STFT(ses[w], n_fft = 1024, hop = 512)
    E_mel = mel_süzgeç_bankası(|X|²)          # 40 mel bandı
    logmel = log(E_mel + ε)
    mfcc   = DCT(logmel)[1..13]
    bant_oranı = enerji(bant_i) / toplam_enerji   # seçili bantlar
    ses_özelliği = ortalama_ve_std( [logmel, mfcc, bant_oranı] over zaman )
    çevre = [T_iç, T_dış, nem, ΔT_kısa, ΔNem_kısa]
    (isteğe bağlı) çevre += [gün_saati_sin, gün_saati_cos]   # ablasyon
```

## A2. Kontrollü bozulma enjeksiyonu

```
GİRDİ: normal_pencereler, gürültü_havuzu (rüzgâr, yağmur, motor, konuşma)
HER SNR IN {0, 5, 10, 15} dB:
    HER pencere p İÇİN rastgele gürültü n seç:
        a = sqrt( güç(p) / (güç(n) * 10^(SNR/10)) )
        p_bozuk = p + a * n
        özellik_çıkar(p_bozuk)  →  yapay_anomali_kümesi
```

Bu küme yalnızca eşik kalibrasyonu ve yan değerlendirme içindir. Gerçek koloni anomalisi yerine geçmez.

## A3. Kovan dışarıda bırakma ile değerlendirme

```
kovanlar = {h1, ..., hK}
HER test_kovanı h IN kovanlar:
    eğitim = normal_dönemler(kovanlar - h)
    ölçek  = öğren(eğitim)

    HER yöntem IN {Mahalanobis, OCSVM/IsoForest, Otokodlayıcı}:
        HER girdi IN {ses, ses+çevre, çevre_koşullu}:
            model = eğit(yöntem, girdi, eğitim)
            skor_bozuk = model.skor(enjekte_edilmiş_kümesi(h))
            τ = skor_bozuk'un %10'luk dilimi          # %90 yakalama
            skor_rutin = model.skor(rutin_dönem(h))
            alarm = skor_rutin >= τ
            YA[h, yöntem, girdi] = sayı(alarm) / saat
            saat_dağılımı[h, ...] = histogram(alarm, saat_of_day)
```

`τ` testten önce, enjekte kümeden seçildiği için yöntemler eşit duyarlılıkta karşılaştırılır.

## A4. Çevre koşullu skor

```
eğit:  f_ψ(çevre) ≈ ses_özelliği         # normal dönemlerde regresyon
skor:  r = ses_özelliği - f_ψ(çevre)
       s = rᵀ Σ_r⁻¹ r                    # kalıntının Mahalanobis uzaklığı
```

Beklenti: gün içi sıcaklık döngüsünün yarattığı sapmalar `f_ψ` tarafından açıklanır, kalıntıda azalır.

## A5. Faz B saha hattı ve olay yanıtı

```
düğüm: her 10 dk → 10 s ses + sıcaklık/nem → SD kart
bilgisayar: yükle → A1 → eğitimli_model.skor → alarm_listesi
arıcı_günlüğü = [(zaman, olay_türü)]
HER olay e İÇİN:
    yanıt[e] = EVET EĞER  ∃ alarm a:  |t_a - t_e| <= Δ
rapor: saatlik_YA, olay_yanıt_oranı, saat_dağılımı_istatistiği
```

## A6. Uç cihaz

```
ESP32: mikrofon → 5 s tampon → log-mel (sabit nokta) → int8 model → skor
ölç: süre, RAM, flash, saatlik ortalama akım
karşılaştır: cihaz_skoru vs bilgisayar_skoru  (korelasyon, ortalama mutlak fark)
```
