# Altı proje önerisinin değerlendirmesi

Bu dosya `projeler.md` içindeki altı fikrin incelenmesi, güçlendirilmesi ve sıralanması için hazırlandı. Her fikir için ayrı bir klasör var ve içinde `Su_Kacagi` ile aynı 12 dosyalık yapı bulunuyor.

## Önce bilmeniz gereken bir şey

`projeler.md` içinde altı kaynağın "2025–2026 yayını" olarak anıldığı satırlar var. Bunları tek tek aradım. Sonuç şöyle:

| Kaynak | Durum |
|---|---|
| Luan vd. (2025), gevşek temas, *Sensors* | Bulundu, DOI 10.3390/s25123682. Elektrik projesinde kullanıldı. |
| Abdollahi vd. (2025), UrBAN, *Scientific Data* | Bulundu, DOI 10.1038/s41597-025-04869-1. Arı projesinde kullanıldı. |
| "Thermal and Chromatic Analysis for Photovoltaic Hotspot Detection" (*Solar Energy*, 2026) | **Bulunamadı.** Kullanılmadı. |
| "Real-time Structural Health Monitoring Using Affordable Sensors" (*Discover Civil Engineering*, 2026) | **Bulunamadı.** Kullanılmadı. |
| "Low-Power IoT-Based Smart Irrigation Using LoRa" (*IoT*, 2026) | **Bulunamadı.** Kullanılmadı. |
| Yangın / ESP32 makaleleri (2026) | Doğrulanamadı. Kullanılmadı. Bunun yerine bulunan Fonollosa vd. (2018) derlemesi kullanıldı. |

Bu kaynakların hiçbiri başvuru metinlerine girmedi. Başvuru öncesi ilgili konularda kendi taramanızı yapın ve yalnızca açıp okuduğunuz makaleleri ekleyin. Başvuruda var olmayan bir kaynağa atıf yapmak, dosyanın en ciddi zayıf noktası olurdu.

## Güçlendirmeler

| Proje | Orijinal fikirdeki zayıflık | Ne değiştirdim |
|---|---|---|
| Elektrik bağlantısı | Güvenlik sınırı ve "erken" kavramı belirsizdi | Mutlak 60 °C sınırı, üç katmanlı kesme, erken uyarı süresinin sabit eşiğe göre tanımı, akım basamağı ve fan gibi zararsız bozucuların deneye eklenmesi |
| Güneş paneli | "Sıcak nokta = arıza" belirsizliği, kalıcı hasar üretememe | Geçici gölgelenme ile bakım gerektiren durumların ayrımı, kendi yapılacak I–V tarama devresi, geri alınabilir anomaliler, ışınım bandı dayanıklılığı |
| Arı kolonisi | Güvenilir biyolojik etiket yok, iş birliği belirsiz | Hastalık/oğul iddiası çıkarıldı. Soru "çevre bilgisi yanlış alarmı azaltır mı" olarak daraltıldı. Önce açık veri, sonra küçük saha kaydı. Saha olmazsa proje yine ayakta kalır |
| Yapısal titreşim | Kütle ve sıkıştırma karıştırıcıları ele alınmamıştı | Aynı kirişte adım adım çentik, ikinci kiriş, kütle yükü, günlük yeniden sıkıştırma, referans ivmeölçer, en küçük ayırt edilebilir hasar |
| Bitki su stresi | Etiket sensörlerden türetilirse döngüsel olur | Etiket günlük saksı tartımından (transpirasyon oranı) ve gözlemden üretiliyor, sensörlerden değil. Bağımsız deney serisi, planlı atmosfer farkları |
| Yangın yanlış alarm | "Orman yangını" iddiası, referans veri yok, güvenlik | Orman ifadesi kaldırıldı. Oda ölçekli hazne, bağımsız ticari alarm referansı, duman benzeri olay listesi, onay çıkmazsa yanma bölümünü atan B planı |

## Sıralama (benim değerlendirmem)

Bu bir kabul olasılığı tahmini değil. Fizibilite, risk ve bilimsel savunulabilirliğe göre bir sıralama.

| Sıra | Proje | Güçlü yan | En büyük risk | Başvurmadan önce gereken |
|---|---|---|---|---|
| 1 | Elektrik bağlantısı | Net soru, ölçülebilir sonuç, donanımı basit | Güvenlik onayı, ısınma süresi | Elektrik laboratuvarı sorumlusunun onayı |
| 2 | Yapısal titreşim | Çok temiz deney tasarımı, tamamen laboratuvarda | Ucuz ivmeölçerin gürültüsü, kiriş işleme imkânı | Atölye ve tezgâh erişimi |
| 3 | Güneş paneli | Güncel konu, hem termal hem elektriksel veri | Güneşli gün sayısı, düşük çözünürlüklü termal sensör | Açık alan ve proje başlangıç mevsimi |
| 4 | Bitki su stresi | Etiket tasarımı sağlam, düşük donanım riski | Biyolojik değişkenlik, 8 ayda 3 seri sığdırmak | Bitki uzmanı ve yetiştirme alanı |
| 5 | Arı kolonisi | Açık veri sayesinde saha olmadan da ilerler | Etiket zayıflığı, sezon, arıcı bulma | Arıcı veya fakülte arılığı onayı, veri kümesinin kontrolü |
| 6 | Yangın yanlış alarm | İlginç soru | Referans veri, yanma güvenliği, kapsamın büyümesi | Güvenlik onayı, kontrollü ortam |

İlk ikisi ile üçüncü arasındaki fark küçük. Hangisini seçeceğiniz büyük ölçüde hangi laboratuvara ve hangi danışmana ulaşabildiğinize bağlı.

## Takvim gerçeği

Son başvuru **11 Kasım 2026, 17.30**. Danışman onayı da bu saate kadar tamamlanmış olmalı. Bugün 3 Kasım. Yani elinizde yaklaşık sekiz gün var. Altı projeyi birden başvuruya hazırlamak gerçekçi değil. Bir kişinin birden fazla 2209 projesinin yürütücüsü olup olamayacağını kural metninden kontrol edin. Muhtemelen tek başvuru yapılabilir. Gerekirse farklı yürütücüler farklı projelerle başvurabilir.

Bu hafta yapılacaklar:
1. İki projeyi seçin (örneğin elektrik bağlantısı ve yapısal titreşim).
2. Seçtiğiniz projenin danışmanıyla ve laboratuvar sorumlusuyla hemen görüşün.
3. İlgili klasördeki `[DOLDURULACAK]` alanlarını tamamlayın.
4. Konuya özel kısa literatür taraması yapın ve kaynakçadaki kayıtları tek tek açıp doğrulayın.
5. Fiyat tekliflerini alıp bütçeyi güncelleyin.

## Yazı üslubu hakkında

Metinleri doğal bir yazıyla, kısa ve uzun cümleleri karıştırarak, noktalı virgülü yalnızca gerekli yerlerde kullanarak yazdım. Yine de siz ve danışmanınız her metni baştan sona okuyup kendi bilginizle düzeltmeli, kendi ağzınıza uydurmalısınız. Ayrıca TÜBİTAK, başvuruda üretken yapay zekâ kullanımına ilişkin bir rehber yayımladı. Gerçek kullanımı rehberde istenen biçimde beyan etmeniz gerekir. Bu dosyalar tam olarak bunun için sizin kontrolünüzden geçmeli.
