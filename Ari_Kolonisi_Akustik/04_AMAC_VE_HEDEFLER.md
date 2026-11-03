# 1.2 Amaç ve Hedefler

Bu projenin amacı, kovan içi ses kayıtlarında yapılan anomali tespitinde sıcaklık ve nem bilgisinin yanlış alarm oranını azaltıp azaltmadığını, önce açık veri üzerinde, sonra küçük bir saha doğrulamasıyla incelemektir. Bir hastalık teşhis sistemi yapmıyoruz. Elimizde bir ölçüm sorusu ve onu sınayan bir yöntem var. Sonunda ortaya çıkacak şey, düşük güçlü bir cihazda çalışabilecek hafif bir model ve bunun ne ölçüde güvenilir olduğunu gösteren bir rapordur.

## Ölçülebilir hedefler

1. Açık erişimli kovan ses ve çevre veri kümesini indirip yapısını, lisansını ve etiketlerini belgelemek. Kayıtları kovan ve gün bazında düzenlemek.
2. Ses özellikleri (log-mel, MFCC, seçili frekans bantları), çevre özellikleri (sıcaklık, nem, değişim hızı, günün saati) ve birleşik özellik kümelerini oluşturmak.
3. En az üç anomali yaklaşımını (örneğin istatistiksel sapma, tek sınıflı SVM / Isolation Forest ve küçük bir otokodlayıcı) ses-only ve ses+çevre girdileriyle karşılaştırmak.
4. En az üç kovanı tamamen test için ayırarak "bir kovanı dışarıda bırak" tipi bir değerlendirme yapmak.
5. Bir veya iki kovanda en az sekiz haftalık sürekli ses, sıcaklık ve nem kaydı almak. Arıcının müdahale günlüğünü zaman damgalı toplamak.
6. Anomali modelini, saatlik yanlış alarm sayısı, müdahale olaylarına duyarlılık ve alarm sürelerinin günün saatine dağılımıyla değerlendirmek.
7. Seçilen modeli mikrodenetleyicide çalıştırıp bellek kullanımını, çıkarım süresini ve saatlik enerji tüketimini ölçmek.
8. Saha kayıt protokolünü, sensör yerleşimini, analiz kodunu ve sonuçları sınırlılıklarıyla birlikte bir teknik raporda toplamak. Veri paylaşım izni varsa saha kayıtlarını da paylaşılabilir biçime getirmek.

**Başarı hedefi ile bilimsel bulguyu ayırıyoruz.** Çevre bilgisinin ne kadar katkı sağlayacağını önceden bilemeyiz. Belirli bir yanlış alarm azalması vaat etmiyoruz. Projenin başarısı, kovan bazlı ayrımla adil bir karşılaştırma yapılması, saha kayıtlarının tutarlı alınması ve hipotezlerin belirsizlikle birlikte test edilmesiyle değerlendirilecektir.
