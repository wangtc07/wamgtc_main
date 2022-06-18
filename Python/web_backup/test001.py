import requests

url = 'https://www.nogizaka46.com/s/n46/diary/MEMBER/list?ima=1735&page=0&ct=36753&cd=MEMBER'
response = requests.get(url=url)
# 設定編碼格式
response.encoding = 'UTF-8'

# 圖片
# data-src="https://www.nogizaka46.com/images/46/445/60cae08cc551e45e9d8aa008f871c.jpg"
# ->
# style="background-image: url("https://www.nogizaka46.com/images/46/445/60cae08cc551e45e9d8aa008f871c.jpg");"


# 頁面 list
# class="bl--card js-pos a--op hv--thumb"
# ->
# class="bl--card js-pos a--op hv--thumb is-v"

# 顯示
# blog 標題
# class="m--allhd js-pos js-tdg is-v"

# 大頭 right
# class="bd--prof js-pos a--op is-v"

# 日曆
# class="bd--arc js-pos a--op js-arccl is-v"

# 分頁
# class="bl--pg js-pos a--op is-v"

# footer
# class="b--ft__nv js-pos js-tdg is-v"
# class="b--ft__sns js-pos js-tdg is-v"
# class="b--ft__sub js-pos js-tdg is-v"


# js
#     <script src="/files/46/assets/js/lib.js" defer></script>
#     <script src="/files/46/assets/js/vndr2.js" defer></script>
#     <script src="/files/46/assets/js/app2.js" defer></script>

# css
# <link rel="preload" href="/files/46/assets/fonts/icons.woff2" as="font" type="font/woff2" crossorigin>
# <link rel="preload" as="style" href="/files/46/assets/css/style2.css" onload="this.onload = null; this.rel='stylesheet';">