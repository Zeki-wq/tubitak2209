# 2. Yöntem

## Araştırmanın deseni

Çalışma iki aşamalı, karşılaştırmalı nicel bir araştırmadır. Birinci aşama açık veri üzerinde bilgisayar ortamında, ikinci aşama küçük bir saha kaydı ve uç cihaz ölçümüyle yürütülecek. Bağımsız değişkenler girdi türü (yalnızca ses, ses+çevre), anomali yöntemi ve kovanın kimliğidir. Bağımlı değişkenler saatlik yanlış alarm sayısı, olaylara duyarlılık, alarmın günün saatine dağılımı ve çıkarım maliyetidir.

## 1. Açık veri hazırlığı ve temel modeller (1–3. aylar)

Veri kümesi indirilip kovan, tarih, ses dosyası ve çevresel kayıt eşleşmeleri çıkarılacak. Eksik veya bozuk kayıtlar, çok gürültülü bölümler ve zaman damgası uyuşmazlıkları belgelenip ayrı işaretlenecek. Ses kayıtları kısa pencerelere (örneğin birkaç saniye) bölünecek ve her pencere için log-mel enerjileri, MFCC'ler (Davis ve Mermelstein, 1980) ve seçili frekans bantlarının enerji oranları hesaplanacak. Çevre özellikleri olarak sıcaklık, nem, bunların kısa süreli değişimi ve günün saati kullanılacak. Günün saati, çevre etkisi ile günlük döngünün karışmaması için ayrı bir ablasyon olarak yalnızca bazı modellerde eklenecek.

Anomali tespiti yaklaşımları: (a) çok değişkenli istatistiksel sapma (ör. Mahalanobis uzaklığı), (b) tek sınıflı SVM veya Isolation Forest, (c) küçük bir otokodlayıcının yeniden oluşturma hatası (Chandola vd., 2009 anomali tespiti çerçevesine bakılacaktır). Her yöntem iki girdi biçimiyle denenecek: yalnızca ses, ses+çevre. Çevre bilgisi ayrıca "çevre koşullu" biçimde de denenecek: model, çevre verilerine bağlı beklenen ses özelliğini tahmin edecek ve alarm, gerçekle beklenen arasındaki farka göre verilecek.

Modeller her kovan için ayrı eğitilmeyecek. Eğitim, birkaç kovanın "normal" kabul edilen ortak dönemlerinden yapılacak. Test, eğitimde hiç görülmemiş kovanlar üzerinde (kovan dışarıda bırakma) yapılacak. Böylece "aynı kovanın komşu penceresini tanıma" etkisi önlenecek (Kapoor ve Narayanan, 2023).

## 2. Açık veride değerlendirme (3–4. aylar)

Veri kümesinin çıkardığımız anomali tanımına doğrudan uygun etiketi olmayabilir. Bu nedenle üç ayrı ölçüt kullanılacak.

- **Yanlış alarm yükü:** Eğitimde görülmemiş kovanların rutin dönemlerinde saatlik alarm sayısı. Duyarlılık düzeyi sabitlendiğinde (ör. eşik, kontrollü enjekte edilmiş bozulmalardan yüzde 90 yakalayacak biçimde ayarlandığında) karşılaştırılacak.
- **Kontrollü bozulma enjeksiyonu:** Normal kayıtlara bilinen dış gürültü örnekleri (rüzgâr, yağmur, motor, konuşma gibi), farklı sinyal-gürültü oranlarında eklenerek yapay anomali kümesi oluşturulacak. Bu, bir yan değerlendirmedir ve gerçek koloni anomalisinin yerini tutmadığı rapora yazılacaktır.
- **Alarmın saat dağılımı:** Alarmların günün saatlerine göre yoğunlaşıp yoğunlaşmadığı. Dağılım dengesini ölçmek için basit bir uyumsuzluk istatistiği kullanılacak.

Veri kümesinde koloni fenotip bilgileri (koloni gücü gibi) varsa, anomali skorunun fenotip değişimleriyle ilişkisi keşifsel analiz olarak ayrıca incelenecek. Bu analizden nedensellik çıkarılmayacak.

## 3. Saha kaydı (2–6. aylar)

Bir veya iki kovana, arıcının onayıyla bir ölçüm düğümü yerleştirilecek. Düğüm, kovan içine konulan bir MEMS mikrofon, kovan içi ve dışı sıcaklık-nem sensörleri, gerçek zamanlı saat ve SD kart içerecek. Düğüm pil ve küçük bir güneş paneliyle çalışacak. Mikrofon, yavru gözlerinden uzakta, bal çıtalarının üstüne yakın, arıların kolayca tıkayamayacağı bir koruma ağıyla yerleştirilecek. Yerleşimin kovana zarar vermemesi arıcıyla birlikte belirlenecek.

Kayıt planı, örneğin her on dakikada on saniyelik ses ve her dakika bir sıcaklık-nem ölçümü olacak. Bu yaklaşık günde 144 kayıt ve birkaç yüz megabayt veri eder. Pilotta örnekleme hızı (16 kHz yeterli olabilir), bellek ve pil süresi belirlenecek.

Arıcıdan, kovan açma, bakım, bal alma, besleme, ilaçlama ve gözlemlediği olağan dışı durumları tarih ve saatle bir günlüğe yazması istenecek. Biyolojik tanı koymaları beklenmeyecek. Bu günlük bir "olay etiketi" olarak kullanılacak. Müdahale zamanları, modelin tepki vermesinin beklenebileceği ve beklenmeyen zamanları ayırmamıza yarar.

## 4. Uç cihaz çıkarımı (5–7. aylar)

Açık veri ve saha verisinde en iyi sonucu veren model, bellek sınırı gözetilerek küçültülecek. Ses özellikleri cihaz üzerinde hesaplanacak ve model int8 niceleme ile çalıştırılacak (David vd., 2021). Çıkarım süresi, RAM/flash kullanımı ve saatlik ortalama akım tüketimi ölçülecek. Cihazdaki tahminlerin bilgisayardaki tahminlerle uyumu raporlanacak.

## 5. Bağımsız doğrulama ve istatistik (6–8. aylar)

Saha kaydı eğitimde kullanılmayacak, yalnızca bağımsız test için saklanacak. Saatlik yanlış alarm sayısı, olay günlüğündeki müdahalelere tepki (alarmın müdahaleden önce veya sonra kısa pencere içinde gelmesi) ve alarm dağılımı raporlanacak. Yöntemler arasındaki farklar kovan veya gün düzeyinde eşleştirilmiş farklarla ve yeniden örneklemeli yüzde 95 güven aralıklarıyla verilecek. Kovan sayısı az olduğu için p değeriyle kesin üstünlük iddia edilmeyecek, etki büyüklüğü ve örnek hatalar tartışılacaktır.

## Ön çalışma durumu

Bu metnin hazırlanması sırasında proje için veri indirildiğine, saha kaydı alındığına veya pilot sonuç elde edildiğine dair doğrulanmış bir bilgi bulunmamaktadır. Başvuru öncesinde gerçekten bir ön inceleme yapılırsa tarih ve gözlemler danışmanın kontrolüyle bu bölüme eklenecektir.
