# 1.1 Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Bir arıcı kovanı açtığında koloniyi rahatsız eder. Sık müdahale hem arıya hem arıcıya yük bindirir. Bu nedenle kovanı açmadan, dışarıdan ve sürekli izleme fikri uzun zamandır ilgi çekiyor. Kovan sesi bu amaçla en çok denenen sinyallerden biri. Arıların kanat çırpışı, kovan içi havalandırma ve koloni hareketliliği sesin spektrumunda iz bırakıyor. Daha önce oğul verme dönemine ait seslerin izlenebileceği gösterilmiştir (Ferrari vd., 2008). Kovan sesinin neden önemli bir bilgi kaynağı olabileceği ise derlemelerde tartışılmıştır (Terenzi vd., 2020), ölçüm sistemleri de geliştirilmiştir (Cecchi vd., 2020).

Bu çalışmaların çoğunda ortak bir zorluk var. Kovan sesi yalnızca koloninin durumuna değil, havanın sıcaklığına, nemine ve günün saatine de bağlı. Sabah soğuğunda bir kovan, öğleden sonra sıcağında aynı kovandan farklı ses çıkarır. Anomali tespiti "normalden sapma" arar, bu yüzden normalin ne olduğunu çevre koşulundan bağımsız tanımlayamazsanız sistem, hiçbir sorun olmadığı hâlde, günün rutin değişimine alarm verir.

Bu açıdan geniş bir veri kümesi mevcut. Abdollahi ve arkadaşlarının (2025) yayımladığı UrBAN veri kümesi, bir arılıktaki on kovandan binlerce saatlik ses ve çevresel ölçüm içeriyor ve açık erişime sahip. Biz bu veriyi, yeni bir veri toplamadan da yanıtlanabilecek soruyu sınamak için kullanacağız.

**Araştırma sorusu:** Kovan içi ses özelliklerine sıcaklık ve nem bilgisini eklemek, anomali tespitinde yanlış alarm sayısını, özellikle günün farklı saatlerinde ve eğitimde görülmemiş kovanlarda azaltır mı?

**H1:** Ses ve çevre bilgisini birlikte kullanan model, yalnızca ses kullanan modele göre, aynı duyarlılık düzeyinde, eğitimde görülmemiş kovanlarda saatlik yanlış alarm sayısını azaltacaktır.

**H2:** Yalnızca ses kullanan modelin alarmları günün belirli saatlerinde (özellikle sıcaklığın hızla değiştiği sabah ve akşam saatlerinde) yoğunlaşacak, çevre bilgisi eklendiğinde bu saatlik dağılım dengelenecektir.

**H3:** Seçilen modelin küçültülmüş hali, ESP32-S3 sınıfı bir mikrodenetleyicide gerçek zamanlı çalışabilecek ve kayıp, bilgisayardaki modele göre sınırlı kalacaktır.

Hipotezlerin hiçbiri önceden kabul edilmiyor. Sıcaklık ve nem eklenmesi fayda sağlamazsa, bu da sensör maliyeti açısından yararlı bir bulgudur.

Çalışmanın kapsamı bilinçli olarak dar tutuldu. Burada "anomali", kovanın kendi normal örüntüsünden istatistiksel sapmadır. Bu sapmanın biyolojik nedenini (hastalık, oğul, ana arı durumu) belirlemiyoruz. Böyle bir iddia için arıcılık veya veterinerlik uzmanının doğruladığı etiketler gerekir. Saha bölümü yalnızca küçük ölçekli bir doğrulamadır ve istatistiksel genelleme iddiası taşımaz.
