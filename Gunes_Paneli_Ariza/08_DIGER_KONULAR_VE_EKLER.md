# 5. Belirtmek İstediğiniz Diğer Konular

Bu çalışmada "arıza tespiti" ile "yanlış alarmın azaltılması" aynı şey sayılmayacak. Sistem anomaliyi hiç yakalamasa da yanlış alarm vermiyor olabilir, bu bir başarı değildir. Bu yüzden iki ölçüt birlikte raporlanacak: geçici gölgelenmenin arıza sanılma oranı ve bakım gerektiren durumların yakalanma oranı.

Kalıcı hücre hasarı, hücre çatlağı, bypass diyot arızası ve potansiyel kaynaklı bozulma (PID) gibi durumlar kapsam dışındadır. Paneli bilerek zarara uğratacak hiçbir deney yapılmayacaktır. Anomaliler gölgeleme, geri alınabilir yüzey malzemesi ve seri direnç eklenmesiyle üretilecek, bu üç yöntemin gerçek arızaları ne kadar temsil ettiği sonuçların sınırlılıkları arasında açıkça yazılacaktır.

Açık havada çalışılacağı için yağış, rüzgâr ve elektrik güvenliği (ıslak ortam, kablo bağlantıları) dikkate alınacak. Panelin bağlı olduğu devre düşük gerilimli ve düşük güçlüdür.

# 6. Ekler

## Ek A — Örnek oturum kayıt formu

| Alan | Kaydedilecek değer |
|---|---|
| Oturum kodu | GNS_001 |
| Tarih ve saat | [KAYIT SIRASINDA] |
| Durum | N / G / K / B ve şiddet düzeyi |
| Gölgelenme oranı veya direnç değeri | [ÖLÇÜLEN / AYARLANAN] |
| Ortalama ışınım (referans hücre) | [ÖLÇÜLEN] ve bant: yüksek / orta |
| Panel arka yüzey sıcaklığı | [ÖLÇÜLEN] |
| Ortam sıcaklığı, rüzgâr, bulut durumu | [GÖZLEM] |
| Termal kare aralığı | [PİLOTLA BELİRLENEN] |
| I–V tarama aralığı | Hedef 10 s |
| Oturum süresi | Hedef 3 dakika |
| Gözlem ve olağan dışı durum | [NOT] |

## Ek B — Örnek sınıf etiketleri

- N: Normal (bakım gerektirmeyen)
- G: Geçici gölgelenme (bakım gerektirmeyen)
- K: Kalıcı yüzey kirlenmesi (bakım gerektiren)
- B: Seri direnç artışı (bakım gerektiren)
- İkili görev: N+G = 0, K+B = 1

## Ek C — Sistemin metinsel akışı

Panel → termal sensör, I–V tarama devresi, referans ışınım ve sıcaklık sensörleri → zaman damgalı kayıt → termal ve elektriksel özellikler → eşik kuralı, termal, elektriksel ve birleşik model → yanlış alarm ve F1 karşılaştırması → rapor.

**Not:** Bu ekler önerilen içeriklerdir. TYBS'nin ek yükleme kısıtları varsa ekran kurallarına uyulmalıdır. Fotoğraf, şema veya pilot veri ancak üretildikten ve doğrulandıktan sonra eklenmelidir.
