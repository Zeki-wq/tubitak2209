# Diyagramlar

Sistem şeması ve deney tasarımı `Proje_Tanitim.pdf` içindedir. Burada algoritma ve güvenlik akışları verilmiştir.

## D1. Veri hattı

```mermaid
flowchart LR
    H[Test haznesi<br/>1 m³, fan, egzoz] --> D1[Düğüm 1]
    H --> D2[Düğüm 2]
    H --> R[2 ticari duman alarmı<br/>+ mikrofon]
    D1 --> LG[LoRa ağ geçidi]
    D2 --> LG
    D1 --> SD[(SD kart)]
    LG --> PC[Bilgisayar]
    SD --> PC
    R --> PC
    PC --> F[Pencere özellikleri]
    F --> Y[Y1 / Y2 / Y3 / Y4]
    Y --> E[Sabit duyarlılıkta<br/>yanlış alarm, gecikme]
    R --> E
```

## D2. Olay türleri ve beklenen alarm

```mermaid
flowchart TB
    O[Olay] --> N{Yanma mı?}
    N -- hayır --> A0[0 arka plan]
    N -- hayır --> A1[1 buhar]
    N -- hayır --> A2[2 pişirme aerosolü]
    N -- hayır --> A3[3 toz]
    N -- hayır --> A4[4 su bazlı sprey]
    N -- hayır --> A5[5 sıcaklık sıçraması]
    N -- hayır --> A6[6 gliserin sisi]
    N -- evet --> A7[7 tütsü çubuğu<br/>yazılı onaya bağlı]
    A0 --> NA[Beklenen: alarm YOK]
    A1 --> NA
    A2 --> NA
    A3 --> NA
    A4 --> NA
    A5 --> NA
    A6 --> NA
    A7 --> AL[Beklenen: alarm VAR]
```

## D3. Faz A ve Faz B

```mermaid
flowchart LR
    A[Faz A: açık veri<br/>oturum bazlı bölme] --> K[Yöntem karşılaştırması<br/>yalnız yangın var/yok]
    K --> G[Gerekçe: tür bazlı analiz için<br/>kendi verimiz gerekli]
    G --> B[Faz B: 80 olay kaydı<br/>8 tür x 2 şiddet x 5 gün]
    B --> T[Eğitimde olmayan günlerde test]
    B --> L[Bir olay türünü dışarıda bırak]
```

## D4. Yanma deneyi için güvenlik kapısı

```mermaid
flowchart TD
    S[Yanma olayı planlandı] --> W{Yazılı güvenlik<br/>onayı var mı?}
    W -- hayır --> X[Olay 7 çıkarılır<br/>yanma sınıfı açık veriden]
    W -- evet --> C{Kontrol listesi tamam mı?<br/>söndürücü, CO uyarı cihazı,<br/>havalandırma, gözetmen}
    C -- hayır --> X
    C -- evet --> R[Deneyi yap]
    R --> V[Havalandır, CO düşene kadar bekle]
```

## D5. Sabit duyarlılıkta karşılaştırma

```mermaid
flowchart LR
    TR[Eğitim günleri] --> S1[Yanma olaylarının %90'ı<br/>yakalanacak τ seç]
    S1 --> TE[Test günleri: τ sabit]
    TE --> YA[Yanma dışı kayıtlarda<br/>yanlış alarm oranı]
```
