import json
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="tg">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ҲадисТоҷикӣ</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: #edf4ef;
    color: #183d2b;
    padding: 20px;
    margin: 0;
}
header {
    text-align: center;
    background: #155d40;
    color: white;
    padding: 25px 10px;
    border-radius: 15px;
}
.card {
    background: white;
    padding: 20px;
    margin: 18px auto;
    max-width: 600px;
    border-radius: 14px;
    box-shadow: 0 3px 12px #ccd8ce;
}
.arabic {
    font-size: 27px;
    text-align: right;
    line-height: 2;
    direction: rtl;
}
.source {
    color: #50715d;
    font-size: 14px;
}
</style>
</head>
<body>
<header>
    <h1>🕌 ҲадисТоҷикӣ</h1>
    <p>Ҳадисҳои Расулуллоҳ ﷺ бо тарҷумаи тоҷикӣ</p>
</header>

{% for h in hadislar %}
<div class="card">
    <h3>Ҳадиси {{ loop.index }}</h3>
    <p class="arabic">{{ h.arabic }}</p>
    <p>{{ h.tajik }}</p>
    <p class="source">Манбаъ: {{ h.source }}</p>
</div>
{% endfor %}

</body>
</html>
"""

@app.route("/")
def home():
    try:
        with open("hadislar.json", "r", encoding="utf-8") as f:
            hadislar = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        hadislar = []

    return render_template_string(HTML, hadislar=hadislar)

if __name__ == "__main__":
    app.run(debug=True)
