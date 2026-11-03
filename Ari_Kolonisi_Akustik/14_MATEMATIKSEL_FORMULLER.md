# Matematiksel Formüller

## 1. Ses özellikleri

Kısa süreli Fourier dönüşümü ($w$ pencere işlevi, $m$ çerçeve, $k$ frekans indeksi):

$$X_m[k] = \sum_{n=0}^{N-1} x[n + mH]\,w[n]\,e^{-j2\pi kn/N}$$

Mel bandı enerjisi ($H_i[k]$ $i$. üçgen süzgeç):

$$E_i = \sum_k H_i[k]\,|X[k]|^2$$

Mel ölçeği: $\;\text{mel}(f) = 2595\log_{10}(1 + f/700)$

MFCC (Davis ve Mermelstein, 1980), $M$ süzgeç sayısı:

$$c_n = \sum_{i=1}^{M} \log(E_i)\cos\!\left[\frac{\pi n}{M}\left(i - \tfrac{1}{2}\right)\right]$$

Bant enerji oranı: $\;r_b = \dfrac{\sum_{k\in B}|X[k]|^2}{\sum_k |X[k]|^2}$

## 2. Anomali skorları

**Mahalanobis** ($\mu$, $\Sigma$ eğitimdeki normal pencerelerden):

$$D^2(\mathbf{x}) = (\mathbf{x}-\mu)^\top \Sigma^{-1}(\mathbf{x}-\mu)$$

**Otokodlayıcı** yeniden oluşturma hatası:

$$s(\mathbf{x}) = \|\mathbf{x} - g(f(\mathbf{x}))\|_2^2$$

**Tek sınıflı SVM** karar işlevi $\;h(\mathbf{x}) = \sum_i \alpha_i K(\mathbf{x}_i,\mathbf{x}) - \rho$. Küçük $h$ anomaliye işaret eder.

**Çevre koşullu skor:** çevre vektörü $\mathbf{e}$ için beklenen özellik $\hat{\mathbf{x}} = f_\psi(\mathbf{e})$, kalıntı $\mathbf{r} = \mathbf{x} - \hat{\mathbf{x}}$:

$$s_{koşullu} = \mathbf{r}^\top \Sigma_r^{-1}\mathbf{r}$$

## 3. Kontrollü bozulma ve eşik

Hedef sinyal-gürültü oranı SNR (dB) için gürültü ölçeği:

$$a = \sqrt{\frac{P_x}{P_n\,10^{\,\text{SNR}/10}}}, \qquad x_{bozuk} = x + a\,n$$

Alarm kuralı $s \ge \tau$. Eşik, enjekte edilmiş kümenin skorlarının %10'luk dilimidir ve yüzde 90 yakalama sağlar:

$$\tau = Q_{0{,}10}\big(\{s(x_{bozuk})\}\big), \qquad \text{DUY}(\tau) = 0{,}90$$

## 4. Ölçütler

Saatlik yanlış alarm yükü (kovan $h$, yöntem $y$):

$$\text{YA}_{h,y} = \frac{N_{alarm}}{T_{rutin}\;[\text{saat}]}$$

Alarmın günün saatine dağılımı: gözlenen $O_j$, düzgün dağılım beklentisi $E = N/24$:

$$\chi^2 = \sum_{j=0}^{23}\frac{(O_j - E)^2}{E}$$

Küçük $\chi^2$ alarmların günün saatine bağlı olmadığını, büyük $\chi^2$ günlük döngüye yapışıldığını gösterir. Bunu, bir istatistiksel test olarak değil, **yöntemler arası karşılaştırma ölçüsü** olarak kullanacağız.

Olay yanıtı (arıcı günlüğündeki olay $e$ için, pencere $\Delta$):

$$\text{Yanıt}_e = \mathbb{1}\big[\exists a:\ |t_a - t_e| \le \Delta\big]$$

Uç cihaz uyumu: $\;\rho = \text{corr}(s_{cihaz}, s_{bilgisayar})$ ve $\;\overline{|\Delta s|}$.

## 5. Belirsizlik

Kovan sayısı az olduğundan yüzde 95 güven aralığı, kovan veya gün bloklarının yerine koyarak yeniden örneklenmesiyle hesaplanır. Kesin üstünlük iddiası yerine etki büyüklüğü sunulur.
