# Literatür Taraması

> **Durum:** Bu dosya iki parçadır. Birinci parça, elimizdeki kaynaklardan kurulan çerçevedir. İkinci parça, başvuru öncesinde yürütülecek sistematik taramanın planıdır. Tarama henüz yapılmadı, bu yüzden "literatürde bir boşluk var" ya da "ilk kez" gibi bir iddia kurulmadı.

## 1. Çerçeve: konu hangi bilgi tabanına dayanıyor?

| Başlık | Kaynak | Bu projedeki rolü | Teyit durumu |
|---|---|---|---|
| Temas direnci ve Joule ısınması | Holm (1967); Slade (2014) | Gevşek bir bağlantıda direncin neden arttığını ve ısının nereden geldiğini açıklar. Isıl modelin fiziksel dayanağıdır. | Kitap künyesi (baskı, yıl) kütüphaneden teyit edilecek |
| Gevşek temasın veriye dayalı tanılanması | Luan vd. (2025) | Gerilim farkı bilgisinin tanıda işe yarayabileceğini gösteren yakın çalışma. Bizim görünür direnç özelliğimizin gerekçesidir. | Özeti web üzerinden görüldü, tam metin okunmadı |
| Makine öğrenmesi araçları | Pedregosa vd. (2011) | Lojistik regresyon ve Random Forest uygulamaları | Künye teyit edilecek |
| Veri sızıntısı | Kapoor ve Narayanan (2023) | Koşu ve gün bazlı bölmenin gerekçesi | DOI açılıp teyit edilecek |

## 2. Konumlandırma (şimdilik hipotez düzeyinde)

Literatürde gevşek bağlantıyı gerilim, akım veya sıcaklıkla tanıyan çalışmaların olduğunu biliyoruz. Bizim yaklaşımımız üç noktada farklılaşmaya aday: sabit sıcaklık eşiğine göre **erken uyarı süresini** birincil ölçüt yapmak, normal koşullarda akım basamağı ve fan değişimini bilerek eklemek (yanlış uyarıyı gerçekçi ölçmek için) ve modeli mikrodenetleyicide çalıştırıp işlem maliyetini raporlamak. Bu üç noktanın literatürde ne kadar karşılandığı tarama sonunda yazılacaktır. Karşılanmışsa proje "tekrar ve karşılaştırma" olarak çerçevelenir.

## 3. Planlanan sistematik tarama

**Veri tabanları:** Web of Science, Scopus, IEEE Xplore, Google Scholar, TR Dizin. Patent için Espacenet ve TÜRKPATENT.

**Arama dizileri (İngilizce):**
- `("loose connection" OR "loose contact" OR "contact resistance") AND ("overheating" OR "thermal") AND ("detection" OR "diagnosis")`
- `("terminal" OR "connector") AND "temperature rise" AND ("early warning" OR "prediction")`
- `("smart meter" OR "switchgear" OR "busbar") AND "temperature monitoring" AND "machine learning"`
- `"contact resistance" AND "Kelvin" AND "voltage drop" AND "monitoring"`

**Türkçe:** "gevşek bağlantı", "temas direnci", "aşırı ısınma", "erken uyarı", "klemens".

**Dahil etme:** 2015 sonrası, hakemli, deneysel veri içeren, tespit/tahmin yöntemini açıkça tanımlayan çalışmalar. Klasik temas fiziği kaynakları bu yıl sınırının dışındadır.
**Dışlama:** Yalnızca simülasyon yapan, ölçüm yöntemini açıklamayan, özeti dışında erişilemeyen çalışmalar.

**Kayıt tablosu (her çalışma için doldurulacak):**

| Künye | Ölçülen büyüklükler | Yöntem | Veri (gerçek/sim., koşu sayısı) | Birincil ölçüt | Sınırlılık | Bize katkısı |
|---|---|---|---|---|---|---|

## 4. Tarama sonrası yazılacak sorular

1. Erken uyarı süresini sabit eşiğe göre ölçen bir çalışma var mı?
2. Normal koşuldaki akım ve hava değişimleri yanlış uyarı hesabına katılmış mı?
3. Mikrodenetleyicide çalıştırılmış örnek var mı, işlem maliyeti raporlanmış mı?
4. Kullanılan veri koşu bazlı mı bölünmüş, yoksa pencereler rastgele mi dağıtılmış?

Son soru önemlidir. Pencereler rastgele dağıtılmışsa o çalışmaların başarı oranlarını bizim sonuçlarımızla doğrudan karşılaştırmayacağız.
