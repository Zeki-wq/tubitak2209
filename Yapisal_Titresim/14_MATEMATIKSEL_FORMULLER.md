# Matematiksel Formüller

## 1. Konsol kiriş doğal frekansları (Euler–Bernoulli)

$$f_n = \frac{(\beta_n L)^2}{2\pi L^2}\sqrt{\frac{EI}{\rho A}}, \qquad \beta_1L = 1{,}8751,\ \beta_2L = 4{,}6941,\ \beta_3L = 7{,}8548$$

Kesit için $I = bh^3/12$, $A = bh$.

**Ön hesap (alüminyum, $E\approx 69$ GPa, $\rho\approx 2700$ kg/m³; $L=0{,}5$ m, $b=40$ mm, $h=4$ mm):**

$I \approx 2{,}13\times10^{-10}$ m⁴, $EI \approx 14{,}7$ N·m², $\rho A \approx 0{,}432$ kg/m. Buradan $f_1 \approx 13$ Hz çıkar. Bu, 10–20 Hz beklentisiyle uyumludur. Malzeme sabitleri nominal değerlerdir, gerçek frekans pilotta ölçülür.

## 2. Uç kütlesinin etkisi (Rayleigh yaklaşımı)

Uç rijitliği $k = 3EI/L^3 \approx 353$ N/m. Kirişin etkin kütlesi $\approx 0{,}2357\,m_k$ ($m_k = \rho A L \approx 0{,}216$ kg):

$$f_1 \approx \frac{1}{2\pi}\sqrt{\frac{3EI}{L^3\,(M + 0{,}2357\,m_k)}}$$

Yaklaşık değerler: $M=0$ için $\approx 13{,}3$ Hz, $M=50$ g için $\approx 9{,}4$ Hz, $M=100$ g için $\approx 7{,}7$ Hz. Kütlenin yarattığı kayma hasarınkinden çok büyük olabilir. Bu yüzden kütle düzeyleri bilerek deneye konmuştur ve model kütleye göre normalleştirilmiş özelliklerle de sınanır.

## 3. Hasarın frekansa etkisi

Rijitlikteki yerel azalma $\Delta EI(x)$ için birinci mertebe kayma (Rayleigh bölümü), $\phi_n$ mod şekli:

$$\frac{\Delta f_n}{f_n} \approx -\frac{1}{2}\,\frac{\int_0^L \Delta EI(x)\,[\phi_n''(x)]^2\,dx}{\int_0^L EI\,[\phi_n''(x)]^2\,dx}$$

Çentik, eğrilik $\phi_n''$ yüksekken (köke yakın) açıldığı için ilk modda belirgin kayma beklenir. Bu bağıntı yalnızca fiziksel makullük denetimi içindir.

Normalize frekans kayması (referans = aynı kirişin ilk gün, sağlam durumu):

$$\delta_n = \frac{f_n - f_n^{ref}}{f_n^{ref}}$$

## 4. Serbest sönümlü titreşim modeli

$$y(t) = \sum_{n=1}^{3} A_n\,e^{-\zeta_n\omega_n t}\sin\!\big(\omega_n\sqrt{1-\zeta_n^2}\,t + \varphi_n\big), \qquad \omega_n = 2\pi f_n$$

Parametreler bant geçiren süzgeçlenmiş her mod için en küçük kareler ile uydurulur.

## 5. Spektral kestirim ve çözünürlük

Welch kestirimi: $K$ örtüşen bölümün periyodogram ortalaması,

$$\hat P(f) = \frac{1}{K}\sum_{k=1}^{K}\frac{1}{U}\left|\sum_{n} w[n]\,x_k[n]\,e^{-j2\pi fn/f_s}\right|^2$$

Frekans çözünürlüğü $\Delta f = f_s/N$. 4 s kayıt ve $f_s=1$ kHz için $\Delta f = 0{,}25$ Hz. Hasar kaymaları bundan küçük olabileceği için parabolik ara değerleme ve sinüs uydurma kullanılır:

$$\hat f = f_k + \frac{\Delta f}{2}\,\frac{P_{k-1}-P_{k+1}}{P_{k-1}-2P_k+P_{k+1}}$$

## 6. Ölçütler

Makro F1 ve dengeli doğruluk ($R_c$ sınıf duyarlılığı):

$$\text{MakroF1} = \frac1C\sum_c F1_c, \qquad \text{DD} = \frac1C\sum_c R_c$$

**En küçük ayırt edilebilir hasar:** düzey $L$ için ortalama kayma $\bar\delta_L$ ile sağlam durum arasındaki fark $d_L$ ve yeniden örneklemeli güven aralığı:

$$d_L = \bar\delta_L - \bar\delta_0, \qquad \text{EKDH} = \min\{L: 0 \notin \text{GA}_{95}(d_L)\}$$

Frekans kestirim hatası: $\;e_f = |f_{\text{ölçüm}} - f_{\text{referans}}|$.

## 7. Plan sayımı

$$N = 2_{kiriş}\times 4_{durum}\times 3_{kütle}\times 2_{yerleşim}\times 5_{gün} = 240$$
