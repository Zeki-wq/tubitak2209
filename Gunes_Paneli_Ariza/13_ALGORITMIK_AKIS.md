# Algoritmik Akış (Kaba Kod)

Kodlar yöntemi anlatan taslaktır. Sabitler pilotta kesinleşecektir.

## A1. I–V taraması (ölçüm devresi)

```
GİRDİ: MOSFET kapı-kaynak gerilimi basamakları V_GS[1..K]  # düşükten yükseğe: açık devre → kısa devre
HER oturumda, her 10 s'de bir:
    G_rel = oku(referans_hücre)                         # kalibre değilse göreli ışınım göstergesi
    T_p1, T_p2 = oku(panel_arka_sıcaklıkları)
    HER k = 1..K İÇİN:
        kapı_kaynak_gerilimi_ayarla(V_GS[k])
        bekle(oturma_süresi)
        V[k], I[k] = oku(ölçüm_modülü)
        EĞER bileşen_sıcaklığı_güvenli_değil() VEYA olağan_dışı_durum_var():
            MOSFET'i_kesime_al(); oturumu_işaretle("güvenlik"); TARAMAYI_KES; SONRAKİ_OTURUMA_GEÇ
    MOSFET'i_kesime_al()                           # panel boşta
    I_sc  = V = 0 civarında enterpolasyonla bulunan akım
    V_oc  = I = 0 civarında enterpolasyonla bulunan gerilim
    P[k]  = V[k] * I[k];  P_mp = max(P);  (V_mp, I_mp) = argmax(P)
    FF    = P_mp / (I_sc * V_oc)
    S_oc  = -dV/dI, V_oc civarında yerel doğrusal uydurma  # tanısal eğim özelliği
    kaydet(zaman, G_rel, T_p, V[], I[], özetler, kamera_geometrisi, hava_notu)
EĞER |G_rel(başlangıç) - G_rel(bitiş)| / G_rel(başlangıç) > %5:
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
    koşul_etiketi = protokolden_oku()                     # N/G/K/B; model bu etiketi üretmez
    kalite = kontrol_et(ışınım_değişimi, sensör_hatası, panel_maskesi)
    EĞER kalite == "uygunsuz":
        oturumu_işaretle("analiz_dışı"); DEVAM_ET
    HER geçerli tarama/kare İÇİN özellikleri_hesapla()
    termal_özet = oturum_içi_medyan(termal_özellikler)
    I_sc_n = medyan(I_sc * (G_rel_hedef / G_rel) / (1 + α_I * (T_p - T_ref)))
    V_oc_n = medyan(V_oc - β_V * (T_p - T_ref))     # basit doğrusal düzeltme
    P_mp_rel = medyan(P_mp / G_rel)                  # yalnızca göreli karşılaştırma için
    elektriksel = [I_sc_n, V_oc_n, P_mp_rel, medyan(FF), medyan(S_oc), medyan(G_rel), medyan(T_p)]
    özellik = birleştir(termal_özet, elektriksel)    # oturum başına tek vektör

test_günleri = veri_toplama_öncesi_ayır(günler, her_operasyonel_banttan_en_az_2)
eğitim = oturumlar - test_günleri
ölçek = öğren(eğitim)                            # yalnızca eğitimden

HER özellik_kümesi IN {yalnız_termal, yalnız_elektrik, birleşik}:
    C = GünGrupluCV_ile_seç(düzenlileştirme_katsayıları, eğitim, grup = gün)
    model = sınıf_ağırlıklı_düzenlileştirilmiş_lojistik(C)
    model.eğit(eğitim)

# dayanıklılık: yalnızca yeterli gün ve sınıf varsa bir ışınım bandı eğitim dışında
EĞER yeterli_geçerli_gün_ve_sınıf_varsa:
    HER özellik_kümesi IN {yalnız_termal, yalnız_elektrik, birleşik}:
        ilgili_modeli_eğit(ışınım = yüksek); ilgili_modeli_test_et(ışınım = orta)

# raporlama
gölgelenme_yanlış_sınıf_oranı = sayı(G → {K, B}) / sayı(G)
makro_F1, duyarlılık, özgüllük, karışıklık_matrisi
fark = eşleştirilmiş_test_oturumu_farkı
EĞER testte_en_az_8_gün_varsa: GA95 = gün_bloklu_bootstrap(fark)
DEĞİLSE: farkı_betimsel_raporla()
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
