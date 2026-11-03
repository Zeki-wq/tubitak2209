# Literatür Taraması

> **Durum:** Bu dosya iki parçadır. Birinci parça, elimizdeki kaynaklardan kurulan çerçevedir. İkinci parça, başvuru öncesinde yürütülecek sistematik taramanın planıdır. Tarama henüz yapılmadı, bu yüzden "literatürde bir boşluk var" ya da "ilk kez" gibi bir iddia kurulmadı.

## 1. Çerçeve

| Başlık | Kaynak | Bu projedeki rolü | Teyit durumu |
|---|---|---|---|
| PV modül arıza türleri, sıcak nokta oluşumu | Köntges vd. (2014) | Arıza sınıflarını (kirlenme, seri direnç artışı, gölgelenme kaynaklı sıcak nokta) fiziksel zemine oturtur. | IEA-PVPS rapor numarası ve yıl teyit edilecek |
| Dış mekân kızılötesi termografi koşulları | IEC 62446-3 | Termal ölçümde ışınım, rüzgâr ve bakış açısı koşullarının neden kaydedileceğini belirler. | Sürüm ve yıl kurum erişiminden teyit edilecek |
| I–V ölçümü ve normalleştirme | IEC 60904-1; King vd. (2004) | I–V eğrisinin ışınım ve sıcaklığa göre düzeltilmesi | Künye teyit edilecek |
| Makine öğrenmesi araçları | Pedregosa vd. (2011) | Lojistik regresyon, Random Forest | Teyit edilecek |
| Veri sızıntısı | Kapoor ve Narayanan (2023) | Oturum ve gün bazlı bölme | DOI teyit edilecek |

## 2. Konumlandırma (hipotez düzeyinde)

Termografi ve I–V eğrisi ayrı ayrı yaygın arıza tespit araçlarıdır. Bu projenin sorusu şudur: geçici gölgelenme ile bakım gerektiren arızayı (kalıcı kirlenme, seri direnç artışı) ayırmada ikisini birleştirmek tek başına birinden daha mı iyi? Ölçütümüz, gölgelenmenin yanlışlıkla "bakım gerekli" sınıfına atanma oranıdır. Bunun literatürde bu biçimiyle ölçülüp ölçülmediği taramada bakılacak. Düşük maliyetli sensörle ve kendi yaptığımız I–V devresiyle çalışmak da bir tercih. Bu tercihin doğruluk bedeli rapor edilecek.

## 3. Planlanan sistematik tarama

**Veri tabanları:** Web of Science, Scopus, IEEE Xplore, Google Scholar, TR Dizin. Patent için Espacenet ve TÜRKPATENT.

**Arama dizileri:**
- `("photovoltaic" OR "PV module") AND ("fault detection" OR "fault diagnosis") AND ("thermal" OR "infrared") AND "I-V curve"`
- `("partial shading" OR "soiling") AND ("hot spot") AND ("classification" OR "machine learning")`
- `"series resistance" AND "PV" AND ("degradation" OR "fault") AND "low-cost"`
- `("shading" AND "soiling") AND ("distinguish" OR "discrimination") AND "PV"`

**Türkçe:** "fotovoltaik arıza tespiti", "gölgelenme", "kirlenme", "sıcak nokta".

**Dahil etme:** 2018 sonrası, hakemli, deneysel veri kullanan; arıza sınıflarını açıkça tanımlayan çalışmalar. **Dışlama:** Yalnızca uydu/İHA görüntüsüyle büyük santral çalışması yapan ve modül düzeyi ölçüm içermeyenler (isterse ayrı bir bağlam notunda anılır).

**Kayıt tablosu:**

| Künye | Sensör(ler) | Arıza sınıfları | Gölgelenme ayrı sınıf mı? | Veri (gerçek/sim.) | Bölme yöntemi | Sınırlılık |
|---|---|---|---|---|---|---|

## 4. Tarama sonrası yazılacak sorular

1. Gölgelenme ile kalıcı arıza ayrımı birincil ölçüt olarak raporlanmış mı?
2. Termal ve elektriksel özellikler birlikte, aynı oturumda ölçülmüş mü?
3. Işınım bandı dışarıda bırakılarak dayanıklılık sınanmış mı?
4. Aynı günden pencereler hem eğitimde hem testte yer almış mı?
