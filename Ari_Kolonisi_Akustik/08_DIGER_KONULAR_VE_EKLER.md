# 5. Belirtmek İstediğiniz Diğer Konular

Bu çalışmada "anomali" kelimesi dar anlamıyla kullanılıyor: kovanın ses ve çevre örüntüsünden istatistiksel sapma. Sapmanın biyolojik karşılığı aranmıyor. Hastalık, oğul verme ve ana arı kaybı gibi durumlar bu projenin hedefi değildir ve bu konuda hiçbir sonuç iddia edilmeyecektir.

Sensörler kovan içinde pasif olarak çalışacak ve kolonide davranışsal bir değişiklik yaratmamaları için en az müdahale ilkesiyle yerleştirilecek. Arıcı herhangi bir rahatsızlık gözlerse sensör geri alınacaktır. Arılığın bulunduğu yerleşim yerinde başkalarının sesi kaydedilebileceği ihtimaline karşı, mikrofon kovan içine yerleştirilecek ve konuşma gibi içerikler analiz dışı bırakılacak ya da kayıtlardan silinecektir. Kişisel veri toplanması planlanmamaktadır.

Kapsam dışı olanlar: kovanı açmadan hastalık teşhisi, ana arı tespiti, bal veriminin tahmini ve ticari ürün geliştirme.

# 6. Ekler

## Ek A — Örnek saha kayıt ve olay günlüğü formu

| Alan | Kaydedilecek değer |
|---|---|
| Kovan kodu | KVN_01 |
| Tarih ve saat | [KAYIT SIRASINDA] |
| Olay türü | Kovan açma / bakım / bal alma / besleme / ilaçlama / olağan dışı gözlem / olay yok |
| Olay süresi | [DAKİKA] |
| Hava durumu notu | [GÖZLEM] |
| Cihaz durumu | Pil seviyesi, SD kart doluluğu |
| Gözlem | [NOT] |

## Ek B — Örnek veri etiketleri

- Rutin dönem: arıcı müdahalesi ve olağan dışı gözlem yok
- Müdahale dönemi: olaydan önce ve sonra tanımlı pencere
- Enjekte edilmiş bozulma: dış gürültü türü ve sinyal-gürültü oranı (yalnızca açık veri analizinde)

## Ek C — Sistemin metinsel akışı

Kovan ses kaydı + sıcaklık ve nem → zaman damgalı kayıt → ses ve çevre özellikleri → ses-only ve ses+çevre anomali modelleri → yanlış alarm, olay tepkisi ve saat dağılımı değerlendirmesi → küçültülmüş modelin mikrodenetleyicide çalıştırılması → rapor.

**Not:** Bu ekler önerilen içeriklerdir. TYBS'nin ek yükleme kısıtları varsa ekran kurallarına uyulmalıdır. Arıcı iş birliğini gösteren onay yazısı, TYBS izin veriyorsa ek olarak eklenmelidir. Fotoğraf, şema veya gerçek kayıt ancak üretildikten ve doğrulandıktan sonra eklenmelidir.
