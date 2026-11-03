# Literatür Taraması

> **Durum:** Bu dosya iki parçadır. Birinci parça, elimizdeki kaynaklardan kurulan çerçevedir. İkinci parça, başvuru öncesinde yürütülecek sistematik taramanın planıdır. Tarama henüz yapılmadı, bu yüzden "boşluk var" ya da "ilk kez" türü bir iddia kurulmadı.

## 1. Çerçeve

| Başlık | Kaynak | Bu projedeki rolü | Teyit durumu |
|---|---|---|---|
| Açık kovan akustiği veri kümesi | Abdollahi vd. (2025), UrBAN | Faz A'nın veri kaynağı | Yazar listesi ve DOI web aramasıyla doğrulandı; içerik ve etiket yapısı kaynak sayfasından okunacak |
| Sürü sesi ve kovan sesinin izlenmesi | Ferrari vd. (2008); Terenzi vd. (2020); Cecchi vd. (2020) | Kovan sesinin izlenebilir bilgi taşıdığına dair önceki çalışmalar | **Hafızadan yazıldı. Açılıp künye ve içerik teyit edilmeden metinde atıf yapılmayacak** |
| Anomali tespiti çerçevesi | Chandola vd. (2009) | Yöntem sınıflaması: istatistiksel, yakınlık, yeniden oluşturma | Künye teyit edilecek |
| Ses özelliği | Davis ve Mermelstein (1980) | MFCC tanımı | Künye teyit edilecek |
| Uç cihazda model | David vd. (2021) | TFLite Micro ile int8 çıkarım | Künye teyit edilecek |
| Veri sızıntısı | Kapoor ve Narayanan (2023) | Kovan dışarıda bırakma gerekçesi | DOI teyit edilecek |

## 2. Konumlandırma (hipotez düzeyinde)

Kovan sesiyle durum izleme literatürde var. Bu projenin eksenini farklı kuruyoruz: **bir kovana özel model yerine, görülmemiş kovanlarda saatlik yanlış alarm yükü**, ve çevre bilgisinin (sıcaklık, nem, günün saati) yanlış alarmı azaltıp azaltmadığı. Hastalık ya da koloni sağlığı tanısı iddiamız yok. Bu sınır, arıcıya ve jüriye açıkça söylenecek.

Bu eksenin önceki çalışmalarda ele alınıp alınmadığı taramada netleşecek.

## 3. Planlanan sistematik tarama

**Veri tabanları:** Web of Science, Scopus, IEEE Xplore, Google Scholar, TR Dizin; veri kümesi için ayrıca Zenodo ve Scientific Data.

**Arama dizileri:**
- `("honey bee" OR "beehive") AND ("acoustic" OR "sound") AND ("monitoring" OR "anomaly detection")`
- `beehive AND (swarming OR queenless) AND audio AND "machine learning"`
- `"beehive" AND "environmental" AND ("temperature" OR "humidity") AND "sound" AND "confound*"`
- `"edge" AND "beehive" AND ("TinyML" OR "embedded")`

**Türkçe:** "arı kolonisi akustik", "kovan sesi", "anomali tespiti".

**Dahil etme:** 2015 sonrası, hakemli, kovan sesi kaydı kullanan. **Dışlama:** Sesi hiç kullanmayan (yalnızca ağırlık/sıcaklık) çalışmalar ana tabloya girmez; bağlam notunda anılabilir.

**Kayıt tablosu:**

| Künye | Kovan sayısı | Etiket kaynağı | Çevre değişkeni kullanıldı mı? | Bölme (kovan/gün/pencere) | Ölçüt | Sınırlılık |
|---|---|---|---|---|---|---|

## 4. Tarama sonrası yazılacak sorular

1. Test kovanları eğitimde görülmeden mi sınanmış?
2. Günün saati ve sıcaklık gibi karıştırıcılar kontrol edilmiş mi?
3. Alarmın günün saatine dağılımı raporlanmış mı?
4. Uç cihazda çalıştırılmış çalışma var mı?

## 5. Etik ve kapsam notu

Arı sağlığına dair biyolojik yorum yetkisi bir arı uzmanı ya da veterinerdedir. Raporda "anomali skoru" ifadesi kullanılır, "hastalık" ya da "kraliçesizlik" gibi tanı terimleri kullanılmaz.
