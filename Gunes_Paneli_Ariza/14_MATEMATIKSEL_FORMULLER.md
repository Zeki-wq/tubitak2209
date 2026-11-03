# Matematiksel Formüller

Gösterimler: $G$ ışınım, $T_p$ panel sıcaklığı, $I_{sc}$ kısa devre akımı, $V_{oc}$ açık devre gerilimi, $R_s$ seri direnç.

## 1. Tek diyotlu hücre modeli

$$I = I_{ph} - I_0\left[\exp\!\left(\frac{V + I R_s}{n\,N_s\,V_t}\right) - 1\right] - \frac{V + I R_s}{R_{sh}}$$

$V_t = kT/q$ ısıl gerilimdir, $N_s$ seri hücre sayısı, $n$ idealite katsayısıdır. Modelin tüm parametrelerini kestirmek amacımız değil. Modeli, **seri direnç arttığında eğrinin neden açık devre ucunda yatıklaştığını** açıklamak için kullanıyoruz.

## 2. Seri direnç eklemenin beklenen etkisi (B durumu)

Dışarıdan $R_{ek}$ eklenirse, maksimum güç noktasında yaklaşık olarak:

$$\Delta V_{mp} \approx I_{mp}\,R_{ek}, \qquad \Delta P_{mp} \approx I_{mp}^2\,R_{ek}$$

Bu iki bağıntı, B koşulunda ölçülen gücün makul olup olmadığını kontrol etmek için kullanılır. Ölçüm bundan belirgin saparsa devre veya kalibrasyon hatası aranır.

## 3. I–V özetleri

$$P = VI, \qquad P_{mp} = \max_k (V_kI_k), \qquad FF = \frac{P_{mp}}{I_{sc}V_{oc}}$$

Seri direnç kestirimi (açık devre civarında):

$$\hat R_s \approx -\left.\frac{dV}{dI}\right|_{V\approx V_{oc}}$$

## 4. Normalleştirme (basit doğrusal düzeltme)

$$I_{sc}^{n} = I_{sc}\,\frac{G_{ref}}{G}\,\frac{1}{1+\alpha\,(T_p-T_{ref})}, \qquad V_{oc}^{n} = V_{oc} - \beta\,(T_p - T_{ref})$$

$\alpha$ ve $\beta$ panel veri sayfasından alınır. Düzeltme IEC 60891'deki yöntemlerin sadeleştirilmiş halidir. Sadeleştirmenin hatası, referans hücre ve sıcaklık değiştirilerek pilotta ölçülür ve rapora yazılır.

## 5. Termal özellikler

$$\Delta T_{sıcak} = T_{maks} - \bar T, \qquad f_{sıcak} = \frac{\#\{\text{piksel}: T > \bar T + 2\sigma\}}{\#\{\text{panel pikseli}\}}$$

$$\sigma_{uzay} = \sqrt{\frac{1}{N-1}\sum_i (T_i - \bar T)^2}$$

## 6. Sınıflandırma ölçütleri

Her sınıf $c$ için $F1_c = \dfrac{2P_cR_c}{P_c+R_c}$. Makro F1:

$$\text{MakroF1} = \frac{1}{C}\sum_{c=1}^{C} F1_c$$

**Birincil ölçüt** (gölgelenmenin bakım sınıfına karışması):

$$\text{GK} = \frac{N(\text{gerçek}=G,\ \text{tahmin}\in\{K,B\})}{N(\text{gerçek}=G)}$$

Özgüllük $=TN/(TN+FP)$, duyarlılık $=TP/(TP+FN)$.

## 7. Belirsizlik

Eşleştirilmiş oturum farkı $d_s = \text{GK}_s^{termal} - \text{GK}_s^{birleşik}$ için yüzde 95 güven aralığı, oturumların yerine koyarak yeniden örneklenmesiyle bulunur. Aynı gündeki oturumlar bir blok sayılır.

## 8. Plan sayımı

$$N_{oturum} = (1 + 3 + 2 + 3)_{koşul}\times 2_{ışınım}\times 5_{gün} = 90$$
