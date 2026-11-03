# 2. Yöntem

## Araştırmanın deseni

Çalışma, kontrollü laboratuvar deneyine dayalı karşılaştırmalı nicel araştırma olarak planlandı. Bağımsız değişkenler kaçak durumu, kaçak konumu, kaçak açıklığı, akış/debi düzeyi, ek mekanik gürültü ve kullanılan sensör grubu olacaktır. Bağımlı değişkenler kaçak tespit başarısı, bölgesel konumlandırma başarısı, yanlış alarm oranı ve karar süresidir. Deneyler mümkün olduğunca aynı boru, pompa, sensör sabitleme yöntemi ve veri kayıt altyapısıyla yürütülecektir.

## 1. Deney düzeneği ve ilk ölçümler (1–2. aylar)

Kapalı devre çalışan bir su deposu, düşük gerilimli pompa, plastik boru hattı ve kontrollü açılıp kapanabilen üç kaçak çıkışı hazırlanacaktır. Kaçak noktaları K1, K2 ve K3 olarak etiketlenecektir. Sensörlerin hat üzerindeki mesafeleri ölçülerek kayıt altına alınacaktır. Akustik algılayıcılar boruya temas edecek biçimde sabitlenecek, basınç sensörü ise uygun bağlantı elemanıyla hatta yerleştirilecektir. Basınç sensörünün yalnızca yavaş değişimleri ölçmesi durumunda yüksek frekanslı basınç dalgası analizi yapılmayacak, ortalama ve değişim eğilimi gibi özellikler kullanılacaktır. Akustik algılayıcının kullanılabilir bant genişliği ve sensör montajının tekrarlanabilirliği pilot ölçümlerde incelenecektir.

Ölçüm düğümlerinde mikrodenetleyici kullanılacaktır. Veriler bir bilgisayara ya da kurumdaki mevcut küçük ölçekli işlem birimine aktarılacaktır. Ayrı bir tek kart bilgisayarın satın alınması bu deneyin zorunlu koşulu değildir. Analizler bilgisayarda yapılacak, kaynak gereksinimi uygun olan basit karar yöntemi mikrodenetleyici üzerinde ayrıca denenecektir.

## 2. Deney koşulları ve veri toplama (3–4. aylar)

Normal akış ve K1, K2, K3 kaçak bölgeleri kaydedilecektir. İlk plan iki debi düzeyi, iki mekanik gürültü durumu ve her koşul için en az beş bağımsız tekrar yapılmasıdır. Tam faktöriyel plan buna göre 4 durum × 2 debi × 2 gürültü × 5 tekrar = 80 kayıt oturumu oluşturur. Her oturumun süresi pilot deneyden sonra belirlenecek, başlangıç hedefi 30 saniyedir. Uygun görülürse kaçak açıklığının iki seviyesi ek bir deney serisinde incelenecektir. Veri dosyası adı veya eşlik eden kayıt tablosu; tarih, sensör, debi, kaçak noktası, kaçak açıklığı, gürültü ve deney tekrarını içerecektir.

Değişkenlerin birbirine karışmaması için ölçümler önceden hazırlanmış bir sırayla ve oturumlar arasında sistemin kararlı duruma ulaşması beklenerek yapılacaktır. Normal duruma ait ölçümler yalnızca deney başlangıcında değil, farklı zamanlarda da alınacaktır. Böylece zamanla değişen pompa davranışının belirli bir sınıfla karışması azaltılacaktır.

## 3. Sinyal işleme ve özellik çıkarımı (4–5. aylar)

Akustik kayıtlarda uygun filtreleme sonrasında kısa zaman pencerelerinden RMS, varyans, spektral enerji ve seçili frekans bantlarının enerji oranı çıkarılacaktır. Basınç verisinde ortalama, standart sapma, değişim hızı ve pencere içi minimum-maksimum farkı hesaplanacaktır. Özellikler yalnızca eğitim verisinden öğrenilen ölçekleme değerleriyle dönüştürülecektir. Akustik, basınç ve birleşik özellik kümeleri ayrı ayrı oluşturulacaktır.

Öncelikle sensör düzeyinde basit eşikler ve lojistik regresyon gibi yorumlanabilir başlangıç yöntemleri denenecektir. Ardından Random Forest modeli karşılaştırmaya eklenecektir. Veri miktarı yeterli olmadığı takdirde karmaşık derin öğrenme mimarileri kullanılmayacaktır. Böylece küçük bir veri kümesinde yanıltıcı derecede yüksek eğitim başarısı üretme riski azaltılacaktır.

## 4. Eğitim, test ve istatistiksel değerlendirme (5–7. aylar)

Bir oturumdan çıkarılan pencerelerin tümü aynı veri bölmesinde tutulacaktır. Özellikle test ölçümleri, eğitimde kullanılmayan bağımsız kayıt oturumlarından seçilecektir. Model seçimi ve hiperparametre ayarı eğitim kümesinde grup bazlı çapraz doğrulamayla yapılacaktır. Nihai test kümesi model seçimi sırasında kullanılmayacaktır. Ayrıca mümkünse bir debi/gürültü koşulunun eğitim dışında bırakıldığı ek dayanıklılık deneyi yapılacaktır.

Birinci görev, **kaçak var/yok** ikili sınıflandırmasıdır. İkinci görev, **kaçak bulunduğunda K1/K2/K3 bölgesini belirleme** olarak ele alınacaktır. Gerektiğinde dört sınıflı tek aşamalı sınıflandırma da ek analiz olarak raporlanacaktır. Birincil değerlendirme makro F1 skoru, dengeli doğruluk ve karışıklık matrisi olacaktır. Yanlış alarm oranı, duyarlılık ve test karar gecikmesi de verilecektir.

Sensör grupları arasındaki farklar aynı test oturumlarında ölçülecektir. Sonuçlar için oturum düzeyinde eşleştirilmiş farklar ve yeniden örneklemeli yüzde 95 güven aralıkları raporlanacaktır. Çok az oturum bulunursa p-değeri üzerinden kesin üstünlük iddia edilmeyecektir. Bunun yerine etki büyüklüğü, güven aralığı ve hata örnekleri değerlendirilecektir. Aghashahi ve arkadaşlarının (2023) çok koşullu deney yaklaşımı ile Chew ve arkadaşlarının (2023) ölçüm kalitesi ve özellik çıkarımına verdiği önem yöntem planı açısından yol göstericidir.

## 5. Son doğrulama ve analiz (7–8. aylar)

En iyi yaklaşımın farklı günlerde tekrarlanan ölçümlerde nasıl davrandığı kontrol edilecektir. Sonuçlar sensör maliyeti, elde edilen kazanç ve hatalı kararlar açısından yorumlanacaktır. Sensörün boruya sabitlenme biçimi, farklı boru malzemeleri, gerçek şebeke basınçları ve çevre koşulları çalışmanın sınırlılıkları arasında tartışılacaktır. Küçük ölçekli deneyden elde edilen başarının gerçek şehir şebekesinde aynı olacağı ileri sürülmeyecektir.

## Ön çalışma durumu

Bu metnin hazırlanması sırasında proje için veri toplandığına, donanımın kurulduğuna veya pilot performans elde edildiğine ilişkin doğrulanmış bir bilgi bulunmamaktadır. Başvuru öncesinde gerçekten pilot ölçüm yapılırsa tarih, düzenek ve gözlem sonuçları danışmanın kontrolüyle bu bölüme eklenecektir.
