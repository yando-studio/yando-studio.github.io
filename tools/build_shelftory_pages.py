#!/usr/bin/env python3
"""Build the ShelfTory landing page in Korean and English.

    python3 tools/build_shelftory_pages.py

Writes shelftory/index.html (ko) and shelftory/en/index.html from one template.
Edit the copy in COPY below and re-run; do not edit the generated HTML by hand.

Layout and styles come from build_cashtory_pages.py with ShelfTory's colors swapped
in, so both product pages stay alike. Copy follows the Play listing in the app repo
(yando-studio/Shelftory, store/PLAY_LISTING.md) so the page claims only what ships.

Screenshots: shelftory/assets/screens/<lang>/ are captured from the web demo
(shelftory/demo/app/); shelftory/assets/store/ are crops of the Korean store screenshots
(store/0N-*.png in the app repo).
"""
from html import escape
from pathlib import Path

from build_cashtory_pages import CSS as CASHTORY_CSS, webp_size

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://yandostudio.co.kr"
PLAY = "https://play.google.com/store/apps/details?id=com.yandostudio.shelftory"
PRIVACY = "https://yando-studio.github.io/Shelftory-privacy/"
MAIL = "mailto:official.yo.studio@gmail.com"
LANGS = ["ko", "en"]
PATHS = {"ko": "/shelftory/", "en": "/shelftory/en/"}
OG_LOCALE = {"ko": "ko_KR", "en": "en_US"}

# CashTory purple → ShelfTory's brand (the 1.6 app icon): ivory paper, dark green ink,
# the app's teal-green (brand-600 in the app's tailwind.config.js) as the point colour.
IVORY, GREEN, POINT, MAPLE = "#F4EFE6", "#0B3B32", "#307E6F", "#E2BF8C"
COLORS = [
    ("--accent:#6750C7;--accent-soft:#ECE9F7;--point:#6750C7;--point-soft:#ECE9F7",
     f"--accent:{GREEN};--accent-soft:#E7EFEB;--point:{POINT};--point-soft:#E7F2EE"),
    ("#F6F7FB", "#F7F4EE"), ("#E4E5EC", "#E7E1D5"),
    ("rgba(246,247,251,.88)", "rgba(247,244,238,.88)"), ("rgba(228,229,236,.8)", "rgba(231,225,213,.8)"),
    ("rgba(103,80,199,.22)", "rgba(11,59,50,.22)"), ("rgba(28,17,71,.16)", "rgba(11,59,50,.16)"),
    ("rgba(36,28,75,.09)", "rgba(43,38,25,.08)"), ("rgba(31,25,62,.22)", "rgba(11,59,50,.2)"),
    ("#DDD7FF 0,#EFEAFF 48%,rgba(239,234,255,0) 72%", "#EBDDC6 0,#F2EADC 48%,rgba(242,234,220,0) 72%"),
    ("linear-gradient(180deg,#F0EDFB,#F7F6FC)", f"linear-gradient(180deg,{IVORY},#F8F6F1)"),
    ("linear-gradient(135deg,#6750C7,#4B36A8)", f"linear-gradient(135deg,{GREEN},#1C4A3F)"),
    ("#E2DCFF", "#D3E2DC"), ("#5547a1", "#215147"),
    (".tryBand .pill{background:#fff;color:var(--accent);", f".tryBand .pill{{background:{MAPLE};color:{GREEN};"),
]
CSS = CASHTORY_CSS
for a, b in COLORS:
    assert a in CSS, a
    CSS = CSS.replace(a, b)

COPY = {
    "ko": {
        "title": "ShelfTory — 남은 물품은 한눈에, 필요한 물품은 장보기로",
        "desc": "남은 물품과 유통기한을 한눈에. 영수증·바코드 등록부터 장보기·이번 주 메뉴·홈 화면 위젯까지 간편하게 관리하는 물품·유통기한 관리 앱.",
        "nav": [("#expiry", "기한 알림"), ("#shopping", "장보기"), ("#menu", "메뉴"), ("#widgets", "위젯"), ("/shelftory/demo/", "체험하기")],
        "hero_h1": "남은 물품은 한눈에,<br>필요한 물품은 장보기로.",
        "hero_lead": "수량과 유통기한을 확인하고, 장보기와 이번 주 메뉴까지 함께 정리하세요. 가정부터 가게까지, 물품을 알기 쉽게 관리합니다.",
        "hero_play": "Google Play에서 시작하기",
        "hero_demo": "설치 없이 체험하기",
        "hero_micro": "무료 · 회원가입 없이 바로 시작 · 한국어 · English",
        "float1": ("유통기한이 다가오면", "홈과 알림으로"),
        "float2": ("밀어서 한 번에", "사용 · 버림 · 장보기"),
        "alt_home": "ShelfTory 홈 화면",
        "trust": [("회원가입 없이", "설치하고 바로 시작하세요."),
                  ("내 기기에 저장", "앱 데이터는 서버가 아닌 기기에."),
                  ("홈 화면 위젯 4종", "앱을 열지 않고 기한·장보기 확인."),
                  ("백업 & Excel 무료", "기록을 앱 안에만 가두지 않아요.")],
        "sections": [
            {"id": "expiry", "k": "EXPIRY ALERTS", "h": "놓치기 쉬운 기한,<br>미리 확인하세요.",
             "p": "유통기한이 다가오면 홈과 알림에서 알려 줘요. 카테고리별로 알림 시점을 정할 수 있고, 지남·오늘·D-day가 한눈에 구분됩니다.",
             "img": ("/shelftory/assets/store/04-alert.webp", "유통기한 알림과 오늘 확인할 물품"), "frame": "shot"},
            {"id": "favorites", "k": "FAVORITES", "h": "자주 보는 물품은<br>홈에서 바로.",
             "p": "우유·계란처럼 자주 확인하는 품목에 ☆를 달면 홈 카드에 남은 양과 가장 급한 D-day가 모여요. 다 써도 카드에 남아 있어 '담기' 한 번으로 장보기에 담을 수 있어요.",
             "list": [("☆ 하나로 지정", "물품 수정 화면이나 품목 정보 관리에서"),
                      ("남은 양 · D-day", "단위가 다르면 2개 · 500g처럼 나눠 보여요"),
                      ("다 쓰면 바로 담기", "이미 담겼으면 '담김'으로 표시")]},
            {"id": "organize", "k": "ORGANIZE", "h": "카테고리와 위치별로,<br>보기 쉽게.",
             "p": "냉장고·냉동실·상온 식품·생활용품처럼 카테고리를 나누고, '냉장고 문칸'·'채소칸' 같은 위치·종류로 묶어 보세요. 기본·격자·촘촘히 보기 중에서 고르고, 'ㄱㅊ'처럼 초성만 쳐도 '김치'를 찾아요.",
             "img": ("/shelftory/assets/screens/ko/list.webp", "카테고리와 위치별 물품 목록"), "frame": "phone"},
            {"id": "input", "k": "FAST INPUT", "h": "하나하나 입력하는<br>수고를 줄이세요.",
             "p": "영수증이나 쇼핑앱 주문 캡처에서 품목과 수량을 읽고, 확인한 뒤 한 번에 등록해요. 바코드로 상품 이름을 불러오거나 직접 입력할 수도 있어요. 사진은 기기 안에서 인식하며 앱 서버로 보내지 않습니다.",
             "list": [("영수증 찍기", "품목과 수량을 읽어 한 번에 등록"),
                      ("주문 캡처 불러오기", "쇼핑앱 주문 화면을 그대로 활용"),
                      ("바코드 스캔", "상품 이름을 불러오거나 직접 입력")],
             "img": ("/shelftory/assets/screens/ko/add.webp", "물품 추가 화면"), "frame": "phone"},
            {"id": "swipe", "k": "USE & DISCARD", "h": "먹고 쓴 건 오른쪽으로,<br>살 건 왼쪽으로.",
             "p": "목록에서 물품을 오른쪽으로 밀면 먹은 것·쓴 것·버린 것을 기록하고, 왼쪽으로 밀면 장보기에 담겨요. 일부만 쓰거나 버린 양도 남길 수 있어요.",
             "img": ("/shelftory/assets/store/05-swipe.webp", "밀어서 사용·버림과 장보기 담기"), "frame": "shot"},
            {"id": "shopping", "k": "SHOPPING", "h": "담고, 체크하고,<br>장본 뒤 바로 추가.",
             "p": "구매처나 목적별로 장보기 목록을 만들고 장보면서 체크하세요. 남은 양과 유통기한 지남·임박 정보를 보며 준비하고, 장본 물품은 물품 목록에 바로 추가해요.",
             "img": ("/shelftory/assets/screens/ko/shop.webp", "장보기 목록 화면"), "frame": "phone"},
            {"id": "menu", "k": "WEEKLY MENU", "h": "가지고 있는 재료로<br>이번 주 메뉴를.",
             "p": "요일과 끼니별로 메뉴를 정하고 재료와 사용할 양을 적어 두세요. ‘요리했어요’를 누르면 사용한 양이 줄고, 물품 목록에 없는 재료는 장보기에 담을 수 있어요. 메뉴 메모와 날짜별 일정(매년 양력·음력 반복)을 적고, 고른 날의 메뉴를 가족에게 보내거나 받은 메뉴를 가져올 수도 있어요.",
             "img": ("/shelftory/assets/store/07-menu.webp", "이번 주 메뉴 화면"), "frame": "shot"},
            {"id": "widgets", "k": "WIDGETS", "h": "앱을 열지 않아도<br>위젯으로 한눈에.",
             "p": "Android 홈 화면 위젯 4종을 무료로 쓸 수 있어요. 유통기한 임박 물품과 오늘 메뉴를 확인하고, 장보기 목록은 위젯에서 바로 체크해요. 스캔·영수증·등록·살 것 추가도 한 번에 열려요.",
             "list": [("빠른 실행", "스캔 · 영수증 · 등록 · 살 것 추가"),
                      ("유통기한 임박", "알림과 같은 물품을 크기에 맞춰"),
                      ("장보기 · 오늘 메뉴", "앱을 열지 않고 체크하고 확인")],
             "img": ("/shelftory/assets/store/02-widgets.webp", "홈 화면 위젯"), "frame": "shot"},
            {"id": "stats", "k": "FREE TO USE", "h": "통계·Excel·백업까지<br>무료로.",
             "p": "소진·버림 통계로 월별 흐름을 보고, 처리 기록은 Excel로 받아 보세요. 품목 정보 관리는 카테고리·단위·유통기한 기본값을 기억해 다음 입력을 줄여요. 홈 카드와 하단의 장보기·메뉴 탭도 필요한 것만 골라 구성해요.",
             "img": ("/shelftory/assets/store/08-free.webp", "무료로 쓰는 기능들"), "frame": "shot"},
        ],
        "data_k": "YOUR DATA",
        "data_h": "기록은 내 기기에, 필요하면 파일로.",
        "data": [("↻", "백업 · 복원", "JSON 백업 파일로 기기를 바꿔도 그대로 옮겨요. 무료입니다."),
                 ("⇩", "Excel 내보내기", "처리 기록과 통계를 파일로 꺼내 확인하세요."),
                 ("⌂", "가정부터 가게까지", "장소 이름과 홈 카드 순서·표시 여부를 직접 정해요."),
                 ("⌁", "이미지는 기기에서 인식", "영수증·주문 캡처 사진을 앱 서버로 보내지 않습니다.")],
        "try_h": "설치하기 전에,<br>먼저 눌러 보세요.",
        "try_p": "예시 물품과 장보기 목록이 들어 있는 실제 앱을 브라우저에서 바로 사용해 볼 수 있어요. 입력한 내용은 저장되지 않습니다.",
        "try_btn": "웹에서 체험하기",
        "final_h": "기억할 것은 줄이고,<br>필요한 것은 놓치지 않도록.",
        "final_p": "무료로 이용할 수 있으며 앱 내 광고가 표시됩니다.",
        "final_play": "Google Play에서 다운로드",
        "footer": [("/", "Y&O STUDIO"), (PRIVACY, "개인정보처리방침"), (MAIL, "문의하기")],
    },
    "en": {
        "title": "ShelfTory — See what's left, shop for what you need",
        "desc": "Track what you have and when it expires. Add items from receipts, order screenshots or barcodes, then plan shopping lists, this week's meals and home screen widgets.",
        "nav": [("#expiry", "Expiry alerts"), ("#shopping", "Shopping"), ("#menu", "Meals"), ("#widgets", "Widgets"), ("/shelftory/demo/", "Try it")],
        "hero_h1": "See what's left at a glance.<br>Shop for what you need.",
        "hero_lead": "Keep track of quantities and expiry dates, then plan your shopping list and this week's meals in the same app — at home or for a small shop.",
        "hero_play": "Get it on Google Play",
        "hero_demo": "Try it without installing",
        "hero_micro": "Free · No sign-up · English · 한국어",
        "float1": ("Expiry coming up?", "Home card & alerts"),
        "float2": ("Swipe to log", "used · discarded · cart"),
        "alt_home": "ShelfTory home screen",
        "trust": [("No sign-up", "Install and start right away."),
                  ("Stored on your device", "Your data stays on your phone."),
                  ("4 home screen widgets", "Check expiry and your list without opening the app."),
                  ("Free backup & Excel", "Your records aren't locked inside the app.")],
        "sections": [
            {"id": "expiry", "k": "EXPIRY ALERTS", "h": "Expiry dates<br>you won't miss.",
             "p": "As dates get close, ShelfTory tells you on the home screen and with notifications. Set when to be alerted for each category, and see past due, today and days left at a glance.",
             "img": ("/shelftory/assets/screens/en/home.webp", "Items to check today on the home screen"), "frame": "phone"},
            {"id": "favorites", "k": "FAVORITES", "h": "Things you check often,<br>right on the home screen.",
             "p": "Star the items you check all the time — milk, eggs — and the home screen shows how much is left and the nearest expiry date. Even when they run out they stay on the card, so one tap puts them back on your list.",
             "list": [("Star it", "From the item screen or Item settings"),
                      ("What's left · D-day", "Mixed units shown as 2 pcs · 500 g"),
                      ("Ran out? Add to cart", "Shows “Added” when it's already there")]},
            {"id": "organize", "k": "ORGANIZE", "h": "Sorted by category<br>and by where it lives.",
             "p": "Split things into Fridge, Freezer, Pantry and Supplies, then group them by spot — the fridge door, the crisper. Choose a standard, grid or compact view, and search by name.",
             "img": ("/shelftory/assets/screens/en/list.webp", "Items grouped by category and spot"), "frame": "phone"},
            {"id": "input", "k": "FAST INPUT", "h": "Less typing,<br>item by item.",
             "p": "Read items and quantities from a receipt or a shopping-app order screenshot, check them, and add them all at once. Or look up a product name by barcode, or type it in. Photos are read on your device and never sent to our servers.",
             "list": [("Scan a receipt", "Items and quantities, added in one go"),
                      ("Order screenshot", "Reuse the order screen from a shopping app"),
                      ("Scan a barcode", "Fill in the product name, or type it in")],
             "img": ("/shelftory/assets/screens/en/add.webp", "Add item screen"), "frame": "phone"},
            {"id": "swipe", "k": "USE & DISCARD", "h": "Swipe right when it's used,<br>left when you need more.",
             "p": "Swipe an item right to log what you ate, used or threw away; swipe left to add it to your cart. You can log partial amounts too.",
             "list": [("Used or eaten", "Quantity goes down as you use it"),
                      ("Discarded", "Kept separately so you can see what goes to waste"),
                      ("Add to cart", "Running low? One swipe puts it on your list")]},
            {"id": "shopping", "k": "SHOPPING", "h": "Add, check off,<br>and stock up in one step.",
             "p": "Make shopping lists by store or purpose and check things off as you shop. See what's left and what's expired or expiring while you plan, then move what you bought straight into your items.",
             "img": ("/shelftory/assets/screens/en/shop.webp", "Shopping list screen"), "frame": "phone"},
            {"id": "menu", "k": "WEEKLY MENU", "h": "Plan this week's meals<br>with what you have.",
             "p": "Plan meals by day and mealtime, and note the ingredients and amounts. Tap “Cooked” and the amounts used come off your items; ingredients you don't have can go straight to your cart. Add meal notes and day notes that repeat every year, and share a day's meals with family.",
             "list": [("By day and meal", "Breakfast, lunch and dinner for the whole week"),
                      ("Cooked", "Used amounts come off your items automatically"),
                      ("Missing ingredients", "Add them to your shopping list")]},
            {"id": "widgets", "k": "WIDGETS", "h": "See it all without<br>opening the app.",
             "p": "Four free Android home screen widgets: items about to expire, today's meals, a shopping list you can check off right on the widget, and shortcuts to scan, add a receipt, add an item or add to your list.",
             "list": [("Quick actions", "Scan · Receipt · Add · Add to list"),
                      ("Expiring soon", "The same items as your alerts, sized to fit"),
                      ("Shopping · Today's meals", "Check off and glance without opening the app")]},
            {"id": "stats", "k": "FREE TO USE", "h": "Stats, Excel and backups,<br>all free.",
             "p": "See monthly trends of used and discarded items, and export your records to Excel. Item settings remember category, unit and expiry defaults so the next entry is faster.",
             "list": [("Monthly stats", "Used vs. discarded, month by month"),
                      ("Excel export", "Download your records as a spreadsheet"),
                      ("Item defaults", "Category, unit and expiry remembered for next time")]},
        ],
        "data_k": "YOUR DATA",
        "data_h": "On your device, and in a file when you need it.",
        "data": [("↻", "Backup · Restore", "Move everything to a new phone with a JSON backup file. Free."),
                 ("⇩", "Excel export", "Download your records and stats as a file."),
                 ("⌂", "Home or shop", "Name your place and choose which home cards to show, in your order."),
                 ("⌁", "Images read on-device", "Receipt and order screenshots are never sent to our servers.")],
        "try_h": "Before you install,<br>take it for a spin.",
        "try_p": "Use the real app right in your browser, with sample items and a shopping list. Nothing you enter is saved.",
        "try_btn": "Try it on the web",
        "final_h": "Remember less.<br>Miss nothing you need.",
        "final_p": "Free to use, with in-app ads.",
        "final_play": "Download on Google Play",
        "footer": [("/", "Y&O STUDIO"), (PRIVACY, "Privacy Policy"), (MAIL, "Contact")],
    },
}

EXTRA_CSS = """
.listItem span.check{margin-top:2px}
.textCard{background:#fff;border:1px solid var(--line);border-radius:24px;padding:26px;box-shadow:var(--shadow);width:min(420px,100%)}
.textCard .list{margin-top:0}
.phone.flat{transform:none}
"""


def page(lang: str) -> str:
    c = COPY[lang]
    e = escape
    url = SITE + PATHS[lang]

    def img(src, alt, eager=False):
        w, h = webp_size(ROOT / src.lstrip("/"))
        loading = "" if eager else ' loading="lazy" decoding="async"'
        return f'<img src="{src}" alt="{e(alt)}" width="{w}" height="{h}"{loading}>'

    def items(rows):
        return "".join(
            f'<div class="listItem"><span class="check">✓</span><div><b>{e(b)}</b><small>{e(s)}</small></div></div>'
            for b, s in rows
        )

    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{l}" href="{SITE}{PATHS[l]}" />' for l in LANGS
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}{PATHS["ko"]}" />'
    # The demo follows the browser language unless told otherwise, so pass this page's language along.
    demo = f"/shelftory/demo/?lang={lang}"
    nav = "".join(f'<a href="{demo if h == "/shelftory/demo/" else h}">{e(t)}</a>' for h, t in c["nav"])
    langs = "".join(
        f'<a href="{PATHS[l]}" hreflang="{l}" lang="{l}"' + (' aria-current="page"' if l == lang else "")
        + f'>{l.upper()}</a>' for l in LANGS
    )
    trust = "".join(f'<div class="trustItem"><b>{e(b)}</b><span>{e(s)}</span></div>' for b, s in c["trust"])

    sections = []
    for i, s in enumerate(c["sections"]):
        cls = "block" + (" tint" if i % 2 == 0 else "")
        rev = " rev" if i % 2 == 1 else ""
        lst = f'<div class="list">{items(s["list"])}</div>' if s.get("list") and s.get("img") else ""
        if s.get("img"):
            src, alt = s["img"]
            media = (f'<div class="phone flat">{img(src, alt)}</div>' if s["frame"] == "phone"
                     else f'<figure class="shot">{img(src, alt)}</figure>')
        else:
            media = f'<div class="textCard"><div class="list">{items(s["list"])}</div></div>'
        sections.append(f"""
    <section class="{cls}" id="{s['id']}">
      <div class="wrap split{rev}">
        <div>
          <p class="kicker">{s['k']}</p>
          <h2>{s['h']}</h2>
          <p class="sectionLead">{e(s['p'])}</p>{lst}
        </div>
        <div class="media">{media}</div>
      </div>
    </section>""")

    data = "".join(
        f'<div class="card dataCard"><i aria-hidden="true">{i}</i><div><b>{e(t)}</b><p>{e(p)}</p></div></div>'
        for i, t, p in c["data"]
    )
    footer = "".join(f'<a href="{h}">{e(t)}</a>' for h, t in c["footer"])

    return f"""<!doctype html>
<!-- Generated by tools/build_shelftory_pages.py — edit that file, not this one. -->
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="{GREEN}" />
  <meta name="description" content="{e(c['desc'])}" />
  <link rel="canonical" href="{url}" />
{alternates}
  <link rel="icon" href="/shelftory/assets/favicon-48.png" type="image/png" />
  <link rel="apple-touch-icon" href="/shelftory/assets/apple-touch-icon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Y&amp;O STUDIO" />
  <meta property="og:locale" content="{OG_LOCALE[lang]}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{e(c['title'])}" />
  <meta property="og:description" content="{e(c['desc'])}" />
  <meta property="og:image" content="{SITE}/shelftory/assets/og-image.jpg?v=20261017" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <title>{e(c['title'])}</title>
  <style>{CSS}{EXTRA_CSS}  </style>
</head>
<body>
  <header class="top">
    <div class="wrap nav">
      <a class="brand" href="{PATHS[lang]}"><img src="/shelftory/assets/app-icon.webp" alt="" width="36" height="36"><span>ShelfTory</span></a>
      <div class="navRight">
        <nav class="navlinks" aria-label="ShelfTory">{nav}</nav>
        <nav class="lang" aria-label="Language">{langs}</nav>
        <a class="pill small" href="{PLAY}">Google Play</a>
      </div>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="wrap heroGrid">
        <div>
          <div class="eyebrow">SHELF + STORY</div>
          <h1>{c['hero_h1']}</h1>
          <p class="lead">{e(c['hero_lead'])}</p>
          <div class="cta">
            <a class="pill" href="{PLAY}">{e(c['hero_play'])}</a>
            <a class="pill ghost" href="{demo}">{e(c['hero_demo'])}</a>
          </div>
          <div class="micro">{e(c['hero_micro'])}</div>
        </div>
        <div class="stage">
          <div class="halo"></div>
          <div class="phone">{img(f"/shelftory/assets/screens/{lang}/home.webp", c['alt_home'], eager=True)}</div>
          <div class="float one">{e(c['float1'][0])}<em>{e(c['float1'][1])}</em></div>
          <div class="float two">{e(c['float2'][0])}<em>{e(c['float2'][1])}</em></div>
        </div>
      </div>
    </section>

    <section class="trust" aria-label="ShelfTory">
      <div class="wrap grid4">{trust}</div>
    </section>
{''.join(sections)}

    <section class="block">
      <div class="wrap">
        <div class="head">
          <p class="kicker">{c['data_k']}</p>
          <h2>{e(c['data_h'])}</h2>
        </div>
        <div class="grid2">{data}</div>
      </div>
    </section>

    <section class="wrap">
      <div class="tryBand">
        <div>
          <h2>{c['try_h']}</h2>
          <p>{e(c['try_p'])}</p>
        </div>
        <a class="pill" href="{demo}">{e(c['try_btn'])}</a>
      </div>
    </section>

    <section class="centerCta">
      <div class="wrap">
        <h2>{c['final_h']}</h2>
        <p>{e(c['final_p'])}</p>
        <div class="cta"><a class="pill" href="{PLAY}">{e(c['final_play'])}</a></div>
      </div>
    </section>
  </main>

  <footer>
    <div class="wrap footerRow">
      <span>© 2026 Y&amp;O STUDIO · ShelfTory</span>
      <div class="footerLinks">{footer}</div>
    </div>
  </footer>
</body>
</html>
"""


def main():
    for lang in LANGS:
        out = ROOT / PATHS[lang].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
