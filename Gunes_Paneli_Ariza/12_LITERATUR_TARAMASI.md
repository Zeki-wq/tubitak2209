# Literatür Taraması

> **Taramanın kapsamı ve dürüstlük notu:** Bu bölüm, 4 Kasım 2026 tarihinde yayıncı, standart kuruluşu, üniversite arşivi veya resmî rapor sayfasından künyesi doğrulanan kaynaklarla hazırlanmıştır. İncelenen çalışmaların ölçekleri, panel teknolojileri ve arıza etiketleri birbirinden farklıdır; bu nedenle çalışmaların başarı oranları doğrudan karşılaştırılmamış, bu proje için çıkarımları verilmiştir. "İlk", "literatürde yok" veya kesin üstünlük iddiası yapılmamaktadır.

## 1. Problem alanı

Fotovoltaik (PV) modüllerde sıcak bölge, tek başına arızanın türünü kesinleştirmez. IEA-PVPS'nin modül arızaları derlemesi; hücre çatlağı, bağlantı/ribbon sorunu, bypass diyot sorunu, yanık izi, PID ve yüzeyle ilişkili etkiler gibi farklı arıza mekanizmalarının hem performans hem de güvenlik açısından incelenmesi gerektiğini belirtir (Köntges vd., 2014). Bu nedenle termal görüntüdeki bir sıcaklık anomalisi, doğrudan "bakım gerekir" kararına çevrilmeden önce ölçüm koşulları ve elektriksel davranışla birlikte yorumlanmalıdır.

Kızılötesi (IR) incelemelerin çevresel koşullara duyarlı olması, ölçüm protokolünün parçasıdır. IEC TS 62446-3:2017; ölçüm donanımı, ortam koşulları, inceleme prosedürü, raporlama ve termal anomali matrisine yönelik gereklilikleri tanımlar. Buerhop vd. (2022) de gölgelenme, kirlenme ve ölçüm koşullarının IR bulgusunun yorumunu etkilediğini; IR görüntülerini I–V ölçümleri veya izleme verileriyle tamamlamanın önemini vurgular. Bu proje bu nedenle referans ışınımı, panel arka yüzey sıcaklığını, rüzgâr/bulut gözlemini ve kamera geometrisini her oturumda kaydedecektir.

## 2. Termal ve elektriksel ölçümün tamamlayıcılığı

Muttillo vd. (2020), çalışan panellerde eşzamanlı termal görüntü ile elektriksel karakterizasyonu eşleştirerek termal ve elektriksel imzaların birlikte yorumlanabileceğini göstermiştir. Daher vd. (2024) ise açık hava koşullarındaki bir santralde görsel inceleme, IR, I–V, UV floresans ve elektrolüminesans yöntemlerini birlikte kullanmıştır. Bu çalışmalar, tek bir ölçüm türünün tüm arıza nedenleri için yeterli bir doğrulama sağlamadığını; yöntemlerin birbirini tamamladığını gösterir.

Kısmi gölgelenme ve kirlenme için termal yanıt ile I–V davranışının ilişkisi özellikle önemlidir. Álvarez-Tey vd. (2019), kristal PV modüllerde gölgelenme veya kirlenme koşullarında I–V eğrisi, bypass diyot akımı ve termal yanıtı birlikte incelemiştir. Çalışma, gölgelenme/kirlenme koşullarında bypass diyot davranışı nedeniyle I–V ve P–V eğrilerinde farklı yerel güç noktalarının oluşabileceğini bildirir. Bu bulgu, yalnızca $I_{sc}$ veya yalnızca maksimum sıcaklıkla karar vermek yerine eğrinin özet özelliklerini birlikte kullanma gerekçesidir.

I–V eğrisinin tanısal değeri de bağımsız biçimde gösterilmiştir. Spataru vd. (2015), I–V eğrisi şeklinden hesaplanabilen boyutsuz tanısal parametrelerle kısmi gölgelenme ve artmış seri direnç kayıplarını ayırmaya yönelik bir yöntem önermiştir. Bu proje onların yöntemini aynen yeniden üretmeyecektir; ancak $I_{sc}$, $V_{oc}$, $P_{mp}$, doluluk oranı ve eğim-tabanlı bir özellik kümesi seçmesinin fiziksel dayanağı bu çalışmayla uyumludur.

## 3. Makine öğrenmesi ve deney tasarımı açısından çıkarım

Eltuhamy vd. (2023), CIGS ince film modüllerde IR görüntülerinden çıkarılan istatistiksel/matematiksel özelliklerle I–V ölçümlerini birlikte kullanarak sınıflandırma yapmıştır. Panel teknolojisi, veri büyüklüğü ve arıza kümeleri bu projeden farklıdır; dolayısıyla bildirilen performans değerleri hedef alınmayacaktır. Buna karşılık, iki modaliteden öz nitelik çıkarıp sınıflandırıcıya verme yaklaşımı proje tasarımıyla uyumludur.

Küçük veri kümesinde en büyük risklerden biri, aynı ölçüm oturumundan veya aynı günden gelen birbirine çok benzer kayıtların hem eğitim hem testte bulunmasıdır. Böyle bir sızıntı başarıyı olduğundan yüksek gösterebilir (Kapoor ve Narayanan, 2023). Bu nedenle bu projede:

- bir oturuma ait tüm zaman pencereleri aynı veri bölmesinde tutulacaktır;
- eğitim/test ayrımı takvim gününe göre, model ve ölçekleme seçilmeden önce yapılacaktır;
- ölçekleyici, özellik seçimi ve hiperparametre seçimi yalnızca eğitim verisinde, gün-gruplu çapraz doğrulama ile yapılacaktır;
- nihai test sonuçları, model seçimine hiç katılmayan günler üzerinde yalnızca bir kez hesaplanacaktır.

90 oturumluk planlanan veri hacminde, çok sayıda algoritma ve ayar denemek yanıltıcı iyimserlik riski taşır. Bu nedenle yalnızca sınıf-ağırlıklı, düzenlileştirilmiş lojistik regresyon kullanılacak; düzenlileştirme katsayısı eğitim günlerinde gruplu çapraz doğrulamayla seçilecektir. Uygulama yapılırsa kullanılan yazılım sürümü, rasgele tohum, veri bölmeleri ve model ayarları raporda verilecektir. Scikit-learn araçlarının atfı için Pedregosa vd. (2011) kullanılacaktır.

## 4. Bu projenin literatür içindeki konumu

Literatür, IR görüntüleme ile I–V karakterizasyonunun tamamlayıcı olduğunu ve gölgelenme/kirlenme/seri direnç etkilerinin I–V eğrisinde ayırt edici izler oluşturabildiğini desteklemektedir. İncelenen kaynaklar, bu projenin özel hedefi olan **düşük çözünürlüklü termal sensör ile aynı anda alınan I–V özelliklerinin, kontrollü ve geri döndürülebilir koşullarda geçici gölgelenmenin yanlış bakım alarmına etkisini** doğrudan sınayan bir kanıt olarak sunulamaz. Bu nedenle önerinin katkısı yeni bir arıza türü keşfetmek değil; daraltılmış bu soruda termal, elektriksel ve birleşik özellik kümelerini aynı deney düzeni içinde adil biçimde karşılaştırmaktır.

Bu kapsamın iki sınırı vardır:

1. Çıkışa eklenen direnç, kapsül içindeki gerçek bağlantı bozulmasının kendisi değildir; yalnızca artmış seri direnç kaybını temsil eden, geri alınabilir bir deney koşuludur.
2. Yarı saydam filmle oluşturulan kirlenme, doğal tozun tüm optik ve ısıl davranışını temsil etmez; "kontrollü yüzey geçirgenliği azalması" olarak raporlanacaktır.

## 5. Kaynak–yöntem eşleştirme tablosu

| Kaynak | Doğrulanmış katkı | Bu projedeki kullanım | Doğrudan genellenmeyecek nokta |
|---|---|---|---|
| Köntges vd. (2014) | Modül arıza türleri ve inceleme yöntemleri derlemesi | Arıza sınıflarının fiziksel arka planı | Farklı modül yaşları ve saha koşulları |
| IEC TS 62446-3:2017 | Dış ortam IR inceleme koşulları ve raporlama | Ölçüm protokolü ve metadata | Düşük çözünürlüklü sensör doğruluğu |
| IEC 60904-1:2020; IEC 60891:2021/COR1:2024 | I–V ölçümü ile sıcaklık/ışınım düzeltme çerçevesi | I–V taraması, kalibrasyon ve düzeltme sınırı | Basitleştirilmiş modelin tam standart çevirisi olduğu iddiası |
| Álvarez-Tey vd. (2019) | Gölgelenme/kirlenmede I–V, bypass diyot ve termal davranış | Koşul tasarımı ve özellik seçimi | Kullanılan panel/sensör düzeni |
| Spataru vd. (2015) | I–V şekliyle gölgelenme ve seri direnç kaybı tanısı | Elektriksel özelliklerin fiziksel gerekçesi | Önerilen tanı kurallarını aynen uygulama |
| Muttillo vd. (2020); Daher vd. (2024) | IR ve elektriksel karakterizasyonun tamamlayıcılığı | Çoklu ölçüm yaklaşımının gerekçesi | Santral ölçeği sonuçları |
| Eltuhamy vd. (2023) | IR ve I–V özellikleriyle sınıflandırma | Birleşik özellik yaklaşımının örneği | CIGS teknoloji ve bildirilen skorlar |
| Kapoor ve Narayanan (2023) | Veri sızıntısı ve tekrarlanabilirlik riski | Gün ve oturum bazlı bölme | Bu alana özgü bir deney sonucu değildir |

## 6. Başvuru öncesi son tarama protokolü

Başvuruya girecek sürümden önce Web of Science, Scopus, IEEE Xplore, Google Scholar ve TR Dizin’de aşağıdaki diziler çalıştırılacak; her bulunan çalışma için DOI veya yayıncı sayfası açılarak künye teyit edilecektir.

- `("photovoltaic" OR "PV module") AND ("fault diagnosis" OR "fault detection") AND ("infrared" OR "thermal") AND "I-V"`
- `("partial shading" OR soiling) AND ("thermal imaging" OR thermography) AND (classification OR diagnosis)`
- `"photovoltaic" AND "series resistance" AND "I-V curve" AND diagnosis`
- `("thermal image" AND "I-V curve") AND photovoltaic AND (fusion OR multimodal OR classification)`

**Dahil etme ölçütleri:** hakemli makale veya resmî standart/teknik rapor; yöntem ve veri kaynağını açıkça belirten çalışma; PV modül veya dizi düzeyinde doğrudan ölçüm. **Dışlama ölçütleri:** sadece benzetim verisi kullanan ve saha/deney doğrulaması vermeyen çalışmalar (ayrı bağlam notu dışında); künyesi veya kalıcı bağlantısı doğrulanamayan kayıtlar.

Kayıt tablosunda şu alanlar tutulacaktır: künye/DOI, modül teknolojisi, ölçüm türleri, arıza sınıfları, veri kaynağı, örnek/grup sayısı, eğitim-test bölmesi, ana ölçüt, sınırlılık ve bu projeye etkisi. Başvuru metninde yalnızca bu kontrolden geçen ve metin içinde gerçekten atıf yapılan kaynaklar bırakılacaktır.
