# 2. Yöntem

## Araştırmanın deseni

Çalışma, kontrollü saksı deneyine dayalı karşılaştırmalı nicel bir araştırmadır. Bağımsız değişkenler sulama grubu, atmosferik koşul bloğu ve tahmin modeline giren sensör grubudur. Bağımlı değişkenler günlük transpirasyon oranı, stres durumu, tahmin başarısı, erken uyarı süresi ve su kullanımıdır. Aynı tür, aynı saksı hacmi, aynı toprak karışımı ve aynı ölçüm altyapısı kullanılacaktır.

## 1. Bitki, düzenek ve sensör hazırlığı (1–2. aylar)

Kısa sürede gelişen tek bir sebze türü (örneğin domates) seçilecek. Tür, saksı hacmi ve toprak karışımı bir bitki uzmanıyla netleştirilecek. Her deney serisinde 18 saksı, tam sulama, hafif kısıt ve orta kısıt gruplarına altı saksı olacak şekilde rastgele atanacak. Ayrıca bitki ekilmemiş 3 saksı, topraktan buharlaşma kaybını ölçmek için kullanılacak. Toprak yüzeyi, buharlaşmayı sınırlamak için kapatılacak.

Dokuz saksı (her gruptan üçü) elektronik olarak izlenecek. Her birine kapasitif toprak nemi sensörü yerleştirilecek ve bir yaprağa dar görüş açılı temassız kızılötesi sıcaklık sensörü yönlendirilecek. Ortamda iki hava sıcaklığı ve nem sensörü ile iki ışık sensörü olacak. Veriler mikrodenetleyiciyle zaman damgalı kaydedilecek.

Toprak nemi sensörleri, kullanılacak toprak karışımında, bilinen su içeriklerinde tartarak kalibre edilecek. Sensörlerin sıcaklıkla kayması pilotta incelenecek (Kizito vd., 2008). Yaprak sıcaklığı sensörünün görüş alanı ve yaprağa uzaklığı ölçülecek, arkaplan etkisi kontrol edilecek. Pilot serisinde sulama grupları arasındaki ayrışmanın yeterli olup olmadığına bakılacak.

## 2. Deney serileri (2–7. aylar)

Her seri yaklaşık altı ila yedi hafta sürecek: fidelerin saksılara alışması için iki hafta, ardından yaklaşık dört ila beş haftalık sulama koşulları. Üç seri yürütülecek (pilot serisi, ikinci seri ve bağımsız test serisi). Pilot serisi, protokol değişmediyse eğitim verisine dahil edilecek.

Sulama, günlük ağırlık hedeflerine göre yapılacak: tam sulama grubu kapasiteye geri döndürülür, hafif kısıt grubu bunun yaklaşık yüzde 70'i, orta kısıt grubu yaklaşık yüzde 50'si kadar su alır. Oranlar pilotta, bitkilerin gerçekten farklı tepki vereceği düzeyde kesinleştirilecek. Her seride atmosferik koşul bloğu eklenecek: önceden belirlenmiş günlerde bir fan ısıtıcı ve nemlendirici ile sıcak-kuru veya serin-nemli koşullar oluşturulacak. Bu, çevre bilgisinin katkısını sınayabilmek için gerekli.

Her gün aynı saatte sulamadan önce her saksı tartılacak. Günlük transpirasyon, bir önceki sulama sonrası ile bugün sulamadan önceki ağırlık farkından, bitkisiz saksılarda ölçülen buharlaşma kaybı çıkarılarak hesaplanacak. Yaprak durumu, iki bağımsız gözlemcinin (biri bitki uzmanı) üç basamaklı solgunluk skoruyla kaydedilecek. Seri sonunda yaş ve kuru biyokütle ile yaprak alanı ölçülecek.

## 3. Etiket ve özellik üretimi (3–7. aylar)

**Stres etiketi:** Her saksının günlük transpirasyonu, aynı günün tam sulama grubu ortalamasına bölünerek normalize transpirasyon oranı elde edilir. Bu oran bir eşiğin altına düştüğünde o gün "stresli" sayılır. Eşik pilot verisi ve bitki fizyolojisi literatürü doğrultusunda belirlenecek (başlangıç önerisi 0,8) (Sinclair ve Ludlow, 1986). Etiketin güvenilirliği, solgunluk skoru ile uyum (örneğin Cohen kappa) üzerinden kontrol edilecek. Etiket üretiminde toprak nemi, yaprak sıcaklığı veya hava sensörleri **kullanılmayacak**.

**Tahmin hedefi:** t gününe kadar olan sensör verisiyle t+1 günü için stres durumu (sınıflandırma) ve normalize transpirasyon oranı (regresyon).

**Özellikler:** Toprak nemi (kalibre edilmiş) günlük ortalaması ve değişimi, hava sıcaklığı ve nemi, buhar basıncı açığı (Allen vd., 1998'deki bağıntıyla), ışık, yaprak-hava sıcaklık farkı, gündüz ve gece ayrı özetler, önceki günlerin eğilimi. Ölçekleme değerleri yalnızca eğitim kümesinden öğrenilecek.

## 4. Modeller ve değerlendirme (4–8. aylar)

Karşılaştırılan modeller: M1 yalnızca toprak nemi, M2 toprak nemi + hava koşulları (sıcaklık, nem, VPD, ışık), M3 tüm sensörler (yaprak sıcaklığı dahil). Referans yöntem sabit toprak nemi eşiği kuralıdır. Modeller lojistik regresyon ve Random Forest ile başlayacak, regresyon için ek olarak düzenlileştirilmiş doğrusal modeller denenecek. Veri az olduğu için derin öğrenme kullanılmayacak.

Aynı saksının ardışık günleri birbirine bağımlıdır. Bu nedenle bir saksıya ait tüm günler aynı veri bölmesinde tutulacak, ayrıca seri bazlı ayırma yapılacak (Kapoor ve Narayanan, 2023). Model seçimi, ilk iki serinin saksı bazlı gruplanmış çapraz doğrulamasıyla yapılacak. Nihai test, üçüncü ve hiç görülmemiş serinin saksılarıyla yapılacak.

Birincil ölçüt makro F1'dir. İkincil ölçütler duyarlılık, yanlış alarm oranı, ortalama mutlak hata ve erken uyarı süresi (modelin stres eşiğinin aşıldığı günden kaç gün önce uyardığı) olacaktır. Farklar, saksı düzeyinde eşleştirilmiş ve saksı bloklarıyla yeniden örneklemeli yüzde 95 güven aralığıyla raporlanacak. Test saksı sayısı az olduğu için p değeriyle kesin üstünlük iddia edilmeyecek, etki büyüklüğü ve örnek hatalar tartışılacaktır.

Keşifsel olarak, günlük su dengesi verisiyle iki strateji simüle edilecek: sabit nem eşiğine göre sulama ve model uyarısına göre sulama. Su kullanımı ve stresli gün sayısı karşılaştırılacak. Bu simülasyon gerçek bir sulama deneyinin yerini tutmaz, bu bölüm raporda ayrı işaretlenecektir.

## Ön çalışma durumu

Bu metnin hazırlanması sırasında proje için bitki yetiştirildiğine, veri toplandığına veya pilot sonuç alındığına dair doğrulanmış bir bilgi bulunmamaktadır. Başvuru öncesinde gerçekten bir ön deneme yapılırsa tarih, düzenek ve gözlemler danışmanın kontrolüyle bu bölüme eklenecektir.
