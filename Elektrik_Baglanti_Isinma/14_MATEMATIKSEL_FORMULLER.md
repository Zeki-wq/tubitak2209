# Matematiksel Formüller

Gösterimler: $T$ bağlantı sıcaklığı, $T_a$ ortam sıcaklığı, $I$ akım, $R_c$ temas direnci, $R_{th}$ ısıl direnç, $C_{th}$ ısıl sığa.

## 1. Isınmanın fiziği

Temasta harcanan güç:

$$P = I^2 R_c$$

Tek kütleli (toplu parametreli) ısıl model:

$$C_{th}\,\frac{dT}{dt} = I^2 R_c - \frac{T - T_a}{R_{th}}$$

Sabit $I$ ve $R_c$ için çözüm:

$$T(t) = T_a + I^2 R_c R_{th}\left(1 - e^{-t/\tau}\right), \qquad \tau = R_{th}C_{th}$$

Denge sıcaklığı $T_\infty = T_a + I^2 R_c R_{th}$. Sabit alarm eşiği $T_a + 25\,\text{K}$ ise, $I^2R_cR_{th} > 25$ koşulunda bağlantı eşiği aşar. Gevşeklik $R_c$'yi büyüttüğü için aşma süresi kısalır.

Eşiğe ulaşma süresi:

$$t_{thr} = -\tau \ln\!\left(1 - \frac{25}{I^2 R_c R_{th}}\right)$$

Bu bağıntı, hangi $R_c$ ve $I$ değerlerinde koşunun 20 dakikalık sınır içinde eşiğe ulaşacağını pilot öncesinde tahmin etmeye yarar. $R_{th}$ ve $\tau$ pilotta ölçülür.

## 2. Ölçümden türetilen büyüklükler

Görünür direnç (Kelvin gerilim düşümünden):

$$R_{app} = \frac{\Delta V}{I}$$

Termokupl gecikmesi için birinci derece düzeltme:

$$T_{gerçek}(t) \approx T_{ölç}(t) + \tau_{tc}\,\frac{dT_{ölç}}{dt}$$

$\tau_{tc}$ basamak tepkisinden ölçülür. Gürültüyü büyüttüğü için düzeltme ana sonuca değil, duyarlılık analizine girer.

Pencere eğimi (en küçük kareler), $n$ örnekli pencerede:

$$m = \frac{\sum_{i}(t_i-\bar t)(T_i-\bar T)}{\sum_{i}(t_i-\bar t)^2}$$

## 3. Tahmin hedefi ve karar kuralı

Etiket ($H$ = 60 s ufuk):

$$y(t) = \mathbb{1}\!\left[\max_{s\in[t,\,t+H]} T(s) \ge T_{thr}\right]$$

Lojistik model:

$$p(t) = \sigma(\mathbf{w}^\top \mathbf{x}(t) + b), \qquad \sigma(z) = \frac{1}{1+e^{-z}}$$

Alarm: $p(t)\ge\tau$. Eşik $\tau$, yalnızca eğitimdeki normal pencerelerde seçilir:

$$\tau = \min\{\tau' : \text{YU}_{eğitim}(\tau') \le \text{YU}_{hedef}\}$$

## 4. Ölçütler

Erken uyarı süresi (koşu $k$ için):

$$L_k = t_{thr,k} - t_{uyarı,k}$$

Pozitif $L_k$ modelin sabit eşikten önce uyardığı anlamına gelir.

Saatlik yanlış uyarı:

$$\text{YU} = \frac{N_{yu}}{T_{normal}\;[\text{saat}]}$$

Duyarlılık: uyarı beklenen koşularda en az bir uyarı verilen koşuların oranı.

$$\text{DUY} = \frac{TP}{TP+FN}$$

## 5. Belirsizlik

Yöntemler arası eşleştirilmiş fark: $d_k = L_k^{Y3} - L_k^{Y1}$. Ortalama $\bar d$ için yüzde 95 güven aralığı, koşuların yerine koyarak yeniden örneklenmesiyle (bootstrap, $B = 5000$) bulunur:

$$\text{GA}_{95} = \left[\bar d^{*}_{(0.025)},\; \bar d^{*}_{(0.975)}\right]$$

Koşu sayısı az olduğu için sonuç p değeriyle değil, aralık ve etki büyüklüğüyle yorumlanır.

## 6. Plan sayımı

$$N_{koşu} = 4_{temas}\times 2_{akım}\times 2_{hava}\times 5_{tekrar} = 80$$
