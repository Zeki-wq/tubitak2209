# Algoritmik Akış (Kaba Kod)

Kodlar yöntemi anlatan taslaktır. Sabitler pilotta kesinleşecektir.

## A1. I–V taraması (ölçüm devresi)

```
GİRDİ: MOSFET kapı gerilimi basamakları V_g[1..K]
HER oturumda, her 10 s'de bir:
    G_ref = oku(referans_hücre)
    T_p1, T_p2 = oku(panel_arka_sıcaklıkları)
    HER k = 1..K İÇİN:
        kapı_gerilimi_ayarla(V_g[k])
        bekle(oturma_süresi)
        V[k], I[k] = oku(ölçüm_modülü)
    kapıyı_aç()                                   # panel boşta
    I_sc  = I'nın V ≈ 0 değeri
    V_oc  = V'nin I ≈ 0 değeri
    P     = V * I;  P_mp = max(P);  (V_mp, I_mp) = argmax(P)
    FF    = P_mp / (I_sc * V_oc)
    R_s   = -dV/dI, V_oc civarında doğrusal uydurma
    kaydet(zaman, G_ref, T_p, V[], I[], özetler)
EĞER |G_ref(başlangıç) - G_ref(bitiş)| / G_ref > %5:
    oturumu_işaretle("ışınım_değişken")
```

## A2. Termal özellikler (kare başına)

```
GİRDİ: termal_kare (ör. 8×8 veya 32×24 piksel)
maske = panel_bölgesi(kare)
T_ort = ortalama(kare[maske]);  T_maks = maksimum(kare[maske])
ΔT_sıcak  = T_maks - T_ort
sıcak_oran = sayı(kare > T_ort + 2σ) / sayı(maske)
σ_uzay    = std(kare[maske])
konum     = ağırlık_merkezi(kare > T_ort + 2σ)
ÇIKTI: [ΔT_sıcak, sıcak_oran, σ_uzay, konum]
```

## A3. Normalleştirme ve model

```
HER oturum İÇİN:
    I_sc_n = I_sc * (G_ref_STC / G_ref) / (1 + α * (T_p - 25))
    V_oc_n = V_oc - β * (T_p - 25)                 # basit doğrusal düzeltme
    elektriksel = [I_sc_n, V_oc_n, P_mp_n, FF, R_s]
    özellik = birleştir(termal_özet, elektriksel)

gün_grupları = ayır(oturumlar, gün bazlı)
test = eğitimde_görülmeyen_günler
ölçek = öğren(eğitim)                            # yalnızca eğitimden

HER özellik_kümesi IN {yalnız_termal, yalnız_elektrik, birleşik}:
    HER model IN {lojistik, RF}:
        skor = GrupluCV(model, eğitim, grup = gün)
en_iyi_model = seç(skor)

# dayanıklılık: bir ışınım bandı eğitim dışında
eğit(en_iyi, ışınım = yüksek);  test(ışınım = orta)

# raporlama
gölgelenme_yanlış_sınıf_oranı = sayı(G → bakım_gerekli) / sayı(G)
makro_F1, duyarlılık, özgüllük, karışıklık_matrisi
fark = eşleştirilmiş_oturum_farkı;  GA95 = bootstrap(fark)
```

## A4. Kart üzerinde çıkarım ve enerji ölçümü

```
tekrarla N kez:
    t_başla = saat()
    x = özellikleri_hesapla(son_kare, son_IV)
    ŷ = model(x)
    t_süre.ekle(saat() - t_başla)
enerji_döngü = ∫ (V_besleme * I_akım) dt     # ölçüm döngüsü boyunca
rapor(ortalama(t_süre), enerji_döngü)
```
