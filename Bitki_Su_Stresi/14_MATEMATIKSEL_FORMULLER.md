# Matematiksel Formüller

## 1. Günlük transpirasyon (tartıdan)

Saksı $i$, gün $d$. $W^{post}$ sulama sonrası, $W^{pre}$ sulama öncesi ağırlık (g). $\bar E_{buh}$ bitkisiz saksıların ortalama buharlaşma kaybı:

$$\bar E_{buh}(d) = \frac{1}{n_0}\sum_{k\in\text{bitkisiz}}\Big(W_k^{post}(d-1) - W_k^{pre}(d)\Big)$$

$$Tr_i(d) = W_i^{post}(d-1) - W_i^{pre}(d) - \bar E_{buh}(d)$$

## 2. Normalize transpirasyon oranı ve stres etiketi

$$NTR_i(d) = \frac{Tr_i(d)}{\overline{Tr}_{tam}(d)}, \qquad y_i(d) = \mathbb{1}\big[NTR_i(d) < \theta\big]$$

Başlangıç $\theta = 0{,}8$. Duyarlılık analizinde 0,7 ve 0,9 da denenir. Etiketin ölçüsü tartıdır. Toprak nemi, yaprak sıcaklığı ve hava sensörleri etikette **yoktur**.

Etiket tutarlılığı için Cohen kappa ($p_o$ gözlenen, $p_e$ rastlantısal uyum):

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

## 3. Toprak nemi kalibrasyonu

Ağırlıkça (gravimetrik) hacimsel su içeriği, $m_{ıslak}$ ve $m_{kuru}$ toprak kütleleri, $V$ hacim:

$$\theta_v = \frac{(m_{ıslak} - m_{kuru})/\rho_w}{V}$$

Sensör çıktısı $s$ (ADC) için doğrusal kalibrasyon, $\hat\theta_v = a\,s + b$. Sıcaklık duyarlılığı varsa $\hat\theta_v = a\,s + c\,(T - T_0) + b$ biçiminde düzeltilir (Kizito vd., 2008 gerekçesiyle). Kalibrasyon hatası RMSE ile rapor edilir.

## 4. Atmosferik talep göstergesi

Doymuş buhar basıncı (kPa), $T$ °C:

$$e_s(T) = 0{,}6108\,\exp\!\left(\frac{17{,}27\,T}{T + 237{,}3}\right)$$

Buhar basıncı açığı:

$$VPD = e_s(T)\left(1 - \frac{RH}{100}\right)$$

Yaprak-hava sıcaklık farkı $\Delta T = T_{yaprak} - T_{hava}$. Jackson vd. (1981) ile ilişkili stres endeksi (isteğe bağlı özellik), $\Delta T_{LL}$ ve $\Delta T_{UL}$ ıslak ve kuru referans sınırları:

$$CWSI = \frac{\Delta T - \Delta T_{LL}}{\Delta T_{UL} - \Delta T_{LL}}$$

## 5. Tahmin modelleri

Sınıflandırma (lojistik): $\;P(y_i(d+1)=1\mid\mathbf{x}_i(d)) = \sigma(\mathbf{w}^\top\mathbf{x}_i(d) + b)$.

Regresyon (ridge):

$$\hat{\mathbf{w}} = \arg\min_{\mathbf{w}}\ \sum_{d}\big(NTR(d+1) - \mathbf{w}^\top\mathbf{x}(d)\big)^2 + \lambda\|\mathbf{w}\|_2^2$$

## 6. Ölçütler

Makro F1 $=\frac{1}{2}(F1_{stresli}+F1_{stressiz})$. Yanlış alarm oranı $FAR = FP/(FP+TN)$. Ortalama mutlak hata:

$$MAE = \frac{1}{n}\sum_{i,d}\big|NTR_i(d) - \widehat{NTR}_i(d)\big|$$

Erken uyarı süresi (saksı $i$ için, gün cinsinden):

$$L_i = d_i^{stres} - d_i^{uyarı}$$

## 7. Su dengesi simülasyonu

$$S_{d+1} = S_d + I_d - Tr_d, \qquad 0 \le S_d \le S_{kap}$$

$I_d$ sulama miktarı. Stratejiler, stresli gün sayısı $\sum_d \mathbb{1}[NTR_d<\theta]$ ve toplam su $\sum_d I_d$ ile karşılaştırılır.

## 8. Belirsizlik

Aynı saksının günleri bağımlı olduğundan yüzde 95 güven aralığı, **saksı bloklarının** yerine koyarak yeniden örneklenmesiyle bulunur.
