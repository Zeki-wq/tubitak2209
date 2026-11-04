# 3. Proje Yönetimi

## 3.1 Çalışma Takvimi

Proje süresi sekiz aydır. Aşağıdaki yüzde değerleri iş paketlerinin **başarıya katkı ağırlıklarıdır** ve toplamları 100'dür. Satın alma, literatür taraması, rapor yazımı veya sonuç paylaşımı ayrı iş paketi yapılmamıştır.

| İş paketi ve faaliyet | Aylar | Ölçülebilir başarı ölçütü | Başarıya katkı (%) |
|---|---|---|---:|
| İP1: Ölçüm düzeneğinin kurulması (panel, termal sensör, I–V devresi, referans sensörler) ve pilot ölçüm | 1–2 | Normal ve en az iki anomali durumunda zaman damgalı termal ve I–V kaydı, sensör gürültü ve çözünürlük sınırlarının belgelenmesi | 25 |
| İP2: Ana deney serisi ve veri kümesinin hazırlanması | 3–5 | En az on takvim gününe dağıtılmış 90 oturumun tamamlanması veya eksik oturumların nedeninin kayıt altına alınması | 30 |
| İP3: Özellik çıkarımı ve model gruplarının kurulması | 4–6 | Eşik kuralı ile termal, elektriksel ve birleşik modellerin aynı protokolle eğitilmesi | 25 |
| İP4: Bağımsız gün testi, ışınım dayanıklılığı, tek kart bilgisayarda çıkarım ve değerlendirme | 6–8 | Eğitimde kullanılmayan günlerde yanlış alarm oranı, makro F1 ve çıkarım süresinin belirsizlikle raporlanması | 20 |
| **Toplam** | **8 ay** | | **100** |

## 3.2 Risk Yönetimi

| Risk | Etki | B planı ve yönteme etkisi |
|---|---|---|
| Düşük çözünürlüklü termal sensör küçük sıcak noktaları ayıramaz | Termal özelliklerin katkısı düşer | Gölgelenme oranları büyütülür, sensör panele yaklaştırılır. Kurumdan daha yüksek çözünürlüklü kamera ödünç alınabilirse referans olarak kullanılır. Sonuç olumsuzsa "bu sensörle yeterli değil" bulgusu raporlanır. |
| Kış aylarında yeterli ışınım olmaz | Ölçüm günü sayısı azalır | Ölçüm takvimi ışınım açısından uygun günlere kaydırılır, oturum başına süre kısaltılır. Kapalı alan için yapay aydınlatma yalnızca ek, ayrı bir seri olarak denenir ve ısınmanın farklı olduğu açıkça belirtilir. |
| Ölçüm günleri arasında ışınım ve rüzgâr farkları büyük | Sınıflar ışınımla karışır | Referans hücre ile normalleştirme, ışınım bandına göre sınıflama ve bulut/rüzgâr kaydı. Aşırı değişken oturumlar ayrı analiz edilir. |
| I–V tarama devresi hatalı veya sıcakta kararsız | Elektriksel özellikler güvenilmez olur | Devre önce bilinen dirençlerle doğrulanır, ısınan parçalar soğutucuyla korunur, tarama süresi kısa tutulur. |
| MOSFET, şönt veya B koşulundaki seri direnç aşırı ısınır | Ölçüm güvenliği ve bileşen bütünlüğü tehlikeye girer | Güç değerleri en yüksek $I^2R$ hesabına göre en az iki güvenlik katsayısıyla seçilir. Bileşen sıcaklığı izlenir; olağan dışı ısınmada devre kesime alınır, koşul durdurulur ve daha düşük direnç/akım seviyesine geçilir. |
| Panel veya ölçüm cihazı yağmur ya da rüzgârdan zarar görür | Kayıp ve gecikme | Yağış öngörülen günlerde ölçüm yapılmaz, elektronik su geçirmez kutuda tutulur, panel sabitleme güçlendirilir. |
| Modeller veriye aşırı uyum sağlar | Test başarısı gerçeği yansıtmaz | Gün bazlı ayırma, önceden belirlenmiş düzenlileştirilmiş lojistik regresyon, sınırlı ayar seçimi ve basit eşik kuralıyla karşılaştırma |
| Tek kart bilgisayar bütçeye sığmaz | Çıkarım ölçümü yapılamaz | Kurumdaki mevcut bir bilgisayar kullanılır, çıkarım süresi bu cihazda ölçülür. Ana karşılaştırma etkilenmez. |

## 3.3 Araştırma Olanakları

Proje için açık havada güvenli ve izinli bir panel yerleştirme alanı, elektronik çalışma masası, bilgisayar, multimetre ve temel ölçüm aletleri gerekir. **Bu olanakların mevcut olduğu henüz teyit edilmemiştir.** Başvuruya girmeden önce aşağıdaki alanlar danışmanla doldurulacaktır.

- Panelin yerleştirileceği açık alan (çatı, teras, bahçe) ve erişim izni: **[YER VE İZİN]**
- Kullanılacak laboratuvar / birim: **[ADI VE KONUMU]**
- Mevcut bilgisayar ve yazılım altyapısı: **[GERÇEK CİHAZ / OLANAK]**
- Mevcut multimetre / osiloskop / güç kaynağı: **[VAR / YOK VE DETAY]**
- Varsa ödünç alınabilecek referans termal kamera veya ışınım ölçer: **[VAR / YOK]**
- Danışmanın projeye sağlayacağı teknik/laboratuvar desteği: **[TEYİT EDİLMİŞ DESTEK]**

Bu bölüm yalnızca gerçekten var olan ve erişim izni alınmış kaynaklarla tamamlanmalıdır.
