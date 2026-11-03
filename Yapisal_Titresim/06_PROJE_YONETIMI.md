# 3. Proje Yönetimi

## 3.1 Çalışma Takvimi

Proje süresi sekiz aydır. Aşağıdaki yüzde değerleri iş paketlerinin **başarıya katkı ağırlıklarıdır** ve toplamları 100'dür. Satın alma, literatür taraması, rapor yazımı veya sonuç paylaşımı ayrı iş paketi yapılmamıştır.

| İş paketi ve faaliyet | Aylar | Ölçülebilir başarı ölçütü | Başarıya katkı (%) |
|---|---|---|---:|
| İP1: Deney düzeneğinin kurulması, sensör gürültü ve vurucu tekrarlanabilirliği pilot ölçümü | 1–2 | İlk üç modun görünür olduğu, tekrarlanabilir darbe kayıtlarının ve gürültü tabanı değerlerinin belgelenmesi | 25 |
| İP2: Hasar aşamaları ve bozucu etkilerle ana deney serisi | 3–5 | Planlanan 240 koşulun tamamlanması veya eksik koşulların nedeninin kayıt altına alınması | 30 |
| İP3: Modal özellik çıkarımı ve model gruplarının kurulması | 4–6 | Frekans kuralı, tek, iki ve üç sensörlü modellerin aynı protokolle eğitilmesi | 25 |
| İP4: Bağımsız gün ve ikinci kiriş testi, sensör sayısı/konumu analizi ve değerlendirme | 6–8 | Bağımsız test sonuçlarının, en küçük ayırt edilebilir hasar düzeyinin ve sınırlılıkların belirsizlikle raporlanması | 20 |
| **Toplam** | **8 ay** | | **100** |

## 3.2 Risk Yönetimi

| Risk | Etki | B planı ve yönteme etkisi |
|---|---|---|
| Düşük maliyetli ivmeölçer küçük frekans kaymalarını ayıramaz | Ayrıştırma başarısı düşer | Daha büyük çentik derinlikleri ve daha esnek (ince) kiriş seçilir, referans ivmeölçer kullanılır, kayıt süresi uzatılır. Sonuç olumsuzsa "bu sensörle şu hasar düzeyinin altı ayırt edilemez" bulgusu olarak raporlanır. |
| Vurucu her darbede farklı enerji verir | Genlik ve frekans yayılımı artar | Vurucu serbest bırakma yüksekliği veya sürücü akımı sabitlenir, darbe genliği özelliklere dahil edilmez, gerekirse darbe sayısı artırılır. |
| Sıkıştırma koşulu her gün farklı frekans verir | Hasarla karışır | Tork kontrollü sıkma, sıkma sırası standardı ve her gün sağlam kiriş kontrol ölçümü. Bu gün-gün değişim zaten bir bozucu etki olarak plana alınmıştır. |
| Çentik açma işlemi kirişi beklenenden fazla zayıflatır | Aşamalar atlanır | Önce yedek kirişte deneme kesimi yapılır, derinlik pilotta ayarlanır. Üçüncü kiriş yedek olarak bulundurulur. |
| Üç ivmeölçer senkron olmaz veya SPI hızı yetmez | Genlik oranları güvenilmez | Tek mikrodenetleyici ve ortak zaman tabanı kullanılır. Hız yetmezse örnekleme hızı düşürülür veya sensör başına ayrı kart ve ortak tetik denenir. |
| Ortam sıcaklığı etkisi ayırt edilemez | Frekans kaymaları sıcaklıkla karışır | Sıcaklık kaydedilir ve özellik olarak denenir, ölçümler benzer sıcaklıkta yapılmaya çalışılır. Büyük etki varsa sınırlılık olarak raporlanır. |
| Modeller veriye aşırı uyum sağlar | Test başarısı gerçeği yansıtmaz | Gün ve kiriş bazlı ayırma, sınırlı model karmaşıklığı ve basit frekans kuralıyla karşılaştırma |
| Laboratuvarda kiriş işleme/sıkıştırma imkânı yok | Düzenek kurulamaz | Atölye veya başka bölümden hizmet alınır, basit bir mengene ve kelepçe düzeni denenir. |

## 3.3 Araştırma Olanakları

Proje için sağlam bir tezgâh veya mengene, kirişi kesip çentik açabilecek bir atölye imkânı, bilgisayar ve temel elektronik ölçüm ekipmanı gerekir. **Bu olanakların mevcut olduğu henüz teyit edilmemiştir.** Başvuruya girmeden önce aşağıdaki alanlar danışmanla doldurulacaktır.

- Kullanılacak laboratuvar / birim: **[ADI VE KONUMU]**
- Kiriş kesim ve çentik açma imkânı: **[ATÖLYE / SORUMLU]**
- Mevcut bilgisayar ve yazılım altyapısı: **[GERÇEK CİHAZ / OLANAK]**
- Mevcut osiloskop / multimetre / güç kaynağı: **[VAR / YOK VE DETAY]**
- Varsa ödünç alınabilecek referans ivmeölçer veya modal analiz ekipmanı: **[VAR / YOK]**
- Danışmanın projeye sağlayacağı teknik/laboratuvar desteği: **[TEYİT EDİLMİŞ DESTEK]**

Bu bölüm yalnızca gerçekten var olan ve erişim izni alınmış kaynaklarla tamamlanmalıdır.
