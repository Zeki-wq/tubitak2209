# Algoritmik Akış (Kaba Kod)

Kodlar yöntemi anlatan taslaktır. Örnekleme hızı, kayıt süresi ve çentik derinlikleri pilotta kesinleşir.

## A1. Darbe ve kayıt

```
GİRDİ: koşul (kiriş, durum, kütle, yerleşim, gün)
sıkıştır(kiriş, tork = SABİT)
HER darbe d = 1..10 İÇİN:
    tetikle(vurucu)
    bekle_ta_ki( ivme > TETİK_EŞİĞİ )            # kayıt tetikle
    kaydet(3 kanal, fs = 1 kHz, süre = 4 s)       # ortak zaman tabanı
    kaydet(referans_ivmeölçer, sıcaklık)
    bekle( sönümün bitmesi )
```

## A2. Modal özellik çıkarımı (her darbe, her kanal)

```
y = ham[tetikten_sonra]; y = y - ortalama(y)
Pxx = Welch(y, pencere = Hann, örtüşme = %50)
pik_frekans[1..3] = ilk_üç_tepe(Pxx, beklenen_aralık)
f_hassas[i]  = parabolik_ara_değerleme(Pxx, pik_frekans[i])

# zaman alanı iyileştirme: sönümlü sinüs uydurma
HER mod i İÇİN:
    (A, ζ, f, φ) = en_küçük_kareler( y_bandgeçiren_i , A·exp(-ζ·2πf·t)·sin(2πf√(1-ζ²)·t + φ) )
genlik_oranı[a,b] = |Y_a(f_i)| / |Y_b(f_i)|
faz_farkı[a,b]    = arg(Y_a(f_i)) - arg(Y_b(f_i))

# referansa göre normalize
δ_i = (f_i - f_i_ref(kiriş)) / f_i_ref(kiriş)     # ilk gün, sağlam durum
özellik = [f_i, δ_i, ζ_i, genlik_oranları, faz_farkları]
```

## A3. Karar yöntemleri

```
Y1: EĞER |δ_1| > τ_f  →  "hasarlı";  sınıf = en yakın δ_1 düzeyi
Y2: HER sensör s İÇİN model_s = eğit(özellik[s])
Y3: HER çift (s1, s2) İÇİN model = eğit(özellik[s1] ∪ özellik[s2])
Y4: model = eğit(özellik[tüm sensörler])
```

## A4. Değerlendirme ve en küçük ayırt edilebilir hasar

```
eğitim = kiriş1, günler 1..3        # model seçimi: gün bazlı gruplu CV
test_A = kiriş1, gün 5              # aynı kiriş, eğitimde olmayan gün
test_B = kiriş2, tüm günler         # bağımsız kiriş
dayanıklılık: bir kütle düzeyini eğitim dışında bırak

HER yöntem, HER test kümesi İÇİN:
    makro_F1, dengeli_doğruluk, karışıklık_matrisi
    frekans_hatası = |f_ölçüm - f_referans_ivmeölçer|

# en küçük ayırt edilebilir hasar
HER hasar düzeyi L > 0 İÇİN:
    d = δ_1[L koşulları]  -  δ_1[sağlam koşullar]    # koşul ortalamaları
    GA = bootstrap(d, koşul bazlı yeniden örnekleme)
    EĞER 0 ∉ GA: ayırt_edilebilir[L] = EVET
EKDH = en küçük L  öyle ki  ayırt_edilebilir[L]
```

## A5. Mikrodenetleyicide pik frekans

```
tampon(4 s) → pencere → FFT(sabit nokta) → tepe + parabolik ara değer → f_MCU
karşılaştır: f_MCU - f_bilgisayar  (ortalama ve en büyük fark)
ölç: süre, RAM
```

## A6. Fiziksel makullük denetimi

```
HER çentik derinliği L İÇİN:
    EI_yerel = EI · azaltma_katsayısı(L)         # sonlu eleman ya da analitik
    f_beklenen[L] = ÖzdeğerÇöz(kiriş, EI_yerel)
karşılaştır( δ_ölçülen[L] , δ_beklenen[L] )
```
