# 2. Yöntem

## Araştırmanın deseni

Çalışma, kontrollü laboratuvar deneyine dayalı karşılaştırmalı nicel bir araştırmadır. Bağımsız değişkenler hasar düzeyi, uç kütlesi, sensör yerleşimi, sensör sayısı ve model türüdür. Bağımlı değişkenler hasar sınıflandırma başarısı, frekans kestirim hatası ve en küçük ayırt edilebilir hasar düzeyidir. Aynı kiriş tipi, aynı sıkıştırma yöntemi, aynı vurucu ve aynı kayıt altyapısı kullanılacaktır.

## 1. Düzenek ve pilot ölçüm (1–2. aylar)

Yaklaşık 500 mm boyunda, 40 mm genişliğinde ve 4 mm kalınlığında iki alüminyum kiriş bir ucundan, tork kontrollü cıvatalarla bir sıkıştırma plakasına bağlanacak. Basit Euler-Bernoulli kiriş kuramına göre bu geometri için ilk doğal frekans 10–20 Hz mertebesinde beklenir (Rao, 2011). Bu değer yalnızca ön hesaptır, gerçek frekans pilotta ölçülecek. Kirişin serbest ucuna yakın bir noktaya, solenoid veya servo ile çalışan, her darbede aynı enerjiyi vermesi hedeflenen bir vurucu yerleştirilecek. Elle vurma yönteminin tekrarlanabilirliği düşük olduğu için kullanılmayacak, ancak pilotta karşılaştırma amacıyla denenebilir.

Üç ivmeölçer tek bir mikrodenetleyiciye SPI veriyoluyla bağlanacak. Böylece üç kanal aynı zaman tabanıyla örneklenecek ve kablosuz zaman senkronizasyonu sorunu ortadan kalkacak. Örnekleme hızı pilotta belirlenecek, başlangıç önerisi 1 kHz. Aynı kirişe, bir referans için daha düşük gürültülü bir ivmeölçer de bağlanacak. Kiriş yakınına bir sıcaklık sensörü konacak.

Pilotta şunlar ölçülecek: sensörlerin sessiz ortamda gürültü tabanı, vurucunun tekrarlanabilirliği (aynı koşulda genlik ve frekans yayılımı), yeniden sıkıştırmanın frekansa etkisi ve ilk üç modun görünürlüğü. Bu sonuçlara göre örnekleme hızı, kayıt süresi (bir darbe için birkaç saniye) ve hasar derinlikleri kesinleştirilecek.

## 2. Hasar ve bozucu etkiler (3–5. aylar)

Hasar, kirişin sabit uçtan yaklaşık 100 mm uzaklıkta, eğilme momentinin yüksek olduğu bir bölgesinde, kalınlığın bir kısmına kadar kesilen çentikle oluşturulacak. Tercih edilen yaklaşımda aynı kirişe çentik derinleştirilerek ilerlenir: önce sağlam durum ölçülür, sonra ilk çentik açılıp ölçülür, sonra derinleştirilip tekrar ölçülür. Böylece "hangi sınıf hangi kirişten geldi" karışıklığı önlenir. Derinlikler pilotla kesinleştirilecek, başlangıç önerisi kalınlığın yüzde 15, 30 ve 45'idir. İkinci kiriş aynı şekilde işlenerek bağımsız bir doğrulama kirişi olarak kullanılacak. Çentik açma işlemi geri alınamaz, bu yüzden her aşamada tüm günlerin ölçümleri tamamlanmadan bir sonraki aşamaya geçilmeyecek.

Bozucu etkiler şunlardır: uç kütlesi (ek kütle yok, 50 g ve 100 g gibi üç düzey), iki farklı sensör yerleşimi (örneğin kökten yaklaşık 0,2, 0,5 ve 0,9 uzunluk noktaları ile 0,3, 0,6 ve 1,0 noktaları) ve her ölçüm günü kirişin sökülüp aynı torkla yeniden sıkıştırılması. Ortam sıcaklığı her koşulda kaydedilecek.

Toplam plan 2 kiriş × 4 durum × 3 kütle × 2 yerleşim × 5 gün = 240 koşul eder. Her koşulda yaklaşık 10 darbe kaydedilecek. Koşul sırası günler içinde rastgele belirlenecek.

## 3. Özellik çıkarımı (4–6. aylar)

Her darbe sonrası serbest sönümlü titreşim kaydından güç spektrumu (Welch, 1967 yöntemiyle) ve zaman alanında sönümlü sinüs uydurmasıyla ilk üç doğal frekans, sönüm oranı, sensörler arası genlik oranları ve faz farkı çıkarılacak. Frekans çözünürlüğünü artırmak için uygun pencere ve sıfır doldurma kullanılacak. Aynı kirişin sağlam durumundaki ilk günün ölçümleri, o kiriş için "referans" olarak alınacak ve frekanslar bu referansa göre oransal (normalize) biçimde de kullanılacak. Ölçekleme değerleri yalnızca eğitim kümesinden öğrenilecek.

## 4. Modeller ve değerlendirme (5–8. aylar)

Karşılaştırılacak yaklaşımlar:

- **Y1:** Yalnızca ilk doğal frekans kaymasına dayanan eşik kuralı.
- **Y2:** Tek sensörlü model (her sensör için ayrı).
- **Y3:** İki sensörlü modeller (tüm çiftler).
- **Y4:** Üç sensörlü model.

Başlangıçta lojistik regresyon ve Random Forest kullanılacak, veri az olduğu için derin öğrenme denenmeyecek.

Bir koşuldaki tüm darbeler ve aynı gündeki tüm koşullar aynı veri bölmesinde tutulacak (Kapoor ve Narayanan, 2023). Model seçimi, gün bazlı gruplanmış çapraz doğrulamayla birinci kirişin ilk günleri üzerinde yapılacak. Nihai test, birincisi aynı kirişin eğitimde kullanılmayan günü, ikincisi bağımsız ikinci kiriş olmak üzere iki kümeyle yapılacak. Kütle yükünün etkisini ölçmek için bir kütle düzeyi eğitim dışında bırakılarak ek bir dayanıklılık deneyi yapılacak.

Birincil ölçüt makro F1 ve dengeli doğruluktur. İkincil ölçütler karışıklık matrisi, frekans kestirim hatası (referans ivmeölçere göre), sensör sayısına göre performans ve en küçük ayırt edilebilir hasar düzeyidir. Son ölçüt için her hasar düzeyinin sağlam duruma göre frekans kaymasının güven aralığı hesaplanacak ve aralığın sıfırı dışarıda bıraktığı en küçük düzey belirlenecek. Yöntemler arasındaki farklar, koşul düzeyinde eşleştirilmiş ve yeniden örneklemeli yüzde 95 güven aralığıyla raporlanacak. Koşul sayısı az kalırsa kesin üstünlük iddia edilmeyecek, etki büyüklüğü ve hata örnekleri tartışılacak.

Ayrıca kirişin basit bir sonlu eleman veya analitik modeli ile çentik derinliğine göre beklenen frekans kayması hesaplanıp ölçümle karşılaştırılacak. Bu karşılaştırma ölçümün fiziksel olarak makul olup olmadığını denetlemek içindir.

Son olarak pik frekans kestirimi mikrodenetleyicide gerçek zamanlı çalıştırılacak ve bilgisayardaki sonuçla farkı raporlanacaktır.

## Ön çalışma durumu

Bu metnin hazırlanması sırasında proje için veri toplandığına, düzeneğin kurulduğuna veya pilot sonuç alındığına dair doğrulanmış bir bilgi bulunmamaktadır. Başvuru öncesinde gerçekten bir pilot yapılırsa tarih, düzenek ve gözlemler danışmanın kontrolüyle bu bölüme eklenecektir.
