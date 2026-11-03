# 1.1 Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Tarımda tatlı suyun büyük kısmı sulamaya gidiyor. Gereğinden fazla sulamak su ve enerji israfı, az sulamak ise verim kaybı demek. Bu yüzden sulamanın bitkinin gerçek ihtiyacına göre yapılması uzun zamandır hedefleniyor. Piyasadaki akıllı sulama çözümlerinin birçoğu kapasitif veya dirençsel toprak nemi sensörüne dayanıyor. Basit, ucuz ve anlaşılır bir yöntem.

Ama toprak nemi, bitki su stresinin dolaylı bir göstergesidir. Bitkinin suya ihtiyacı havadaki buhar basıncı açığına, ışığa ve sıcaklığa göre saat saat değişir. Aynı toprak neminde, serin ve nemli bir günde sorun yaşamayan bir bitki, sıcak ve kuru bir günde su kaybına yetişemeyebilir (Allen vd., 1998). Bitki yaprağı su kaybettikçe terlemesi azalır, yaprak sıcaklığı yükselir. Bu nedenle yaprak sıcaklığı uzun süredir bitki su stresi göstergesi olarak kullanılmaktadır (Jackson vd., 1981). Toprak suyu azaldıkça transpirasyonun belirli bir noktadan sonra düşmeye başlaması ise bitki fizyolojisinde iyi bilinen bir davranıştır (Sinclair ve Ludlow, 1986).

Düşük maliyetli kapasitif toprak nemi sensörlerinin ise sıcaklık ve tuzluluktan etkilendiği, sensörden sensöre farklı davrandığı bilinmektedir (Kizito vd., 2008). Bu da nem değerinin tek başına güvenilir bir karar girdisi olmasını zorlaştırır.

Toprak nemi, ESP32 sınıfı kartlar, uzun menzilli haberleşme ve bitki su stresi göstergelerini bir araya getiren sulama sistemleri farklı çalışmalarda gösterilmiştir. Bu nedenle bu sensörleri birleştirmek tek başına yeni sayılmaz. Biz farklı bir yerden başlıyoruz. Sulama koşulları bilerek ve kontrollü oluşturulmuş aynı tür bitkilerde, hangi sensör bilgisinin stresi ne kadar önceden haber verdiğini, **sensörlerden bağımsız bir referansla** karşılaştırmak istiyoruz. Referans olarak bitkinin gerçek su kaybı kullanılacak, yani saksıyı her gün tartacağız.

Bu tasarımın ana nedeni etiket güvenilirliğidir. Eğer "stres var" etiketini toprak neminden üretip sonra toprak nemiyle tahmin etmeye çalışırsak sonuç döngüsel olur. Aynı sorun yaprak sıcaklığından hesaplanan stres indeksleri için de geçerlidir. Biz etiketi sensörlerden bağımsız bir yoldan, gerçek transpirasyon ve gözlemden üreteceğiz.

**Araştırma sorusu:** Hava koşulları ve temassız yaprak sıcaklığı bilgisi, yalnızca toprak nemi kullanan modele kıyasla bitki su stresini daha erken ve daha doğru tahmin edebilir mi?

**H1:** Toprak nemine hava koşulları ve yaprak sıcaklığı eklenen model, eğitimde kullanılmayan bağımsız seride, ertesi gün stres durumunu tahmin etmede yalnızca toprak nemi kullanan modelden daha yüksek makro F1 skoru verecektir.

**H2:** Toprak nemi aynı düzeyde olduğunda, buhar basıncı açığı ve yaprak-hava sıcaklık farkı bilgisi transpirasyon oranındaki değişimin daha büyük bölümünü açıklayacaktır.

**H3:** Çok sensörlü model, sabit toprak nemi eşiğine göre stres eşiğine girmeden önce daha uzun bir uyarı süresi sağlayacaktır.

Hipotezlerin hiçbiri önceden doğru kabul edilmiyor. Ek sensörler katkı sağlamazsa, tarımsal uygulamalar için ucuz çözüm olan toprak nemi sensörünün hangi koşullarda yettiği gösterilmiş olur.

Çalışma, tek tür, kontrollü saksı koşulları ve birkaç haftalık deney serileriyle sınırlıdır. Tarla koşulları, farklı türler ve toprak tipleri kapsam dışındadır.
