# 1.1 Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Elektrik bağlantıları çoğu zaman sessizce bozulur. Vida gevşer, kablo ucu oksitlenir, temas yüzeyi küçülür. Gerçek temas alanı daraldıkça bağlantının direnci artar ve üzerinden akım geçtikçe bu noktada I²R kadar güç ısıya dönüşür (Holm, 1967; Slade, 2014). Birkaç miliohmluk bir artış bile yüksek akımda fark edilir bir ısınma yaratabilir. Isınan metal genleşir, yüzey oksitlenir, direnç daha da yükselir. Süreç kendini besler.

Pratikte kullanılan koruma çoğunlukla basittir. Sıcaklık bir sınırı geçerse alarm verilir. Sorun, alarmın olay başladıktan epey sonra gelmesidir. Eşiği düşürmek de çözüm değildir, çünkü ortam sıcaklığı, akım basamakları ve havalandırma değişimi de sıcaklığı oynatır ve sistem gereksiz yere alarm verir.

Literatürde gevşek temasın veriye dayalı tanılanması üzerine çalışmalar var. Luan ve arkadaşları (2025), akıllı sayaçlardaki gevşek vidalı terminalleri ele almış ve aynı kutudaki sayaçların gerilim farkından yararlanan iki aşamalı bir yöntem önermiştir. Yöntemde ark benzeri olaylar için aykırı değer tespiti, temas direncinin kestirimi içinse çoklu doğrusal regresyon kullanılmıştır. Bu çalışma bizim için iki şeyi gösteriyor. Gerilim düşümü, bağlantının durumu hakkında sıcaklıktan farklı ve değerli bir bilgi taşıyor. Ayrıca bu tür tanılama makine öğrenmesiyle yapılabiliyor.

Biz farklı bir noktaya bakacağız. Elimizdeki soru bir sayaç kutusu için değil, tekrar kurulabilir bir laboratuvar düzeneği için ve **zamanlama** üzerine: akım, gerilim düşümü ve sıcaklığın değişim hızı birlikte kullanıldığında, sıcaklık sabit eşiğe varmadan ne kadar önce, kaç yanlış uyarıyla bir uyarı üretilebilir? Üstelik bunu bir mikrodenetleyicinin bellek ve işlem sınırları içinde yapabilir miyiz? Yenilik iddiamız yeni bir sensör ya da algoritma değil. Aynı fiziksel düzenekte, aynı verilerle, dört karar yöntemini adil biçimde karşılaştırmak ve bunu zararsız bozucu etkiler (akım basamağı, fan) varken yapmaktır.

**Araştırma sorusu:** Akım, bağlantı gerilim düşümü ve sıcaklık değişim hızından yararlanan çok değişkenli bir yöntem, yalnızca sıcaklık eşiği kullanan alarma göre anormal ısınmayı daha erken ve kabul edilebilir yanlış uyarı düzeyinde bildirebilir mi?

**H1:** Çok değişkenli model, sabit sıcaklık eşiğine göre ortanca erken uyarı süresini artıracaktır.

**H2:** Gerilim düşümü özelliği eklendiğinde, yalnızca sıcaklık değişim hızına dayanan kurala göre normal çalışmadaki akım basamağı ve fan kaynaklı yanlış uyarılar azalacaktır.

**H3:** Mikrodenetleyiciye sığacak tamsayı (int8) veya sabit noktalı hafif bir model, bilgisayardaki esnek modele göre erken uyarı süresinde sınırlı bir kayıpla çalışacaktır.

Hipotezlerin hiçbiri önceden doğru kabul edilmiyor. Gerilim düşümünün sıcaklığa göre belirgin bir ek bilgi vermediği ortaya çıkarsa bu da yararlı bir sonuçtur. Düşük maliyetli bir sistemde sadece sıcaklık ve akımla yetinmenin yeterli olduğunu göstermiş oluruz.

Çalışmanın geçerliliği düşük gerilimli, akım sınırlı, kısa sürekli deney düzeniyle sınırlıdır. Şebeke gerilimi, alternatif akım, ark olayları ve uzun süreli yaşlanma kapsam dışındadır. Sonuçlar bir elektrik tesisatı güvenlik ürününün yerine geçmez.
