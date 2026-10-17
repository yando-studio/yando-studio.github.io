#!/usr/bin/env python3
"""Build the CashTory landing page in Korean, Japanese and English.

    python3 tools/build_cashtory_pages.py

Writes cashtory/index.html (ko), cashtory/ja/index.html and cashtory/en/index.html
from one template, so layout fixes land in all three at once. Edit the copy in
COPY below and re-run; do not edit the generated HTML by hand.

Screenshots live in cashtory/assets/screens/<lang>/ and are captured from the web
demo (cashtory/demo/app/) so every image is the real app in that language.
"""
import struct
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://yandostudio.co.kr"
PLAY = "https://play.google.com/store/apps/details?id=com.yandostudio.cashtory"
PRIVACY = "https://yando-studio.github.io/cashtory-privacy/"
MAIL = "mailto:official.yo.studio@gmail.com"
LANGS = ["ko", "ja", "en"]
PATHS = {"ko": "/cashtory/", "ja": "/cashtory/ja/", "en": "/cashtory/en/"}
OG_LOCALE = {"ko": "ko_KR", "ja": "ja_JP", "en": "en_US"}

COPY = {
    "ko": {
        "title": "CashTory — 기록은 가볍게, 돈의 흐름은 한눈에",
        "desc": "영수증 입력부터 카드·할부, 자산·부채, 차계부, 월말 리뷰와 메모·디데이까지. 회원가입 없이 시작하는 생활 가계부.",
        "nav": [("#features", "기능"), ("#vehicle", "차계부"), ("#review", "월말 리뷰"), ("/cashtory/demo/", "체험하기"),
                ("/cashtory/guide/", "사용법"), ("/cashtory/faq/", "FAQ")],
        "play": "Google Play",
        "hero_h1": "기록은 가볍게,<br>돈의 흐름은 한눈에.",
        "hero_lead": "영수증 입력부터 카드·할부, 자산과 차계부, 월말 리뷰까지. 복잡한 금융 용어 대신 내가 쓰는 돈의 흐름을 편하게 기록해 보세요.",
        "hero_play": "Google Play에서 시작하기",
        "hero_demo": "설치 없이 체험하기",
        "hero_micro": "회원가입 없이 바로 시작 · 6개 언어 · 13개 통화",
        "float1": ("가운데 버튼 하나로", "네 가지 입력"),
        "float2": ("메모·디데이도", "가계부 옆에"),
        "alt_ledger": "CashTory 가계부 화면",
        "trust": [("회원가입 없이", "설치하고 바로 시작하세요."),
                  ("내 기기에 저장", "가계부 기록은 서버가 아닌 기기에."),
                  ("6개 언어 · 13개 통화", "한국어 · 日本語 · English 외."),
                  ("백업 & 엑셀", "기록을 앱 안에만 가두지 않아요.")],
        "input_k": "FAST INPUT",
        "input_h": "가운데 버튼 하나로,<br>네 가지 입력.",
        "input_lead": "가운데 + 버튼을 톡 누르면 직접 입력, 누른 채 밀면 영수증 · 즐겨찾기 · 메모·디데이. 금액을 넣으면 다음 칸이 자동으로 열려요.",
        "inputs": [("✎", "직접 입력", "계산기로 금액을 넣고 자산과 분류를 고르면 끝. 지출·수입·이체를 한 화면에서."),
                   ("▣", "영수증 입력", "날짜·가게·금액·품목 인식을 도와줘요. 총액 1건 또는 품목별로 나눠 저장."),
                   ("★", "즐겨찾기", "커피·점심·교통비처럼 자주 쓰는 내용을 오늘 날짜로 바로 불러와요."),
                   ("◷", "메모·디데이", "그날의 메모와 다가오는 기념일을 가계부 날짜 사이에 함께 보여줘요.")],
        "alt_guide": "입력 방법 안내 화면", "alt_add": "거래 입력 화면",
        "receipt": {"k": "RECEIPT TO TRANSACTIONS",
                    "h": "한 장의 영수증을<br>필요한 만큼 나눠 기록하세요.",
                    "p": "읽어 온 품목을 확인하고, 필요한 품목만 골라 각각 다른 분류로 저장할 수 있습니다. 공통 날짜·자산·분류도 한 번에 지정할 수 있어요.",
                    "note": "영수증은 기기 안에서 인식하며, CashTory가 사진을 서버로 보내지 않습니다.",
                    "img": "/cashtory/assets/receipt-items.webp?v=20261012",
                    "alt": "영수증 품목별 저장 화면"},
        "cards_k": "CARD & INSTALLMENT",
        "cards_h": "카드로 쓴 돈도,<br>앞으로 낼 돈도 함께.",
        "cards_lead": "카드 사용은 구매한 날 지출로, 카드값 납부는 부채를 갚는 이동으로 처리해 같은 소비가 두 번 잡히지 않습니다.",
        "cards_list": [("카드 결제 예정", "결제일·출금 통장·D-day를 한 줄에"),
                       ("자동결제", "결제계좌와 결제일로 알아서 처리"),
                       ("할부 관리", "원리금균등·원금균등·단리 이자 계산"),
                       ("선결제", "미리 갚은 회차까지 정리")],
        "alt_cards": "자산 탭의 카드 결제 예정 화면",
        "stats_k": "STATS",
        "stats_h": "이번 달 흐름을<br>사진 한 장과 한마디로.",
        "stats_lead": "통계 첫 카드가 이번 달 지출을 지난달·6개월 평균과 비교해 한마디로 알려줘요. 고정비·변동비, 6개월 추이, 분류별 비중과 전월 대비 증감까지 이어서 보여줍니다.",
        "alt_stats": "통계 요약 화면", "alt_category": "분류별 지출 화면",
        "vehicle_k": "VEHICLE LOG",
        "vehicle_h": "차에 드는 돈도,<br>가계부 안에서.",
        "vehicle_lead": "차를 등록해 두면 주유·정비 지출을 적을 때 주행거리·주유량·교체 항목이 함께 기록돼요. 연비와 유지비, 다음 정비 시기는 통계의 '차량' 탭에서 한눈에 볼 수 있어요.",
        "vehicle": [("⛽", "주유도 지출 한 번에", "주유비를 적으면서 주행거리와 주유량을 함께 남기세요. 연비와 km당 비용은 알아서 계산돼요."),
                    ("⚙", "정비 교체 시기", "엔진오일·필터·타이어를 거리나 기간으로 챙기고, 지났거나 곧 다가오는 항목을 알려줘요."),
                    ("⚡", "전기차도, 두 대도", "휘발유·경유·LPG·하이브리드·전기차 모두. 차는 무료로 2대까지 등록할 수 있어요."),
                    ("◔", "차량 통계", "이번 달 유지비, 최근 6개월 유지비와 연비 그래프, 정비 항목을 한 화면에.")],
        "alt_vehicle": "통계의 차량 탭 화면", "alt_vehicle2": "차량 유지비 추이와 상세 기록",
        "review_k": "MONTHLY REVIEW",
        "review_h": "한 달의 숫자에<br>이야기를 더했어요.",
        "review_lead": "수입·지출과 저축률, 지난달과 달라진 점, 고정비·변동비, 카드·할부, 자산 변화와 다음 달 예정까지 한 화면에서 돌아보세요.",
        "review_list": ["달이 바뀌면 가계부 위에 리뷰가 준비돼요",
                        "지난달·최근 3개월과 비교한 변화를 한 줄로",
                        "한 장의 이미지로 저장해 공유"],
        "review_quote": "CashTory의 이름처럼, 매달 쌓인 기록이 하나의 돈 이야기가 되도록.",
        "alt_review": "월말 마감 리뷰 화면",
        "assets_k": "ASSETS",
        "assets_h": "가계부 기록이<br>자산의 흐름으로.",
        "assets_lead": "통장·현금·카드·투자·대출을 한 줄씩 보고, 맨 위 세 칸에서 자산·부채·순자산을 바로 확인하세요. 앞으로 30일 동안 나갈 카드값·정기 지출·정기 이체는 가계부의 '곧 나갈 돈'에서 날짜별로 미리 보여줍니다.",
        "alt_assets": "자산 탭 화면", "alt_upcoming": "곧 나갈 돈 화면",
        "dday_k": "MEMO & D-DAY",
        "dday_h": "돈 드는 날은<br>미리 알고 있게.",
        "dday_lead": "결혼기념일·생일·여행처럼 돈이 드는 날을 디데이로 챙기고, 그날의 메모를 남기세요. 매년·매월 반복도 되고, 가계부 날짜 사이에 함께 보여요.",
        "alt_dday": "메모·기념일 화면",
        "widgets_k": "WIDGETS",
        "widgets_h": "앱을 열지 않아도,<br>필요한 기능은 바로.",
        "widgets_lead": "이번 달 요약, 지출·수입 바로 입력, 영수증 촬영까지 위젯 6종. 바탕 투명도도 홈 화면에 맞게 고를 수 있어요.",
        "widgets_img": ("/cashtory/assets/widgets.webp", "안드로이드 홈 화면에 배치한 CashTory 위젯"),
        "widgets_cards": [],
        "data_k": "YOUR DATA",
        "data_h": "내 기록은 내가 관리합니다.",
        "data_lead": "기본 가계부 기록은 기기에 저장됩니다. 필요할 때 백업하고, 파일로 보관하고, 다른 가계부 기록도 가져올 수 있어요.",
        "data": [("↻", "백업 · 복원", "백업 파일을 내보내 앱 삭제나 기기 교체에 대비하세요."),
                 ("⇩", "엑셀 내보내기", "거래 내역을 파일로 꺼내 직접 확인하거나 보관하세요."),
                 ("⇧", "다른 앱에서 가져오기", "다른 가계부의 Excel(.xlsx)·CSV 파일을 열 매핑과 미리보기 후 가져옵니다."),
                 ("⌁", "영수증은 기기에서 인식", "영수증 사진을 CashTory 서버로 보내거나 보관하지 않습니다.")],
        "personal_k": "MAKE IT YOURS",
        "personal_h": "생활 방식에 맞게 바꿔 쓰세요.",
        "personal": [("월별 집계 시작일", "월급날이 25일이라면 가계부의 한 달도 25일부터 시작하게."),
                     ("24가지 테마 색상", "보라색부터 민트·코랄·앰버까지 강조색을 취향대로."),
                     ("라이트 · 다크", "시스템 설정에 맞춰 편안하게."),
                     ("6개 언어 · 13개 통화", "한국어, English, 日本語, हिन्दी, Português, Bahasa Indonesia.")],
        "try_h": "설치하기 전에,<br>먼저 눌러 보세요.",
        "try_p": "1년치 예시 기록이 들어 있는 실제 앱을 브라우저에서 바로 사용해 볼 수 있어요. 입력한 내용은 저장되지 않습니다.",
        "try_btn": "웹에서 체험하기",
        "final_h": "매일의 돈 이야기를<br>CashTory에 기록해 보세요.",
        "final_p": "회원가입 없이 바로 시작할 수 있습니다.",
        "final_play": "Google Play에서 다운로드",
        "footer": [("/", "Y&O STUDIO"), ("/cashtory/guide/", "사용법"), ("/cashtory/faq/", "FAQ"),
                   (PRIVACY, "개인정보처리방침"), (MAIL, "문의하기")],
    },
    "ja": {
        "title": "CashTory — 記録は軽く、お金の流れはひと目で",
        "desc": "レシート入力からカード・分割払い、資産・負債、車の家計簿、月末レビュー、メモ・Dデーまで。会員登録なしで始められる家計簿アプリ。",
        "nav": [("#features", "機能"), ("#vehicle", "車の家計簿"), ("#review", "月末レビュー"), ("/cashtory/demo/", "体験版")],
        "play": "Google Play",
        "hero_h1": "記録は軽く、<br>お金の流れは<wbr>ひと目で。",
        "hero_lead": "レシート入力からカード・分割払い、資産と車の家計簿、月末レビューまで。難しい金融用語ではなく、自分のお金の流れを気軽に記録できます。",
        "hero_play": "Google Play で始める",
        "hero_demo": "インストールなしで試す",
        "hero_micro": "会員登録なしですぐ開始 · 6言語 · 13通貨",
        "float1": ("中央のボタンで", "4つの入力方法"),
        "float2": ("メモ・Dデーも", "家計簿のそばに"),
        "alt_ledger": "CashTory の家計簿画面",
        "trust": [("会員登録なし", "インストールしてすぐ使えます。"),
                  ("端末に保存", "家計簿の記録はサーバーではなく端末に。"),
                  ("6言語 · 13通貨", "日本語 · 한국어 · English ほか。"),
                  ("バックアップ & Excel", "記録をアプリの中に閉じ込めません。")],
        "input_k": "FAST INPUT",
        "input_h": "中央のボタン<wbr>ひとつで、<br>4つの<wbr>入力方法。",
        "input_lead": "中央の + ボタンを軽く押すと手入力、押したままスライドするとレシート・よく使う項目・メモ・Dデー。金額を入れると次の項目が自動で開きます。",
        "inputs": [("✎", "手入力", "電卓で金額を入れて、資産と分類を選ぶだけ。支出・収入・振替を1画面で。"),
                   ("▣", "レシート", "日付・店名・金額・品目の読み取りを手伝います。合計1件でも、品目ごとにも保存できます。"),
                   ("★", "よく使う項目", "コーヒー・ランチ・交通費など、よく使う内容を今日の日付ですぐ呼び出せます。"),
                   ("◷", "メモ・Dデー", "その日のメモと近づく記念日を、家計簿の日付の間に一緒に表示します。")],
        "alt_guide": "入力方法の案内画面", "alt_add": "記録の入力画面",
        "receipt": None,
        "cards_k": "CARD & INSTALLMENT",
        "cards_h": "カードで<wbr>使ったお金も、<br>これから<wbr>払うお金も。",
        "cards_lead": "カード利用は購入日に支出として、カード代金の引き落としは負債の返済として記録するので、同じ支出が二重に数えられません。",
        "cards_list": [("カードの支払予定", "引き落とし日・口座・Dデーを1行で"),
                       ("自動引き落とし", "引き落とし口座と日付で自動処理"),
                       ("分割払いの管理", "元利均等・元金均等・単利の利息計算"),
                       ("繰上返済", "前払いした回までまとめて整理")],
        "alt_cards": "資産タブのカード支払予定",
        "stats_k": "STATS",
        "stats_h": "今月の流れを、<br>写真と<wbr>ひとことで。",
        "stats_lead": "統計の最初のカードが、今月の支出を先月・6か月平均と比べてひとことで伝えます。固定費・変動費、6か月の推移、分類ごとの割合と前月比まで続けて確認できます。",
        "alt_stats": "統計のまとめ画面", "alt_category": "分類別の支出画面",
        "vehicle_k": "VEHICLE LOG",
        "vehicle_h": "車にかかる<wbr>お金も、<br>家計簿の中で。",
        "vehicle_lead": "車を登録しておくと、給油・整備の支出を入力するときに走行距離・給油量・交換した項目も一緒に記録されます。燃費や維持費、次の整備時期は統計の「車両」タブでひと目で確認できます。",
        "vehicle": [("⛽", "給油も1回の入力で", "給油代を入力しながら走行距離と給油量も残せます。燃費と1kmあたりの費用は自動で計算されます。"),
                    ("⚙", "整備の交換時期", "エンジンオイル・フィルター・タイヤを距離や期間で管理し、過ぎた項目や近づく項目をお知らせします。"),
                    ("⚡", "EVも、2台目も", "ガソリン・軽油・LPG・ハイブリッド・EVに対応。車は無料で2台まで登録できます。"),
                    ("◔", "車両の統計", "今月の維持費、直近6か月の維持費と燃費のグラフ、整備項目を1画面で。")],
        "alt_vehicle": "統計の車両タブの画面", "alt_vehicle2": "車の維持費の推移と詳細記録",
        "review_k": "MONTHLY REVIEW",
        "review_h": "ひと月の数字に、<br>ストーリーを。",
        "review_lead": "収入・支出と貯蓄率、先月からの変化、固定費・変動費、カード・分割払い、資産の変化と来月の予定まで1画面で振り返れます。",
        "review_list": ["月が変わると家計簿の上にレビューが届きます",
                        "先月・直近3か月との違いをひとことで",
                        "1枚の画像として保存・共有"],
        "review_quote": "CashTory という名前のとおり、毎月の記録がひとつのお金のストーリーになるように。",
        "alt_review": "月末まとめレビュー画面",
        "assets_k": "ASSETS",
        "assets_h": "家計簿の記録が、<br>資産の流れへ。",
        "assets_lead": "口座・現金・カード・投資・ローンを1行ずつ確認し、いちばん上の3つの欄で資産・負債・純資産をすぐに把握できます。今後30日のカード代金・定期支出・定期振替は、家計簿の「今後の支払い」で日付ごとに前もって表示します。",
        "alt_assets": "資産タブの画面", "alt_upcoming": "今後の支払いの画面",
        "dday_k": "MEMO & D-DAY",
        "dday_h": "お金が<wbr>かかる日は、<br>前もって<wbr>わかるように。",
        "dday_lead": "結婚記念日・誕生日・旅行など、お金がかかる日を D デーで管理し、その日のメモも残せます。毎年・毎月の繰り返しにも対応し、家計簿の日付の間にも表示されます。",
        "alt_dday": "メモ・記念日の画面",
        "widgets_k": "WIDGETS",
        "widgets_h": "アプリを<wbr>開かなくても、<br>必要な機能は<wbr>すぐに。",
        "widgets_lead": "今月のまとめ、支出・収入のクイック入力、レシート撮影まで、6種類のウィジェット。背景の透明度もホーム画面に合わせて選べます。",
        "widgets_img": None,
        "widgets_cards": [("今月のまとめ", "今月の支出・収入をホーム画面でひと目で。"),
                          ("クイック入力", "支出・収入の入力画面をワンタップで開きます。"),
                          ("レシート撮影", "ホーム画面からすぐにレシートを撮影。")],
        "data_k": "YOUR DATA",
        "data_h": "記録は<wbr>自分で管理。",
        "data_lead": "家計簿の記録は端末に保存されます。必要なときにバックアップし、ファイルで保管し、他の家計簿アプリの記録も取り込めます。",
        "data": [("↻", "バックアップ · 復元", "バックアップファイルを書き出して、アプリの削除や機種変更に備えましょう。"),
                 ("⇩", "Excel 書き出し", "記録をファイルに書き出して、自分で確認・保管できます。"),
                 ("⇧", "他のアプリから取り込み", "他の家計簿の Excel(.xlsx)・CSV を、列の対応とプレビューを確認して取り込みます。"),
                 ("⌁", "レシートは端末で読み取り", "レシートの写真を CashTory のサーバーに送ったり保管したりしません。")],
        "personal_k": "MAKE IT YOURS",
        "personal_h": "暮らし方に<wbr>合わせて。",
        "personal": [("集計開始日", "給料日が25日なら、家計簿のひと月も25日から始められます。"),
                     ("24色のテーマカラー", "パープルからミント・コーラル・アンバーまで、好みの色に。"),
                     ("ライト · ダーク", "システム設定に合わせて快適に。"),
                     ("6言語 · 13通貨", "日本語、한국어、English、हिन्दी、Português、Bahasa Indonesia。")],
        "try_h": "インストール<wbr>する前に、<br>まず<wbr>触ってみてください。",
        "try_p": "1年分のサンプル記録が入った実際のアプリを、ブラウザですぐに試せます。入力した内容は保存されません。",
        "try_btn": "Web で体験する",
        "final_h": "毎日のお金の<wbr>ストーリーを、<br>CashTory に。",
        "final_p": "会員登録なしですぐに始められます。",
        "final_play": "Google Play でダウンロード",
        "footer": [("/", "Y&O STUDIO"), (PRIVACY, "プライバシーポリシー"), (MAIL, "お問い合わせ")],
    },
    "en": {
        "title": "CashTory — Log lightly, see your money flow at a glance",
        "desc": "From receipt scanning to cards and installments, assets, a vehicle log, a monthly review and memos & D-days. A budget app you can start without signing up.",
        "nav": [("#features", "Features"), ("#vehicle", "Vehicle log"), ("#review", "Monthly review"), ("/cashtory/demo/", "Try it")],
        "play": "Google Play",
        "hero_h1": "Log lightly.<br>See your money at a glance.",
        "hero_lead": "From receipts to cards and installments, assets, your car and a monthly review. No finance jargon — just an easy way to keep track of where your money goes.",
        "hero_play": "Get it on Google Play",
        "hero_demo": "Try it without installing",
        "hero_micro": "No sign-up · 6 languages · 13 currencies",
        "float1": ("One center button,", "four ways to add"),
        "float2": ("Memos & D-days,", "right in your ledger"),
        "alt_ledger": "CashTory ledger screen",
        "trust": [("No sign-up", "Install and start right away."),
                  ("Stored on your device", "Your records stay on your phone, not our servers."),
                  ("6 languages · 13 currencies", "English · 日本語 · 한국어 and more."),
                  ("Backup & Excel", "Your records aren't locked inside the app.")],
        "input_k": "FAST INPUT",
        "input_h": "One center button,<br>four ways to add.",
        "input_lead": "Tap the center + to type it in, or hold and slide for receipts, favorites, or a memo & D-day. After the amount, the next field opens on its own.",
        "inputs": [("✎", "Type it in", "Enter the amount on the calculator, pick an account and category, done. Expense, income and transfer on one screen."),
                   ("▣", "Receipt", "Helps read the date, store, total and items. Save it as one record or split it by item."),
                   ("★", "Favorites", "Save things you buy often — coffee, lunch, transit — and add them for today in a tap."),
                   ("◷", "Memo & D-day", "See the day's memo and upcoming anniversaries right between the dates in your ledger.")],
        "alt_guide": "Input methods guide", "alt_add": "Add record screen",
        "receipt": None,
        "cards_k": "CARD & INSTALLMENT",
        "cards_h": "Money you spent by card,<br>and money still to pay.",
        "cards_lead": "Card purchases count as spending on the day you buy; paying the card bill is a transfer that pays down the debt — so nothing gets counted twice.",
        "cards_list": [("Upcoming card bills", "Due date, paying account and D-day in one row"),
                       ("Auto-pay", "Handled by payment account and due date"),
                       ("Installments", "Equal payment, equal principal or flat interest"),
                       ("Pay off early", "Settle future installments in one go")],
        "alt_cards": "Card bills on the Assets tab",
        "stats_k": "STATS",
        "stats_h": "This month's flow,<br>in one photo and one line.",
        "stats_lead": "The first card in Stats compares this month's spending with last month and your 6-month average, and sums it up in one line. Then fixed vs. variable costs, the 6-month trend, and each category's share and change.",
        "alt_stats": "Stats summary screen", "alt_category": "Spending by category",
        "vehicle_k": "VEHICLE LOG",
        "vehicle_h": "What your car costs,<br>right in your ledger.",
        "vehicle_lead": "Add your car, and fuel and service expenses also log mileage, fuel and replaced parts. Fuel economy, running costs and the next service are all on the Vehicle tab in Stats.",
        "vehicle": [("⛽", "Fuel-ups in one entry", "Log the odometer and fuel as you record the expense. Fuel economy and cost per mile are worked out for you."),
                    ("⚙", "Service reminders", "Track oil, filters and tires by distance or time, and see what's overdue or coming up."),
                    ("⚡", "EVs and a second car", "Gas, diesel, LPG, hybrid or electric; miles and gallons or km and liters. Add up to 2 cars for free."),
                    ("◔", "Vehicle stats", "This month's running costs, 6-month cost and fuel economy charts, and maintenance items on one screen.")],
        "alt_vehicle": "Vehicle tab in Stats", "alt_vehicle2": "Vehicle running costs and details",
        "review_k": "MONTHLY REVIEW",
        "review_h": "A story behind<br>each month's numbers.",
        "review_lead": "Income, spending and savings rate, what changed since last month, fixed and variable costs, cards and installments, how your assets moved and what's coming next month — all on one screen.",
        "review_list": ["A new review waits on your ledger when the month turns",
                        "Changes vs. last month and the last 3 months, in one line",
                        "Save and share it as a single image"],
        "review_quote": "Just like the name — Cash + Story — so each month's records add up to your money story.",
        "alt_review": "Monthly review screen",
        "assets_k": "ASSETS",
        "assets_h": "From daily records<br>to the bigger picture.",
        "assets_lead": "See bank accounts, cash, cards, investments and loans one row each, with assets, debt and net worth in three boxes at the top. Card bills, recurring payments and transfers for the next 30 days are listed by date under Coming up in your ledger.",
        "alt_assets": "Assets tab", "alt_upcoming": "Coming up screen",
        "dday_k": "MEMO & D-DAY",
        "dday_h": "Know the costly days<br>before they arrive.",
        "dday_lead": "Track anniversaries, birthdays and trips as D-days, and leave a memo for any day. They can repeat yearly or monthly, and show up between the dates in your ledger.",
        "alt_dday": "Memos and anniversaries screen",
        "widgets_k": "WIDGETS",
        "widgets_h": "Without opening the app,<br>right from your home screen.",
        "widgets_lead": "Six widgets: this month's summary, quick expense and income entry, and a receipt shortcut. Set the background transparency to suit your home screen.",
        "widgets_img": None,
        "widgets_cards": [("Monthly summary", "This month's spending and income at a glance."),
                          ("Quick add", "Open expense or income entry in one tap."),
                          ("Receipt shortcut", "Snap a receipt straight from your home screen.")],
        "data_k": "YOUR DATA",
        "data_h": "Your records, your control.",
        "data_lead": "Your ledger is stored on your device. Back it up when you like, keep it as a file, and bring in records from other budget apps.",
        "data": [("↻", "Backup · Restore", "Export a backup file to be ready for reinstalling or a new phone."),
                 ("⇩", "Excel export", "Export your records to a file to check or keep."),
                 ("⇧", "Import from other apps", "Bring in Excel (.xlsx) or CSV files from other budget apps, with column mapping and a preview."),
                 ("⌁", "Receipts read on-device", "Receipt photos are never sent to or kept on CashTory servers.")],
        "personal_k": "MAKE IT YOURS",
        "personal_h": "Make it fit how you live.",
        "personal": [("Monthly period start", "Paid on the 25th? Start each budget month on the 25th."),
                     ("24 theme colors", "From purple to mint, coral and amber — pick your accent."),
                     ("Light · Dark", "Follows your system setting."),
                     ("6 languages · 13 currencies", "English, 한국어, 日本語, हिन्दी, Português, Bahasa Indonesia.")],
        "try_h": "Before you install,<br>take it for a spin.",
        "try_p": "Use the real app right in your browser, filled with a year of sample records. Nothing you enter is saved.",
        "try_btn": "Try it on the web",
        "final_h": "Start writing your<br>money story with CashTory.",
        "final_p": "No sign-up needed — start right away.",
        "final_play": "Download on Google Play",
        "footer": [("/", "Y&O STUDIO"), (PRIVACY, "Privacy Policy"), (MAIL, "Contact")],
    },
}

LANG_LABEL = {"ko": "한국어", "ja": "日本語", "en": "English"}
SWATCHES = ["#6750C7", "#2B67C2", "#117872", "#33754D", "#BA3E6E"]

CSS = """
:root{--accent:#6750C7;--accent-soft:#ECE9F7;--point:#6750C7;--point-soft:#ECE9F7;--bg:#F6F7FB;--card:#fff;--text:#1C1D22;--sub:#747783;--line:#E4E5EC;--shadow:0 18px 55px rgba(36,28,75,.09);--max:1120px}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans KR","Apple SD Gothic Neo","Hiragino Sans","Noto Sans JP",sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased}
:root:lang(ko) body{word-break:keep-all}
:root:lang(ja) :is(h1,h2,.tryBand h2){word-break:keep-all}
a{color:inherit;text-decoration:none}
img{display:block;max-width:100%;height:auto}
.wrap{width:min(calc(100% - 40px),var(--max));margin:0 auto}
.top{position:sticky;top:0;z-index:20;background:rgba(246,247,251,.88);backdrop-filter:blur(18px);border-bottom:1px solid rgba(228,229,236,.8)}
.nav{min-height:68px;display:flex;align-items:center;justify-content:space-between;gap:20px}
.brand{display:flex;align-items:center;gap:10px;font-weight:850;letter-spacing:-.03em}
.brand img{width:36px;height:36px;border-radius:11px;box-shadow:0 4px 12px rgba(28,17,71,.16)}
.navRight{display:flex;align-items:center;gap:20px}
.navlinks{display:flex;align-items:center;gap:20px;font-size:14px;color:#565965;font-weight:650}
.navlinks a:hover{color:var(--point)}
.lang{display:flex;gap:2px;padding:3px;border:1px solid var(--line);border-radius:999px;background:#fff;font-size:12px;font-weight:800}
.lang a{padding:4px 9px;border-radius:999px;color:var(--sub)}
.lang a[aria-current]{background:var(--accent);color:#fff}
.pill{white-space:nowrap;display:inline-flex;align-items:center;justify-content:center;min-height:46px;padding:0 20px;border-radius:999px;background:var(--accent);color:#fff;font-weight:800;box-shadow:0 8px 18px rgba(103,80,199,.22)}
.pill.ghost{background:#fff;color:var(--text);border:1px solid var(--line);box-shadow:none}
.pill.small{min-height:40px;padding:0 16px;font-size:14px}
.hero{padding:72px 0 64px;overflow:hidden}
.heroGrid{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center}
.eyebrow{display:inline-flex;align-items:center;gap:8px;margin-bottom:18px;font-size:13px;font-weight:800;color:var(--point);letter-spacing:.08em}
.eyebrow::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--point)}
h1{margin:0;font-size:clamp(38px,4.9vw,62px);line-height:1.08;letter-spacing:-.05em}
h2{margin:0;font-size:clamp(30px,4.2vw,48px);line-height:1.15;letter-spacing:-.045em}
.lead{margin:22px 0 0;max-width:600px;font-size:clamp(17px,2vw,20px);color:var(--sub)}
.cta{display:flex;gap:10px;flex-wrap:wrap;margin-top:30px}
.micro{margin-top:16px;font-size:13px;color:#8A8C97}
.stage{position:relative;display:grid;place-items:center;min-height:620px}
.halo{position:absolute;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,#DDD7FF 0,#EFEAFF 48%,rgba(239,234,255,0) 72%)}
.phone{position:relative;width:min(300px,78vw);border-radius:44px;background:#17181F;padding:9px;box-shadow:0 34px 80px rgba(31,25,62,.22)}
.phone img{width:100%;border-radius:36px}
.hero .phone{transform:rotate(2deg)}
.float{position:absolute;background:#fff;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);padding:11px 15px;font-size:13px;font-weight:750;line-height:1.4}
.float em{display:block;font-style:normal;color:var(--point)}
.float.one{left:0;top:110px}.float.two{right:0;bottom:110px}
.trust{padding:0 0 64px}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.trustItem{background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px}
.trustItem b{display:block;font-size:15px}.trustItem span{font-size:13px;color:var(--sub)}
section.block{padding:96px 0}
.tint{background:linear-gradient(180deg,#F0EDFB,#F7F6FC)}
.white{background:#fff}
.head{max-width:720px;margin-bottom:36px}
.kicker{margin:0 0 10px;color:var(--point);font-size:13px;font-weight:850;letter-spacing:.08em}
.sectionLead{margin:16px 0 0;color:var(--sub);font-size:17px}
.split{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.split.rev>.media{order:-1}
.media{display:flex;justify-content:center;gap:18px;flex-wrap:wrap}
.shot{margin:0;width:min(390px,100%);border-radius:24px;overflow:hidden;background:#fff;border:1px solid var(--line);box-shadow:var(--shadow)}
.shots{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start;width:min(600px,100%)}
.features{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:40px}
.feature{background:#fff;border:1px solid var(--line);border-radius:22px;padding:22px}
.featureIcon{width:42px;height:42px;border-radius:14px;background:var(--point-soft);display:grid;place-items:center;color:var(--point);font-size:19px;font-weight:900}
.feature h3{margin:18px 0 6px;font-size:19px;letter-spacing:-.03em}.feature p{margin:0;color:var(--sub);font-size:14px}
.inputMedia{display:flex;justify-content:center;gap:24px;margin-top:48px}
.inputMedia .phone{width:min(280px,44vw)}
.receipt{margin-top:56px;display:grid;grid-template-columns:.8fr 1.2fr;gap:32px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:28px;padding:24px;box-shadow:var(--shadow)}
.scrollShot{background:#15151a;border-radius:30px;padding:8px;width:min(320px,100%);height:560px;margin:0 auto;overflow:hidden}
.scrollShot img{width:100%;border-radius:23px;animation:shotScroll 12s cubic-bezier(.65,0,.35,1) infinite alternate}
@keyframes shotScroll{0%,10%{transform:translateY(0)}90%,100%{transform:translateY(calc(-100% + 544px))}}
.receipt h3{font-size:26px;letter-spacing:-.035em;margin:0 0 10px;line-height:1.3}.receipt p{margin:0;color:var(--sub)}
.note{margin-top:14px;padding:12px 14px;border-radius:14px;background:var(--point-soft);color:#5547a1;font-size:13px;font-weight:700}
.list{display:grid;gap:14px;margin-top:26px}
.listItem{display:flex;gap:12px;align-items:flex-start}
.check{flex:none;width:22px;height:22px;margin-top:2px;border-radius:50%;background:var(--point-soft);color:var(--point);display:grid;place-items:center;font-size:12px;font-weight:900}
.listItem b{display:block;font-size:15px}.listItem small{color:var(--sub);font-size:14px}
.reviewSec{padding:104px 0;background:#1C1640;color:#fff;overflow:hidden}
.reviewSec .kicker{color:#BDB3FF}.reviewSec .sectionLead{color:#C9C7D8}
.reviewSec .check{background:rgba(189,179,255,.18);color:#BDB3FF}
.reviewSec .listItem span{color:#E4E1F5}
.quote{margin-top:28px;border-left:3px solid #8B7CE0;padding-left:18px;color:#DEDBF4;font-size:15px}
.reviewPhone{width:min(290px,86vw);height:640px;margin:0 auto;background:#17181F;border-radius:44px;padding:9px;box-shadow:0 30px 80px rgba(0,0,0,.35);overflow:hidden}
.reviewScreen{height:100%;overflow:hidden;border-radius:36px;background:#f4f5f9}
.reviewScreen img{width:100%;animation:reviewScroll 16s cubic-bezier(.65,0,.35,1) infinite alternate}
@keyframes reviewScroll{0%,8%{transform:translateY(0)}92%,100%{transform:translateY(calc(-100% + 622px))}}
.widgetImg{max-width:420px;margin:0 auto;border-radius:24px;overflow:hidden}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.card{background:#fff;border:1px solid var(--line);border-radius:20px;padding:20px}
.card b{font-size:17px}.card p{margin:6px 0 0;color:var(--sub);font-size:14px}
.dataCard{display:flex;gap:14px}
.dataCard i{flex:none;font-style:normal;width:42px;height:42px;border-radius:13px;background:var(--point-soft);color:var(--point);display:grid;place-items:center;font-weight:900}
.swatches{display:flex;gap:6px;margin-top:12px}.swatches span{width:18px;height:18px;border-radius:50%}
.tryBand{background:linear-gradient(135deg,#6750C7,#4B36A8);color:#fff;border-radius:30px;padding:44px;display:grid;grid-template-columns:1fr auto;gap:28px;align-items:center}
.tryBand h2{font-size:clamp(26px,3.4vw,38px)}
.tryBand p{margin:12px 0 0;color:#E2DCFF;max-width:560px}
.tryBand .pill{background:#fff;color:var(--accent);box-shadow:none}
.centerCta{text-align:center;padding:100px 0 96px}
.centerCta p{color:var(--sub);margin:16px 0 26px}
.centerCta .cta{justify-content:center}
footer{padding:32px 0 42px;border-top:1px solid var(--line);color:#777A85;font-size:13px}
.footerRow{display:flex;justify-content:space-between;gap:22px;flex-wrap:wrap}.footerLinks{display:flex;gap:16px;flex-wrap:wrap}
@media(max-width:960px){
  .navlinks{display:none}
  .heroGrid,.split,.receipt,.tryBand{grid-template-columns:1fr}
  .split.rev>.media{order:0}
  .features{grid-template-columns:1fr 1fr}
  .grid4{grid-template-columns:1fr 1fr}
  .stage{min-height:0;padding:12px 0}
}
@media(max-width:600px){
  .wrap{width:min(calc(100% - 28px),var(--max))}
  .hero{padding-top:44px}
  .navRight{gap:10px}
  .lang a{padding:4px 7px}
  .float{display:none}
  .features,.grid4,.grid3,.grid2,.shots{grid-template-columns:1fr}
  .pill.small{min-height:36px;padding:0 12px;font-size:13px}
  .brand span{display:none}
  .inputMedia{gap:12px}
  .inputMedia .phone{width:46vw;border-radius:28px;padding:6px}
  .inputMedia .phone img{border-radius:23px}
  section.block,.reviewSec{padding:72px 0}
  .tryBand{padding:30px 24px}
}
@media(prefers-reduced-motion:reduce){.reviewScreen img,.scrollShot img{animation:none}}
"""


def webp_size(path: Path) -> tuple[int, int]:
    """Width and height of a WebP file, so <img> tags reserve the right space."""
    data = path.read_bytes()[:30]
    chunk = data[12:16]
    if chunk == b"VP8X":
        return 1 + int.from_bytes(data[24:27], "little"), 1 + int.from_bytes(data[27:30], "little")
    if chunk == b"VP8L":
        bits = struct.unpack("<I", data[21:25])[0]
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    w, h = struct.unpack("<HH", data[26:30])
    return w & 0x3FFF, h & 0x3FFF

# CashTory colours: the app icon's navy ink for buttons and dark bands, its teal ± as the point colour.
# Purple stays only inside the app screenshots (the app's default theme).
NAVY, TEAL, TEAL_TEXT = "#1B1140", "#22B39B", "#0E8C78"
PALETTE = [
    ("--accent:#6750C7;--accent-soft:#ECE9F7;--point:#6750C7;--point-soft:#ECE9F7",
     f"--accent:{NAVY};--accent-soft:#ECEAF3;--point:{TEAL_TEXT};--point-soft:#E3F4F0"),
    ("rgba(103,80,199,.22)", "rgba(27,17,64,.22)"),
    ("#DDD7FF 0,#EFEAFF 48%,rgba(239,234,255,0) 72%", "#D3EFE8 0,#EAF6F3 48%,rgba(234,246,243,0) 72%"),
    ("linear-gradient(180deg,#F0EDFB,#F7F6FC)", "linear-gradient(180deg,#EEF4F3,#F6F8F8)"),
    ("color:#5547a1;", "color:#0B6E5F;"),
    ("background:#1C1640;", f"background:{NAVY};"),
    (".reviewSec .kicker{color:#BDB3FF}", ".reviewSec .kicker{color:#5FD4BF}"),
    ("background:rgba(189,179,255,.18);color:#BDB3FF", "background:rgba(95,212,191,.16);color:#5FD4BF"),
    ("#C9C7D8", "#C8C9D3"), ("#E4E1F5", "#E6E7EE"), ("#DEDBF4", "#DFE0E8"),
    ("border-left:3px solid #8B7CE0", f"border-left:3px solid {TEAL}"),
    ("linear-gradient(135deg,#6750C7,#4B36A8)", f"linear-gradient(135deg,{NAVY},#2A1F5C)"),
    ("color:#E2DCFF;", "color:#D6D3E4;"),
    (".tryBand .pill{background:#fff;color:var(--accent);", f".tryBand .pill{{background:{TEAL};color:#0B1F1B;"),
]
PAGE_CSS = CSS
for a, b in PALETTE:
    assert a in PAGE_CSS, a
    PAGE_CSS = PAGE_CSS.replace(a, b)


def page(lang: str) -> str:
    c = COPY[lang]
    e = escape
    shot = lambda name: f"/cashtory/assets/screens/{lang}/{name}.webp"
    url = SITE + PATHS[lang]

    def img(name, alt, eager=False):
        w, h = webp_size(ROOT / shot(name).lstrip("/"))
        loading = "" if eager else ' loading="lazy" decoding="async"'
        return f'<img src="{shot(name)}" alt="{e(alt)}" width="{w}" height="{h}"{loading}>'

    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{l}" href="{SITE}{PATHS[l]}" />' for l in LANGS
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}{PATHS["ko"]}" />'
    # The demo follows the browser language unless told otherwise, so pass this page's language along.
    demo = f"/cashtory/demo/?lang={lang}"
    nav = "".join(f'<a href="{demo if h == "/cashtory/demo/" else h}">{e(t)}</a>' for h, t in c["nav"])
    langs = "".join(
        f'<a href="{PATHS[l]}" hreflang="{l}" lang="{l}"' + (' aria-current="page"' if l == lang else "")
        + f'>{l.upper()}</a>' for l in LANGS
    )
    trust = "".join(f'<div class="trustItem"><b>{e(b)}</b><span>{e(s)}</span></div>' for b, s in c["trust"])
    inputs = "".join(
        f'<article class="feature"><div class="featureIcon" aria-hidden="true">{i}</div><h3>{e(t)}</h3><p>{e(p)}</p></article>'
        for i, t, p in c["inputs"]
    )
    r = c["receipt"]
    receipt = "" if not r else f"""
        <div class="receipt">
          <div class="scrollShot"><img src="{r['img']}" alt="{e(r['alt'])}" loading="lazy" decoding="async"></div>
          <div>
            <p class="kicker">{r['k']}</p>
            <h3>{r['h']}</h3>
            <p>{e(r['p'])}</p>
            <div class="note">{e(r['note'])}</div>
          </div>
        </div>"""
    cards_list = "".join(
        f'<div class="listItem"><span class="check">✓</span><div><b>{e(b)}</b><small>{e(s)}</small></div></div>'
        for b, s in c["cards_list"]
    )
    vehicle = "".join(
        f'<article class="feature"><div class="featureIcon" aria-hidden="true">{i}</div><h3>{e(t)}</h3><p>{e(p)}</p></article>'
        for i, t, p in c["vehicle"]
    )
    review_list = "".join(
        f'<div class="listItem"><span class="check">✓</span><span>{e(t)}</span></div>' for t in c["review_list"]
    )
    if c["widgets_img"]:
        src, alt = c["widgets_img"]
        w, h = webp_size(ROOT / src.lstrip("/"))
        widgets = f'<div class="widgetImg"><img src="{src}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
    else:
        widgets = '<div class="grid3">' + "".join(
            f'<div class="card"><b>{e(b)}</b><p>{e(p)}</p></div>' for b, p in c["widgets_cards"]
        ) + "</div>"
    data = "".join(
        f'<div class="card dataCard"><i aria-hidden="true">{i}</i><div><b>{e(t)}</b><p>{e(p)}</p></div></div>'
        for i, t, p in c["data"]
    )
    swatches = '<div class="swatches">' + "".join(f'<span style="background:{s}"></span>' for s in SWATCHES) + "</div>"
    personal = "".join(
        f'<div class="card"><b>{e(t)}</b><p>{e(p)}</p>{swatches if k == 1 else ""}</div>'
        for k, (t, p) in enumerate(c["personal"])
    )
    footer = "".join(f'<a href="{h}">{e(t)}</a>' for h, t in c["footer"])

    return f"""<!doctype html>
<!-- Generated by tools/build_cashtory_pages.py — edit that file, not this one. -->
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="{NAVY}" />
  <meta name="description" content="{e(c['desc'])}" />
  <link rel="canonical" href="{url}" />
{alternates}
  <link rel="icon" href="/cashtory/assets/favicon-48.png" type="image/png" />
  <link rel="apple-touch-icon" href="/cashtory/assets/apple-touch-icon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Y&amp;O STUDIO" />
  <meta property="og:locale" content="{OG_LOCALE[lang]}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{e(c['title'])}" />
  <meta property="og:description" content="{e(c['desc'])}" />
  <meta property="og:image" content="{SITE}/cashtory/assets/og-image.jpg?v=20261017" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <title>{e(c['title'])}</title>
  <style>{PAGE_CSS}  </style>
</head>
<body>
  <header class="top">
    <div class="wrap nav">
      <a class="brand" href="{PATHS[lang]}"><img src="/cashtory/assets/app-icon.webp" alt="" width="36" height="36"><span>CashTory</span></a>
      <div class="navRight">
        <nav class="navlinks" aria-label="CashTory">{nav}</nav>
        <nav class="lang" aria-label="Language">{langs}</nav>
        <a class="pill small" href="{PLAY}">{e(c['play'])}</a>
      </div>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="wrap heroGrid">
        <div>
          <div class="eyebrow">CASH + STORY</div>
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
          <div class="phone">{img('ledger', c['alt_ledger'], eager=True)}</div>
          <div class="float one">{e(c['float1'][0])}<em>{e(c['float1'][1])}</em></div>
          <div class="float two">{e(c['float2'][0])}<em>{e(c['float2'][1])}</em></div>
        </div>
      </div>
    </section>

    <section class="trust" aria-label="CashTory">
      <div class="wrap grid4">{trust}</div>
    </section>

    <section class="block white" id="features">
      <div class="wrap">
        <div class="head">
          <p class="kicker">{c['input_k']}</p>
          <h2>{c['input_h']}</h2>
          <p class="sectionLead">{e(c['input_lead'])}</p>
        </div>
        <div class="inputMedia">
          <div class="phone">{img('guide', c['alt_guide'])}</div>
          <div class="phone">{img('add', c['alt_add'])}</div>
        </div>
        <div class="features">{inputs}</div>{receipt}
      </div>
    </section>

    <section class="block tint">
      <div class="wrap split">
        <div>
          <p class="kicker">{c['cards_k']}</p>
          <h2>{c['cards_h']}</h2>
          <p class="sectionLead">{e(c['cards_lead'])}</p>
          <div class="list">{cards_list}</div>
        </div>
        <div class="media"><figure class="shot">{img('cards', c['alt_cards'])}</figure></div>
      </div>
    </section>

    <section class="block">
      <div class="wrap split rev">
        <div>
          <p class="kicker">{c['stats_k']}</p>
          <h2>{c['stats_h']}</h2>
          <p class="sectionLead">{e(c['stats_lead'])}</p>
        </div>
        <div class="media">
          <div class="shots">
            <figure class="shot">{img('stats', c['alt_stats'])}</figure>
            <figure class="shot">{img('category', c['alt_category'])}</figure>
          </div>
        </div>
      </div>
    </section>

    <section class="block white" id="vehicle">
      <div class="wrap">
        <div class="head">
          <p class="kicker">{c['vehicle_k']}</p>
          <h2>{c['vehicle_h']}</h2>
          <p class="sectionLead">{e(c['vehicle_lead'])}</p>
        </div>
        <div class="inputMedia">
          <div class="phone">{img('vehicle', c['alt_vehicle'])}</div>
          <div class="phone">{img('vehicle2', c['alt_vehicle2'])}</div>
        </div>
        <div class="features">{vehicle}</div>
      </div>
    </section>

    <section class="reviewSec" id="review">
      <div class="wrap split">
        <div>
          <p class="kicker">{c['review_k']}</p>
          <h2>{c['review_h']}</h2>
          <p class="sectionLead">{e(c['review_lead'])}</p>
          <div class="list">{review_list}</div>
          <div class="quote">{e(c['review_quote'])}</div>
        </div>
        <div class="media">
          <div class="reviewPhone"><div class="reviewScreen">{img('review', c['alt_review'])}</div></div>
        </div>
      </div>
    </section>

    <section class="block">
      <div class="wrap split">
        <div>
          <p class="kicker">{c['assets_k']}</p>
          <h2>{c['assets_h']}</h2>
          <p class="sectionLead">{e(c['assets_lead'])}</p>
        </div>
        <div class="media">
          <div class="shots">
            <figure class="shot">{img('assets', c['alt_assets'])}</figure>
            <figure class="shot">{img('upcoming', c['alt_upcoming'])}</figure>
          </div>
        </div>
      </div>
    </section>

    <section class="block tint">
      <div class="wrap split rev">
        <div>
          <p class="kicker">{c['dday_k']}</p>
          <h2>{c['dday_h']}</h2>
          <p class="sectionLead">{e(c['dday_lead'])}</p>
        </div>
        <div class="media"><div class="phone">{img('dday', c['alt_dday'])}</div></div>
      </div>
    </section>

    <section class="block">
      <div class="wrap">
        <div class="head">
          <p class="kicker">{c['widgets_k']}</p>
          <h2>{c['widgets_h']}</h2>
          <p class="sectionLead">{e(c['widgets_lead'])}</p>
        </div>
        {widgets}
      </div>
    </section>

    <section class="block tint">
      <div class="wrap">
        <div class="head">
          <p class="kicker">{c['data_k']}</p>
          <h2>{c['data_h']}</h2>
          <p class="sectionLead">{e(c['data_lead'])}</p>
        </div>
        <div class="grid2">{data}</div>
      </div>
    </section>

    <section class="block">
      <div class="wrap">
        <div class="head">
          <p class="kicker">{c['personal_k']}</p>
          <h2>{c['personal_h']}</h2>
        </div>
        <div class="grid4">{personal}</div>
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
      <span>© 2026 Y&amp;O STUDIO · CashTory</span>
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
