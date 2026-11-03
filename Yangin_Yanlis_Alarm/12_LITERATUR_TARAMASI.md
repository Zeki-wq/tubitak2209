# Literatür Taraması

> **Durum:** Bu dosya iki parçadır. Birinci parça, elimizdeki kaynaklardan kurulan çerçevedir. İkinci parça, başvuru öncesi sistematik taramanın planıdır. Tarama henüz yapılmadı; "boşluk" ya da "ilk kez" iddiası kurulmadı.

## 1. Çerçeve

| Başlık | Kaynak | Bu projedeki rolü | Teyit durumu |
|---|---|---|---|
| Gaz sensörleriyle yangın tespiti ve yanlış alarm | Fonollosa vd. (2018) | Çok değişkenli veri işlemenin neden gerektiğini ve yanlış alarm sorununu özetleyen derleme | Yazar, dergi ve DOI web aramasıyla doğrulandı; tam metin okunacak |
| Nokta tipi duman dedektörleri ve test yangınları | EN 54-7 | Projenin kapsam sınırı: standart test yangınlarını yeniden üretmiyoruz | Yayın yılı ve baskı kurum erişiminden teyit edilecek |
| Açık duman algılama veri kümesi | Blattmann (t.y.), Kaggle | Faz A | **Sahibi, yılı, lisansı, oturum yapısı kaynak sayfasından doğrulanacak** |
| Uç cihazda model | David vd. (2021) | TFLite Micro | Künye teyit edilecek |
| LoRa | Augustin vd. (2016) | Haberleşme özellikleri | Künye teyit edilecek |
| Makine öğrenmesi araçları | Pedregosa vd. (2011) | Lojistik regresyon, RF | Teyit edilecek |
| Veri sızıntısı | Kapoor ve Narayanan (2023) | Oturum bazlı bölme | DOI teyit edilecek |

## 2. Konumlandırma (hipotez düzeyinde)

Duman alarmlarının buhar, pişirme ve toz gibi yanma dışı kaynaklarla yanlış alarm verdiği bilinen bir sorundur. Bu projenin eksenleri: (i) yanma dışı olay türlerini **tek tek ve iki şiddet düzeyinde** kaydetmek, (ii) yöntemleri **sabit duyarlılıkta** karşılaştırmak, böylece "daha çok alarm = daha duyarlı" yanılgısından kaçınmak, (iii) iki ticari alarmı aynı olaylarda referans almak, (iv) uç cihaz enerji ve LoRa teslim oranını ölçmek. Sertifikalı bir yangın alarmı geliştirdiğimiz iddiası yoktur ve olmayacaktır.

Bu eksenlerin önceki çalışmalarda nasıl ele alındığı taramada bakılacak.

## 3. Planlanan sistematik tarama

**Veri tabanları:** Web of Science, Scopus, IEEE Xplore, Google Scholar, TR Dizin. Standartlar için TSE ve CEN katalogları.

**Arama dizileri:**
- `("smoke detection" OR "fire detection") AND ("false alarm" OR "nuisance alarm") AND ("multi-sensor" OR "sensor fusion")`
- `("steam" OR "cooking" OR "dust") AND "smoke detector" AND ("false alarm")`
- `("particulate matter" OR "PM2.5") AND "fire detection" AND "machine learning" AND "embedded"`
- `"LoRa" AND "fire" AND ("early detection" OR "wireless sensor")`

**Türkçe:** "yangın algılama", "yanlış alarm", "duman dedektörü", "çok sensörlü".

**Dahil etme:** Yanma dışı olay türlerini ayrı ele alan veya yanlış alarm oranını açıkça raporlayan deneysel çalışmalar. **Dışlama:** Görüntü tabanlı (kamera) yangın tespiti kapsam dışıdır.

**Kayıt tablosu:**

| Künye | Sensörler | Olay türleri | Yanlış alarm kaynakları ayrı mı? | Bölme (oturum/rastgele) | Duyarlılık sabitlendi mi? | Sınırlılık |
|---|---|---|---|---|---|---|

## 4. Tarama sonrası yazılacak sorular

1. Yöntemler aynı duyarlılıkta mı karşılaştırılmış?
2. Ardışık saniyelik satırlar rastgele dağıtılıp başarı abartılmış mı?
3. Bir olay türü eğitimden çıkarılarak genelleme sınanmış mı?
4. Enerji ve haberleşme maliyeti raporlanmış mı?

## 5. Güvenlik notu

Yanma kaynaklı duman deneyi yalnızca laboratuvar veya yangın güvenliği sorumlusunun yazılı onayıyla yapılır. Onay çıkmazsa bu olay türü Faz B'den çıkarılır ve yanma sınıfı açık veriden alınır.
