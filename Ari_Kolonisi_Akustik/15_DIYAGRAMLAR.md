# Diyagramlar

Sistem şeması ve deney tasarımı `Proje_Tanitim.pdf` içindedir. Burada algoritma akışları verilmiştir.

## D1. İki aşamalı yapı

```mermaid
flowchart LR
    subgraph FazA[Faz A: açık veri]
        U[UrBAN verisi] --> H[Hazırlık, kalite işaretleme]
        H --> O[Özellik çıkarımı]
        O --> M[Üç anomali yöntemi<br/>x üç girdi biçimi]
        M --> E[Kovan dışarıda bırak<br/>yanlış alarm yükü]
    end
    subgraph FazB[Faz B: saha]
        N[Kovan düğümü<br/>mikrofon, T/nem, SD] --> K[Kayıt + arıcı günlüğü]
        K --> T[Bağımsız test]
    end
    E --> S[Seçilen model]
    S --> I[int8 küçültme<br/>ESP32 çıkarımı]
    S --> T
    I --> R[Rapor]
    T --> R
```

## D2. Girdi biçimleri

```mermaid
flowchart TB
    S[Ses özellikleri] --> G1[G1: yalnız ses]
    S --> G2[G2: ses + çevre]
    C[Çevre: T, nem, değişim] --> G2
    C --> G3[G3: çevre koşullu<br/>f(çevre) → beklenen ses]
    S --> G3
    G3 --> K[Kalıntı skoru]
```

## D3. Kovan dışarıda bırakma

```mermaid
flowchart LR
    K1[Kovan 1] --- A((eğitim))
    K2[Kovan 2] --- A
    K3[Kovan 3] --- A
    K4[Kovan 4<br/>test] -.-> T((test))
    A --> M[Model] --> T
    T --> R[YA/saat, saat dağılımı]
```

Her turda test kovanı değişir. Bir kovanın hiçbir penceresi eğitimde bulunmaz.

## D4. Saha kaydı zamanlaması

```mermaid
gantt
    title Faz B kayıt ve doğrulama (aylar)
    dateFormat X
    axisFormat %s
    section Hazırlık
    Düzenek, arıcı onayı, pilot : 2, 3
    section Kayıt
    Saha kaydı + günlük : 3, 6
    section Çıkarım
    Uç cihaz küçültme ve ölçüm : 5, 7
    section Doğrulama
    Bağımsız test, rapor : 6, 8
```
