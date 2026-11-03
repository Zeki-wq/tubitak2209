# 2. Yöntem

## Araştırmanın deseni

Çalışma iki aşamalı, karşılaştırmalı nicel bir araştırmadır. Birinci aşama açık veri üzerinde bilgisayar ortamında, ikinci aşama oda ölçekli bir test haznesinde kontrollü olay kaydıyla yürütülecek. Bağımsız değişkenler olay türü, olay şiddeti ve karar yöntemidir. Bağımlı değişkenler yanlış alarm oranı, duyarlılık, algılama gecikmesi, enerji tüketimi ve haberleşme başarısıdır.

## 1. Açık veri aşaması, Faz A (1–3. aylar)

Sensör ölçümleri ve yangın etiketi içeren açık erişimli bir duman algılama veri kümesi indirilecek. Veri kümesi, çeşitli ortamlarda (temiz hava, iç mekânda yanma denemeleri) toplanmış, sıcaklık, nem, uçucu organik bileşik, partikül ve basınç gibi sütunlar içerdiği bildirilen bir kümedir. Yapısı, oturum ayrımı, sütunlar ve lisansı ilk adımda kaynak sayfasından doğrulanacak. Ardışık satırlar yüksek oranda benzer olduğu için rastgele satır bölmesi kullanılmayacak. Mümkünse kayıt oturumu, değilse uzun zaman blokları aynı veri bölmesinde tutulacak (Kapoor ve Narayanan, 2023).

Bu veride üç yaklaşım karşılaştırılacak: tek sensör eşiği (örneğin yalnızca PM2.5), basit çok sensörlü kural ve zamansal özelliklerle hafif model. Veri kümesindeki etiketler yalnızca yangın var/yok içerdiği için bu aşamada olay türü bazında analiz yapılamayacak. Bu, ikinci aşamanın gerekçesidir.

## 2. Düğüm, hazne ve pilot ölçüm (1–2. aylar)

İki ölçüm düğümü kurulacak. Her düğümde lazer saçılımlı ve boyut aralıklarına göre sayım veren bir partikül sensörü, gaz ve ortam sensörü (sıcaklık, nem, basınç, gaz direnci), ayrıca CO ve yanıcı gaz/duman duyarlı ucuz modüller bulunacak. Düğümler saniyede bir ölçüm alacak ve veriyi hem SD karta hem LoRa ile ağ geçidine yollayacak. Ağ geçidi bilgisayara bağlı bir mikrodenetleyicidir.

Test haznesi, yanmaz plaka ve cam/şeffaf yüzeylerden yapılmış, yaklaşık bir metreküplük, içeride küçük fan ve dışarı egzoz hattı bulunan bir kutu olacak. Hazneye bağımsız iki ticari duman alarmı yerleştirilecek. Alarm sesi, hazne dışında bir mikrofon ve mikrodenetleyici yardımıyla algılanıp zaman damgasıyla kaydedilecek.

Pilotta sensörlerin gürültü düzeyi, ısınma süreleri, hazne temizlenme süresi, fan etkisi ve referans alarmların tepki süresi ölçülecek. MQ tipi modüllerin ısıtıcıları fazla akım çektiği için bu sensörlerin düğümün pil süresine etkisi ayrıca incelenecek.

## 3. Olay kaydı, Faz B (2–5. aylar)

Olay türleri şunlardır:

- **0, arka plan:** Hazne temiz havada, fan çalışır ve durur durumda.
- **1, buhar:** Ultrasonik nemlendirici veya sıcak su buharı.
- **2, pişirme aerosolü:** Mutfaktan alınmış, kontrollü miktarda kızartma buharı.
- **3, toz:** Küçük miktarda un veya benzeri zararsız toz savurma.
- **4, su bazlı sprey:** Yanıcı gaz içermeyen, su bazlı bir oda spreyi.
- **5, sıcaklık sıçraması:** Fan ısıtıcıyla ısıtılmış hava.
- **6, yanmasız sis:** Gliserin bazlı sis üreteci, yanmasız bir test aerosolü.
- **7, yanma kaynaklı duman:** Çok küçük, kontrollü ve gözetimli ısıl bozunma. Örneğin bir tütsü çubuğunun yanması. Bu, standart test yangınlarının yerini tutmaz ve EN 54-7 testi sayılmaz.

Her tür iki şiddet düzeyinde (örneğin düşük ve yüksek miktar) ve beş ayrı günde uygulanacak. Toplam 8 × 2 × 5 = 80 olay kaydı. Her kaydın başında ve sonunda temiz hava dönemi bırakılacak, hazne her olaydan sonra havalandırılıp sensörlerin temel değere dönmesi beklenecek. Olay başlangıç ve bitiş anları, elle işlenen bir kayıt formuyla not edilecek. Sıra rastgele belirlenecek.

**Güvenlik:** Yanma kaynaklı duman deneyi yalnızca laboratuvar/yangın güvenliği sorumlusunun yazılı onayı olduğunda yapılacak. Hazne yanmaz bir yüzeyde ve havalandırması olan bir ortamda tutulacak. Yanıcı sıvı veya basınçlı yanıcı aerosol kullanılmayacak. Her denemede bir kişi dışarıda bir söndürme aracıyla gözetim yapacak, bir CO kişisel uyarı cihazı bulunacak. Küçük bir tütsü çubuğu dışında yanma kaynağı kullanılmayacak. Onay çıkmazsa bu olay türü Faz B'den çıkarılacak ve yanma sınıfı Faz A'daki açık veriden alınacak.

## 4. Özellik çıkarımı ve karar yöntemleri (4–6. aylar)

Saniyelik veriden 10–30 saniyelik kayan pencerelerle özellikler çıkarılacak: PM1.0, PM2.5 ve sayım aralıkları arasındaki oranlar, partikül sayısının eğimi, CO ve gaz direnci eğimleri, sıcaklık-nem değişimi ve nem-sıcaklık ilişkisi. Ölçekleme değerleri yalnızca eğitim kümesinden öğrenilecek.

Karşılaştırılan yöntemler:

- **Y1, tek sensör eşiği:** Örneğin PM2.5 değeri belirli bir süre eşiği aşarsa alarm.
- **Y2, çok sensörlü kural:** Partikül ve gazdan en az ikisinin belirli süre birlikte artması.
- **Y3, zamansal özellikli hafif model:** Lojistik regresyon ve Random Forest ile başlanacak.
- **Y4, uç cihaz modeli:** Y3'ün küçültülmüş (int8) hali, ESP32 üzerinde çalıştırılacak (David vd., 2021).

Alarm eşikleri eğitim kümesinden, belirlenmiş bir duyarlılık düzeyinde (örneğin yanma olaylarının en az yüzde 90'ında alarm) seçilecek. Böylece yöntemler eşit duyarlılıkta yanlış alarm açısından karşılaştırılabilecek. Test verisi bu seçimde kullanılmayacak.

## 5. Değerlendirme ve istatistik (5–8. aylar)

Bir olay kaydından çıkan tüm pencereler aynı veri bölmesinde tutulacak. Nihai test, eğitimde hiç görülmemiş günlerin olay kayıtlarıyla yapılacak. Ek olarak her duman benzeri olay türü sırayla eğitim dışında bırakılarak "bir olay türünü dışarıda bırak" dayanıklılık deneyi yapılacak.

Birincil ölçüt, sabit duyarlılıkta duman benzeri olay kayıtlarında yanlış alarm veren kayıt oranıdır. İkincil ölçütler algılama gecikmesi (yanma başlangıcından alarma, ayrıca referans alarma göre fark), olay türü bazında karışıklık matrisi, düğüm saatlik enerji tüketimi ve LoRa paket teslim oranıdır. Farklar, olay kaydı düzeyinde eşleştirilmiş ve yeniden örneklemeli yüzde 95 güven aralığıyla raporlanacak. Olay sayısı az olduğundan p değeriyle kesin üstünlük iddia edilmeyecek, etki büyüklüğü ve hata örnekleri tartışılacak.

LoRa paket teslim oranı, düğüm ile ağ geçidi arasındaki farklı mesafelerde (örneğin bina içinde farklı odalar) ölçülecek. Kullanılacak frekans ve çıkış gücü, ilgili düzenlemelere uygun olacak.

## Ön çalışma durumu

Bu metnin hazırlanması sırasında proje için veri indirildiğine, düzeneğin kurulduğuna, olay kaydı alındığına veya pilot sonuç elde edildiğine dair doğrulanmış bir bilgi bulunmamaktadır. Başvuru öncesinde gerçekten bir ön inceleme yapılırsa tarih ve gözlemler danışmanın kontrolüyle bu bölüme eklenecektir.
