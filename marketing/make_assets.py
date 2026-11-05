from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "xhs"
OUT.mkdir(exist_ok=True)

W, H = 1080, 1440
INK = "#17223c"
CREAM = "#fff7e7"
PAPER = "#fffdf7"
MANGO = "#ff7a21"
YELLOW = "#ffd94f"
SKY = "#9bd7ff"
ROSE = "#ffc1b2"
MINT = "#b8e9c9"
MUTED = "#6a6d72"

FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"
ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


def canvas():
    img = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)
    draw.ellipse((-240, -280, 440, 400), fill=YELLOW)
    draw.ellipse((760, -180, 1260, 300), fill=SKY)
    draw.ellipse((820, 1110, 1230, 1540), fill=ROSE)
    draw.rectangle((0, 0, W, 25), fill=MANGO)
    return img, draw


def outlined_box(draw, xy, radius=26, fill=PAPER, shadow=10, width=4):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle((x1 + shadow, y1 + shadow, x2 + shadow, y2 + shadow), radius, fill=INK)
    draw.rounded_rectangle((x1, y1, x2, y2), radius, fill=fill, outline=INK, width=width)


def text(draw, xy, value, size, fill=INK, anchor="la", bold=True, spacing=8):
    draw.multiline_text(xy, value, font=font(size, bold), fill=fill, anchor=anchor, spacing=spacing)


def pill(draw, xy, value, size=26, fill=YELLOW, text_fill=INK):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, (y2-y1)//2, fill=fill, outline=INK, width=3)
    text(draw, ((x1+x2)//2, (y1+y2)//2), value, size, fill=text_fill, anchor="mm")


def cover():
    img, d = canvas()
    pill(d, (74, 100, 648, 162), "芒果TV《后会友期》 · 非官方人物测试", 25, PAPER)
    text(d, (66, 208), "后会友期", 69, MANGO)
    text(d, (61, 302), "你是节目", 137, INK)
    text(d, (61, 452), "里的谁？", 155, INK)
    d.rounded_rectangle((68, 665, 651, 718), 18, fill=YELLOW, outline=INK, width=3)
    text(d, (82, 674), "4组旧友  ×  8种人物  ×  10道题", 31)
    text(d, (68, 781), "不是让你分析别人，\n是看看你会怎么爱朋友。", 40, "#4e5664", spacing=16)

    outlined_box(d, (66, 980, 1014, 1295), 36, PAPER, 11)
    text(d, (112, 1023), "测完直接得到", 31, MANGO)
    text(d, (112, 1081), "你的旅程人物车票", 57)
    cols = [(141, MANGO), (394, YELLOW), (647, SKY), (900, MINT)]
    for i, (x, color) in enumerate(cols):
        d.ellipse((x-45, 1170, x+45, 1260), fill=color, outline=INK, width=3)
        text(d, (x, 1215), "萌宇飞纯"[i], 30, INK, anchor="mm")
    text(d, (84, 1331), "点开测完 · 自动生成可分享结果", 29, MUTED)
    img.save(OUT / "01-cover.png", quality=95)


def pairs():
    img, d = canvas()
    pill(d, (72, 92, 522, 150), "后会友期 · 人物图鉴", 27, PAPER)
    text(d, (68, 205), "4组旧友", 94)
    text(d, (68, 312), "8种人物", 94, MANGO)
    text(d, (72, 431), "你最像哪一个？", 47, "#4d5562")

    groups = [
        ("主动照顾线", "张萌 × 马天宇", "直球照顾者 / 慢热观察者", YELLOW, "萌宇"),
        ("旧日同频线", "厉娜 × 许飞", "旧日收藏家 / 清醒边界派", SKY, "娜飞"),
        ("清醒边界线", "文吉儿 × 王子璇", "讲清派 / 止损派", ROSE, "文璇"),
        ("热烈磨合线", "青稚 × 白小纯", "任务脑 / 热烈回应者", MINT, "稚纯"),
    ]
    coords = [(66, 560), (558, 560), (66, 942), (558, 942)]
    for (title, names, types, color, initials), (x, y) in zip(groups, coords):
        outlined_box(d, (x, y, x+456, y+330), 29, PAPER, 8, 3)
        d.ellipse((x+29, y+28, x+111, y+110), fill=color, outline=INK, width=3)
        text(d, (x+70, y+68), initials, 27, INK, anchor="mm")
        text(d, (x+132, y+29), title, 29, MANGO)
        text(d, (x+32, y+140), names, 37)
        text(d, (x+32, y+205), types, 22, "#5f636b")
        text(d, (x+32, y+260), "你会在哪条线上？", 23, MUTED)
    text(d, (540, 1340), "非官方粉丝向测试 · 不使用嘉宾肖像", 23, MUTED, anchor="mm")
    img.save(OUT / "02-four-pairs.png", quality=95)


def result_preview():
    img, d = canvas()
    pill(d, (72, 92, 544, 151), "测完你会得到什么？", 28, PAPER)
    text(d, (68, 206), "不是四个笼统标签，", 55)
    text(d, (68, 282), "是一张完整人物车票。", 55, MANGO)

    outlined_box(d, (92, 401, 988, 1288), 46, PAPER, 12, 4)
    d.rounded_rectangle((94, 403, 986, 720), 42, fill=MINT, outline=INK, width=3)
    d.rectangle((94, 680, 986, 724), fill=MINT)
    pill(d, (132, 447, 458, 501), "你的后会友期人物", 23, PAPER)
    text(d, (132, 527), "青稚", 91)
    text(d, (135, 631), "冷静的任务脑", 35)

    rows = [
        ("01", "对应哪一条旧友线", "青稚 × 白小纯"),
        ("02", "你的关系底色比例", "主动 / 同频 / 边界 / 磨合"),
        ("03", "这条线的另一端", "你最需要读懂的那种朋友"),
        ("04", "可分享的结果链接", "发给朋友一起测"),
    ]
    y = 784
    for number, title, copy in rows:
        d.ellipse((132, y, 181, y+49), fill=YELLOW, outline=INK, width=2)
        text(d, (156, y+25), number, 15, INK, anchor="mm")
        text(d, (202, y-2), title, 28)
        text(d, (202, y+39), copy, 21, MUTED)
        y += 112
    text(d, (540, 1344), "10题约2分钟 · 完成后直接出结果", 28, MUTED, anchor="mm")
    img.save(OUT / "03-result-preview.png", quality=95)


cover()
pairs()
result_preview()
print("created", ", ".join(path.name for path in sorted(OUT.glob("*.png"))))
