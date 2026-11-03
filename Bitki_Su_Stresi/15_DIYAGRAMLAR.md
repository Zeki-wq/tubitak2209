# Diyagramlar

Sistem şeması ve deney tasarımı `Proje_Tanitim.pdf` içindedir. Burada algoritma akışları verilmiştir.

## D1. Etiket ve girdi ayrımı (projenin ana fikri)

```mermaid
flowchart LR
    subgraph ETIKET[Etiket yolu: sensör YOK]
        T[Günlük tartı] --> TR[Transpirasyon Tr]
        TR --> NTR[NTR = Tr / Tr_tam]
        NTR --> Y[Stres etiketi y]
        S[Solgunluk skoru] -.kappa kontrolü.-> Y
    end
    subgraph GIRDI[Girdi yolu: sensörler]
        N[Toprak nemi] --> X
        H[Hava T, RH, VPD, ışık] --> X
        L[Yaprak sıcaklığı] --> X
        X[Günlük özellikler x_d]
    end
    X --> M[Model M1/M2/M3]
    M --> P[t+1 gün stres tahmini]
    Y --> E[Değerlendirme]
    P --> E
```

## D2. Seri ve saksı bazlı bölme

```mermaid
flowchart TB
    S1[Seri 1] --> TR[Eğitim / seçim<br/>saksı bazlı gruplu CV]
    S2[Seri 2] --> TR
    S3[Seri 3<br/>bağımsız] --> TE[Nihai test]
    TR --> M[Seçilen model]
    M --> TE
```

## D3. Üç sulama grubu ve izleme

```mermaid
flowchart LR
    G1[Tam sulama<br/>6 saksı] --> I1[3 saksı sensörlü]
    G2[Hafif kısıt ~%70<br/>6 saksı] --> I2[3 saksı sensörlü]
    G3[Orta kısıt ~%50<br/>6 saksı] --> I3[3 saksı sensörlü]
    B[Bitkisiz 3 saksı] --> EV[Buharlaşma düzeltmesi]
```

## D4. Bir serinin zaman çizgisi

```mermaid
gantt
    title Bir deney serisi (yaklaşık 6-7 hafta)
    dateFormat X
    axisFormat %s
    section Hazırlık
    Fide uyumu (2 hf) : 0, 2
    section Deney
    Sulama koşulları (4-5 hf) : 2, 7
    section Seri sonu
    Biyokütle ve yaprak alanı : 7, 8
```

## D5. Karar akışı (model tabanlı uyarı)

```mermaid
flowchart TD
    A[Gün d verileri] --> B[Özellik x_d]
    B --> C{p stres > τ?}
    C -- evet --> D[Uyarı: yarın stres olası]
    C -- hayır --> E[Uyarı yok]
    D --> F[Doğrulama: NTR_{d+1} < θ mı?]
    E --> F
    F --> G[TP / FP / FN / TN, erken uyarı süresi]
```
