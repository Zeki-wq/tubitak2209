# Özet

Bir yangın alarmı her çaldığında bir yangın vardır diye düşünmek isteriz. Gerçekte öyle olmuyor. Mutfakta kızarmış yemek buharı, banyodan yayılan sıcak nem, havada savrulan toz veya bir sprey de duman sensörünü tetikleyebilir. Yanlış alarmlar insanları alarma güvensiz hale getirir, bu da asıl yangında tehlikelidir. Bu projede yanlış alarmı azaltmanın yollarını araştırıyoruz.

Çalışmanın merkezinde şu soru var: yalnızca tek bir sensöre bakmak yerine partikül boyutu, gaz ve sıcaklık-nem ölçümlerinin zamansal değişimini birlikte kullanırsak, yanma kaynaklı dumanı duman benzeri zararsız olaylardan daha az yanlış alarmla ayırabilir miyiz? Çalışma iki aşamalı olacak. İlk aşamada açık erişimli bir duman algılama veri kümesi üzerinde yöntemler karşılaştırılacak. İkinci aşamada küçük bir test haznesinde buhar, pişirme aerosolü, toz, su bazlı sprey, sıcaklık sıçraması ve yanmasız sis gibi duman benzeri olaylar ile küçük, kontrollü ve gözetimli bir ısıl bozunma kaynağı (yanma kaynaklı duman) kaydedilecek. Hazneye bağımsız iki ticari duman alarmı konacak ve alarm anları referans olarak kaydedilecek.

Tek sensörlü eşik, çok sensörlü kural tabanlı karar ve zamansal özelliklerle hafif bir makine öğrenmesi modeli aynı verilerle karşılaştırılacak. Model, eğitimde hiç görülmemiş günlerde ve bir olay türü dışarıda bırakılarak sınanacak. Başarı ölçütleri aynı duyarlılıkta yanlış alarm oranı, algılama gecikmesi, düğüm enerji tüketimi ve LoRa paket teslim oranıdır.

Projede orman yangını tespiti iddiası yok. Sonuçlar oda ölçekli bir hazne ve belirli duman benzeri olaylar için geçerlidir. Standart yangın testlerinin yerini tutmaz. Sekiz ay sonunda etiketli bir olay veri kümesi, tekrar kurulabilir bir düzenek ve sınırlılıklarıyla birlikte bir karşılaştırma raporu bekleniyor.

**Anahtar kelimeler:** yanlış alarm, duman algılama, sensör füzyonu, partikül sensörü, LoRa, gömülü sistemler.
