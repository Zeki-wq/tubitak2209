# Algoritmik Akış (Kaba Kod)

Aşağıdaki kodlar uygulama kodu değil, yöntemin işleyişini gösteren kaba taslaktır. Sabitler (60 °C, 25 K, H = 60 s) pilotta kesinleşecektir.

## A1. Güvenli koşu döngüsü (mikrodenetleyici)

```
GİRDİ: koşu_planı (temas düzeyi, akım profili, fan durumu)
SABİT: T_MUTLAK = 60 °C, SÜRE_MAX = 20 dk, f_s = 1 Hz

ayarla(akım_profili, fan)
bekle_ta_ki( T_bağlantı - T_ortam < 1 K )        # koşu öncesi soğuma
t0 = şimdi()
DÖNGÜ her saniye:
    T1, T2   = oku(termokupl)
    V_kelvin = oku(gerilim_düşümü)
    I        = oku(şönt)
    T_ort    = oku(ortam)
    kaydet(zaman, T1, T2, V_kelvin, I, T_ort)
    EĞER max(T1, T2) >= T_MUTLAK  VEYA  şimdi() - t0 >= SÜRE_MAX:
        akımı_kes()
        ÇIK
sogutma_kaydı_al(until = T_ortam + 2 K)
```

Bağımsız mekanik termostat bu döngüden bağımsız çalışır. Yazılım çökse bile devre açılır.

## A2. Özellik çıkarımı (kayan pencere)

```
GİRDİ: koşu kaydı, pencere = 30 s, adım = 5 s
HER pencere w İÇİN:
    dT      = T_ort_bağlantı(w) - T_ortam(w)
    eğim    = en_küçük_kareler_eğimi(T_bağlantı, w)
    ivme    = eğim(w) - eğim(w - 1)
    R_gör   = ortalama(V_kelvin / I)                 # görünür direnç
    dR      = en_küçük_kareler_eğimi(R_gör, w)
    sapma_T = std(T_bağlantı, w);  sapma_R = std(R_gör, w)
    x[w]    = [dT, eğim, ivme, R_gör, dR, sapma_T, sapma_R]
    y[w]    = 1 EĞER  max(T_bağlantı[t_w .. t_w + H]) >= T_EŞİK  DEĞİLSE 0
```

`y` yalnızca gelecekteki sıcaklıktan türetilir. Giriş özelliklerinde gelecek bilgisi bulunmaz.

## A3. Eğitim, eşik seçimi ve bağımsız test

```
koşular = tüm_koşular
test_günleri = ayır(koşular, gün bazlı, eğitime hiç girmeyecek)
eğitim = koşular - test_günleri

# ölçekleme yalnızca eğitimden
ölçek = öğren(eğitim)

# model seçimi: koşu bazlı gruplanmış çapraz doğrulama
HER aday_model İÇİN:
    skor[aday] = GrupluCV(aday, eğitim, grup = koşu_no)
model = en_iyi(skor)

# alarm eşiği: normal koşullarda saatlik yanlış uyarı hedefi
p = model.olasılık(eğitim_normal_pencereleri)
τ = en_küçük τ  öyle ki  yanlış_uyarı_sayısı(p >= τ) / saat  <= HEDEF_YU

# test: τ sabit, test verisine dokunulmadı
HER test_koşusu İÇİN:
    t_uyarı = ilk an  p >= τ
    t_eşik  = sabit_eşiğin_aşıldığı_an (Y1)
    erken[k] = t_eşik - t_uyarı
rapor(erken, yanlış_uyarı_saatlik, duyarlılık)
```

## A4. Mikrodenetleyici çıkarımı (Y4)

```
HER 5 s:
    x = özellikleri_hesapla(son 30 s tampon)
    x_q = nicele_int8(x, ölçek_sabitleri)
    p = model_int8(x_q)
    EĞER p >= τ_q SAYAÇ++ DEĞİLSE SAYAÇ = 0
    EĞER SAYAÇ >= 2: uyarı_ver()                      # tek pencere yetmez
ölç: çıkarım_süresi, RAM, flash, bilgisayar_modeliyle_uyum
```

## Akış özeti

Koşu planı → güvenli koşu (A1) → ham kayıt → pencereler ve etiket (A2) → gruplu bölme ve eğitim (A3) → eşik seçimi → bağımsız gün testi → küçültme ve cihaz ölçümü (A4).
