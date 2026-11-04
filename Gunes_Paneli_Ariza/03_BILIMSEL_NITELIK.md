# 1.1 Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Fotovoltaik sistemlerde bakım kararı çoğunlukla bir görüntüyle başlar. Termal kamera bir panelde sıcak bir bölge gösterir ve teknisyen sahaya gider. Peki o sıcak bölge gerçekten bir sorun mu? Cevap her zaman evet değildir. Bir bulut gölgesi, bir yaprak ya da komşu bir direk, hücrelerin bir kısmına gelen ışığı keser. Gölgelenen hücre akım taşıyamaz, serideki diğer hücreler onu zorlar ve o bölge ısınır. Gölge kalkınca sıcak nokta kaybolur. Aynı panelde bağlantı direncinin artması gibi kalıcı bir sorun da benzer bir lekeyle görünebilir.

Fotovoltaik modül arızalarının türleri ve sıcak nokta oluşumu uluslararası bir derlemede ayrıntılı ele alınmıştır (Köntges vd., 2014). Dış mekân kızılötesi termografi için IEC TS 62446-3:2017; ölçüm donanımı, ortam koşulları, inceleme ve raporlamaya ilişkin çerçeveyi tanımlar. Buerhop vd. (2022), gölgelenme ve kirlenme gibi dış etkilerin IR bulgusunun yorumunu zorlaştırdığını; IR bulgularının I–V ölçümleri veya izleme verileriyle tamamlanabildiğini belirtir. Bu çalışmalar şunu hatırlatıyor: termal görüntü güçlü bir araçtır, ancak yorumu ışınıma, açıya, yüke ve çevre koşullarına bağlıdır.

Termal görüntüden panel arızası tespiti zaten çok araştırılan bir konu. Bu yüzden yenilik iddiamız "termal görüntüyle arıza bulmak" olamaz. Burada daha dar bir soruya bakıyoruz. Panelin elektriksel imzasını (I–V eğrisinden çıkan değerleri) termal görüntü özelliklerine eklediğimizde, geçici gölgelenmeyi bakım isteyen durumdan ayırmak ne kadar iyileşiyor? Üstelik termal bilgi yalnızca 32×24 çözünürlüklü, ucuz bir sensörden geliyorsa? IR ile I–V karakterizasyonunun birlikte kullanıldığı çalışmalar vardır (Muttillo vd., 2020; Daher vd., 2024). Bu nedenle yenilik iddiası, bu yöntemleri ilk kez birleştirmek değildir. Katkı, düşük çözünürlüklü bir termal sensörün aynı oturumda ölçülen I–V özellikleriyle birlikte kullanılmasının, kontrollü ve geri döndürülebilir koşullarda gölgelenmeden kaynaklı yanlış bakım alarmına etkisini karşılaştırmalı olarak test etmektir.

**Araştırma sorusu:** Düşük çözünürlüklü bir termal sensörün görüntü özellikleri ile I–V karakteristiğinden çıkan elektriksel özellikler birlikte kullanıldığında, geçici gölgelenmenin deneydeki K/B bakım temsil koşulları sanılması (yanlış alarm) yalnızca termal özellik kullanan yaklaşıma göre azalır mı?

**H1:** Birleşik model, geçici gölgelenme oturumlarını K/B bakım temsil sınıflarına atama oranında (yanlış alarm oranı) yalnızca termal modele ve sıcak nokta eşik kuralına göre daha düşük değer verecektir.

**H2 (keşifsel):** Yeterli sayıda geçerli oturum oluşursa, eğitimde hiç kullanılmayan operasyonel ışınım bandında birleşik modelin makro F1 skorundaki değişim, yalnızca termal modelle karşılaştırılacaktır. Bu karşılaştırma küçük veri hacminde kesin üstünlük kanıtı olarak yorumlanmayacaktır.

**H3:** Birleşik model, tek kart bilgisayarda bir karar için bir saniyenin altında çalışacak ve ölçülebilir, düşük bir enerji tüketimine sahip olacaktır.

Hipotezler deney sonunda test edilecek. Beklenen kazanç görülmezse bu da bir bulgudur. Düşük maliyetli termal sensörün küçük sıcak noktalarda yetersiz kaldığını gösteren bir sonuç, hangi koşulda ek elektriksel ölçümün zorunlu olduğunu da ortaya koyar.

Çalışma küçük bir panelde ve geri döndürülebilir anomali kaynaklarıyla yapılacak. Kalıcı hücre çatlağı, bypass diyot arızası ve megavat ölçekli santral koşulları kapsam dışındadır.
