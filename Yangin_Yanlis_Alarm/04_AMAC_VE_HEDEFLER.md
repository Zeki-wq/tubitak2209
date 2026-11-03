# 1.2 Amaç ve Hedefler

Bu projenin amacı, düşük maliyetli çok sensörlü bir düğümle yanma kaynaklı dumanın duman benzeri zararsız olaylardan ayrılmasında, sensör füzyonu ve zamansal özelliklerin tek sensör eşiğine göre yanlış alarmı ne ölçüde azalttığını deneysel olarak incelemektir. Yangın alarm ürünü geliştirmiyoruz. Elimizdeki düzenek, yanlış alarm davranışını kontrollü koşullarda karşılaştırmaya yarayan bir prototiptir. Önemli olan, hangi yöntemin hangi olay türünde neden yanıldığını görmektir.

## Ölçülebilir hedefler

1. Açık erişimli bir duman algılama veri kümesini indirip sütunlarını, oturum yapısını ve lisansını belgelemek. Tek sensör eşiği, kural tabanlı karar ve zamansal özellikli modelleri bu veri üzerinde oturum bazlı ayırmayla karşılaştırmak.
2. Partikül (boyut sayımlı), gaz, sıcaklık-nem sensörlerini içeren iki ölçüm düğümü ve LoRa ağ geçidi kurmak.
3. Yangına dayanıklı, fanlı, yaklaşık bir metreküp ölçeğinde bir test haznesi hazırlamak. Hazneye bağımsız iki ticari duman alarmı yerleştirip alarm anlarını kaydetmek.
4. Sekiz durumu (arka plan, buhar, pişirme aerosolü, toz, su bazlı sprey, sıcaklık sıçraması, yanmasız sis, yanma kaynaklı duman) iki şiddet düzeyi ve her biri için beş ayrı günde kaydetmek. Plan 8 × 2 × 5, yani 80 olay kaydıdır.
5. Üç karar yöntemini (tek sensör eşiği, çok sensörlü kural, zamansal özellikli hafif model) ve bir uç cihaz modelini aynı değerlendirme protokolüyle karşılaştırmak.
6. Başarıyı aynı duyarlılıkta yanlış alarm oranı, algılama gecikmesi (referans alarma göre) ve olay türü bazında karışıklık matrisiyle değerlendirmek.
7. Test başarısını eğitimde görülmemiş günlerde ve bir duman benzeri olay türü eğitim dışında bırakılarak ölçmek.
8. Düğümün enerji tüketimini ve LoRa paket teslim oranını ölçmek.
9. Düzenek, protokol, veri kümesi ve karşılaştırma sonuçlarını sınırlılıklarıyla birlikte bir teknik raporda toplamak.

**Başarı hedefi ile bilimsel bulguyu ayırıyoruz.** Zamansal modelin yanlış alarmı ne kadar azaltacağını önceden bilemeyiz. Belirli bir azalma oranı vaat etmiyoruz. Projenin başarısı, güvenli ve tekrarlanabilir veri üretilmesi, yöntemlerin adil karşılaştırılması ve hipotezlerin belirsizlikle birlikte test edilmesiyle değerlendirilecektir.
