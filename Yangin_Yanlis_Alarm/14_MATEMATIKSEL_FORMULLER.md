# Matematiksel Formüller

## 1. Özellikler

Partikül oranları (tek pencere ortalamaları):

$$r_{2.5/1} = \frac{\overline{PM_{2.5}}}{\overline{PM_{1.0}}}, \qquad r_{10/2.5} = \frac{\overline{PM_{10}}}{\overline{PM_{2.5}}}$$

Pencere eğimi ($n$ örnek, en küçük kareler):

$$m = \frac{\sum_i (t_i - \bar t)(x_i - \bar x)}{\sum_i (t_i-\bar t)^2}$$

Oranlar ve eğimler birlikte, parçacık boyut dağılımının nasıl değiştiğini yansıtır. Buhar, pişirme ve yanma kaynaklı duman bu dağılımda farklı iz bırakabilir. Bu bir **hipotezdir**, ölçümle sınanacaktır.

## 2. Karar yöntemleri

**Y1 (tek sensör):** $\;PM_{2.5}(t) \ge \theta_1$ en az $s$ saniye boyunca.

**Y2 (çok sensörlü kural):** $\;\sum_{j} \mathbb{1}[x_j(t) \ge \theta_j] \ge 2$ en az $s$ saniye boyunca.

**Y3 (lojistik):** $\;p(t) = \sigma(\mathbf{w}^\top\mathbf{x}(t) + b)$. Alarm: $p \ge \tau$.

**Y4 (int8):** ağırlıklar $q = \text{round}(w/s_w) + z$ ile 8 bite nicelenir. Ölçek $s_w$ ve sıfır noktası $z$ eğitim verisinden bulunur.

## 3. Sabit duyarlılıkta eşik

Olay düzeyinde duyarlılık, yanma olayı $e$ için olay boyunca en az bir pencerenin alarm vermesi:

$$S(\tau) = \frac{1}{|\mathcal{E}_{yanma}|}\sum_{e\in\mathcal{E}_{yanma}}\mathbb{1}\Big[\max_{w\in e} s(w) \ge \tau\Big]$$

Eşik, yalnızca eğitim günlerinden seçilir:

$$\tau^* = \max\{\tau : S(\tau) \ge 0{,}90\}$$

Aynı duyarlılık düzeyinde yöntemler yanlış alarm açısından karşılaştırılır. Böylece "daha çok alarm veren yöntem daha iyi" yanılgısı önlenir.

## 4. Ölçütler

**Birincil: kayıt düzeyinde yanlış alarm oranı** (yanma dışı kayıtlar, sabit duyarlılıkta):

$$\text{KYA} = \frac{\#\{\text{alarm veren yanma dışı kayıt}\}}{\#\{\text{yanma dışı kayıt}\}}$$

Algılama gecikmesi ($t_0$ yanma başlangıcı):

$$\Delta_{alarm} = t_{alarm} - t_0, \qquad \Delta_{ref} = t_{alarm} - t_{ref}$$

Olay türü bazında karışıklık matrisi $C_{ab}$ ve satır normalize duyarlılık $R_a = C_{aa}/\sum_b C_{ab}$.

## 5. Enerji ve haberleşme

Düğümün saatlik enerjisi, $V$ besleme, $I(t)$ akım:

$$E_{saat} = \int_0^{3600} V\,I(t)\,dt$$

LoRa paket teslim oranı ve sembol süresi ($SF$ yayılma faktörü, $BW$ bant genişliği):

$$\text{PDR} = \frac{N_{alınan}}{N_{gönderilen}}, \qquad T_{sym} = \frac{2^{SF}}{BW}$$

Yüksek $SF$ menzili artırır ama paket süresini uzatır. Frekans, çıkış gücü ve görev döngüsü ilgili düzenlemelere göre seçilir.

## 6. Belirsizlik

Olay kaydı düzeyinde eşleştirilmiş fark $d_r = \text{KYA}_r^{Y1} - \text{KYA}_r^{Y3}$ için yüzde 95 güven aralığı, kayıtların yerine koyarak yeniden örneklenmesiyle bulunur. Aynı günün kayıtları bir blok sayılır.

## 7. Plan sayımı

$$N_{kayıt} = 8_{tür}\times 2_{şiddet}\times 5_{gün} = 80$$
