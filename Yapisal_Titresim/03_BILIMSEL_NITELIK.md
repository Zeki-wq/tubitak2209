# 1.1 Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Köprüler, binalar ve endüstriyel taşıyıcılar zamanla yaşlanır. Çatlak, korozyon veya bağlantı gevşemesi gibi değişimlerin çoğu gözle görünmeden başlar. Rijitlik azaldığında yapının titreşim karakteri de değişir. Doğal frekanslar düşer, mod şekilleri kayar. Titreşime dayalı hasar tespiti bu fikre dayanır ve onlarca yıldır araştırılıyor (Doebling vd., 1996; Sohn vd., 2003; Farrar ve Worden, 2007). Rytter (1993), hasar tanılamayı varlık, yer, şiddet ve kalan ömür olmak üzere dört düzeye ayırmıştır. Bu projede birinci düzeye ve kısmen üçüncü düzeye (varlık ve şiddet sınıfı) bakılacaktır.

Fikir basit, uygulaması değil. Frekansı değiştiren tek şey rijitlik kaybı olmuyor. Üstüne konan bir yük, ortam sıcaklığı, sıkıştırma koşulları ve sensörün bağlanma biçimi de benzer kaymalar üretiyor. Frekans kaymasına bakan bir sistem bunların hepsini hasar olarak yorumlayabilir. Ayrıca düşük maliyetli ivmeölçerlerin gürültüsü yüksek ve çözünürlüğü sınırlıdır. Küçük bir hasarın yarattığı yüzde bir-iki mertebesindeki frekans kaymasını gürültüden ayırmak mümkün mü, bilinmiyor.

Son yıllarda ESP32 benzeri düşük maliyetli kartlarla yapısal izleme düzenekleri sıkça gösteriliyor. Bu nedenle yenilik iddiamız yeni bir sensör ya da düzenek kurmak değil. Aynı fiziksel kirişte ve aynı darbe uyarımıyla üç soruya kontrollü yanıt arıyoruz.

- Hasarı, aynı frekans kaymasını yaratan zararsız kütle yüklemesinden ayırmak için kaç sensör ve hangi özellik gerekir?
- Sensör sayısı ve konumu, ayırt edilebilen en küçük hasar düzeyini nasıl değiştirir?
- Bir kirişte eğitilen model, aynı tipte ikinci bir kirişe ve farklı günlere ne kadar genellenir?

**Araştırma sorusu:** Düşük maliyetli ivmeölçerlerden elde edilen çok sensörlü titreşim özellikleri, değişken kütle yüklemesi ve sıkıştırma koşulları altında rijitlik azalmasını yalnızca frekansa dayanan yaklaşımdan daha güvenilir ayırt edebilir mi?

**H1:** Üç sensörün frekans ve genlik oranı özelliklerini birlikte kullanan model, en iyi tek sensör modeline göre bağımsız günlerde daha yüksek makro F1 skoru verecektir.

**H2:** Uç kütlesi değiştiğinde yalnızca frekansa dayanan modelin performansı belirgin düşecek, sensörler arası genlik oranları (mod şekli göstergesi) eklenen modelde bu düşüş daha küçük olacaktır.

**H3:** Düşük maliyetli ivmeölçerle ayırt edilebilen en küçük hasar düzeyi sensör yerleşimine ve sensör sayısına bağlı olarak değişecektir.

Hipotezlerin hiçbiri önceden doğru kabul edilmiyor. Ucuz sensörün küçük hasarı yakalayamadığı ortaya çıkarsa bu, "bu sensörle şu hasar düzeyinin altı görünmez" diye somut bir sınır verdiği için yararlı bir bulgudur.

Çalışma tek bir laboratuvar kirişi ile yapılacak. Çok katlı bina, köprü, zemin etkileşimi ve gerçek çevresel yükler kapsam dışındadır.
