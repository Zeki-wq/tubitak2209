import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from engine import *
from projects import PROJECTS

ROOT = r"C:\Users\alavh\Desktop\Tübitak 2209"


def build(p):
    out = os.path.join(ROOT, p["folder"], "Proje_Tanitim.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle(p["title"])
    c.setAuthor("TÜBİTAK 2209-A 2026 başvuru hazırlığı")
    col = p["color"]

    # ---------------- page 1
    band(c, col, p["num"], p["title"], 1)
    box(c, M, 64, W - 2 * M, 50, "", HexColor("#FFF8EC"), HexColor("#E8C98A"), lw=1)
    c.setFillColor(col)
    c.setFont("FB", 8.5)
    c.drawString(M + 10, H - 64 - 14, "ARAŞTIRMA SORUSU")
    text_block(c, p["question"], M + 10, 64 + 19, W - 2 * M - 20, 11, "FB", INK, lead=13)
    cw = (W - 2 * M - 3 * 10) / 4
    for i, (big, small) in enumerate(p["cards"]):
        card(c, M + i * (cw + 10), 124, cw, 56, big, small, col)
    section_title(c, "Sistem şeması: proje bir bakışta", M, 190, col)
    diagram(c, M, 214, W - 2 * M, 322, p["nodes"], p["edges"], col)
    legend(c, M, 545, col)

    c.showPage()
    # ---------------- page 2
    band(c, col, p["num"], p["title"], 2)
    section_title(c, "Deney tasarımı: kaç ölçüm, nasıl çarpılıyor?", M, 62, col)
    chips(c, 86, p["chips"], p["result"], col)
    section_title(c, "Veri nasıl bölünüyor? (sızıntı olmasın diye)", M, 156, col)
    split_bar(c, 180, p["split"], p["split_cap"], col)
    section_title(c, "Sınanacak üç hipotez", M, 260, col)
    hyp_cards(c, 284, p["hyps"], col, h=78)
    section_title(c, "Karşılaştırılan yöntemler: aynı veri, aynı test", M, 376, col)
    ladder(c, 400, p["methods"], col, h=84)
    box(c, M, 496, W - 2 * M, 46, "", HexColor("#F1F6FB"), HexColor("#B7CBE3"), lw=1)
    c.setFillColor(col)
    c.setFont("FB", 8.5)
    c.drawString(M + 10, H - 496 - 13, "BAŞARI NASIL ÖLÇÜLÜYOR?")
    text_block(c, p["metrics"], M + 10, 496 + 17, W - 2 * M - 20, 9, "F", INK, lead=11)

    c.showPage()
    # ---------------- page 3
    band(c, col, p["num"], p["title"], 3)
    lw_ = 400
    section_title(c, "8 aylık takvim ve başarı ağırlıkları", M, 62, col, w=lw_)
    gy = gantt(c, M, 86, lw_, p["gantt"], col)
    section_title(c, "Bütçe (tahmini)", M, gy + 16, col, w=lw_)
    bb = budget_bar(c, M, gy + 40, lw_, p["budget"], p["budget_total"], p["budget_note"], col)
    rx = M + lw_ + 20
    rw = W - M - rx
    section_title(c, "En büyük 4 risk ve B planı", rx, 62, col, w=rw)
    ry = risk_table(c, rx, 86, rw, p["risks"], col)
    oh = list_box(c, rx, ry + 14, rw, None, "Sonunda elimizde ne olacak?", p["outputs"], col, bullet="•")
    bottom_top = max(bb, ry + 14 + oh) + 14
    bw = (W - 2 * M - 12) / 2
    bh = max(list_height(p["must"], bw), list_height(p["wont"], bw))
    list_box(c, M, bottom_top, bw, bh, "Başvurmadan önce şart", p["must"], col, bullet="→")
    list_box(c, M + bw + 12, bottom_top, bw, bh, "Bilerek yapmadıklarımız (kapsam dışı)", p["wont"], HexColor("#6B7280"), bullet="×")
    pt = bottom_top + bh + 12
    ph = min(575 - 22 - pt, 64)
    if ph > 30:
        box(c, M, pt, W - 2 * M, ph, "", col, col, r=9)
        c.setFillColor(white)
        c.setFont("FB", 8.5)
        c.drawString(M + 12, H - pt - 15, "TEK CÜMLEYLE")
        text_block(c, p["pitch"], M + 12, pt + 20, W - 2 * M - 24, 11.5, "FB", white, lead=14)
    c.showPage()
    c.save()
    return out


if __name__ == "__main__":
    only = sys.argv[1:]
    for p in PROJECTS:
        if only and p["folder"] not in only:
            continue
        print(build(p))
