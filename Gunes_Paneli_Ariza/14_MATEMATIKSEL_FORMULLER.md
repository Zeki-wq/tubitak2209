# Matematiksel Formüller

Gösterimler: $G$ kalibre edilmişse mutlak ışınım, $G_{rel}$ kalibre edilmemiş referans hücre çıktısı, $T_p$ panel sıcaklığı, $I_{sc}$ kısa devre akımı, $V_{oc}$ açık devre gerilimi, $R_s$ seri dirençtir. Sıcaklık, üstel ifadelerde mutlak sıcaklık (K) cinsinden; doğrusal sıcaklık düzeltmelerinde ise veri sayfasındaki katsayıyla uyumlu °C farkı cinsinden kullanılır.

## 1. Tek diyotlu hücre modeli

$$I = I_{ph} - I_0\left[\exp\!\left(\frac{V + I R_s}{n\,N_s\,V_t}\right) - 1\right] - \frac{V + I R_s}{R_{sh}}$$

$V_t = kT/q$ ısıl gerilimdir, $N_s$ seri hücre sayısı, $n$ idealite katsayısıdır. Modelin tüm parametrelerini kestirmek amacımız değil. Modeli, **seri direnç arttığında eğrinin neden açık devre ucunda yatıklaştığını** açıklamak için kullanıyoruz.

## 2. Haricî seri direnç eklemenin beklenen etkisi (B temsil koşulu)

Dışarıdan $R_{ek}$ eklenir ve gerilim dirençten **sonra**, yani sistem çıkışında ölçülürse $V_{sys}=V_{mod}-IR_{ek}$ olur. Bu durumda maksimum güç noktasında yaklaşık olarak:

$$V_{mp,sys} - V_{mp,mod} \approx -I_{mp,0}\,R_{ek}, \qquad P_{mp,sys} - P_{mp,mod} \approx -I_{mp,0}^{2}\,R_{ek}$$

Burada $R_{ek}$ panel ile yük arasına eklenen haricî dirençtir; $V_{mod}$ panel uçlarındaki, $V_{sys}$ ise dirençten sonraki gerilimdir. Yaklaşım, $I_{mp}$ değişiminin küçük olduğu ilk mertebe varsayımına dayanır. Ek direnç panel ucundan önce ölçülürse panelin kendi $V_{mod}$–$I$ eğrisinde aynı düşüm beklenmez. Bu iki bağıntı B koşulunda ölçülen sistem değişiminin yönünü ve mertebesini kontrol etmek için kullanılır; belirgin sapma, akım değişimi, kablo/ölçüm etkisi veya kalibrasyon hatası açısından incelenir.

Seri dirençteki en yüksek ısıl kayıp için güvenlik denetimi:

$$P_{R,\max}=I_{sc}^{2}R_{ek}, \qquad P_{nominal}\geq 2P_{R,\max}$$

Bu, yalnızca direnç seçimi için muhafazakâr bir sınırdır; direnç yüzey sıcaklığı ayrıca izlenir ve aşırı ısınmada deney durdurulur.

## 3. I–V özetleri

$$P = VI, \qquad P_{mp} = \max_k (V_kI_k), \qquad FF = \frac{P_{mp}}{I_{sc}V_{oc}}$$

Tanısal eğim özelliği (açık devre civarında):

$$S_{oc} = -\left.\frac{dV}{dI}\right|_{V\approx V_{oc}}$$

$S_{oc}$, I–V eğrisinin açık devre ucundaki yerel eğiminden hesaplanan bir **özelliktir**. Tek diyotlu modelde diyotun diferansiyel direnci ve paralel direnç de bu eğime katkı verdiği için $S_{oc}$ doğrudan fiziksel $R_s$ ölçümü olarak yorumlanmayacaktır. Fiziksel seri direnç veya tam eğri düzeltmesi gerektiğinde IEC 60891:2021/COR1:2024'teki prosedürler ve pilot kalibrasyon esas alınır.

## 4. Normalleştirme (basit doğrusal düzeltme)

$$I_{sc}^{n} = I_{sc}\,\frac{G_{ref}}{G}\,\frac{1}{1+\alpha_I\,(T_p-T_{ref})}, \qquad V_{oc}^{n} = V_{oc} - \beta_V\,(T_p-T_{ref})$$

$G_{ref}$ hedef referans ışınımı, $T_{ref}$ hedef sıcaklığı, $\alpha_I$ bağıl kısa-devre-akımı sıcaklık katsayısını, $\beta_V$ ise işaretli açık-devre-gerilimi sıcaklık katsayısını ifade eder (silikon modüllerde tipik olarak negatiftir). Katsayılar panel veri sayfasından alınacak ve pilotta kontrol edilecektir. Referans hücre kalibre değilse burada $G$ yerine $G_{rel}$ kullanılır; bu durumda sonuç mutlak STC çevirisi değil, oturumlar arası göreli bir düzeltmedir. Bu ifade IEC 60891:2021/COR1:2024'teki tam I–V eğrisi çeviri prosedürünün yerine geçmez; sınırlı özellik normalizasyonu için kullanılan açık bir ilk yaklaşımdır. Pilot hata kabul edilemezse, normalleştirme yerine $G_{rel}$ ve $T_p$ modele kovaryant olarak eklenir ve sonuç bu sınırlılıkla raporlanır.

## 5. Termal özellikler

$$\Delta T_{sıcak} = T_{maks} - \bar T, \qquad f_{sıcak} = \frac{\#\{\text{piksel}: T > \bar T + 2\sigma\}}{\#\{\text{panel pikseli}\}}$$

$$\sigma_{uzay} = \sqrt{\frac{1}{N-1}\sum_i (T_i - \bar T)^2}$$

## 6. Görüş alanı ve piksel ölçeği

Termal sensörün yatay görüş açısı $\theta_h$, panel-sensör mesafesi $d$, yatay piksel sayısı $N_x$ ise panel düzlemindeki yaklaşık yatay görüş alanı ve piksel genişliği şöyledir:

$$W_{FOV} = 2d\tan\left(\frac{\theta_h}{2}\right), \qquad a_{px} = \frac{W_{FOV}}{N_x}$$

Panel genişliği $W_p$ için yatayda kapsanan piksel sayısı $n_p = W_p/a_{px}$ olarak kaydedilir. Pilot raporda $n_p$, panel maskesindeki toplam piksel sayısı ve ayırt edilmeye çalışılan sıcak bölgenin yaklaşık piksel alanı verilecektir. Bu bağıntı bir algılama başarısı garantisi değildir; düşük çözünürlüğün sonuçlara etkisini şeffaf biçimde belgelemek içindir.

## 7. Sınıflandırma ölçütleri

Her sınıf $c$ için $F1_c = \dfrac{2P_cR_c}{P_c+R_c}$. Makro F1:

$$\text{MakroF1} = \frac{1}{C}\sum_{c=1}^{C} F1_c$$

**Birincil ölçüt** (gölgelenmenin K/B bakım-temsil sınıflarına karışması):

$$\text{GK} = \frac{N(\text{gerçek}=G,\ \text{tahmin}\in\{K,B\})}{N(\text{gerçek}=G)}$$

Özgüllük $=TN/(TN+FP)$, duyarlılık $=TP/(TP+FN)$.

## 8. Belirsizlik

Gölgelenme sınıfındaki her **test** oturumu $i$ için eşleştirilmiş hata farkı $d_i = \mathbb{1}(\hat y_i^{termal}\in\{K,B\}) - \mathbb{1}(\hat y_i^{birleşik}\in\{K,B\})$ tanımlanır. Birincil ölçütteki fark $\bar d$ ile özetlenir. Bağımsız test kümesinde en az sekiz gün bloğu varsa, yüzde 95 güven aralığı günleri blok kabul eden yerine koymalı yeniden örnekleme ile hesaplanır; aynı güne ait oturumlar birlikte örneklenir. Daha az gün bloğunda bu aralık kararlı kabul edilmeyecek, $\bar d$ ve gün bazlı hata örnekleri betimsel verilecektir. Makro F1 farkı için de, yalnızca yeterli gün sayısında, aynı gün-bloklu yeniden örnekleme her örneklemde ölçüt yeniden hesaplanarak uygulanır.

## 9. Plan sayımı

$$N_{oturum} = (1 + 3 + 2 + 3)_{koşul}\times 2_{operasyonel\ bant}\times 5_{gün} = 90$$

Her ölçüm günü yalnızca bir kararlı operasyonel bantta dokuz koşul uygulanır. Bu nedenle 90 oturum, her koşul-bant birleşiminin en az beş farklı günde gözlenmesi koşuluyla en az on takvim gününe dağıtılır.
