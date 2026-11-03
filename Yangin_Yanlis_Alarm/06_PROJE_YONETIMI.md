# 3. Proje Yönetimi

## 3.1 Çalışma Takvimi

Proje süresi sekiz aydır. Aşağıdaki yüzde değerleri iş paketlerinin **başarıya katkı ağırlıklarıdır** ve toplamları 100'dür. Satın alma, literatür taraması, rapor yazımı veya sonuç paylaşımı ayrı iş paketi yapılmamıştır.

| İş paketi ve faaliyet | Aylar | Ölçülebilir başarı ölçütü | Başarıya katkı (%) |
|---|---|---|---:|
| İP1: Ölçüm düğümlerinin, test haznesinin ve referans alarm kaydının kurulması, pilot ölçüm | 1–2 | Arka plan ve en az iki duman benzeri olay için sensör gürültüsü, hazne temizlenme süresi ve referans alarm gecikmesinin belgelenmesi | 25 |
| İP2: Açık veri analizi ve kendi olay veri kümesinin oluşturulması | 1–5 | Açık veri üzerinde oturum bazlı karşılaştırmanın tamamlanması, planlanan 80 olay kaydının tamamlanması veya eksiklerin nedeninin kayıt altına alınması | 30 |
| İP3: Özellik çıkarımı ve dört karar yönteminin kurulması | 4–6 | Eşik, kural, zamansal model ve uç cihaz modelinin aynı protokolle eğitilmesi ve ayarlanması | 25 |
| İP4: Bağımsız gün ve olay türü dışarıda bırakma testi, LoRa ve enerji ölçümü, değerlendirme | 6–8 | Sabit duyarlılıkta yanlış alarm oranı, gecikme, enerji ve paket teslim sonuçlarının belirsizlikle raporlanması | 20 |
| **Toplam** | **8 ay** | | **100** |

## 3.2 Risk Yönetimi

| Risk | Etki | B planı ve yönteme etkisi |
|---|---|---|
| Yanma deneyi için güvenlik onayı çıkmaz | Yanma sınıfı kendi verimizde olmaz | Faz B'den bu olay türü çıkarılır. Yanma sınıfı açık veriden alınır, ikinci aşama yalnızca duman benzeri olaylarda "yanlış alarm" karşılaştırmasına dönüşür. Bu durum başvuruda B planı olarak yazılıdır. |
| Açık veri beklenen yapıda değil veya lisansı uygun değil | Faz A zayıflar | Başka bir açık veri kümesi denenir veya Faz A kısaltılıp ağırlık Faz B'ye verilir. |
| Düşük maliyetli partikül sensörü ince/iri ayrımını yeterince yapmaz | H1 ve H2'nin dayanağı zayıflar | Boyut sayım oranları yerine kütle bazlı özellikler ve gaz bileşenleri öne çıkarılır. Sonuç raporlanır. |
| MQ tipi gaz modülleri kararsız veya ısınma süresi uzun | Gaz özellikleri güvenilmez | Yeterli ısınma süresi uygulanır, bu modüller ayrı bir ek özellik grubu olarak ele alınır. Temel karşılaştırma partikül ve ortam sensörleriyle de yapılabilir. |
| Hazne temizlenmez, olaylar birbirine taşar | Etiketler bulanıklaşır | Her olaydan sonra havalandırma ve temel değere dönüş koşulu aranır, koşula uymayan kayıt işaretlenir. |
| Referans alarm sesi doğru algılanamaz | Gecikme ölçümü bozulur | Alarmın LED'ine ışık sensörü eklenir veya ses algılama eşiği hazne dışında ayarlanır. |
| LoRa menzili beklenenden kısa veya yasal sınıra takılır | H3 kısmen sınanabilir | Haberleşme başarısı daha kısa mesafelerde ve düşük güçte raporlanır. Çıkış gücü yasal sınırı aşmaz. |
| Modeller veriye aşırı uyum sağlar | Test başarısı gerçeği yansıtmaz | Gün ve olay türü bazlı ayırma, sınırlı model karmaşıklığı ve basit eşik yöntemiyle karşılaştırma |
| Güvenlik olayı (yanıcı malzeme, aşırı duman) | İnsan ve cihaz zararı | Küçük miktar, gözetim, söndürme aracı, CO uyarısı, havalandırma ve onaylı alan. Onay olmadan yanma denemesi yapılmaz. |

## 3.3 Araştırma Olanakları

Proje için havalandırması olan bir laboratuvar veya atölye, yanmaz bir test yüzeyi, bilgisayar ve temel elektronik ekipman gerekir. **Bu olanakların mevcut olduğu henüz teyit edilmemiştir.** Başvuruya girmeden önce aşağıdaki alanlar danışmanla doldurulacaktır.

- Kullanılacak laboratuvar / birim ve havalandırma durumu: **[ADI VE KONUMU]**
- Yangın / laboratuvar güvenliği sorumlusu ve yazılı onay: **[AD, TARİH]**
- Mevcut söndürme aracı ve CO uyarı cihazı: **[VAR / YOK]**
- Mevcut bilgisayar ve yazılım altyapısı: **[GERÇEK CİHAZ / OLANAK]**
- Mevcut osiloskop / multimetre / lehim istasyonu: **[VAR / YOK VE DETAY]**
- Danışmanın projeye sağlayacağı teknik/laboratuvar desteği: **[TEYİT EDİLMİŞ DESTEK]**

Bu bölüm yalnızca gerçekten var olan ve erişim izni alınmış kaynaklarla tamamlanmalıdır.
