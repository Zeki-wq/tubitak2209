# Diyagramlar

Sistem şeması ve deney tasarımı `Proje_Tanitim.pdf` içindedir. Burada algoritma akışları verilmiştir.

## D1. Veri hattı

```mermaid
flowchart LR
    P[12 V panel] --> TS[Termal sensör<br/>panelin tamamı]
    P --> IV[MOSFET ile I–V tarama]
    P --> TB[Arka yüzey sıcaklık x2]
    R[Referans hücre<br/>G_rel göstergesi] --> N
    TS --> F1[Termal özellikler]
    IV --> F2[Elektriksel özellikler<br/>Isc, Voc, Pmp, FF, Soc]
    TB --> N[Normalleştirme / kalite kapısı<br/>G_rel ve Tp'ye göre]
    F1 --> N
    F2 --> N
    N --> D[Oturum veri kaydı<br/>özellikler + koşul etiketi + metadata]
    D --> M[Model<br/>termal / elektrik / birleşik]
    M --> C[N, G, K, B deney sınıfı tahmini<br/>saha bakımı için doğrudan karar değildir]
```

## D2. Kontrollü sınıf etiketleme mantığı

```mermaid
flowchart TB
    A[Operatör deney koşulunu kurar] --> B{Protokol etiketi}
    B -->|müdahale yok| N[N: normal]
    B -->|opak kart| G[G: geçici gölgelenme]
    B -->|yarı saydam film| K[K: kontrollü yüzey geçirgenliği azalması<br/>bakım temsil koşulu]
    B -->|haricî direnç| S[B: seri direnç kaybı temsili<br/>bakım temsil koşulu]
    N --> D[Etiket, model eğitiminden önce kaydedilir<br/>N/G: referans-geçici; K/B: bakım-temsil]
    G --> D
    K --> D
    S --> D
```

## D3. Veri bölme

```mermaid
flowchart TB
    O[Planlanan 90 oturum<br/>en az 10 takvim günü] --> GN[Gün bazlı grupla]
    GN --> T[Test günleri<br/>her operasyonel banttan en az 2 gün, veri toplamadan önce ayrılır]
    GN --> E[Eğitim / model seçimi günleri]
    E --> CV[Gün bazlı gruplu CV]
    CV --> BM[En iyi model]
    BM --> TT[Test günlerinde<br/>tek nihai değerlendirme]
    T --> TT
    E --> RB[Yeterli veri varsa:<br/>bir operasyonel bantla eğit, diğerinde keşifsel test]
```

## D4. Oturum akışı

```mermaid
sequenceDiagram
    participant Op as Operatör
    participant Kart as Ölçüm kartı
    participant Panel
    Op->>Panel: koşulu kur (N/G/K/B), sırayı rastgele al
    Op->>Kart: oturumu başlat
    loop 3 dakika boyunca
        Kart->>Panel: termal kare (birkaç saniyede bir)
        Kart->>Panel: I–V taraması (10 sn'de bir)
        Kart->>Kart: referans hücre, sıcaklık kaydı
    end
    Kart-->>Op: oturum özeti, ışınım değişken mi?
    Op->>Op: bekleme (ısıl denge), bir sonraki koşul
```
