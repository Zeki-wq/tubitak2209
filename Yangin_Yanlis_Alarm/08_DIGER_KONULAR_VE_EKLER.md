# 5. Belirtmek İstediğiniz Diğer Konular

Bu çalışma yangın tespit performansını ölçmeyi hedeflemiyor. Odak yanlış alarmdır ve yanma kaynaklı duman, karşılaştırmada bir referans sınıf olarak yer alıyor. Küçük, kontrollü ve gözetimli bir ısıl bozunma kaynağı gerçek bir yangını, yangın gelişimini veya farklı yakıt türlerini temsil etmez. Sonuçlar oda ölçekli bir hazne için geçerlidir ve orman, bina veya endüstriyel ortam gibi koşullara genellenmeyecektir.

Standart yangın testleri (örneğin EN 54-7 kapsamındaki test yangınları) sertifikalı laboratuvarlarda yapılır. Bu projede onların yerine geçecek bir test iddiası yoktur. Kendi referans alarmımız bağımsız iki ticari dedektördür ve yalnızca alarm anını belirleme amacıyla kullanılır.

Güvenlik bu projenin ayrı bir bileşenidir. Yanma içeren her deneme önceden onaylanmış alanda, küçük miktarla, gözetimle ve havalandırmayla yapılacak, onay yoksa yapılmayacaktır. Yanıcı sıvı, basınçlı yanıcı aerosol ve açık alevli yakıt kullanılmayacaktır.

Kapsam dışı olanlar: orman yangını, saha tespiti, yangın söndürme kontrolü, sertifikasyon testi ve ticari ürün geliştirme.

# 6. Ekler

## Ek A — Örnek olay kayıt formu

| Alan | Kaydedilecek değer |
|---|---|
| Olay kodu | OLY_001 |
| Tarih ve saat | [KAYIT SIRASINDA] |
| Olay türü | 0–7 |
| Şiddet düzeyi | Düşük / yüksek (miktar) |
| Olay başlangıç ve bitiş saati | [KAYIT] |
| Referans alarm 1 ve 2 çalış saati | [KAYIT] |
| Hazne sıcaklığı ve nemi (başlangıç) | [ÖLÇÜLEN] |
| Fan durumu | Açık / kapalı |
| Temel değere dönüş süresi | [ÖLÇÜLEN] |
| Gözlem ve olağan dışı durum | [NOT] |

## Ek B — Örnek sınıf etiketleri

- 0: Arka plan
- 1: Buhar
- 2: Pişirme aerosolü
- 3: Toz
- 4: Su bazlı sprey
- 5: Sıcaklık sıçraması
- 6: Yanmasız sis
- 7: Yanma kaynaklı duman
- İkili görev: 7 = 1 (alarm gerekir), 0–6 = 0

## Ek C — Sistemin metinsel akışı

Test haznesi + olay kaynağı → iki ölçüm düğümü (partikül, gaz, sıcaklık-nem) + referans alarmlar → zaman damgalı kayıt (SD kart ve LoRa) → özellik çıkarımı → tek sensör eşiği, çok sensörlü kural, zamansal model, uç cihaz modeli → sabit duyarlılıkta yanlış alarm, gecikme, enerji ve paket teslim karşılaştırması → rapor.

**Not:** Bu ekler önerilen içeriklerdir. TYBS'nin ek yükleme kısıtları varsa ekran kurallarına uyulmalıdır. Güvenlik onay yazısı, TYBS izin veriyorsa ek olarak eklenmelidir. Fotoğraf, şema veya gerçek veri ancak üretildikten ve doğrulandıktan sonra eklenmelidir.
