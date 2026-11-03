# 3. Proje Yönetimi

## 3.1 Çalışma Takvimi

Proje süresi sekiz aydır. Aşağıdaki yüzde değerleri iş paketlerinin **başarıya katkı ağırlıklarıdır** ve toplamları 100'dür. Satın alma, literatür taraması, rapor yazımı veya sonuç paylaşımı ayrı iş paketi yapılmamıştır.

| İş paketi ve faaliyet | Aylar | Ölçülebilir başarı ölçütü | Başarıya katkı (%) |
|---|---|---|---:|
| İP1: Açık veri hazırlığı, özellik çıkarımı ve ses-only / ses+çevre anomali modellerinin kovan bazlı değerlendirilmesi | 1–4 | Üç anomali yönteminin iki girdi biçimiyle, eğitimde görülmemiş kovanlarda yanlış alarm ve duyarlılık sonuçlarıyla raporlanması | 30 |
| İP2: Saha ölçüm düğümünün kurulması ve en az sekiz haftalık kayıt | 2–6 | Sürekli kayıt süresinin ve veri kaybı oranının belgelenmesi, arıcı olay günlüğünün toplanması | 25 |
| İP3: Uç cihaz (ESP32-S3 sınıfı) çıkarımı ve enerji ölçümü | 5–7 | Bellek, çıkarım süresi ve saatlik enerji değerlerinin ölçülmesi, bilgisayar modeliyle uyumun raporlanması | 20 |
| İP4: Bağımsız saha doğrulaması ve sonuçların değerlendirilmesi | 6–8 | Saha kaydında saatlik yanlış alarm, olay tepkisi ve sınırlılık analizinin tamamlanması | 25 |
| **Toplam** | **8 ay** | | **100** |

## 3.2 Risk Yönetimi

| Risk | Etki | B planı ve yönteme etkisi |
|---|---|---|
| Arıcı veya kovan erişimi sağlanamaz | Saha bölümü yapılamaz | Proje yalnızca açık veri ve uç cihaz çıkarımı (İP1 ve İP3) ile sürdürülür. Saha doğrulaması yerine açık verinin ayrılmış kovanları son test olarak kullanılır. İP2 ve İP4'ün ağırlığı İP1'e aktarılır. Bu durum başvuru öncesi plan olarak belirtilir. |
| Açık veri beklenen yapıda veya lisansta değil | Yöntem değişir | Başvuru öncesi veri kümesinin yapısı kontrol edilir. Gerekirse başka bir açık veri kümesi veya kendi kayıtlarımız temel alınır. |
| Etiket yok, anomaliyi doğrulamak zor | Başarı ölçütü zayıflar | Yanlış alarm yükü, enjekte edilen bozulmalar ve olay günlüğü gibi birden fazla dolaylı ölçüt kullanılır. Biyolojik tanı iddiası kurulmaz. Sonuçlar yalnızca "sapma" olarak yorumlanır. |
| Sıcaklık ve nem bilgisi hiçbir fark yaratmaz | H1 desteklenmez | Sonuç olumsuz olarak raporlanır. Günün saati gibi alternatif bağlam bilgisi ek analiz olarak denenir. |
| Kovan içi nem ve propolis sensörü bozar | Veri kaybı | Mikrofon ve sensör koruma ağıyla yerleştirilir, yedek sensör bulundurulur, ölçüm sıklığı düşürülebilir. |
| Pil veya güneş paneli yetmez | Kayıt kesilir | Kayıt sıklığı azaltılır, daha büyük pil kullanılır, düğüm haftalık bakım ziyaretleriyle kontrol edilir. |
| Sezon dışı başlangıç | Arı faaliyeti azdır, saha verisi sınırlı kalır | Saha kaydı aktif sezonun başlangıcına planlanır. İlk aylar açık veriye ayrılır. |
| Modeller veriye aşırı uyum sağlar | Test başarısı gerçeği yansıtmaz | Kovan bazlı ayırma, sınırlı model karmaşıklığı ve basit istatistiksel referansla karşılaştırma |

## 3.3 Araştırma Olanakları

Proje için bilgisayar, temel elektronik çalışma alanı ve en önemlisi arılık erişimi gerekir. **Bu olanakların mevcut olduğu henüz teyit edilmemiştir.** Başvuruya girmeden önce aşağıdaki alanlar danışmanla doldurulacaktır.

- Saha iş birliği (arıcı / fakülte arılığı / üniversite uygulama arılığı) ve yazılı onay: **[AD, KONUM, KOVAN SAYISI]**
- Arıcının bilgilendirilmesi ve sensör yerleşimine izni: **[TEYİT]**
- Kullanılacak laboratuvar / birim: **[ADI VE KONUMU]**
- Mevcut bilgisayar ve yazılım altyapısı: **[GERÇEK CİHAZ / OLANAK]**
- Mevcut osiloskop / multimetre / lehim istasyonu: **[VAR / YOK VE DETAY]**
- Danışmanın projeye sağlayacağı teknik destek: **[TEYİT EDİLMİŞ DESTEK]**

Bu bölüm yalnızca gerçekten var olan ve erişim izni alınmış kaynaklarla tamamlanmalıdır.
