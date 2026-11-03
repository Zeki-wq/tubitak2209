# 5. Belirtmek İstediğiniz Diğer Konular

Çalışmada üç ayrı soruyu birbirine karıştırmayacağız. Bağlantının bozuk olup olmadığı, ne kadar erken uyarı verildiği ve bu uyarının kaç yanlış alarmla geldiği ayrı ayrı ölçülecek. Erken uyarı süresi yanlış uyarı bedeli olmadan tek başına başarı sayılmayacaktır.

Kapsam dışı olanlar: şebeke gerilimi ve alternatif akım, ark oluşumu, uzun süreli yaşlanma, yangın çıkarma testi ve gerçek tesisat panoları. Deneyler kasıtlı olarak tehlikeli sıcaklığa çıkmayacak biçimde tasarlandı. Bu sınırın dışında bir deney yapılmayacaktır.

Sonuçların bir koruma cihazına dönüştürülmesi, ayrı standartlara ve sertifikasyona tabidir. Proje bunu hedeflemiyor.

# 6. Ekler

## Ek A — Örnek koşu kayıt formu

| Alan | Kaydedilecek değer |
|---|---|
| Koşu kodu | KSU_001 |
| Tarih ve saat | [KAYIT SIRASINDA] |
| Temas düzeyi | Tam sıkılı / gevşek-1 / gevşek-2 / gevşek-3 (tork değeri not edilir) |
| Seri direnç referansı | Yok / [değer] |
| Akım profili | Sabit / basamaklı, nominal akım değeri |
| Hava akışı | Fan kapalı / açık |
| Ortam sıcaklığı | [ÖLÇÜLEN] |
| Başlangıç bağlantı sıcaklığı | [ÖLÇÜLEN] |
| Sabit alarm eşiği | [PİLOTLA BELİRLENEN] |
| Kesme nedeni | Zaman sınırı / güvenlik sınırı / normal bitiş |
| Gözlem | [NOT] |

## Ek B — Örnek etiketler

- 0: Normal bağlantı
- 1: Gevşek-1
- 2: Gevşek-2
- 3: Gevşek-3
- Ayrıca her pencere için: sabit eşiğin aşılmasına kalan süre (saniye)

## Ek C — Sistemin metinsel akışı

Akım sınırlı kaynak → test bağlantısı → akım, gerilim düşümü ve sıcaklık ölçümü → zaman damgalı kayıt → özellik çıkarımı → dört karar yöntemi → erken uyarı süresi ve yanlış uyarı karşılaştırması → rapor.

**Not:** Bu ekler önerilen içeriklerdir. TYBS'nin ek yükleme kısıtları varsa ekran kurallarına uyulmalıdır. Fotoğraf, şema veya pilot veri ancak üretildikten ve doğrulandıktan sonra eklenmelidir.
