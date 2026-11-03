# Algoritmik Akış (Kaba Kod)

Kodlar yöntemi anlatan taslaktır. Pencere ve eşikler pilotta kesinleşir.

## A1. Düğümde ölçüm ve gönderim

```
HER 1 s:
    pm1, pm25, pm10, sayım_aralıkları = oku(partikül)
    T, RH, P, gaz_direnci              = oku(ortam)
    co, yanıcı_gaz                     = oku(MQ_modülleri)
    kaydet_SD(zaman, hepsi)
    EĞER sayaç % 5 == 0:  LoRa_gönder(özet_paket)
```

## A2. Olay kaydı (Faz B)

```
HER (tür, şiddet, gün) İÇİN, sıra rastgele:
    temiz_hava_başlangıcı( 2 dk )
    form.not( olay_başlangıcı = şimdi() )
    olayı_uygula(tür, şiddet)
    form.not( olay_bitişi = şimdi() )
    hazneyi_havalandır();  bekle_ta_ki( sensörler ≈ temel )
    EĞER tür == 7 VE yazılı_onay == YOK:  ATLA ve kaydet("kapsam dışı")
referans_alarm_zamanı = mikrofon_algılama_zamanı( ticari_alarm_sesi )
```

## A3. Özellik çıkarımı

```
pencere = 20 s;  adım = 5 s
HER pencere w İÇİN:
    r_25_1  = ort(pm25) / ort(pm1)
    r_10_25 = ort(pm10) / ort(pm25)
    eğim_pm = en_küçük_kareler_eğimi(pm25, w)
    eğim_co = en_küçük_kareler_eğimi(co, w);  eğim_gaz = ...(gaz_direnci, w)
    ΔT, ΔRH = son - ilk
    x[w] = [r_25_1, r_10_25, eğim_pm, eğim_co, eğim_gaz, ΔT, ΔRH, std'ler]
```

## A4. Sabit duyarlılıkta eşik seçimi

```
eğitim_yanma = pencereler(tür = 7, eğitim_günleri)
eğitim_diğer = pencereler(tür ∈ 0..6, eğitim_günleri)

HER yöntem IN {Y1, Y2, Y3}:
    skor_yanma = yöntem.skor(eğitim_yanma)
    τ = en büyük τ  öyle ki  yanma_olaylarının ≥ %90'ında  skor >= τ  olan
        (olay düzeyinde: olay boyunca en az bir pencere alarm)
    YA_eğitim = yanma_dışı_kayıtlar içinde alarm_veren_oranı(τ)
```

Eşik testten önce, yalnızca eğitim günlerinden seçilir.

## A5. Değerlendirme

```
test = eğitimde olmayan günlerin olay kayıtları
HER yöntem İÇİN:
    kayıt_YA   = alarm_veren_yanma_dışı_kayıt / yanma_dışı_kayıt
    gecikme    = t_alarm - t_yanma_başlangıcı;  fark_ref = t_alarm - t_referans_alarm
    karışıklık = olay_türü_bazında_matris
fark = eşleştirilmiş_kayıt_farkı;  GA95 = bootstrap(fark, olay_kaydı bazlı)

# genelleme
HER duman_benzeri tür k:
    eğit( tür_k hariç );  test( tür_k )          # bir olay türünü dışarıda bırak
```

## A6. Uç cihaz ve LoRa

```
ESP32: pencere → özellik → int8 model → skor → eşik τ_q → alarm
ölç: süre, RAM/flash, saatlik enerji (∫ V·I dt)
LoRa: HER mesafe/oda İÇİN gönder(N paket);  PDR = alınan / gönderilen
```
