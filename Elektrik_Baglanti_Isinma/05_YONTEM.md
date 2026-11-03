# 2. Yöntem

## Araştırmanın deseni

Çalışma, kontrollü laboratuvar deneyine dayalı karşılaştırmalı nicel bir araştırmadır. Bağımsız değişkenler temas düzeyi, akım profili, hava akışı ve kullanılan karar yöntemidir. Bağımlı değişkenler erken uyarı süresi, yanlış uyarı sayısı, duyarlılık, sıcaklık tahmin hatası ve çıkarım maliyetidir. Bütün koşullarda aynı bağlantı elemanı tipi, aynı kablo, aynı sensör yerleşimi ve aynı kayıt altyapısı kullanılacaktır.

## 1. Düzenek, güvenlik ve pilot ölçüm (1–2. aylar)

Düzenek şu parçalardan oluşur: akım sınırlamalı ayarlanabilir doğru akım kaynağı, güç dirençlerinden kurulu yük, test edilecek vidalı bağlantı (klemens) ve ölçüm düğümü. Bağlantının iki yanına ince telli K tipi termokupllar, bağlantı uçlarının arasına ise kelvin (dört telli) usulüyle gerilim ölçümü bağlanacak. Akım, hassas bir şönt direnci üzerinden okunacak. Ortam sıcaklığı için ayrı bir sensör kullanılacak. Veriler mikrodenetleyiciden bilgisayara zaman damgalı aktarılacak.

Temas düzeyi iki yolla değiştirilecek. Birincisi, bağlantı vidasının tork anahtarıyla bilinen farklı değerlere ayarlanmasıdır (tam sıkılı, gevşek-1, gevşek-2, gevşek-3). Böylece gerçek bir gevşek bağlantı koşulu oluşur. İkincisi, referans amacıyla bağlantıya seri küçük bir direnç eklenmesidir. Bu, gevşekliğin ürettiği rastgeleliği ayırıp ısınma modelini kontrollü bir kaynakla sınamamıza yarar. Tork düzeyleri pilotta denenecek ve her düzeyin yaklaşık direnç aralığı kayıt altına alınacaktır.

Güvenlik katmanları şöyle planlandı. Güç kaynağında akım sınırı, düzenekte bağımsız bir mekanik termostat, ayrıca mikrodenetleyiciden yazılımla kesme yer alacak. Mutlak sıcaklık sınırı 60 °C olarak önerilmektedir ve her koşu bu sınıra ulaşmadan sonlandırılacaktır. Deney çalışırken ortamda yanıcı malzeme bulunmayacak, düzeneğin yanında her zaman bir kişi olacak ve çalışma laboratuvar sorumlusunun bilgisi dahilinde yürütülecek. Pilotta sabit alarm eşiği başlangıç olarak ortamın 25 K üzerine (örneğin 50 °C) ayarlanacak ve kesinleştirilecektir.

Pilotta sensörlerin gürültüsü, termokupl zaman sabiti, örnekleme hızının yeterliliği ve koşular arası soğuma süresi ölçülecektir. Ortam sıcaklığına dönmeden yeni koşu başlatılmayacaktır.

## 2. Deney koşulları ve veri toplama (3–5. aylar)

Ana deney planı 4 temas düzeyi × 2 akım profili × 2 hava akışı × 5 tekrardır. Bu, 80 koşu eder. Akım profillerinden biri sabit akım, diğeri bir basamaklı akımdır (örneğin ortada akımın yaklaşık yüzde 30 artması). Hava akışı durumları fan kapalı ve açık biçimindedir. Normal bağlantı koşulları da akım basamağı ve fan değişimini içerdiği için model, gevşek bağlantıyla ilgisiz sıcaklık değişimleriyle karşılaşacaktır. Böylece yanlış uyarı oranı gerçekçi biçimde ölçülür.

Her koşu bir ısınma evresi, en çok 20 dakikalık üst süre sınırı ve bir soğuma evresinden oluşur. Koşular önceden hazırlanmış rastgele bir sırayla ve tekrarlar farklı günlere dağıtılarak yapılacaktır. Her koşu için tarih, temas düzeyi, akım profili, fan durumu, ortam sıcaklığı, tork değeri ve olağan dışı gözlem kaydedilecektir.

## 3. Özellik çıkarımı ve karar yöntemleri (4–6. aylar)

Kayıtlardan kayan pencerelerle şu özellikler çıkarılacaktır: sıcaklığın ortamdan farkı, sıcaklık değişim hızı (eğim), ikinci türev benzeri ivmelenme, bağlantı gerilim düşümünün akıma oranı (görünür direnç), bu oranın değişim hızı ve pencere içi standart sapmalar. Ölçekleme değerleri yalnızca eğitim kümesinden öğrenilecektir.

Karşılaştırılacak dört yöntem:

- **Y1, sabit eşik:** Sıcaklık belirlenen değere ulaştığında alarm. Referans yöntemdir.
- **Y2, değişim hızı kuralı:** Sıcaklık eğimi bir sınırı belirli süre aşarsa uyarı.
- **Y3, çok değişkenli model:** Lojistik regresyon ve karar ağacı tabanlı bir model (Random Forest veya gradyan artırma). Hedef, önümüzdeki H saniye (başlangıç önerisi 60 s) içinde sabit eşiğin aşılıp aşılmayacağıdır.
- **Y4, mikrodenetleyici modeli:** Y3'ün küçültülmüş hali, mikrodenetleyicide int8 veya sabit noktalı çalışan bir model. Gerekirse sığ bir sinir ağı da denenecek.

Uyarı olasılığı için karar eşiği eğitim kümesinden, normal koşularda saatlik yanlış uyarı sayısı önceden belirlenen düzeyi aşmayacak biçimde seçilecektir. Test verisi bu seçimde kullanılmayacaktır. Veri azsa derin öğrenme yerine basit yöntemlerde kalınacaktır.

## 4. Değerlendirme ve istatistik (5–8. aylar)

Bir koşudan çıkan tüm pencereler aynı bölmede tutulacaktır. Model seçimi, koşu bazlı gruplanmış çapraz doğrulamayla yapılacak. Nihai test, eğitimde hiç kullanılmayan deney günlerinin koşularıyla yapılacak. Ayrıca bir akım profili eğitim dışında bırakılarak dayanıklılık analizi yapılacaktır.

Birincil ölçüt, sabit eşik alarmına göre **erken uyarı süresidir** (sabit eşiğin aşıldığı an ile modelin uyardığı an arasındaki fark). İkincil ölçütler normal koşularda saatlik yanlış uyarı sayısı, duyarlılık (uyarı beklenen koşularda uyarı verme oranı), sıcaklık tahmin hatası ve çıkarım maliyetidir. Yöntemler arasındaki fark koşu düzeyinde eşleştirilmiş farklarla, yeniden örneklemeli yüzde 95 güven aralığıyla raporlanacaktır. Koşu sayısı azsa p değeriyle kesin üstünlük iddia edilmeyecek, etki büyüklüğü ve hata örnekleri tartışılacaktır.

Mikrodenetleyici modelinin bellek kullanımı, tek çıkarım süresi ve bilgisayar modeliyle tahmin uyumu ölçülecektir.

## Ön çalışma durumu

Bu metnin hazırlanması sırasında proje için veri toplandığına, düzeneğin kurulduğuna veya pilot sonuç alındığına dair doğrulanmış bir bilgi bulunmamaktadır. Başvuru öncesinde gerçekten bir pilot yapılırsa tarih, düzenek ve gözlemler danışmanın kontrolüyle bu bölüme eklenecektir.
