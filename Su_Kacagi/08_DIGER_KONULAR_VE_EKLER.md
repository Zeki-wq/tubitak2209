# 5. Belirtmek İstediğiniz Diğer Konular

Bu çalışmada **kaçak tespiti** ve **bölgesel konumlandırma** birbirinden ayrı iki problem olarak ele alınacaktır. Böylece bir sistemin kaçak varlığını doğru algılasa da yerini yanlış tahmin etmesi gibi durumlar görünür hale gelecektir. Sensörlerin maliyetleri de analizde göz önünde bulundurulacaktır. Daha pahalı veya çok sayıda sensör kullanıldığında başarının artması tek başına yeterli kabul edilmeyecektir. Ek maliyet karşılığında elde edilen kazanç ayrıca tartışılacaktır.

Gerçek su şebekelerindeki uzun boru hatları, farklı boru malzemeleri ve değişken basınç koşulları bu araştırmanın kapsamı dışındadır. Proje kontrollü bir masaüstü / laboratuvar düzeneğinde yapılacaktır. Bulguların sahaya aktarılması daha sonraki çalışmalar için öneri niteliği taşıyacaktır.

# 6. Ekler

## Ek A — Örnek deney kayıt formu

| Alan | Kaydedilecek değer |
|---|---|
| Oturum kodu | OTR_001 |
| Tarih ve saat | [KAYIT SIRASINDA] |
| Kaçak durumu | Yok / K1 / K2 / K3 |
| Kaçak açıklığı | [MM VEYA DENEYSEL SEVİYE] |
| Debi / pompa ayarı | Düşük / yüksek, ölçülebiliyorsa debi değeri |
| Gürültü | Normal / ek mekanik gürültü |
| Akustik sensör noktası | S1 / S2 |
| Basınç sensörü noktası | P1 |
| Örnekleme frekansı | [PİLOT TESTLE ÖLÇÜLECEK] |
| Kayıt süresi | Hedef 30 saniye |
| Gözlem ve olağan dışı durum | [NOT] |

## Ek B — Örnek sınıf etiketleri

- 0: Normal, kaçak yok
- 1: K1 bölgesinde kaçak
- 2: K2 bölgesinde kaçak
- 3: K3 bölgesinde kaçak

## Ek C — Sistemin metinsel akışı

Kapalı devre boru hattı → akustik ve basınç ölçüm düğümleri → zaman damgalı kayıt → özellik çıkarımı → tek sensör ve sensör füzyonu karşılaştırması → kaçak tespiti → varsa kaçak bölgesi tahmini → test raporu.

**Not:** Bu ekler önerilen içeriklerdir. TYBS'nin ayrı ek yükleme kısıtları varsa mevcut ekran kuralları takip edilmelidir. Fotoğraf, şema veya gerçek pilot veri ancak üretildikten ve doğrulandıktan sonra eklenecektir.
