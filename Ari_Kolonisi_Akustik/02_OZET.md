# Özet

Arı kolonisinin sesi gün boyunca ve gün içinde bile durmadan değişir. Sabah ile öğleden sonra, serin bir gece ile sıcak bir öğle aynı kovanda bile birbirinden farklı ses üretir. Bu yüzden bir kovanın sesinde "olağan dışı" bir şey aramaya kalktığımızda, sistemin bir kısım alarmı yalnızca hava sıcaklığı değiştiği için vermesi beklenir. Biz bu yanlış alarmların sıcaklık ve nem bilgisi eklenince ne kadar azaldığını araştırmak istiyoruz.

Çalışmanın ilk bölümü açık erişimli, kovan içi ses ve çevre ölçümlerini birlikte içeren bir veri kümesi üzerinde yapılacak. Yalnızca ses özelliklerine dayanan anomali modeli ile sese sıcaklık ve nemi ekleyen modeller karşılaştırılacak. Değerlendirmede aynı kovandan gelen kayıtlar eğitim ve test kümesine bölünmeyecek, model eğitimde hiç görmediği kovanlarda sınanacak. İkinci bölümde bir arıcı veya fakülte arılığı iş birliğiyle, bir veya iki kovanda ses, sıcaklık ve nem kaydı yapan düşük güçlü bir ölçüm düğümü kurulacak. Arıcı kovanla yaptığı müdahaleleri (kapak açma, bakım, bal alma) tarihli olarak not edecek. Bu notlar, anomali modelinin tepki vermesi beklenen ve beklenmeyen zamanları ayırt etmemizi sağlayacak.

Son aşamada seçilen model küçültülüp ESP32-S3 sınıfı bir mikrodenetleyicide çalıştırılacak. Bellek, çıkarım süresi ve enerji tüketimi ölçülecek. Başarı ölçütleri saatlik yanlış alarm sayısı, müdahale olaylarına duyarlılık ve bağımsız kovandaki performans kaybıdır.

Projede kovanın hasta olup olmadığı veya oğul verip vermeyeceği tahmin edilmeyecek. Bu tür iddialar için uzman doğrulamalı etiket gerekir. Sekiz ayın sonunda bir karşılaştırma raporu, saha kayıt protokolü ve paylaşılabilir bir çıkarım kodu elde edilmesi planlanıyor.

**Anahtar kelimeler:** bal arısı, kovan akustiği, anomali tespiti, yanlış alarm, sıcaklık ve nem, gömülü sistemler.
