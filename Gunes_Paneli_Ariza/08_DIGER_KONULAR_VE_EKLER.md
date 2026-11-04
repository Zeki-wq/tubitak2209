# 5. Belirtmek İstediğiniz Diğer Konular

Bu çalışmada "arıza tespiti" ile "yanlış alarmın azaltılması" aynı şey sayılmayacak. Sistem anomaliyi hiç yakalamasa da yanlış alarm vermiyor olabilir, bu bir başarı değildir. Bu yüzden iki ölçüt birlikte raporlanacak: geçici gölgelenmenin K/B temsil koşulları sanılma oranı ve K/B temsil koşullarının yakalanma oranı.

Kalıcı hücre hasarı, hücre çatlağı, bypass diyot arızası ve potansiyel kaynaklı bozulma (PID) gibi durumlar kapsam dışındadır. Paneli bilerek zarara uğratacak hiçbir deney yapılmayacaktır. Anomaliler gölgeleme, geri alınabilir yüzey malzemesi ve seri direnç eklenmesiyle üretilecek, bu üç yöntemin gerçek arızaları ne kadar temsil ettiği sonuçların sınırlılıkları arasında açıkça yazılacaktır.

Açık havada çalışılacağı için yağış, rüzgâr ve elektrik güvenliği (ıslak ortam, kablo bağlantıları) dikkate alınacak. Panelin bağlı olduğu devre düşük gerilimli ve düşük güçlüdür.

## Üretken Yapay Zekâ (ÜYZ) Kullanım Beyanı

Bu başvuru paketi hazırlanırken üretken yapay zekâdan önemli ölçüde yararlanılmıştır. Kullanım; taslak metnin yapılandırılması, anlatımın düzenlenmesi, literatür için kaynak adayı aranması, algoritma ve diyagram taslağı oluşturulması ile tutarlılık kontrolüyle sınırlıdır. ÜYZ tarafından üretilen hiçbir deney verisi, ön çalışma sonucu, laboratuvar olanağı, cihaz kalibrasyonu veya kaynak künyesi doğrulanmadan başvuruya gerçek bilgi olarak eklenmemiştir. Kaynakçadaki bilimsel kayıtlar yayınevi, DOI veya standart kuruluşu sayfasından ayrıca doğrulanmıştır.

Bu paketle birlikte kişisel veri, gizli kurum verisi veya yayımlanmamış deney verisi bir ÜYZ aracına girilmemiştir. Başvuru sahibi, TYBS'nin ÜYZ ile ilgili alanlarında bu kullanımı eksiksiz ve gerçeğe uygun biçimde beyan etmeli; akademik danışman da başvuru metninin doğruluğu, güncelliği, özgünlüğü ve bilimsel güvenilirliği için nihai kontrolü yapmalıdır. Beyan, yalnızca gerçekten yapılan kullanımı yansıtacak şekilde TYBS'deki güncel ifadeye göre girilecektir.

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
| Analiz durumu | Geçerli / analiz dışı ve neden kodu |
| Gözlem ve olağan dışı durum | [NOT] |

## Ek B — Örnek sınıf etiketleri

- N: Normal (referans koşulu)
- G: Geçici gölgelenme (geçici koşul)
- K: Kontrollü yüzey geçirgenliği azalması (bakım temsil koşulu)
- B: Haricî seri direnç eklenmesi (bakım temsil koşulu)
- İkili görev: N+G = 0 (referans-geçici koşullar), K+B = 1 (bakım-temsil koşulları). Bu etiketler saha bakım kararı değil, deney protokolündeki kontrollü gruplamadır.

## Ek C — Sistemin metinsel akışı

Panel → termal sensör, I–V tarama devresi, referans ışınım ve sıcaklık sensörleri → zaman damgalı kayıt → oturum içi medyan termal ve elektriksel özellikler → eşik kuralı, termal, elektriksel ve birleşik model → yanlış alarm ve F1 karşılaştırması → rapor.

**Not:** Bu ekler önerilen içeriklerdir. TYBS'nin ek yükleme kısıtları varsa ekran kurallarına uyulmalıdır. Fotoğraf, şema veya pilot veri ancak üretildikten ve doğrulandıktan sonra eklenmelidir.
