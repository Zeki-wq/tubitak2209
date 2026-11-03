# Diyagramlar

Sistem şeması ve deney tasarımı `Proje_Tanitim.pdf` içindedir. Burada algoritma akışları verilmiştir.

## D1. Veri hattı

```mermaid
flowchart LR
    P[12 V panel] --> TS[Termal sensör<br/>panelin tamamı]
    P --> IV[MOSFET ile I–V tarama]
    P --> TB[Arka yüzey sıcaklık x2]
    R[Referans hücre<br/>ışık sensörü] --> N
    TS --> F1[Termal özellikler]
    IV --> F2[Elektriksel özellikler]
    TB --> N[Normalleştirme<br/>G ve Tp'ye göre]
    F2 --> N
    F1 --> M[Model<br/>termal / elektrik / birleşik]
    N --> M
    M --> C[N, G, K, B sınıfı<br/>bakım gerekli mi?]
```

## D2. Sınıf ayrımının mantığı

```mermaid
flowchart TB
    A[Anomali var mı?] -->|hayır| N[N: normal]
    A -->|evet| B{Kalıcı mı?}
    B -->|hayır, ışık engeli| G[G: geçici gölgelenme<br/>bakım GEREKMEZ]
    B -->|evet| C{Kaynak}
    C -->|yüzey filmi| K[K: kirlenme<br/>bakım gerekir]
    C -->|bağlantı direnci| S[B: seri direnç artışı<br/>bakım gerekir]
```

## D3. Veri bölme

```mermaid
flowchart TB
    O[90 oturum] --> GN[Gün bazlı grupla]
    GN --> E[Eğitim günleri]
    GN --> T[Test günleri]
    E --> CV[Gün bazlı gruplu CV]
    CV --> BM[En iyi model]
    BM --> TT[Test günlerinde tek değerlendirme]
    T --> TT
    E --> RB[Yüksek ışınımla eğit,<br/>orta ışınımda test]
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
