# Diyagramlar

Sistem şeması ve deney tasarımı `Proje_Tanitim.pdf` içindedir. Burada algoritma akışları verilmiştir.

## D1. Ölçümden karara

```mermaid
flowchart LR
    V[Vurucu<br/>tekrarlanabilir darbe] --> K[Konsol kiriş<br/>çentik, uç kütlesi]
    K --> S[3 ivmeölçer + referans<br/>ortak zaman tabanı]
    S --> W[Welch PSD,<br/>sönümlü sinüs uydurma]
    W --> F[f1..f3, ζ,<br/>genlik oranı, faz]
    F --> N[Referansa göre<br/>normalize: δ]
    N --> Y1[Y1 frekans kuralı]
    N --> Y2[Y2 tek sensör]
    N --> Y3[Y3 iki sensör]
    N --> Y4[Y4 üç sensör]
    Y1 --> R[Makro F1, EKDH]
    Y2 --> R
    Y3 --> R
    Y4 --> R
```

## D2. Çentik ilerleyişi (geri alınamaz adımlar)

```mermaid
flowchart LR
    A[Sağlam<br/>5 gün x 3 kütle x 2 yerleşim] --> B[Çentik %15<br/>tüm günler tamamlanır]
    B --> C[Çentik %30]
    C --> D[Çentik %45]
    D --> E[Kiriş 2: aynı süreç<br/>bağımsız doğrulama]
```

Bir sonraki adıma, mevcut adımın bütün günleri tamamlanmadan geçilmez.

## D3. Karıştırıcılar ve hasar etkisi

```mermaid
flowchart TB
    H[Hasar düzeyi] --> F[Frekans kayması δ]
    M[Uç kütlesi] --> F
    R[Yeniden sıkıştırma] --> F
    T[Sıcaklık] --> F
    F --> Q{Model, hasarı<br/>diğerlerinden ayırabiliyor mu?}
```

## D4. Veri bölme

```mermaid
flowchart TB
    D[240 koşul] --> E[Kiriş 1, eğitim günleri]
    D --> T1[Kiriş 1, ayrı gün]
    D --> T2[Kiriş 2, tüm günler]
    E --> CV[Gün bazlı gruplu CV]
    CV --> M[Model]
    M --> T1
    M --> T2
    E --> LK[Bir kütle düzeyi dışarıda<br/>dayanıklılık]
```
