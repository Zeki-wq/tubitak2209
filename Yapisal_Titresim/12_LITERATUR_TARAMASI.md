# Literatür Taraması

> **Durum:** Bu dosya iki parçadır. Birinci parça, elimizdeki kaynaklardan kurulan çerçevedir. İkinci parça, başvuru öncesi sistematik taramanın planıdır. Tarama henüz yapılmadı; "boşluk" ya da "ilk kez" iddiası kurulmadı.

## 1. Çerçeve

| Başlık | Kaynak | Bu projedeki rolü | Teyit durumu |
|---|---|---|---|
| Titreşime dayalı hasar tespiti: genel taramalar | Doebling vd. (1996); Sohn vd. (2003) | Alanın temel varsayımı: hasar rijitliği, dolayısıyla doğal frekansı değiştirir | Rapor numarası ve yıl kurum sayfasından teyit edilecek |
| Yapısal sağlık izlemeye giriş | Farrar ve Worden (2007) | Hasar düzeyleri (varlık, yer, şiddet) ve ölçüm-karar zinciri | DOI teyit edilecek |
| Titreşime dayalı muayene | Rytter (1993) | Hasar tespitinin dört düzeyi | Tez künyesi teyit edilecek |
| Kiriş titreşimi kuramı | Rao (2011) | Doğal frekans ön hesabı | Baskı teyit edilecek |
| Spektral kestirim | Welch (1967) | Güç spektrumu | Künye teyit edilecek |
| Makine öğrenmesi araçları | Pedregosa vd. (2011) | Lojistik regresyon, RF | Teyit edilecek |
| Veri sızıntısı | Kapoor ve Narayanan (2023) | Gün bazlı bölme | DOI teyit edilecek |

Bu tablodaki kaynakların çoğu klasiktir ama künyeler hafızadan yazılmıştır. Teyit yapılmadan metinde atıf yapılmayacak.

## 2. Konumlandırma (hipotez düzeyinde)

Hasarın doğal frekansı düşürdüğü bilgisi alanın en eski ve yaygın dayanağıdır. Zor olan, frekans kaymasının **zararsız etkilerden** (ek kütle, yeniden sıkıştırma, sıcaklık) ayrılmasıdır. Bu projenin eksenleri: (i) bu karıştırıcıları bilerek deneye katmak, (ii) sensör sayısı ve konumunun etkisini aynı protokolle ölçmek, (iii) en küçük ayırt edilebilir hasar düzeyini güven aralığıyla vermek, (iv) ikinci kirişte bağımsız doğrulama yapmak.

Düşük maliyetli ivmeölçerlerle yapılmış benzer karşılaştırmaların olup olmadığı taramada bakılacak.

## 3. Planlanan sistematik tarama

**Veri tabanları:** Web of Science, Scopus, IEEE Xplore, Google Scholar, TR Dizin.

**Arama dizileri:**
- `("cantilever" OR "beam") AND ("damage detection") AND ("natural frequency") AND ("MEMS accelerometer" OR "low-cost")`
- `"structural health monitoring" AND "environmental variability" AND ("mass" OR "temperature") AND "frequency shift"`
- `"sensor placement" AND "damage identification" AND "beam" AND "accelerometer"`
- `"minimum detectable damage" AND "vibration"`

**Türkçe:** "yapısal sağlık izleme", "titreşim", "çentikli kiriş", "doğal frekans kayması".

**Dahil etme:** Deneysel kiriş çalışması içeren, hasar düzeyini nicel veren çalışmalar. **Dışlama:** Yalnızca sayısal modelleme yapanlar ana tabloya girmez.

**Kayıt tablosu:**

| Künye | Kiriş/yapı | Sensör türü ve sayısı | Hasar türü ve düzeyleri | Karıştırıcılar | Bölme | Ölçüt | Sınırlılık |
|---|---|---|---|---|---|---|---|

## 4. Tarama sonrası yazılacak sorular

1. Ek kütle veya yeniden sıkıştırma etkisi hasar sınıflandırmasında ayrıca kontrol edilmiş mi?
2. Test, eğitimde olmayan bir kirişte yapılmış mı?
3. Sensör sayısının etkisi aynı veri üzerinde karşılaştırılmış mı?
4. Aynı darbenin tekrarları hem eğitimde hem testte yer almış mı?
