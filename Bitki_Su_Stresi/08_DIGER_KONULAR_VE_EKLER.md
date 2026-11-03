# 5. Belirtmek İstediğiniz Diğer Konular

Çalışmada stres etiketi ile tahmin girdileri bilerek ayrı tutuluyor. Etiket günlük tartımdan ve gözlemden, girdiler elektronik sensörlerden gelecek. Bu ayrımın bozulduğu bir durum fark edilirse (örneğin bir sensör etiket üretimine girerse) analiz yeniden yapılacak.

Sulama grupları arasındaki farkın bitki gelişimine etkisi seri sonunda biyokütle ve yaprak alanıyla ayrıca raporlanacak. Böylece stresin gerçekten bitkiyi etkileyip etkilemediği ikinci bir yoldan kontrol edilmiş olacak.

Kapsam dışı olanlar: tarla ölçeği, farklı bitki türleri ve toprak tipleri, hastalık ve besin eksikliği kaynaklı stresler, tam otomatik sulama kontrolü ve bitki gelişiminin verim açısından değerlendirilmesi. Retrospektif su dengesi simülasyonu gerçek sulama deneyinin yerine geçmez ve keşifsel olarak sunulacaktır.

Sera veya iklim odası kullanılacaksa, ilgili birimin işletme kurallarına uyulacaktır. Kimyasal ilaç veya gübre kullanımı bitki uzmanıyla belirlenecek ve kayıt altına alınacaktır.

# 6. Ekler

## Ek A — Örnek günlük tartım ve gözlem formu

| Alan | Kaydedilecek değer |
|---|---|
| Seri ve gün | S2 / G17 |
| Saksı kodu ve grup | P07 / orta kısıt |
| Sulama öncesi ağırlık (g) | [ÖLÇÜLEN] |
| Verilen su (g) | [ÖLÇÜLEN] |
| Sulama sonrası hedef ağırlık (g) | [HEDEF] |
| Bitkisiz kontrol saksı kaybı (g) | [ÖLÇÜLEN] |
| Solgunluk skoru (gözlemci 1 / 2) | 0–2 |
| Atmosferik blok | Normal / sıcak-kuru / serin-nemli |
| Cihaz durumu | Sensör arızası, bağlantı kopması notu |
| Gözlem | [NOT] |

## Ek B — Örnek veri etiketleri

- Stres durumu: 0 = stres yok, 1 = stresli (normalize transpirasyon oranı eşiğin altında)
- Normalize transpirasyon oranı: saksı / tam sulama grubu ortalaması (sürekli değer)
- Solgunluk skoru: 0 normal, 1 hafif solgun, 2 belirgin solgun
- Grup: tam sulama / hafif kısıt / orta kısıt

## Ek C — Sistemin metinsel akışı

Saksı bitkileri → toprak nemi, hava, ışık ve yaprak sıcaklığı sensörleri + günlük tartım → zaman damgalı kayıt → stres etiketi (tartım ve gözlem) ve sensör özellikleri → M1, M2, M3 modelleri ve sabit eşik kuralı → ertesi gün stres tahmini, erken uyarı süresi ve yanlış alarm değerlendirmesi → rapor.

**Not:** Bu ekler önerilen içeriklerdir. TYBS'nin ek yükleme kısıtları varsa ekran kurallarına uyulmalıdır. Fotoğraf, şema veya gerçek veri ancak üretildikten ve doğrulandıktan sonra eklenmelidir.
