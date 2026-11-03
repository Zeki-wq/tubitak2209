# Literatür Taraması

> **Durum:** Bu dosya iki parçadır. Birinci parça, elimizdeki kaynaklardan kurulan çerçevedir. İkinci parça, başvuru öncesi sistematik taramanın planıdır. Tarama henüz yapılmadı; "boşluk" ya da "ilk kez" iddiası kurulmadı.

## 1. Çerçeve

| Başlık | Kaynak | Bu projedeki rolü | Teyit durumu |
|---|---|---|---|
| Buhar basıncı açığı, bitki su ihtiyacı | Allen vd. (1998), FAO-56 | VPD hesabı ve atmosferik talep kavramı | Künye teyit edilecek |
| Yaprak sıcaklığı ve su stresi | Jackson vd. (1981) | Yaprak-hava sıcaklık farkının stres göstergesi olması | DOI teyit edilecek |
| Toprak suyu azalınca transpirasyon düşüşü | Sinclair ve Ludlow (1986) | Stres eşiği tanımının dayanağı | Künye teyit edilecek; eşik için bitki uzmanı görüşü de alınacak |
| Düşük maliyetli kapasitif toprak nemi sensörü | Kizito vd. (2008) | Sıcaklık ve iletkenlik duyarlılığı, kalibrasyon gerekçesi | Künye teyit edilecek |
| Makine öğrenmesi araçları | Pedregosa vd. (2011) | Lojistik regresyon, RF, düzenlileştirilmiş doğrusal modeller | Teyit edilecek |
| Veri sızıntısı | Kapoor ve Narayanan (2023) | Saksı ve seri bazlı bölme | DOI teyit edilecek |

Bu kaynakların künyeleri hafızadan yazılmıştır. Teyit yapılmadan metinde atıf yapılmayacak.

## 2. Konumlandırma (hipotez düzeyinde)

Toprak nemi eşiğine göre sulama yaygın bir yöntemdir. Biz, **stres etiketini sensörlerden bağımsız** (günlük tartıdan elde edilen transpirasyon oranı) üretip bu etikete karşı toprak nemi, hava koşulları ve yaprak sıcaklığının katkısını ayrı ayrı ölçüyoruz. Etiket ve girdi aynı sensörlerden gelirse model bir totoloji öğrenir. Bu çalışmada o tuzaktan kaçınma tasarımı bir odak noktasıdır. Aynı tasarımın literatürde ne ölçüde uygulandığı taramada bakılacak.

## 3. Planlanan sistematik tarama

**Veri tabanları:** Web of Science, Scopus, IEEE Xplore, Google Scholar, TR Dizin, CAB Abstracts/AGRIS (erişim varsa).

**Arama dizileri:**
- `("plant water stress" OR "drought stress") AND ("prediction" OR "forecast") AND ("low-cost sensor" OR "IoT") AND ("machine learning")`
- `("gravimetric" OR "lysimeter" OR "weighing") AND "transpiration" AND "soil moisture sensor" AND "stress"`
- `"vapor pressure deficit" AND "soil moisture" AND ("irrigation scheduling") AND "machine learning"`
- `"capacitive soil moisture sensor" AND ("calibration" OR "temperature sensitivity")`

**Türkçe:** "bitki su stresi", "transpirasyon", "akıllı sulama", "toprak nemi sensörü".

**Dahil etme:** Stres referansını bağımsız ölçen (tartı, gaz değişimi, su potansiyeli) deneysel çalışmalar. **Dışlama:** Referansı yalnızca sensör eşiğinden üreten ve doğrulamayan çalışmalar ana tabloya girmez; bağlam notunda anılır.

**Kayıt tablosu:**

| Künye | Tür | Stres referansı | Girdi sensörleri | Tahmin ufku | Bölme (saksı/seri/rastgele) | Ölçüt | Sınırlılık |
|---|---|---|---|---|---|---|---|

## 4. Tarama sonrası yazılacak sorular

1. Stres etiketi girdi sensörlerinden bağımsız mı üretilmiş?
2. Aynı saksının ardışık günleri hem eğitimde hem testte yer almış mı?
3. Çevre bilgisinin (VPD, ışık) toprak neminin ötesindeki katkısı ölçülmüş mü?
4. Erken uyarı süresi raporlanmış mı?

## 5. Not

Bitki türü ve stres eşiği biyolojik bir seçimdir. Tarama sonucunda eşik literatürden desteklenemezse, eşik pilotta duyarlılık analiziyle (0,7 / 0,8 / 0,9) verilir ve sonuç eşiğe bağımlılığıyla birlikte raporlanır.
