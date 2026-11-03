from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor, white, black

pdfmetrics.registerFont(TTFont("F", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("FB", "C:/Windows/Fonts/arialbd.ttf"))

W, H = landscape(A4)
M = 28
INK = HexColor("#1F2933")
MUTE = HexColor("#5B6770")
LINE = HexColor("#C9D1D9")
PAPER = HexColor("#FFFFFF")

KIND = {
    "input":   (HexColor("#E8F0FE"), HexColor("#3B6FD4")),
    "device":  (HexColor("#F1F3F4"), HexColor("#5F6368")),
    "sensor":  (HexColor("#E0F5F0"), HexColor("#1A8F7A")),
    "process": (HexColor("#EEE8FA"), HexColor("#6A4BC1")),
    "risk":    (HexColor("#FDE8E7"), HexColor("#C5342B")),
    "key":     (HexColor("#FFF3D6"), HexColor("#D49A00")),
    "output":  (None, None),
}


def wrap(text, font, size, width):
    lines = []
    for part in text.split("\n"):
        lines += simpleSplit(part, font, size, width) or [""]
    return lines


def text_block(c, text, x, top, w, size=9.5, font="F", color=INK, lead=None, align="left"):
    lead = lead or size * 1.28
    c.setFont(font, size)
    c.setFillColor(color)
    y = H - top - size
    n = 0
    for ln in wrap(text, font, size, w):
        if align == "center":
            c.drawCentredString(x + w / 2, y, ln)
        else:
            c.drawString(x, y, ln)
        y -= lead
        n += 1
    return n * lead


def box(c, x, top, w, h, text, fill, stroke, size=9.5, font="F", tcolor=INK, r=7, lw=1.2, pad=5):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(lw)
    c.roundRect(x, H - top - h, w, h, r, fill=1, stroke=1)
    if text:
        lead = size * 1.25
        lines = wrap(text, font, size, w - 2 * pad)
        total = len(lines) * lead
        y = H - top - (h - total) / 2 - size * 0.9
        c.setFont(font, size)
        c.setFillColor(tcolor)
        for ln in lines:
            c.drawCentredString(x + w / 2, y, ln)
            y -= lead


def arrowhead(c, x, y, dx, dy, color, s=5.5):
    # tip at (x,y), direction (dx,dy) unit
    px, py = -dy, dx
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(x, y)
    p.lineTo(x - dx * s * 1.6 + px * s * 0.8, y - dy * s * 1.6 + py * s * 0.8)
    p.lineTo(x - dx * s * 1.6 - px * s * 0.8, y - dy * s * 1.6 - py * s * 0.8)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def poly_arrow(c, pts, color=HexColor("#44505C"), label=None, dash=False):
    c.setStrokeColor(color)
    c.setLineWidth(1.4)
    if dash:
        c.setDash(4, 3)
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    c.drawPath(p, fill=0, stroke=1)
    c.setDash()
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    L = max(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 1e-6)
    arrowhead(c, x2, y2, (x2 - x1) / L, (y2 - y1) / L, color)
    if label:
        # place on longest segment
        best = max(range(len(pts) - 1), key=lambda i: abs(pts[i + 1][0] - pts[i][0]) + abs(pts[i + 1][1] - pts[i][1]))
        mx = (pts[best][0] + pts[best + 1][0]) / 2
        my = (pts[best][1] + pts[best + 1][1]) / 2
        c.setFont("F", 8)
        tw = c.stringWidth(label, "F", 8)
        c.setFillColor(white)
        c.rect(mx - tw / 2 - 2, my - 5, tw + 4, 11, fill=1, stroke=0)
        c.setFillColor(MUTE)
        c.drawCentredString(mx, my - 2.5, label)


def band(c, color, num, title, page, total=3):
    c.setFillColor(color)
    c.rect(0, H - 52, W, 52, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("FB", 22)
    c.drawString(M, H - 36, f"{num:02d}")
    c.setFont("FB", 13)
    lines = wrap(title, "FB", 13, W - 2 * M - 130)
    y = H - 24 if len(lines) > 1 else H - 31
    for ln in lines[:2]:
        c.drawString(M + 46, y, ln)
        y -= 16
    c.setFont("F", 8.5)
    c.drawRightString(W - M, H - 20, "TÜBİTAK 2209-A / 2026")
    c.drawRightString(W - M, H - 32, "Proje tanıtım özeti")
    c.setFillColor(MUTE)
    c.setFont("F", 8)
    c.drawString(M, 14, "Bu özet başvuru taslağındaki planı gösterir. Veri toplanmamıştır, sonuç yoktur, fiyatlar tahminidir.")
    c.drawRightString(W - M, 14, f"{page} / {total}")


def section_title(c, text, x, top, color, w=None):
    c.setFillColor(color)
    c.setFont("FB", 11)
    c.drawString(x, H - top - 10, text.upper())
    c.setStrokeColor(color)
    c.setLineWidth(1.2)
    c.line(x, H - top - 15, x + (w or (W - 2 * M)), H - top - 15)


def card(c, x, top, w, h, big, small, color):
    c.setFillColor(HexColor("#F7F9FB"))
    c.setStrokeColor(LINE)
    c.setLineWidth(1)
    c.roundRect(x, H - top - h, w, h, 8, fill=1, stroke=1)
    c.setFillColor(color)
    c.rect(x, H - top - h, 4, h, fill=1, stroke=0)
    bs = 17
    while c.stringWidth(big, "FB", bs) > w - 22 and bs > 10:
        bs -= 1
    c.setFont("FB", bs)
    c.drawString(x + 12, H - top - 24, big)
    text_block(c, small, x + 12, top + 30, w - 20, 8.8, "F", MUTE)


# ---------- diagram ----------
def diagram(c, fx, ftop, fw, fh, nodes, edges, color):
    pos = {}
    for n in nodes:
        nid, cx, cy, w, h, text, kind = n
        W_, H_ = fw * w / 100.0, fh * h / 100.0
        x = fx + fw * cx / 100.0 - W_ / 2
        top = ftop + fh * cy / 100.0 - H_ / 2
        pos[nid] = (x, top, W_, H_)
    # edges first (under boxes)
    for e in edges:
        a, b = e[0], e[1]
        label = e[2] if len(e) > 2 else None
        opt = e[3] if len(e) > 3 else {}
        ax, at, aw, ah = pos[a]
        bx, bt, bw, bh = pos[b]
        acx, acy = ax + aw / 2, at + ah / 2
        bcx, bcy = bx + bw / 2, bt + bh / 2
        Y = lambda t: H - t
        if abs(acy - bcy) < 6:  # same row
            if bcx > acx:
                pts = [(ax + aw, Y(acy)), (bx, Y(bcy))]
            else:
                pts = [(ax, Y(acy)), (bx + bw, Y(bcy))]
        elif abs(acx - bcx) < 6:  # same column
            if bcy > acy:
                pts = [(acx, Y(at + ah)), (bcx, Y(bt))]
            else:
                pts = [(acx, Y(at)), (bcx, Y(bt + bh))]
        else:
            if bcy > acy:
                s_top, e_top = at + ah, bt
            else:
                s_top, e_top = at, bt + bh
            mid = opt.get("mid", (s_top + e_top) / 2)
            pts = [(acx, Y(s_top)), (acx, Y(mid)), (bcx, Y(mid)), (bcx, Y(e_top))]
        poly_arrow(c, pts, label=label, dash=opt.get("dash", False))
    for n in nodes:
        nid, cx, cy, w, h, text, kind = n
        x, top, W_, H_ = pos[nid]
        fill, stroke = KIND[kind]
        if kind == "output":
            box(c, x, top, W_, H_, text, color, color, size=9.5, font="FB", tcolor=white)
        else:
            box(c, x, top, W_, H_, text, fill, stroke, size=9.3, font="F", lw=1.5 if kind == "key" else 1.2)


def legend(c, x, top, color):
    items = [("input", "girdi / koşul"), ("device", "cihaz"), ("sensor", "sensör"),
             ("process", "işlem"), ("key", "kilit nokta"), ("risk", "güvenlik / risk"), ("output", "çıktı")]
    cx = x
    for k, t in items:
        fill, stroke = KIND[k]
        if k == "output":
            fill = stroke = color
        c.setFillColor(fill)
        c.setStrokeColor(stroke)
        c.setLineWidth(1.1)
        c.roundRect(cx, H - top - 9, 16, 9, 2.5, fill=1, stroke=1)
        c.setFillColor(MUTE)
        c.setFont("F", 8)
        c.drawString(cx + 20, H - top - 8, t)
        cx += 22 + c.stringWidth(t, "F", 8) + 14


# ---------- page 2 parts ----------
def chips(c, top, chips_, result, color):
    n = len(chips_)
    gap = 18
    rw = 150
    avail = W - 2 * M - rw - n * gap
    cw = avail / n
    x = M
    for i, (big, small) in enumerate(chips_):
        c.setFillColor(HexColor("#F7F9FB"))
        c.setStrokeColor(color)
        c.setLineWidth(1.3)
        c.roundRect(x, H - top - 54, cw, 54, 8, fill=1, stroke=1)
        c.setFillColor(color)
        c.setFont("FB", 18)
        c.drawCentredString(x + cw / 2, H - top - 22, big)
        text_block(c, small, x + 4, top + 28, cw - 8, 8.6, "F", MUTE, align="center")
        x += cw
        c.setFillColor(MUTE)
        c.setFont("FB", 15)
        sym = "×" if i < n - 1 else "="
        c.drawCentredString(x + gap / 2, H - top - 32, sym)
        x += gap
    box(c, x, top, rw, 54, result, color, color, size=10.5, font="FB", tcolor=white, r=8)


def split_bar(c, top, segs, caption, color):
    total = sum(s[1] for s in segs)
    x = M
    wtot = W - 2 * M
    cols = [HexColor("#4C8DF6"), HexColor("#F2B134"), HexColor("#2FA36B"), HexColor("#9B6BDB")]
    for i, (label, val) in enumerate(segs):
        w = wtot * val / total
        fill = cols[i % len(cols)]
        c.setFillColor(fill)
        c.setStrokeColor(white)
        c.setLineWidth(2)
        c.rect(x, H - top - 34, w, 34, fill=1, stroke=1)
        size = 9
        lines = wrap(label, "FB", size, w - 8)
        while len(lines) > 2 and size > 7.5:
            size -= 0.5
            lines = wrap(label, "FB", size, w - 8)
        c.setFillColor(white)
        c.setFont("FB", size)
        ty = H - top - 17 + (len(lines) - 1) * size * 0.6
        for ln in lines:
            c.drawCentredString(x + w / 2, ty, ln)
            ty -= size * 1.2
        x += w
    text_block(c, caption, M, top + 40, W - 2 * M, 9, "F", MUTE)


def hyp_cards(c, top, hyps, color, h=92):
    n = len(hyps)
    gap = 12
    w = (W - 2 * M - gap * (n - 1)) / n
    x = M
    for i, t in enumerate(hyps):
        c.setFillColor(HexColor("#F7F9FB"))
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.roundRect(x, H - top - h, w, h, 8, fill=1, stroke=1)
        c.setFillColor(color)
        c.roundRect(x + 8, H - top - 26, 28, 18, 5, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("FB", 10)
        c.drawCentredString(x + 22, H - top - 21, f"H{i+1}")
        text_block(c, t, x + 42, top + 8, w - 50, 9.2, "F", INK)
        x += w + gap


def ladder(c, top, items, color, h=86):
    n = len(items)
    gap = 26
    w = (W - 2 * M - gap * (n - 1)) / n
    x = M
    for i, (code, title, desc) in enumerate(items):
        shade = [HexColor("#EEF1F4"), HexColor("#E4E9EF"), HexColor("#D6DEE7"), HexColor("#C5D1DE")][min(i, 3)]
        c.setFillColor(shade)
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.roundRect(x, H - top - h, w, h, 8, fill=1, stroke=1)
        c.setFillColor(color)
        c.roundRect(x + 8, H - top - 24, 26, 17, 5, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("FB", 9.5)
        c.drawCentredString(x + 21, H - top - 19, code)
        text_block(c, title, x + 40, top + 7, w - 46, 9.8, "FB", INK)
        text_block(c, desc, x + 10, top + 32, w - 18, 8.8, "F", MUTE)
        if i < n - 1:
            poly_arrow(c, [(x + w + 3, H - top - h / 2), (x + w + gap - 3, H - top - h / 2)])
        x += w + gap


# ---------- page 3 parts ----------
def gantt(c, x, top, w, rows, color):
    lab = 150
    mw = (w - lab) / 8
    rh = 30
    c.setFont("FB", 8.5)
    c.setFillColor(MUTE)
    for m in range(8):
        c.drawCentredString(x + lab + mw * m + mw / 2, H - top - 9, f"{m+1}. ay")
    y0 = top + 16
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    for m in range(9):
        c.line(x + lab + mw * m, H - y0, x + lab + mw * m, H - y0 - rh * len(rows))
    for i, (name, s, e, wt) in enumerate(rows):
        yt = y0 + rh * i
        c.line(x, H - yt, x + w, H - yt)
        text_block(c, f"İP{i+1}  {name}", x, yt + 3, lab - 8, 8.6, "F", INK, lead=10)
        bx = x + lab + mw * (s - 1) + 2
        bw = mw * (e - s + 1) - 4
        c.setFillColor(color)
        c.roundRect(bx, H - yt - rh + 6, bw, rh - 12, 5, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("FB", 9)
        c.drawCentredString(bx + bw / 2, H - yt - rh / 2 - 3, f"%{wt}")
    c.line(x, H - y0 - rh * len(rows), x + w, H - y0 - rh * len(rows))
    return y0 + rh * len(rows)


def risk_table(c, x, top, w, rows, color):
    c1 = w * 0.38
    c.setFillColor(color)
    c.rect(x, H - top - 18, w, 18, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("FB", 9)
    c.drawString(x + 6, H - top - 13, "Risk")
    c.drawString(x + c1 + 6, H - top - 13, "B planı")
    y = top + 18
    for i, (r, p) in enumerate(rows):
        l1 = wrap(r, "FB", 8.6, c1 - 12)
        l2 = wrap(p, "F", 8.6, w - c1 - 12)
        h = max(len(l1), len(l2)) * 10.6 + 8
        c.setFillColor(HexColor("#FBFCFD") if i % 2 == 0 else HexColor("#F1F4F7"))
        c.rect(x, H - y - h, w, h, fill=1, stroke=0)
        text_block(c, r, x + 6, y + 4, c1 - 12, 8.6, "FB", INK, lead=10.6)
        text_block(c, p, x + c1 + 6, y + 4, w - c1 - 12, 8.6, "F", INK, lead=10.6)
        y += h
    c.setStrokeColor(LINE)
    c.line(x, H - y, x + w, H - y)
    return y


def budget_bar(c, x, top, w, items, total_txt, note, color):
    items = sorted(items, key=lambda t: -t[1])
    top5 = items[:5]
    rest = sum(v for _, v in items[5:])
    segs = top5 + ([("Diğer", rest)] if rest else [])
    total = sum(v for _, v in segs)
    cols = [color, HexColor("#4C8DF6"), HexColor("#F2B134"), HexColor("#2FA36B"), HexColor("#9B6BDB"), HexColor("#9AA5B1")]
    cx = x
    for i, (n, v) in enumerate(segs):
        sw = w * v / total
        c.setFillColor(cols[i % len(cols)])
        c.setStrokeColor(white)
        c.setLineWidth(1.5)
        c.rect(cx, H - top - 22, sw, 22, fill=1, stroke=1)
        cx += sw
    ly = top + 28
    colw = w / 2
    for i, (n, v) in enumerate(segs):
        lx = x + (i % 2) * colw
        ry = ly + (i // 2) * 12
        c.setFillColor(cols[i % len(cols)])
        c.rect(lx, H - ry - 8, 8, 8, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont("F", 8.4)
        s = f"{n}: {v:,.0f} TL".replace(",", ".")
        c.drawString(lx + 12, H - ry - 7.5, s)
    yy = ly + ((len(segs) + 1) // 2) * 12 + 4
    c.setFont("FB", 10)
    c.setFillColor(INK)
    c.drawString(x, H - yy - 10, total_txt)
    used = text_block(c, note, x, yy + 14, w, 8.6, "F", MUTE)
    return yy + 14 + used


def list_height(items, w, size=9.2, lead=11.2):
    return 30 + sum(len(wrap(t, "F", size, w - 32)) * lead + 4 for t in items)


def list_box(c, x, top, w, h, title, items, color, bullet="•"):
    if h is None:
        h = list_height(items, w)
    c.setFillColor(HexColor("#F7F9FB"))
    c.setStrokeColor(LINE)
    c.setLineWidth(1)
    c.roundRect(x, H - top - h, w, h, 8, fill=1, stroke=1)
    c.setFillColor(color)
    c.setFont("FB", 10)
    c.drawString(x + 10, H - top - 17, title)
    y = top + 26
    for it in items:
        c.setFillColor(color)
        c.setFont("FB", 9)
        c.drawString(x + 10, H - y - 9, bullet)
        used = text_block(c, it, x + 22, y, w - 32, 9.2, "F", INK, lead=11.2)
        y += used + 4
    return h
