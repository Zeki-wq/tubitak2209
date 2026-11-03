# 1.1 Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Duman dedektörleri hayat kurtarır, ama yalnızca çalıştıkları sürece. Sık yanlış alarm veren bir dedektör ya pilini çıkarılarak ya da yok sayılarak etkisiz hale gelir. Ticari optik duman dedektörlerinin bu konuda zayıf bir yanı var: ışığı saçan her partikül aynı görünür. Mutfak buharı, toz, bazı aerosoller ve gerçek duman benzer tepki üretebilir.

Gaz sensörlerine dayalı yangın tespiti 1990'lardan beri çalışılıyor. Fonollosa ve arkadaşlarının (2018) derlemesi, gaz sensörlerinin yanma dışı birçok uçucu bileşene de tepki verdiğini ve bu nedenle duyarlılık ile yanlış alarm arasındaki dengeyi kurmak için çok değişkenli veri işlemenin gerektiğini vurgular. Aynı derleme, yöntemlerin hem yangın hem de rahatsız edici olay senaryolarıyla kapsamlı biçimde test edilmesi gerektiğini belirtir. Yangın dedektörleri için standart test yangınlarının tanımlandığı EN 54-7 gibi standartlar da bu zorluğun ticari karşılığıdır.

Bu proje bu boşluğun küçük ve ölçülebilir bir parçasına bakıyor. Düşük maliyetli sensörlerle (lazer saçılımlı partikül sayıcı, gaz ve sıcaklık-nem sensörü) kurulan bir düğümde şu üç karar yöntemi aynı veriyle karşılaştırılabilir mi? Tek sensör eşiği, çok sensörlü kural tabanlı karar ve zamansal özelliklere dayalı hafif bir model. Önemli bir ayrıntı şu: partikül sayıcıların çıkışı yalnızca kütle yoğunluğu değil, farklı boyut aralıklarındaki partikül sayıları da verir. Buhar ve toz genelde daha iri partiküller üretirken yanma dumanı daha ince partikül ve gaz bileşenleri (örneğin CO) içerir. Bu fiziksel farkın, düşük maliyetli sensörlerde bile ayrım için kullanılıp kullanılamadığını görmek istiyoruz.

Yenilik iddiamız yeni bir sensör veya algoritma değil. Aynı hazne, aynı olay listesi ve aynı kayıt altyapısında, yanlış alarm odaklı bir karşılaştırma yapmak ve bunu eğitimde görülmeyen olay türlerine dayanıklılıkla birlikte raporlamaktır. Benzer karşılaştırmaların literatürde bulunma ihtimali yüksektir. Bu nedenle başvuru öncesinde konuya özel bir tarama yapılacak, katkı bu sınırla ifade edilecektir.

**Araştırma sorusu:** Parçacık boyut dağılımı, gaz ve sıcaklık-nem ölçümlerinin zamansal özelliklerini birlikte kullanan hafif bir model, tek sensör eşiğine ve kural tabanlı çok sensörlü karara göre, aynı duyarlılık düzeyinde duman benzeri çevresel olaylarda daha az yanlış alarm verir mi?

**H1:** Zamansal özellikli hafif model, aynı duyarlılıkta, duman benzeri olaylarda tek sensör eşiğine ve kural tabanlı çok sensörlü karara göre daha düşük yanlış alarm oranı verecektir.

**H2:** Eğitimde bulunmayan bir duman benzeri olay türü test edildiğinde, çok sensörlü zamansal model tek sensör eşiğine göre daha az yanlış alarm verecektir.

**H3:** Düğümün düşük güç yapılandırması ve LoRa paket teslim oranı, yangın erken uyarı uygulaması için tanımlanan alt sınırlarla karşılaştırıldığında ölçülebilir ve raporlanabilir olacaktır.

Hipotezlerin hiçbiri önceden doğru kabul edilmiyor. Çok sensörlü modelin tek sensörden iyi çıkmadığı bir sonuç da, düşük maliyetli düğümlerde fazladan sensör maliyetinin gereksiz olabileceğini göstermesi açısından yararlıdır.

Çalışma oda ölçekli, küçük bir hazne ve belirli olay türleriyle sınırlı. Yangın tespit sisteminin sahada güvenilir çalıştığına dair bir iddia kurulmayacaktır.
