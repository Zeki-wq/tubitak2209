# Algoritmik Akış (Kaba Kod)

Kodlar yöntemi anlatan taslaktır. Eşik ve sulama oranları pilotta kesinleşir.

## A1. Günlük deney rutini

```
HER gün, sabit saatte:
    HER saksı i (18 bitkili + 3 bitkisiz) İÇİN:
        W_pre[i] = tart(i)                       # sulamadan önce
    HER saksı i İÇİN:
        hedef = ağırlık_hedefi(grup[i])          # tam / %70 / %50
        su_ver( hedef - W_pre[i] )  EĞER  su > 0
        W_post[i] = tart(i)
    solgunluk[i] = {gözlemci_A, gözlemci_B}      # 0-1-2 skoru
    kaydet(tarih, W_pre, W_post, solgunluk)
# sensör düğümü bu sırada sürekli çalışır (dakikalık kayıt)
```

## A2. Etiket üretimi (sensör kullanılmaz)

```
Ē_buh[d] = ortalama( W_post[bitkisiz][d-1] - W_pre[bitkisiz][d] )   # buharlaşma
HER saksı i, gün d İÇİN:
    Tr[i,d]  = W_post[i][d-1] - W_pre[i][d] - Ē_buh[d]
Tr_tam[d]   = ortalama( Tr[j,d]  j ∈ tam_sulama )
NTR[i,d]    = Tr[i,d] / Tr_tam[d]
y[i,d]      = 1 EĞER NTR[i,d] < θ  (θ = 0,8)  DEĞİLSE 0
tutarlılık  = Cohen_kappa( y , solgunluk_skoru >= 1 )
```

## A3. Özellik ve hedef

```
HER izlenen saksı i, gün d İÇİN:
    θ_v   = kalibre_nem(ADC)                     # a·ADC + b
    VPD   = es(T_hava)·(1 - RH/100)
    ΔT    = T_yaprak - T_hava
    x[i,d] = [ort(θ_v), Δ(θ_v), ort(T_hava), ort(RH), VPD, ort(ışık),
              ort(ΔT), gündüz_özetleri, gece_özetleri, önceki_3_gün_eğilimi]
    hedef_sınıf[i,d]  = y[i,d+1]
    hedef_regres[i,d] = NTR[i,d+1]
```

`x[i,d]` yalnızca `d` gününe kadar olan veriden üretilir. Hedef ertesi gündür.

## A4. Modeller ve gruplu doğrulama

```
M1: x_sadece_nem;  M2: nem + hava (T, RH, VPD, ışık);  M3: tüm sensörler
REF: EĞER θ_v < θ_eşik → stres uyarısı

seri 1+2  →  saksı bazlı gruplu CV  →  model seçimi
seri 3    →  nihai test (hiç görülmemiş saksılar ve seri)

HER model İÇİN:
    makro_F1, duyarlılık, yanlış_alarm_oranı, MAE(NTR)
    erken[i] = gün(y=1 ilk) - gün(model uyarısı ilk)
    fark = eşleştirilmiş_saksı_farkı;  GA95 = blok_bootstrap(fark, blok = saksı)
```

## A5. Sulama simülasyonu (keşifsel, ayrı işaretli)

```
S[0] = kapasite
HER gün d:
    EĞER strateji == "sabit_eşik":  sula EĞER θ_v < θ_eşik
    EĞER strateji == "model":       sula EĞER model_uyarısı(d)
    S[d+1] = S[d] + sulama[d] - Tr_tahmin[d]
sayaç: toplam_su, stresli_gün_sayısı
```

Bu bölüm gerçek bir sulama deneyi yerine geçmez.
