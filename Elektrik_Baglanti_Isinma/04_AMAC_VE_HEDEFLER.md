# 1.2 Amaç ve Hedefler

Bu projenin amacı, düşük gerilimli bir elektrik bağlantısında temas direnci arttığında oluşan ısınmayı, sıcaklık sabit bir eşiğe ulaşmadan önce fark edebilen bir yöntemin ne kadar işe yaradığını deneysel olarak incelemektir. Burada yeni bir ürün geliştirmiyoruz. Elimizdeki düzenek araştırma sorusunu sınamak için kurulmuş bir prototip olacak. Odaklandığımız şey, hangi ölçümün uyarıyı ne kadar öne çektiği ve bunun bedelinin (yanlış uyarı, işlem yükü) ne olduğudur.

## Ölçülebilir hedefler

1. Akımı sınırlandırılmış, donanımsal sıcaklık kesmeli, 12–24 V doğru akımla çalışan ve bağlantı noktasının temas durumu kontrollü değiştirilebilen bir deney düzeneği kurmak.
2. Akım, bağlantı uçları arası gerilim düşümü, bağlantı sıcaklığı ve ortam sıcaklığını en az 10 Hz ortak zaman damgasıyla kaydetmek. Termokupl gecikmesini pilotta ölçüp rapora eklemek.
3. Normal bağlantı ve üç gevşeklik düzeyini, iki akım profilinde ve iki hava akışı koşulunda ölçmek. Her koşul için en az beş bağımsız tekrar yapmak (toplam 80 koşu).
4. Dört karar yöntemini aynı verilerle karşılaştırmak: sabit sıcaklık eşiği, sıcaklık değişim hızı kuralı, çok değişkenli model ve mikrodenetleyici üzerinde çalışan hafif model.
5. Başarıyı erken uyarı süresi, normal çalışmada saatlik yanlış uyarı sayısı, duyarlılık ve sıcaklık tahmin hatasıyla (MAE) değerlendirmek.
6. Test başarısını eğitimde hiç görülmemiş deney günlerinden gelen koşularla ölçmek. En az bir akım profilini eğitim dışında bırakarak dayanıklılık analizi yapmak.
7. Modelin mikrodenetleyicide kapladığı bellek ile bir çıkarımın süresini ölçüp bilgisayardaki sonuçla uyumunu raporlamak.
8. Düzeneğin kurulumunu, güvenlik adımlarını, veri protokolünü ve karşılaştırma sonuçlarını sınırlılıklarıyla birlikte bir teknik raporda toplamak. Veri kümesini cihaz ve ortam bilgisiyle birlikte paylaşılabilir biçimde düzenlemek.

**Başarı hedefi ile bilimsel bulguyu ayırıyoruz.** Çok değişkenli modelin sabit eşikten ne kadar önce uyarı vereceğini şimdiden bilemeyiz. Bu yüzden belirli bir süre kazancı vaat etmiyoruz. Projenin başarısı, güvenli ve tekrarlanabilir veri üretilmesi, dört yöntemin adil karşılaştırılması ve hipotezlerin belirsizlikle birlikte raporlanmasıyla değerlendirilecektir.
