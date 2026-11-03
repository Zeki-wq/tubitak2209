# 2. Yöntem

## Araştırmanın deseni

Çalışma, açık havada kontrollü koşullarda yapılan, karşılaştırmalı nicel bir deneydir. Bağımsız değişkenler panel durumu, anomalinin şiddeti, ışınım bandı ve kullanılan sensör grubudur. Bağımlı değişkenler geçici gölgelenmenin bakım gerektiren sınıfa atanma oranı, makro F1, duyarlılık, çıkarım süresi ve enerji tüketimidir. Aynı panel, aynı eğim ve yönelim, aynı ölçüm devresi ve aynı kayıt altyapısı kullanılacaktır.

## 1. Düzenek ve pilot ölçüm (1–2. aylar)

Küçük, 12 V sınıfı bir monokristal panel sabit bir standa, ölçüm yapılacak eğimde ve güneye bakacak şekilde yerleştirilecek. Termal sensör panelin tamamını görecek mesafede ve sabit açıda sabitlenecek, yüzeyden yansıyan sıcak cisim ve rüzgârdan etkilenmesini azaltacak bir konum seçilecek. Panelin arka yüzeyine iki küçük sıcaklık sensörü yapıştırılacak. Referans ışınım için ayrı bir küçük hücre ve ışık sensörü panele paralel konumlandırılacak.

I–V eğrisi, panelin ucuna bağlı bir güç MOSFET'i ile yapılacak. MOSFET'in kapı gerilimi kademeli artırılarak panel kısa devreden açık devreye taranacak, gerilim ve akım hassas bir ölçüm modülüyle okunacak. Tek bir tarama kısa süreceği için ışınımın tarama içinde değişmediği varsayılabilecek. Her oturumda her on saniyede bir tarama yapılacak. Bu devre bir güç elektroniği ürünü değil, ölçüm aracıdır. Panel gücü küçük olduğu için akım ve ısı düzeyi güvenli sınırdadır.

Pilotta şunlar ölçülecektir: termal sensörün gürültüsü ve en küçük ayırt edilebilir sıcak nokta alanı, ışık sensörünün panel akımıyla ilişkisi, I–V taramasının tekrarlanabilirliği ve panelin ısınma süresi. Elimizde güvenilir bir referans termal kamera (kurumdan) varsa, birkaç oturumda sensör çıktısıyla karşılaştırma yapılacaktır.

## 2. Deney koşulları ve veri toplama (3–5. aylar)

Dört durum şu biçimde oluşturulacaktır:

- **N, normal:** Hiçbir müdahale yok.
- **G, geçici gölgelenme:** Panelin bir hücre sırasının belirli bir oranı opak bir kartla kapatılır. Üç oran denenir (yaklaşık yüzde 10, 25 ve 50 hücre alanı). Gölgelenme her oturumda kısa tutulur.
- **K, kalıcı yüzey kirlenmesi:** Panelin bir bölgesine yarı saydam bir film veya benzeri bir malzeme yapıştırılarak ışık geçirgenliği azaltılır. Geri alınabilir bir yöntemdir. İki yoğunluk denenir.
- **B, seri direnç artışı:** Panelin çıkışına küçük, bilinen bir seri direnç eklenir. Üç değer denenir. Bu, bağlantı direncinin artmasının elektriksel etkisini temsil eder.

Toplam koşul sayısı 1 + 3 + 2 + 3 = 9'dur. Bunlar iki ışınım bandında (referans hücreyle ölçülen yüksek ve orta ışınım) ve her biri en az beş ayrı günde tekrarlanır. 9 × 2 × 5 = 90 oturum eder. Her oturum yaklaşık üç dakika sürer. Termal kareler birkaç saniyede bir, I–V taramaları on saniyede bir alınır.

Yüzeyin ısıl dengeye gelmesi için koşullar arasında bekleme süresi bırakılacak, koşul sırası rastgele belirlenecek, rüzgâr ve bulut durumu kaydedilecektir. Bulutlu veya ışınımın çok değiştiği oturumlar işaretlenip ayrı değerlendirilecektir.

## 3. Özellik çıkarımı (4–6. aylar)

Termal karelerden en sıcak bölgenin panel ortalamasından farkı, sıcak bölge alan oranı, uzaysal standart sapma ve sıcak bölgenin konumu çıkarılacaktır. I–V eğrilerinden kısa devre akımı, açık devre gerilimi, maksimum güç noktası, doluluk oranı ve eğimden seri direnç kestirimi hesaplanacak. Elektriksel değerler referans ışınım ve panel sıcaklığına göre normalleştirilecektir. Ölçekleme değerleri yalnızca eğitim kümesinden öğrenilecektir.

## 4. Modeller ve değerlendirme (5–8. aylar)

Karşılaştırılacak yaklaşımlar şunlardır: sıcak nokta eşik kuralı (referans), yalnızca termal özelliklerle, yalnızca elektriksel özelliklerle ve birleşik özelliklerle eğitilmiş modeller. Başlangıçta lojistik regresyon ve Random Forest kullanılacak. Veri az olduğu için karmaşık derin öğrenme mimarileri denenmeyecektir.

İki görev tanımlanıyor. Birincisi ikili görev: "bakım gerektiren (K veya B)" ile "gerektirmeyen (N veya G)". İkincisi dört sınıflı ayrım. Birincil ölçüt, gölgelenme oturumlarının bakım gerektiren sınıfa atanma oranıdır. İkincil ölçütler makro F1, duyarlılık, özgüllük ve karışıklık matrisidir.

Bir oturumdan çıkan tüm pencereler ve aynı gündeki tüm oturumlar aynı veri bölmesinde tutulacak. Model seçimi gruplanmış çapraz doğrulamayla yapılacak, nihai test model seçiminde kullanılmayan günlerden seçilecektir. Ayrıca bir ışınım bandının eğitim dışında bırakıldığı dayanıklılık deneyi yapılacak. Farklar, oturum düzeyinde eşleştirilmiş ve yeniden örneklemeli yüzde 95 güven aralığıyla verilecektir. Oturum sayısı az kalırsa kesin üstünlük iddiası yerine etki büyüklüğü ve hata örnekleri tartışılacaktır.

Son olarak birleşik modelin tek kart bilgisayarda ortalama çıkarım süresi ve bir ölçüm döngüsünün enerjisi ölçülecektir.

## Ön çalışma durumu

Bu metnin hazırlanması sırasında proje için veri toplandığına, düzeneğin kurulduğuna veya pilot sonuç alındığına dair doğrulanmış bir bilgi yoktur. Başvuru öncesinde gerçekten pilot yapılırsa tarih, düzenek ve gözlemler danışmanın kontrolüyle bu bölüme eklenecektir.
