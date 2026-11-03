# 3. Proje Yönetimi

## 3.1 Çalışma Takvimi

Proje süresi sekiz aydır. Aşağıdaki yüzde değerleri iş paketlerinin **başarıya katkı ağırlıklarıdır** ve toplamları 100'dür. Satın alma, literatür taraması, rapor yazımı veya sonuç paylaşımı ayrı iş paketi yapılmamıştır.

| İş paketi ve faaliyet | Aylar | Ölçülebilir başarı ölçütü | Başarıya katkı (%) |
|---|---|---|---:|
| İP1: Güvenli deney düzeneğinin kurulması, sensörlerin sınanması ve pilot ölçüm | 1–2 | Normal ve en az iki gevşeklik düzeyi için güvenlik sınırı içinde, zaman damgalı ve tekrarlanabilir örnek koşuların alınması | 25 |
| İP2: Kontrollü koşularda ana deney serisi | 3–5 | Planlanan 80 koşunun tamamlanması veya eksik koşuların nedeninin kayıt altına alınması | 30 |
| İP3: Özellik çıkarımı ve dört karar yönteminin kurulması | 4–6 | Dört yöntemin aynı değerlendirme protokolüyle eğitilmesi ve ayarlanması | 25 |
| İP4: Bağımsız gün testi, mikrodenetleyici çıkarımı ve sonuçların değerlendirilmesi | 6–8 | Eğitimde kullanılmayan günlerde erken uyarı süresi, yanlış uyarı ve işlem yükü sonuçlarının belirsizlikle raporlanması | 20 |
| **Toplam** | **8 ay** | | **100** |

## 3.2 Risk Yönetimi

| Risk | Etki | B planı ve yönteme etkisi |
|---|---|---|
| Gevşek bağlantı tekrarlanabilir ısınma üretmez | Koşular arası farklar büyür, karşılaştırma zayıflar | Tork değerleri sıkı kontrol edilir. Gerekirse seri direnç ekli kontrollü referans koşulu ana kaynak yapılır. Gerçek gevşek bağlantı ek seri olarak raporlanır. |
| Isınma çok yavaş, koşu süreleri uzar | Deney takvimi kayar | Akım düzeyi güvenli sınırlar içinde artırılır, bağlantı yalıtım bloğuna alınır. Koşu üst süresi gerekirse 20 dakikadan uzatılmaz, koşu sayısı yerine tekrar sayısı azaltılarak plan korunur. |
| Termokupl gecikmesi uyarı süresini bozar | Erken uyarı kazancı gerçekte daha farklı çıkar | İnce telli sensör ve ısıl macun kullanılır, gecikme basamak tepkisiyle ölçülüp rapora yazılır. Sonuçlar bu gecikme payıyla birlikte yorumlanır. |
| Gerilim düşümü ölçümü gürültülü | Yeni özelliğin katkısı görünmez | Kelvin bağlantı, kısa ve bükülü kablolar, yüksek çözünürlüklü ADC ve ortalama alma denenir. Katkı yoksa bu açıkça sonuç olarak yazılır. |
| Güvenlik olayı (aşırı ısınma, kısa devre) | İnsan ve cihaz zararı | Akım sınırlı kaynak, bağımsız termostat, yazılımla kesme, gözetimsiz çalıştırmama, yanıcı malzeme bulundurmama. Laboratuvar sorumlusu onayı alınmadan deneye başlanmaz. |
| Pahalı kalemler (güç kaynağı, tork anahtarı) laboratuvarda yok | Bütçe artar | Kurumdan ödünç alma, ikinci el veya daha basit kaynak seçilir. Maksimum akım 6 A'ya indirilerek yük gereksinimi azaltılır. |
| Modeller veriye aşırı uyum sağlar | Test başarısı gerçeği yansıtmaz | Koşu bazlı ayrım, sınırlı model karmaşıklığı ve basit referans yöntemlerle karşılaştırma |
| Mikrodenetleyici modeli belleğe sığmaz | Y4 uygulanamaz | Özellik sayısı ve model boyutu azaltılır. Y4 yalnızca kısmi sonuçla raporlanır, Y1–Y3 karşılaştırması etkilenmez. |

## 3.3 Araştırma Olanakları

Proje için elektrik laboratuvarında bir çalışma masası, ayarlanabilir doğru akım kaynağı, multimetre ve osiloskop, yanıcı olmayan bir test yüzeyi ve bilgisayar gerekir. **Bu olanakların mevcut olduğu henüz teyit edilmemiştir.** Başvuruya girmeden önce aşağıdaki alanlar danışmanla doldurulacaktır.

- Kullanılacak laboratuvar / birim: **[ADI VE KONUMU]**
- Mevcut bilgisayar ve yazılım altyapısı: **[GERÇEK CİHAZ / OLANAK]**
- Mevcut güç kaynağı, multimetre, osiloskop: **[VAR / YOK VE DETAY]**
- Mevcut tork tornavida / milliohm ölçer: **[VAR / YOK]**
- Laboratuvar güvenliğinden sorumlu kişi ve onay: **[BİLGİ]**
- Danışmanın projeye sağlayacağı teknik destek: **[TEYİT EDİLMİŞ DESTEK]**

Bu bölüm yalnızca gerçekten var olan ve erişim izni alınmış kaynaklarla tamamlanmalıdır.
