# Diyagramlar

Sistem şeması ve deney tasarımı şeması `Proje_Tanitim.pdf` içinde yer alır. Burada algoritma ve güvenlik akışları verilmiştir. Mermaid destekleyen bir görüntüleyicide çizim olarak görünür.

## D1. Veri ve karar hattı

```mermaid
flowchart LR
    A[Kaynak ve bağlantı<br/>klemens] --> B[Sensörler<br/>termokupl, Kelvin V, şönt, ortam]
    B --> C[Mikrodenetleyici<br/>zaman damgalı kayıt]
    C --> D[30 s kayan pencere<br/>özellik çıkarımı]
    D --> E1[Y1 sabit eşik]
    D --> E2[Y2 eğim kuralı]
    D --> E3[Y3 lojistik / RF]
    E3 --> E4[Y4 int8 model<br/>cihaz üzerinde]
    E1 --> F[Erken uyarı süresi<br/>yanlış uyarı, duyarlılık]
    E2 --> F
    E3 --> F
    E4 --> F
```

## D2. Güvenlik durum makinesi

```mermaid
stateDiagram-v2
    [*] --> Hazir
    Hazir --> Soguma: koşu başlat isteği
    Soguma --> Kosu: T - Ta < 1 K
    Kosu --> Kesildi: T >= 60 °C
    Kosu --> Kesildi: süre >= 20 dk
    Kosu --> Kesildi: termostat açtı
    Kosu --> Kesildi: operatör acil durdurma
    Kesildi --> Sogutma_Kaydi
    Sogutma_Kaydi --> Hazir: T <= Ta + 2 K
```

## D3. Veri bölme (sızıntıyı önleyen düzen)

```mermaid
flowchart TB
    K[80 koşu] --> G[Gün bazlı ayır]
    G --> TR[Eğitim günleri]
    G --> TE[Test günleri<br/>eğitimde hiç görülmez]
    TR --> CV[Koşu bazlı gruplu CV<br/>model ve hiperparametre seçimi]
    CV --> TH[Eşik τ: eğitim normal pencerelerinde]
    TH --> EV[Test günlerinde tek değerlendirme]
    TE --> EV
    TR --> LO[Bir akım profilini dışarıda bırak<br/>dayanıklılık deneyi]
```

## D4. Isınma eğrisinin okunuşu (kavramsal)

```mermaid
flowchart LR
    S[Başla: T = Ta] --> R[Gevşek bağlantı: Rc büyür]
    R --> P[Güç I²Rc artar]
    P --> U[Sıcaklık eğimi artar]
    U --> M{Model uyarı<br/>verdi mi?}
    M -- evet --> L[Erken uyarı süresi L > 0]
    M -- hayır --> T[Sabit eşik aşıldı]
    T --> L2[L = 0 ya da negatif]
```
