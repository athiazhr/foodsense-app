import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="FoodSense", page_icon="🍽️", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ===== GLOBAL ===== */
html, body, [class*="css"] {
    font-family: 'Inter', 'Segoe UI', sans-serif !important;
}

/* ===== FILE UPLOADER ===== */
[data-testid="stFileUploadDropzone"] {
    background-color: #1e293b !important;
    border-color: rgba(255,255,255,0.1) !important;
}
[data-testid="stFileUploadDropzone"] * {
    color: #e2e8f0 !important;
}

/* ===== TEXT INPUT ===== */
.stTextInput input,
.stTextInput textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    background-color: #1e293b !important;
    color: #e2e8f0 !important;
    border-color: rgba(255,255,255,0.1) !important;
    caret-color: #e2e8f0 !important;
}

/* Placeholder */
.stTextInput input::placeholder {
    color: #64748b !important;
}

/* ===== FORCE DARK MODE ===== */
html, body, [data-testid="stAppViewContainer"], 
[data-testid="stMain"], .main {
    background-color: #0a1121 !important;
    color: #e2e8f0 !important;
}

[data-testid="stHeader"] {
    background-color: #0a1121 !important;
}

[data-testid="stToolbar"] {
    background-color: #0a1121 !important;
}

/* ===== FORCE ALL ELEMENTS DARK ===== */
[data-testid="stFileUploader"],
[data-testid="stFileUploadDropzone"],
.stTextInput input,
[data-testid="stSelectbox"] > div > div,
.stButton button,
[data-testid="stExpander"],
[data-testid="metric-container"] {
    background-color: #1e293b !important;
    color: #e2e8f0 !important;
    border-color: rgba(255,255,255,0.1) !important;
}

/* Button khusus */
.stButton button {
    background-color: #1e293b !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}

.stButton button:hover {
    background-color: #334155 !important;
}

/* Progress bar track */
[data-testid="stProgressBar"] {
    background-color: #1e293b !important;
}

/* Metric value & label */
[data-testid="metric-container"] label,
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #e2e8f0 !important;
}

/* ===== DATAFRAME / TABEL ===== */
[data-testid="stDataFrame"] {
    background-color: #1e293b !important;
}
[data-testid="stDataFrame"] table,
[data-testid="stDataFrame"] th,
[data-testid="stDataFrame"] td {
    background-color: #1e293b !important;
    color: #e2e8f0 !important;
}

/* ===== METRIC VALUE & LABEL ===== */
[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 2rem !important;
}
[data-testid="stMetricLabel"] {
    color: #e2e8f0 !important;
}
[data-testid="stMetricDelta"] {
    color: #94a3b8 !important;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    padding: 24px 16px;
    border-right: 1px solid rgba(255,255,255,0.06);
}
[data-testid="stSidebar"] h1 {
    color: #f1f5f9;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}
[data-testid="stSidebar"] .stButton button {
    width: 100%;
    text-align: left;
    background: transparent;
    border: none;
    border-radius: 8px;
    color: #94a3b8;
    font-size: 14px;
    font-weight: 500;
    padding: 10px 14px;
    margin-bottom: 2px;
    transition: all 0.2s ease;
}
[data-testid="stSidebar"] .stButton button:hover {
    background: rgba(255,255,255,0.07);
    color: #f1f5f9;
}

/* ===== MAIN CONTENT ===== */
.main .block-container {
    padding: 2.5rem 3rem 3rem;
    max-width: 1200px;
}

/* ===== TYPOGRAPHY ===== */
h1 { font-size: 1.9rem !important; font-weight: 700 !important; letter-spacing: -0.3px; }
h2 { font-size: 1.4rem !important; font-weight: 600 !important; }
h3 { font-size: 1.1rem !important; font-weight: 600 !important; }

/* ===== METRIC CARDS ===== */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 16px 20px;
    transition: border-color 0.2s;
}
[data-testid="metric-container"]:hover {
    border-color: rgba(255,255,255,0.15);
}

/* ===== EXPANDER ===== */
[data-testid="stExpander"] {
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 14px !important;
    background: rgba(255,255,255,0.02) !important;
    margin-bottom: 8px !important;
}
[data-testid="stExpander"]:hover {
    border-color: rgba(255,255,255,0.13) !important;
}

/* ===== BUTTONS ===== */
.stButton button {
    border-radius: 10px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    transition: all 0.2s ease !important;
}

/* ===== INPUT ===== */
[data-testid="stTextInput"] input {
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    background: rgba(255,255,255,0.04) !important;
    font-size: 14px !important;
    padding: 10px 14px !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}

/* ===== SELECT BOX ===== */
[data-testid="stSelectbox"] > div > div {
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    background: rgba(255,255,255,0.04) !important;
}

/* ===== ALERT / INFO ===== */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    border: none !important;
}

/* ===== FILE UPLOADER ===== */
[data-testid="stFileUploader"] {
    border-radius: 14px !important;
}

/* ===== DATAFRAME ===== */
[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden;
}

/* ===== PROGRESS BAR ===== */
[data-testid="stProgressBar"] > div > div {
    border-radius: 99px !important;
}

/* ===== DIVIDER ===== */
hr {
    border-color: rgba(255,255,255,0.06) !important;
    margin: 1.5rem 0 !important;
}

/* ===== SECTION HEADER ===== */
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}

/* ===== STAT CARD ===== */
.stat-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    transition: all 0.2s;
}
.stat-card:hover {
    border-color: rgba(255,255,255,0.15);
    background: rgba(255,255,255,0.05);
}

/* ===== HERO BANNER ===== */
.hero-banner {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 40px 48px;
    margin-bottom: 32px;
}

/* ===== RESTAURANT CARD ===== */
.resto-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 12px;
    transition: all 0.2s;
}
.resto-card:hover {
    border-color: rgba(255,255,255,0.15);
    background: rgba(255,255,255,0.05);
}

/* ===== TAG PILL ===== */
.tag-pill {
    display: inline-block;
    background: rgba(99,102,241,0.15);
    color: #818cf8;
    border-radius: 99px;
    padding: 3px 12px;
    font-size: 12px;
    font-weight: 500;
    margin: 2px;
}
</style>
""", unsafe_allow_html=True)

# ================= SESSION STATE =================
if "menu" not in st.session_state:
    st.session_state.menu = "Home"
if "df" not in st.session_state:
    st.session_state.df = None
if "kota_pilih" not in st.session_state:
    st.session_state.kota_pilih = None

if st.session_state.df is None:
    try:
        st.session_state.df = pd.read_csv("data_clean_restaurant.csv")
    except:
        pass

# ================= LOGO MAP =================
LOGO_MAP = {
    "Unagi Kurofune Indonesia": "logos/unagi.jpg",
    "Bobby\u2019s Burgers": "logos/bobys.jpg",
    "Mil Toast House": "logos/miltoast.jpg",
    "Little Olie": "logos/littleolie.jpg",
    "Lawless Burgerbar": "logos/lawlessburger.jpeg",
    "Sushi Maru": "logos/sushimaru.png",
    "海底捞火锅 Haidilao Hot Pot": "logos/haidilao.jpg",
    "Dream Dates Artisan Bakery & Restaurant": "logos/dreamdates.png",
    "Osteria Gia": "logos/osteriagia.jpg",
    "Little Red Dot": "logos/littlereddot.png",
    "Five Monkeys Burger": "logos/fivemonkeys.jpg",
    "Potteria": "logos/potteria.jpg",
    "Gabon African": "logos/gabon.png",
    "Chikuro": "logos/chikuro.png",
    "UNION": "logos/union.png",
    "Kappa Sushi": "logos/kappasushi.jpg",
    "Iga Panggang Panglima BBQ Ribs": "logos/igapanggang.jpg",
    "Paris Baguette": "logos/parisbaguette.png",
    "Nasi Goreng Kambing Kebon Sirih": "logos/nasigoreng.png",
    "Mie Gacoan": "logos/miegacoan.png",
    "Meatguy Steakhouse SCBD": "logos/meatguy.png",
    "Sate Taichan Bang Yoyo": "logos/taichan.jpg",
    "Sec Bowl": "logos/secbowl.png",
    "Sànùk Thai Boat Noodle": "logos/sanuk.jpg",
    "Obihiro Nikudon": "logos/obihiro.jpg",
}

# ================= KATEGORI MAP =================
KATEGORI_MAP = {
    "Unagi Kurofune Indonesia": ["japanese", "jepang", "unagi", "belut", "seafood", "laut", "fine dining", "mewah"],
    "Bobby\u2019s Burgers": ["burger", "american", "amerika", "fast food", "makanan cepat saji", "sandwich", "beef", "daging"],
    "Mil Toast House": ["pastry", "dessert", "kue", "cafe", "kafe", "toast", "roti", "western", "barat", "brunch", "sarapan", "coffee", "kopi", "manis", "sweet"],
    "Little Olie": ["chicken", "ayam", "chicken tender", "goreng", "renyah", "fast food", "makanan cepat saji", "murah", "viral", "nasi", "terjangkau", "semanggi", "alam sutera", "estetik"],
    "Lawless Burgerbar": ["burger", "american", "amerika", "bbq", "bakar", "beef", "daging", "fast food", "makanan cepat saji", "bar"],
    "Sushi Maru": ["japanese", "jepang", "sushi", "seafood", "laut", "salmon", "tuna", "maki", "nigiri", "mentai", "roll"],
    "海底捞火锅 Haidilao Hot Pot": ["hotpot", "hot pot", "shabu", "chinese", "china", "cina", "steamboat", "kuah", "sup", "soup", "pedas", "spicy", "mewah", "ramai"],
    "Dream Dates Artisan Bakery & Restaurant": ["bakery", "bakeri", "pastry", "dessert", "kue", "roti", "cafe", "kafe", "manis", "sweet", "brunch", "sarapan", "coffee", "kopi", "romantis"],
    "Osteria Gia": ["italian", "italia", "pasta", "pizza", "western", "barat", "fine dining", "mewah", "romantis", "steak"],
    "Little Red Dot": ["singaporean", "singapura", "asian", "asia", "cafe", "kafe", "fusion", "western", "barat", "nasi", "mie"],
    "Five Monkeys Burger": ["burger", "american", "amerika", "beef", "daging", "fast food", "makanan cepat saji", "cheese", "keju"],
    "Potteria": ["japanese", "jepang", "donburi", "rice bowl", "nasi", "ayam", "chicken", "asian", "asia", "murah", "enak"],
    "Gabon African": ["african", "afrika", "fusion", "unik", "eksotis", "berbeda", "daging", "meat", "spicy", "pedas"],
    "Chikuro": ["japanese", "jepang", "chicken", "ayam", "karaage", "goreng", "asian", "asia", "nasi", "rice"],
    "UNION": ["western", "barat", "cafe", "kafe", "brunch", "sarapan", "coffee", "kopi", "steak", "pasta", "santai", "hangout", "nongkrong"],
    "Kappa Sushi": ["japanese", "jepang", "sushi", "seafood", "laut", "salmon", "maki", "roll", "mentai", "conveyor", "murah"],
    "Iga Panggang Panglima BBQ Ribs": ["bbq", "bakar", "ribs", "iga", "indonesian", "indonesia", "daging", "meat", "beef", "sapi", "kambing", "smoky"],
    "Paris Baguette": ["bakery", "bakeri", "pastry", "dessert", "kue", "roti", "cafe", "kafe", "korean", "korea", "manis", "sweet", "coffee", "kopi", "croissant"],
    "Nasi Goreng Kambing Kebon Sirih": ["indonesian", "indonesia", "nasi goreng", "nasi", "kambing", "goat", "street food", "makanan jalanan", "lokal", "murah", "enak"],
    "Mie Gacoan": ["indonesian", "indonesia", "mie", "noodle", "mie ayam", "pedas", "spicy", "street food", "makanan jalanan", "lokal", "murah", "viral"],
    "Meatguy Steakhouse SCBD": ["steak", "western", "barat", "beef", "daging", "sapi", "fine dining", "mewah", "american", "amerika", "bbq", "bakar"],
    "Sate Taichan Bang Yoyo": ["sate", "indonesian", "indonesia", "street food", "makanan jalanan", "pedas", "spicy", "ayam", "chicken", "lokal", "murah", "viral"],
    "Sec Bowl": ["bowl", "rice bowl", "nasi", "ayam", "chicken", "salted egg", "telur asin", "indonesian", "indonesia", "lokal", "pedas", "spicy", "fast food", "makanan cepat saji", "kung pao", "mongolian", "sambalado", "blackpepper", "lada hitam", "murah", "viral"],
    "Sànùk Thai Boat Noodle": ["thai", "thailand", "noodle", "mie", "soup", "sup", "kuah", "asian", "asia", "pedas", "spicy", "seafood", "laut"],
    "Obihiro Nikudon": ["japanese", "jepang", "beef", "daging", "sapi", "donburi", "rice bowl", "nasi", "asian", "asia", "nikudon"],
}

import base64

def get_logo(brand_name):
    path = LOGO_MAP.get(brand_name)
    if path and os.path.exists(path):
        return path
    return None

import base64

def get_logo_base64(brand_name):
    path = LOGO_MAP.get(brand_name)
    if path and os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        ext = path.split(".")[-1].replace("jpg", "jpeg")
        return f"data:image/{ext};base64,{data}"
    return None

# ================= SPEEDOMETER =================
def render_speedometer(final_score, rating_score, avg_sentiment, volume_score, THRESHOLD=0.9):
    if final_score >= THRESHOLD:
        kategori_label = "Berkualitas Baik"
        kategori_color = "#22c55e"
        needle_color = "#22c55e"
    else:
        kategori_label = "FOMO-driven"
        kategori_color = "#ef4444"
        needle_color = "#ef4444"

    spd_html = f"""
<div style="font-family:'Inter','Segoe UI',sans-serif; display:flex; flex-direction:column; align-items:center; padding:16px;">
  <p style="margin:0 0 8px; font-size:11px; color:#64748b; font-weight:600; letter-spacing:1.5px; text-transform:uppercase;">Skor Kategorisasi</p>
  <div style="position:relative; width:300px; height:165px; overflow:hidden;">
    <canvas id="speedoCanvas" width="300" height="165" style="display:block;"></canvas>
    <div id="needleWrap" style="position:absolute; left:150px; top:150px; width:0; height:0; transform-origin:0px 0px; transform:rotate(-90deg);">
      <svg style="position:absolute; left:-2px; top:-120px;" width="4" height="120" overflow="visible">
        <line x1="2" y1="120" x2="2" y2="10" stroke="{needle_color}" stroke-width="3" stroke-linecap="round"/>
        <polygon points="2,2 -3,16 7,16" fill="{needle_color}"/>
      </svg>
      <div style="position:absolute; left:-8px; top:-8px; width:16px; height:16px; border-radius:50%; background:{needle_color}; border:2px solid white; box-shadow:0 0 6px rgba(0,0,0,0.4);"></div>
    </div>
  </div>
  <div style="width:300px; display:flex; justify-content:space-between; margin-top:-6px; padding:0 8px;">
    <span style="font-size:11px; font-weight:700; color:#ef4444;">FOMO</span>
    <span style="font-size:11px; font-weight:700; color:#22c55e;">Berkualitas Baik</span>
  </div>
  <div style="margin-top:20px; text-align:center;">
    <p style="margin:0; font-size:52px; font-weight:800; color:{kategori_color}; line-height:1; letter-spacing:-2px;">{final_score:.2f}</p>
    <p style="margin:8px 0 2px; font-size:15px; font-weight:600; color:{kategori_color};">{kategori_label}</p>
    <p style="margin:0; font-size:11px; color:#64748b;">Threshold ≥ {THRESHOLD} = Berkualitas Baik &nbsp;·&nbsp; &lt; {THRESHOLD} = FOMO</p>
  </div>
  <div style="margin-top:16px; display:flex; gap:20px; font-size:11px; color:#94a3b8; background:rgba(255,255,255,0.04); border-radius:10px; padding:10px 20px;">
    <span>Rating <b style="color:#e2e8f0;">{rating_score:.2f}</b> · 30%</span>
    <span>Sentimen <b style="color:#e2e8f0;">{avg_sentiment:.2f}</b> · 30%</span>
    <span>Volume <b style="color:#e2e8f0;">{volume_score:.2f}</b> · 40%</span>
  </div>
</div>
<script>
(function() {{
  var canvas = document.getElementById('speedoCanvas');
  var ctx = canvas.getContext('2d');
  var cx = 150, cy = 150, r = 130, thickness = 32;
  var THRESHOLD = {THRESHOLD};
  var splitAngle = (1 - THRESHOLD) * Math.PI;

  ctx.beginPath(); ctx.arc(cx, cy, r-thickness/2, splitAngle, Math.PI, false);
  ctx.lineWidth = thickness; ctx.strokeStyle = '#fca5a5'; ctx.lineCap = 'butt'; ctx.stroke();

  ctx.beginPath(); ctx.arc(cx, cy, r-thickness/2, 0, splitAngle, false);
  ctx.lineWidth = thickness; ctx.strokeStyle = '#86efac'; ctx.lineCap = 'butt'; ctx.stroke();

  ctx.beginPath(); ctx.arc(cx-(r-thickness/2), cy, thickness/2, 0, Math.PI*2);
  ctx.fillStyle='#fca5a5'; ctx.fill();
  ctx.beginPath(); ctx.arc(cx+(r-thickness/2), cy, thickness/2, 0, Math.PI*2);
  ctx.fillStyle='#86efac'; ctx.fill();

  var iR=r-thickness-4, oR=r+4;
  var tx1=cx+iR*Math.cos(splitAngle), ty1=cy-iR*Math.sin(splitAngle);
  var tx2=cx+oR*Math.cos(splitAngle), ty2=cy-oR*Math.sin(splitAngle);
  ctx.beginPath(); ctx.moveTo(tx1,ty1); ctx.lineTo(tx2,ty2);
  ctx.strokeStyle='rgba(255,255,255,0.8)'; ctx.lineWidth=2.5; ctx.stroke();

  [{{'v':'0','a':Math.PI}},{{'v':'0.5','a':Math.PI/2}},{{'v':'1.0','a':0}}].forEach(function(t){{
    ctx.beginPath();
    ctx.moveTo(cx+(r-thickness-4)*Math.cos(t.a), cy-(r-thickness-4)*Math.sin(t.a));
    ctx.lineTo(cx+(r+3)*Math.cos(t.a), cy-(r+3)*Math.sin(t.a));
    ctx.strokeStyle='rgba(255,255,255,0.3)'; ctx.lineWidth=1.5; ctx.stroke();
    ctx.font='bold 8px Inter'; ctx.fillStyle='rgba(255,255,255,0.4)'; ctx.textAlign='center';
    ctx.fillText(t.v, cx+(r+14)*Math.cos(t.a), cy-(r+14)*Math.sin(t.a)+3);
  }});

  var targetDeg = -90 + ({final_score} * 180);
  var needle = document.getElementById('needleWrap');
  needle.style.transition = 'none';
  needle.style.transform = 'rotate(-90deg)';
  setTimeout(function(){{
    needle.style.transition = 'transform 1.4s cubic-bezier(0.34,1.56,0.64,1)';
    needle.style.transform = 'rotate('+targetDeg+'deg)';
  }}, 300);
}})();
</script>"""
    return spd_html

# ================= DETAIL RESTORAN =================
def show_detail_restoran(brand_name, df):
    import matplotlib.pyplot as plt
    import re
    from datetime import datetime, timedelta
    import numpy as np

    brand_df = df[df["brand_name"] == brand_name]
    if brand_df.empty:
        st.warning("Data restoran tidak ditemukan.")
        return

    # ---- HEADER ----
    logo_path = get_logo(brand_name)
    h1, h2 = st.columns([1, 4])
    with h1:
        if logo_path:
            st.image(logo_path, width=130)
        else:
            st.markdown("<div style='width:130px;height:90px;background:rgba(255,255,255,0.06);border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:44px;'>🍽️</div>", unsafe_allow_html=True)
    with h2:
        st.markdown(f"<h1 style='margin:0;padding:0;'>{brand_name}</h1>", unsafe_allow_html=True)
        kota_col = "Kota" if "Kota" in brand_df.columns else ("City" if "City" in brand_df.columns else None)
        if kota_col:
            kota_list = brand_df[kota_col].unique()
            st.caption(f"📍 {', '.join(kota_list)}")
        cabang_list = brand_df["branch_name"].unique()
        st.markdown(f"<p style='color:#94a3b8;font-size:13px;margin-top:4px;'>📌 {len(cabang_list)} cabang: {' · '.join(cabang_list)}</p>", unsafe_allow_html=True)

    avg_rating = brand_df["rating"].mean()
    total_reviews = len(brand_df)
    positif_pct = round(len(brand_df[brand_df["rating"] >= 4]) / total_reviews * 100)
    negatif_pct = round(len(brand_df[brand_df["rating"] <= 2]) / total_reviews * 100)
    netral_pct = 100 - positif_pct - negatif_pct

    st.markdown("---")

    # ---- STATS ROW ----
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.metric("Rating Rata-rata", f"⭐ {avg_rating:.2f}")
    with s2:
        st.metric("Total Review", f"{total_reviews:,}")
    with s3:
        st.metric("Jumlah Cabang", brand_df["branch_name"].nunique())
    with s4:
        st.metric("Sentimen Positif", f"{positif_pct}%")

    st.markdown("---")

    # ---- SENTIMEN + CHART ----
    col_sent, col_chart = st.columns([1, 2])

    with col_sent:
        st.markdown("**Analisis Sentimen**")
        st.markdown(f"""
        <div style='margin-top:12px;'>
          <div style='display:flex;justify-content:space-between;margin-bottom:4px;'>
            <span style='font-size:13px;color:#86efac;font-weight:500;'>Positif</span>
            <span style='font-size:13px;font-weight:600;'>{positif_pct}%</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(positif_pct / 100)
        st.markdown(f"""
        <div style='margin-top:8px;'>
          <div style='display:flex;justify-content:space-between;margin-bottom:4px;'>
            <span style='font-size:13px;color:#fca5a5;font-weight:500;'>Negatif</span>
            <span style='font-size:13px;font-weight:600;'>{negatif_pct}%</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(negatif_pct / 100)
        st.markdown(f"""
        <div style='margin-top:8px;'>
          <div style='display:flex;justify-content:space-between;margin-bottom:4px;'>
            <span style='font-size:13px;color:#fde68a;font-weight:500;'>Netral</span>
            <span style='font-size:13px;font-weight:600;'>{netral_pct}%</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(netral_pct / 100)

    with col_chart:
        st.markdown("**Distribusi Rating**")
        rating_counts = brand_df["rating"].value_counts().sort_index()
        colors_bar = ["#fca5a5","#fdba74","#fde68a","#86efac","#4ade80"]
        bar_colors = [colors_bar[int(r)-1] for r in rating_counts.index if 1 <= int(r) <= 5]
        fig_bar, ax_bar = plt.subplots(figsize=(5, 2.8))
        fig_bar.patch.set_alpha(0)
        ax_bar.set_facecolor('none')
        bars = ax_bar.bar(rating_counts.index, rating_counts.values, color=bar_colors, width=0.6, edgecolor='none')
        ax_bar.set_xlabel("Rating", fontsize=9, color='#94a3b8')
        ax_bar.set_ylabel("Jumlah Review", fontsize=9, color='#94a3b8')
        ax_bar.tick_params(colors='#94a3b8', labelsize=8)
        ax_bar.spines['top'].set_visible(False)
        ax_bar.spines['right'].set_visible(False)
        ax_bar.spines['left'].set_color('#334155')
        ax_bar.spines['bottom'].set_color('#334155')
        for bar, val in zip(bars, rating_counts.values):
            ax_bar.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                        str(val), ha='center', va='bottom', fontsize=8, color='#e2e8f0')
        fig_bar.tight_layout()
        st.pyplot(fig_bar)

    # ---- TREND ----
    st.markdown("---")
    st.markdown("**📈 Trend Review per Bulan**")

    def parse_relative_date(date_str):
        if not isinstance(date_str, str): return None
        s = date_str.lower().replace("edited ", "").strip()
        now = datetime(2025, 4, 1)
        try:
            if "hour" in s: return now
            elif s in ("a day ago","1 day ago"): return now - __import__('datetime').timedelta(days=1)
            elif "day" in s: return now - __import__('datetime').timedelta(days=int(re.search(r'(\d+)', s).group(1)))
            elif s in ("a week ago","1 week ago"): return now - __import__('datetime').timedelta(weeks=1)
            elif "week" in s: return now - __import__('datetime').timedelta(weeks=int(re.search(r'(\d+)', s).group(1)))
            elif s in ("a month ago","1 month ago"): return now - __import__('datetime').timedelta(days=30)
            elif "month" in s: return now - __import__('datetime').timedelta(days=30*int(re.search(r'(\d+)', s).group(1)))
            elif s in ("a year ago","1 year ago"): return now - __import__('datetime').timedelta(days=365)
            elif "year" in s: return now - __import__('datetime').timedelta(days=365*int(re.search(r'(\d+)', s).group(1)))
        except: return None
        return None

    brand_df2 = brand_df.copy()
    if "review_date_converted" in brand_df2.columns:
        try: brand_df2["parsed_date"] = pd.to_datetime(brand_df2["review_date_converted"], errors="coerce")
        except: brand_df2["parsed_date"] = brand_df2["review_date"].apply(parse_relative_date)
    else:
        brand_df2["parsed_date"] = brand_df2["review_date"].apply(parse_relative_date)
    brand_df2 = brand_df2.dropna(subset=["parsed_date"])

    if not brand_df2.empty:
        brand_df2["bulan"] = brand_df2["parsed_date"].dt.to_period("M")
        trend = (brand_df2.groupby("bulan")
                 .agg(jumlah_review=("rating","count"), avg_rating=("rating","mean"))
                 .reset_index().sort_values("bulan").tail(12))
        trend["bulan_str"] = trend["bulan"].astype(str)

        col_chart1, col_chart2 = st.columns(2)

        # ---- CHART 1: Jumlah Review per Bulan ----
        with col_chart1:
            st.markdown("<p style='font-size:13px;color:#94a3b8;margin-bottom:6px;'>Jumlah Review per Bulan</p>", unsafe_allow_html=True)
            fig1, ax1 = plt.subplots(figsize=(5, 3))
            fig1.patch.set_alpha(0)
            ax1.set_facecolor('none')
            bars = ax1.bar(trend["bulan_str"], trend["jumlah_review"],
                           color="#818cf8", alpha=0.6, width=0.6, edgecolor='none')
            ax1.set_ylabel("Jumlah Review", fontsize=8, color="#94a3b8")
            ax1.set_ylim(0, trend["jumlah_review"].max() * 1.3)
            ax1.tick_params(axis='y', labelcolor="#94a3b8", labelsize=7)
            ax1.tick_params(axis='x', labelsize=7, rotation=30)
            ax1.spines['top'].set_visible(False)
            ax1.spines['right'].set_visible(False)
            ax1.spines['left'].set_color('#334155')
            ax1.spines['bottom'].set_color('#334155')
            ax1.tick_params(colors='#94a3b8')
            for bar, val in zip(bars, trend["jumlah_review"]):
                ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                         str(val), ha='center', va='bottom', fontsize=6, color='#e2e8f0')
            fig1.tight_layout()
            st.pyplot(fig1)

        # ---- CHART 2: Avg Rating per Bulan ----
        with col_chart2:
            st.markdown("<p style='font-size:13px;color:#94a3b8;margin-bottom:6px;'>Rata-rata Rating per Bulan</p>", unsafe_allow_html=True)
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            fig2.patch.set_alpha(0)
            ax2.set_facecolor('none')
            ax2.plot(trend["bulan_str"], trend["avg_rating"],
                     color="#fb923c", marker="o", linewidth=2, markersize=5)
            ax2.fill_between(trend["bulan_str"], trend["avg_rating"],
                             alpha=0.1, color="#fb923c")
            ax2.set_ylabel("Avg Rating", fontsize=8, color="#94a3b8")
            ax2.set_ylim(0, 5.5)
            ax2.tick_params(axis='y', labelcolor="#94a3b8", labelsize=7)
            ax2.tick_params(axis='x', labelsize=7, rotation=30)
            ax2.spines['top'].set_visible(False)
            ax2.spines['right'].set_visible(False)
            ax2.spines['left'].set_color('#334155')
            ax2.spines['bottom'].set_color('#334155')
            ax2.tick_params(colors='#94a3b8')
            for x, y in zip(range(len(trend)), trend["avg_rating"]):
                ax2.annotate(f"{y:.1f}", (trend["bulan_str"].iloc[x], y),
                             textcoords="offset points", xytext=(0, 7),
                             ha='center', fontsize=6, color="#fb923c", fontweight='bold')
            fig2.tight_layout()
            st.pyplot(fig2)
    else:
        st.info("Data tanggal tidak cukup.")

    # ---- SPEEDOMETER ----
    st.markdown("---")
    st.markdown("**🎯 Kategorisasi Restoran**")

    w_rating, w_sentiment, w_volume = 0.3, 0.3, 0.4
    MAX_REVIEWS, THRESHOLD = 100, 0.9
    sentiment_mapping = {"positive": 1.0, "neutral": 0.5, "negative": 0.0}
    brand_df_calc = brand_df.copy()
    brand_df_calc["sentiment_score"] = brand_df_calc["sentiment"].str.lower().map(sentiment_mapping).fillna(0.5)
    brand_df_calc["rating_score_col"] = brand_df_calc["rating"] / 5.0

    cabang_agg = brand_df_calc.groupby("branch_name").agg(
        rating_score=("rating_score_col","mean"),
        avg_sentiment=("sentiment_score","mean"),
        n_reviews=("rating","count")
    ).reset_index()
    cabang_agg["volume_score"] = (cabang_agg["n_reviews"] / MAX_REVIEWS).clip(0, 1)
    cabang_agg["final_score"] = (w_rating * cabang_agg["rating_score"] +
                                  w_sentiment * cabang_agg["avg_sentiment"] +
                                  w_volume * cabang_agg["volume_score"])
    final_score = (cabang_agg["final_score"] * cabang_agg["n_reviews"]).sum() / cabang_agg["n_reviews"].sum()
    rating_score = brand_df_calc["rating_score_col"].mean()
    avg_sentiment_val = brand_df_calc["sentiment_score"].mean()
    volume_score = min(total_reviews / MAX_REVIEWS, 1.0)

    import streamlit.components.v1 as components
    components.html(render_speedometer(final_score, rating_score, avg_sentiment_val, volume_score, THRESHOLD), height=360)

    with st.expander("ℹ️ Cara membaca skor ini"):
        st.markdown(f"""
| Faktor | Bobot | Nilai |
|--------|-------|-------|
| Rating (avg ÷ 5) | 30% | `{rating_score:.3f}` |
| Sentimen (dari data NLP) | 30% | `{avg_sentiment_val:.3f}` |
| Volume review (per cabang ÷ 100) | 40% | `{volume_score:.3f}` |
| **Skor Akhir** | | **`{final_score:.3f}`** |

**Berkualitas Baik** ≥ 0.90 → Restoran konsisten dan terpercaya ✅  
**FOMO-driven** < 0.90 → Mungkin viral, tapi konsistensinya perlu dicek ⚠️
        """)

    # ---- SAMPLE REVIEW ----
    st.markdown("---")
    st.markdown("**💬 Sample Review**")
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("<p style='color:#86efac;font-weight:600;font-size:13px;'>Review Positif</p>", unsafe_allow_html=True)
        for _, row in brand_df[brand_df["rating"] >= 4].head(3).iterrows():
            st.markdown(f"""<div style='background:rgba(134,239,172,0.05);border-left:3px solid #86efac;border-radius:0 8px 8px 0;padding:10px 14px;margin-bottom:8px;font-size:13px;color:#e2e8f0;'>
                ⭐ {row['rating']} — {str(row['review_text'])[:160]}...
                <br><span style='font-size:11px;color:#64748b;'>{row['review_date']}</span>
            </div>""", unsafe_allow_html=True)
    with r2:
        st.markdown("<p style='color:#fca5a5;font-weight:600;font-size:13px;'>Review Negatif</p>", unsafe_allow_html=True)
        neg = brand_df[brand_df["rating"] <= 2].head(3)
        if neg.empty:
            st.info("Tidak ada review negatif.")
        else:
            for _, row in neg.iterrows():
                st.markdown(f"""<div style='background:rgba(252,165,165,0.05);border-left:3px solid #fca5a5;border-radius:0 8px 8px 0;padding:10px 14px;margin-bottom:8px;font-size:13px;color:#e2e8f0;'>
                    ⭐ {row['rating']} — {str(row['review_text'])[:160]}...
                    <br><span style='font-size:11px;color:#64748b;'>{row['review_date']}</span>
                </div>""", unsafe_allow_html=True)

    # ===== WORD CLOUD =====
    st.markdown("---")
    st.markdown("**☁️ Word Cloud Review**")
    
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    
    all_text = " ".join(brand_df["review_text"].dropna().astype(str).tolist())
    
    if all_text.strip():
        wc = WordCloud(
            width=800, height=300,
            background_color=None, mode="RGBA",
            colormap="coolwarm",
            max_words=80,
            stopwords={"the","a","an","and","or","is","it","in","on","at","to","of",
                       "was","were","i","my","we","our","this","that","for","with",
                       "have","has","had","be","are","not","but","so","very","yg",
                       "yang","di","dan","ke","nya","itu","ini","dengan","untuk",
                       "ada","tidak","tapi","juga","sudah","saya","kami","kita",
                       "mereka","dari","lebih","bisa","saja","aja","banget","kalo",
                       "kalau","karena","si","ga","gak","nya","ku","mu"},
            prefer_horizontal=0.85,
            min_font_size=10,
        ).generate(all_text)

        fig_wc, ax_wc = plt.subplots(figsize=(10, 3.5))
        fig_wc.patch.set_alpha(0)
        ax_wc.imshow(wc, interpolation="bilinear")
        ax_wc.axis("off")
        fig_wc.tight_layout(pad=0)
        st.pyplot(fig_wc)
    else:
        st.info("Tidak ada teks review.")

    # ===== RESTORAN SERUPA =====
    st.markdown("---")
    st.markdown("**🍽️ Restoran Serupa**")
    st.markdown("<p style='color:#64748b;font-size:13px;margin-top:-8px;margin-bottom:16px;'>Restoran lain dengan kategori makanan yang sama</p>", unsafe_allow_html=True)

    # Cari kategori brand ini
    current_tags = set(KATEGORI_MAP.get(brand_name, []))
    
    # Hitung similarity dengan restoran lain
    similar = []
    for other_brand, other_tags in KATEGORI_MAP.items():
        if other_brand == brand_name:
            continue
        # Hitung jumlah tag yang sama
        overlap = len(current_tags & set(other_tags))
        if overlap > 0:
            other_df = df[df["brand_name"] == other_brand]
            if not other_df.empty:
                similar.append({
                    "brand": other_brand,
                    "overlap": overlap,
                    "avg_rating": other_df["rating"].mean(),
                    "total_reviews": len(other_df),
                })

    # Sort by overlap terbanyak, ambil top 3
    similar = sorted(similar, key=lambda x: (x["overlap"], x["avg_rating"]), reverse=True)[:3]

    if similar:
        sim_cols = st.columns(3)
        for i, resto in enumerate(similar):
            with sim_cols[i]:
                logo_path = get_logo(resto["brand"])
                # Tags yang sama
                shared_tags = current_tags & set(KATEGORI_MAP.get(resto["brand"], []))
                tag_display = list(shared_tags)[:3]

                st.markdown(f"""
                <div style='background:rgba(255,255,255,0.03);border:none;
                            border-radius:14px;padding:16px;text-align:center;'>
                """, unsafe_allow_html=True)
                if logo_path:
                    st.image(logo_path, width=60)
                else:
                    st.markdown("<p style='font-size:32px;margin:0;'>🍽️</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-weight:700;font-size:13px;margin:8px 0 4px;'>{resto['brand'][:25]}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color:#94a3b8;font-size:12px;margin:0;'>⭐ {resto['avg_rating']:.1f} · {resto['total_reviews']:,} review</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color:#818cf8;font-size:11px;margin:6px 0 0;'>{' · '.join(tag_display)}</p>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

                if st.button(f"Lihat →", key=f"sim_{brand_name}_{resto['brand']}"):
                    st.session_state.kategori_pilih = resto["brand"]
                    st.rerun()
    else:
        st.info("Tidak ada restoran serupa.")

# ================= SIDEBAR =================
st.sidebar.markdown("""
<div style='text-align:center; margin-bottom:15px; margin-top:-70px;'>
    <p style='font-size:40px; margin:0;'>🍽️</p>
    <h1 style='margin:-19px 0 0; font-size:18px;'>FoodSense</h1>
</div>
""", unsafe_allow_html=True)

menu_items = [("🏠", "Home"), ("🔍", "Search"), ("🏪", "Categories"), ("📍", "City")]
for icon, label in menu_items:
    disabled = label in ["Categories", "City"] and st.session_state.df is None
    if disabled:
        st.sidebar.markdown(f"<div style='padding:10px 14px;color:#475569;font-size:14px;cursor:not-allowed;'>🔒 {label}</div>", unsafe_allow_html=True)
    else:
        if st.sidebar.button(f"{icon}  {label}", key=f"nav_{label}"):
            st.session_state.menu = label
            if label == "Categories" and "kategori_pilih" in st.session_state:
                del st.session_state.kategori_pilih
            if label == "City":
                st.session_state.kota_pilih = None

st.sidebar.markdown("---")
if st.session_state.df is not None:
    st.sidebar.markdown(f"""
    <div style='background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.2);border-radius:10px;padding:12px 14px;'>
        <p style='margin:0;font-size:12px;color:#86efac;font-weight:600;'>✅ Data Termuat</p>
        <p style='margin:4px 0 0;font-size:13px;color:#e2e8f0;font-weight:500;'>{len(st.session_state.df):,} review</p>
        <p style='margin:2px 0 0;font-size:11px;color:#64748b;'>{st.session_state.df['brand_name'].nunique()} restoran</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.sidebar.markdown("""
    <div style='background:rgba(251,191,36,0.08);border:1px solid rgba(251,191,36,0.15);border-radius:10px;padding:12px 14px;'>
        <p style='margin:0;font-size:12px;color:#fbbf24;font-weight:600;'>⚠️ Belum ada data</p>
        <p style='margin:4px 0 0;font-size:11px;color:#64748b;'>Upload CSV di menu Search</p>
    </div>
    """, unsafe_allow_html=True)

menu = st.session_state.menu

# ================= HOME =================
if menu == "Home":
    st.markdown("""
    <div class="hero-banner">
        <h1 style='margin:0;font-size:2.2rem;color:#f1f5f9;'>Analisis Sentimen Restoran 🍽️</h1>
        <p style='margin:10px 0 0;color:#94a3b8;font-size:15px;max-width:600px;'>
            Temukan restoran terbaik di Jakarta berdasarkan analisis sentimen review Google Maps secara mendalam.
        </p>
        <div style='margin-top:20px;display:flex;gap:12px;flex-wrap:wrap;'>
            <span class='tag-pill'>📊 Analisis Sentimen</span>
            <span class='tag-pill'>🏆 Leaderboard</span>
            <span class='tag-pill'>📍 Filter per Kota</span>
            <span class='tag-pill'>🎯 Kategorisasi FOMO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.df is not None:
        df = st.session_state.df
        brands_summary = (df.groupby("brand_name")
                          .agg(avg_rating=("rating","mean"), total_reviews=("rating","count"))
                          .reset_index())
        positif_counts = df[df["rating"] >= 4].groupby("brand_name").size().reset_index(name="positif")
        brands_summary = brands_summary.merge(positif_counts, on="brand_name", how="left").fillna(0)
        brands_summary["sentimen_pct"] = (brands_summary["positif"] / brands_summary["total_reviews"] * 100).round(0).astype(int)
        top5 = brands_summary.sort_values("avg_rating", ascending=False).head(5).reset_index(drop=True)

        # Stats overview
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Total Restoran", df["brand_name"].nunique())
        with c2:
            st.metric("Total Review", f"{len(df):,}")
        with c3:
            st.metric("Rata-rata Rating", f"⭐ {df['rating'].mean():.2f}")

        st.markdown("---")
        st.markdown("### 🏆 Leaderboard")
        st.markdown("<p style='color:#64748b;font-size:13px;margin-top:-10px;margin-bottom:20px;'>Trending berdasarkan rating tertinggi</p>", unsafe_allow_html=True)

        rank1, rank2 = top5.iloc[0], top5.iloc[1] if len(top5) > 1 else None
        rank3 = top5.iloc[2] if len(top5) > 2 else None

        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if rank2 is not None:
                logo2 = get_logo_base64(rank2['brand_name'])
                img2 = f"<img src='{logo2}' style='width:55px;height:55px;object-fit:contain;border-radius:8px;margin-bottom:6px;'>" if logo2 else "<p style='font-size:30px;margin:0;'>🥈</p>"
                st.markdown(f"""
                <div style='text-align:center;padding:20px 16px;border-radius:16px;
                            background:linear-gradient(135deg,#dce8f0,#c8dce8);min-height:200px;'>
                    {img2}
                    <p style='margin:4px 0;font-size:20px;'>🥈</p>
                    <p style='margin:6px 0 2px;color:#1a1a1a;font-weight:700;font-size:13px;'>{rank2['brand_name'][:22]}</p>
                    <p style='margin:0;color:#1a1a1a;font-size:13px;'>⭐ {rank2['avg_rating']:.2f}</p>
                    <p style='margin:2px 0 0;color:#374151;font-size:12px;'>Positif: {rank2['sentimen_pct']}%</p>
                </div>""", unsafe_allow_html=True)

        with col2:
            logo1 = get_logo_base64(rank1['brand_name'])
            img1 = f"<img src='{logo1}' style='width:65px;height:65px;object-fit:contain;border-radius:8px;margin-bottom:6px;'>" if logo1 else "<p style='font-size:38px;margin:0;'>🥇</p>"
            st.markdown(f"""
            <div style='text-align:center;padding:20px 16px;border-radius:16px;
                        background:linear-gradient(135deg,#f5e6c8,#e8d0a0);min-height:200px;'>
                {img1}
                <p style='margin:4px 0;font-size:26px;'>🥇</p>
                <p style='margin:6px 0 2px;color:#1a1a1a;font-weight:700;font-size:15px;'>{rank1['brand_name'][:22]}</p>
                <p style='margin:0;color:#1a1a1a;font-size:14px;'>⭐ {rank1['avg_rating']:.2f}</p>
                <p style='margin:2px 0 0;color:#374151;font-size:13px;'>Positif: {rank1['sentimen_pct']}%</p>
            </div>""", unsafe_allow_html=True)

        with col3:
            if rank3 is not None:
                logo3 = get_logo_base64(rank3['brand_name'])
                img3 = f"<img src='{logo3}' style='width:55px;height:55px;object-fit:contain;border-radius:8px;margin-bottom:6px;'>" if logo3 else "<p style='font-size:30px;margin:0;'>🥉</p>"
                st.markdown(f"""
                <div style='text-align:center;padding:20px 16px;border-radius:16px;
                            background:linear-gradient(135deg,#e8d8c8,#d4c0a8);min-height:200px;'>
                    {img3}
                    <p style='margin:4px 0;font-size:20px;'>🥉</p>
                    <p style='margin:6px 0 2px;color:#1a1a1a;font-weight:700;font-size:13px;'>{rank3['brand_name'][:22]}</p>
                    <p style='margin:0;color:#1a1a1a;font-size:13px;'>⭐ {rank3['avg_rating']:.2f}</p>
                    <p style='margin:2px 0 0;color:#374151;font-size:12px;'>Positif: {rank3['sentimen_pct']}%</p>
                </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**📊 Ranking Lengkap**")
        ranking_df = top5.copy()
        ranking_df.index = ranking_df.index + 1
        ranking_df.index.name = "Rank"
        st.dataframe(
            ranking_df[["brand_name","avg_rating","total_reviews","sentimen_pct"]].rename(columns={
                "brand_name":"Nama Restoran","avg_rating":"Rating Rata-rata",
                "total_reviews":"Total Review","sentimen_pct":"Sentimen Positif (%)"}),
            use_container_width=True, height=210)
    else:
        st.markdown("""
        <div style='text-align:center;padding:60px 20px;background:rgba(255,255,255,0.02);border:1px dashed rgba(255,255,255,0.1);border-radius:16px;'>
            <p style='font-size:48px;margin:0;'>📂</p>
            <p style='margin:12px 0 4px;font-size:16px;font-weight:600;color:#e2e8f0;'>Belum ada data</p>
            <p style='margin:0;font-size:13px;color:#64748b;'>Upload file CSV di menu <b>Search</b> untuk mulai melihat analisis</p>
        </div>
        """, unsafe_allow_html=True)

# ================= SEARCH =================
if menu == "Search":
    st.markdown("<h1>🔍 Search Restoran</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;margin-top:-8px;margin-bottom:24px;'>Cari restoran berdasarkan nama, kategori, atau jenis makanan</p>", unsafe_allow_html=True)

    # Upload area
    st.markdown("**Upload Data**")
    uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"],
        help="Kolom yang dibutuhkan: brand_name, branch_name, rating, review_text, review_date, sentiment")
    if uploaded_file is not None:
        try:
            df_upload = pd.read_csv(uploaded_file)
            required_cols = {"brand_name","branch_name","rating","review_text","review_date"}
            if not required_cols.issubset(df_upload.columns):
                st.error(f"❌ Kolom tidak sesuai. Dibutuhkan: {', '.join(required_cols)}")
            else:
                st.session_state.df = df_upload
                st.success(f"✅ Berhasil! **{len(df_upload):,}** review dari **{df_upload['brand_name'].nunique()}** restoran.")
                st.rerun()
        except Exception as e:
            st.error(f"❌ Gagal membaca file: {e}")

    if st.session_state.df is not None:
        df = st.session_state.df
        st.markdown("---")

        col_q, col_r = st.columns([3, 1])
        with col_q:
            query = st.text_input("", placeholder="Cari: nama restoran, japanese, burger, pedas, murah...",
                                  label_visibility="collapsed")
        with col_r:
            min_rating = st.selectbox("Min. Rating", [1,2,3,4,5], index=2)

        df_filtered = df[df["rating"] >= min_rating]
        brands = []
        if query.strip():
            q = query.lower()
            matched_by_kategori = [b for b,tags in KATEGORI_MAP.items() if any(q in tag for tag in tags)]
            df_filtered = df_filtered[
                df_filtered["brand_name"].str.contains(query, case=False, na=False) |
                df_filtered["branch_name"].str.contains(query, case=False, na=False) |
                df_filtered["brand_name"].isin(matched_by_kategori)
            ]
            brands = (df_filtered.groupby("brand_name")["rating"].mean()
                      .sort_values(ascending=False).index.tolist())

        if not query.strip():
            st.markdown("""
            <div style='text-align:center;padding:40px;color:#64748b;'>
                <p style='font-size:32px;margin:0;'>🔍</p>
                <p style='margin:8px 0 0;font-size:14px;'>Ketik nama atau kategori restoran untuk mulai pencarian</p>
                <p style='margin:4px 0 0;font-size:12px;'>Contoh: "japanese", "burger", "pedas", "murah"</p>
            </div>""", unsafe_allow_html=True)
        elif len(brands) == 0:
            st.info("Tidak ada restoran yang cocok dengan pencarian kamu.")
        else:
            st.markdown(f"<p style='color:#64748b;font-size:13px;'>{len(brands)} restoran ditemukan</p>", unsafe_allow_html=True)
            for brand in brands:
                brand_df = df_filtered[df_filtered["brand_name"] == brand]
                avg_rating = brand_df["rating"].mean()
                total_reviews = len(brand_df)
                positif_pct = round(len(brand_df[brand_df["rating"] >= 4]) / total_reviews * 100)
                negatif_pct = round(len(brand_df[brand_df["rating"] <= 2]) / total_reviews * 100)
                netral_pct = 100 - positif_pct - negatif_pct

                with st.expander(f"**{brand}**  ·  ⭐ {avg_rating:.1f}  ·  {total_reviews:,} review"):
                    logo_path = get_logo(brand)
                    ea, eb = st.columns([2, 1])
                    with ea:
                        if logo_path:
                            st.image(logo_path, width=70)
                        st.markdown("**Analisis Sentimen**")
                        st.markdown(f"Positif: **{positif_pct}%**")
                        st.progress(positif_pct / 100)
                        st.markdown(f"Negatif: **{negatif_pct}%**")
                        st.progress(negatif_pct / 100)
                        st.markdown(f"Netral: **{netral_pct}%**")
                        st.progress(netral_pct / 100)
                    with eb:
                        st.metric("Rating", f"⭐ {avg_rating:.1f}")
                        st.metric("Review", f"{total_reviews:,}")
                        st.metric("Cabang", brand_df["branch_name"].nunique())
                    st.markdown("---")
                    if st.button(f"Lihat Detail Lengkap →", key=f"detail_{brand}"):
                        st.session_state.kategori_pilih = brand
                        st.session_state.menu = "Categories"
                        st.rerun()
    else:
        st.info("⬆️ Upload data CSV di atas untuk mulai pencarian.")

# ================= CATEGORIES =================
if menu == "Categories":
    if st.session_state.df is None:
        st.warning("⚠️ Data belum diupload.")
        if st.button("→ Pergi ke Search"):
            st.session_state.menu = "Search"
            st.rerun()
    else:
        df = st.session_state.df
        brands_summary = (df.groupby("brand_name")
                          .agg(avg_rating=("rating","mean"), total_reviews=("rating","count"))
                          .reset_index().sort_values("avg_rating", ascending=False))
        positif_counts = df[df["rating"] >= 4].groupby("brand_name").size().reset_index(name="positif")
        brands_summary = brands_summary.merge(positif_counts, on="brand_name", how="left").fillna(0)
        brands_summary["sentimen_pct"] = (brands_summary["positif"] / brands_summary["total_reviews"] * 100).round(0).astype(int)

        if "kategori_pilih" not in st.session_state or st.session_state.kategori_pilih is None:
            st.markdown("<h1>🏪 Kategori Restoran</h1>", unsafe_allow_html=True)
            st.markdown("<p style='color:#64748b;margin-top:-8px;margin-bottom:24px;'>Pilih restoran untuk melihat analisis lengkap</p>", unsafe_allow_html=True)

            cols = st.columns(3)
            for i, row in enumerate(brands_summary.itertuples()):
                with cols[i % 3]:
                    logo_path = get_logo(row.brand_name)
                    st.markdown(f"""
                    <div style='background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);
                                border-radius:14px;padding:14px;margin-bottom:12px;'>
                        <div style='display:flex;align-items:center;gap:10px;margin-bottom:8px;'>
                            <span style='font-size:12px;color:#64748b;'>⭐ {row.avg_rating:.1f} · {row.total_reviews:,} review</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    if logo_path:
                        st.image(logo_path, width=50)
                    if st.button(row.brand_name[:28], key=f"btn_{row.brand_name}", use_container_width=True):
                        st.session_state.kategori_pilih = row.brand_name
                        st.rerun()
        else:
            if st.button("← Kembali ke Daftar"):
                st.session_state.kategori_pilih = None
                st.rerun()
            st.markdown("---")
            show_detail_restoran(st.session_state.kategori_pilih, df)

# ================= CITY =================
if menu == "City":
    if st.session_state.df is None:
        st.warning("⚠️ Data belum diupload.")
        if st.button("→ Pergi ke Search"):
            st.session_state.menu = "Search"
            st.rerun()
    else:
        df = st.session_state.df
        st.markdown("<h1>📍 Restoran Berdasarkan Kota</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#64748b;margin-top:-8px;margin-bottom:24px;'>Jelajahi restoran berdasarkan wilayah Jakarta</p>", unsafe_allow_html=True)

        kota_col = next((c for c in df.columns if c.lower() in ["kota","city","wilayah"]), None)

        if kota_col is None:
            st.warning("Kolom 'Kota' tidak ditemukan.")
        else:
            kota_list = sorted(df[kota_col].dropna().unique())
            kota_cols = st.columns(len(kota_list))
            for i, kota in enumerate(kota_list):
                with kota_cols[i]:
                    if st.button(kota, key=f"kota_{kota}", use_container_width=True):
                        st.session_state.kota_pilih = kota

            st.markdown("---")

            if st.session_state.kota_pilih:
                kota = st.session_state.kota_pilih
                df_kota = df[df[kota_col] == kota]

                st.markdown(f"### 📍 {kota}")
                k1, k2, k3 = st.columns(3)
                with k1: st.metric("Restoran", df_kota["brand_name"].nunique())
                with k2: st.metric("Total Review", f"{len(df_kota):,}")
                with k3: st.metric("Avg Rating", f"⭐ {df_kota['rating'].mean():.2f}")

                st.markdown("---")

                kota_brands = (df_kota.groupby("brand_name")
                               .agg(avg_rating=("rating","mean"), total_reviews=("rating","count"))
                               .reset_index().sort_values("avg_rating", ascending=False))
                pos_kota = df_kota[df_kota["rating"] >= 4].groupby("brand_name").size().reset_index(name="positif")
                kota_brands = kota_brands.merge(pos_kota, on="brand_name", how="left").fillna(0)
                kota_brands["sentimen_pct"] = (kota_brands["positif"] / kota_brands["total_reviews"] * 100).round(0).astype(int)

                cols = st.columns(3)
                for i, (_, brand_row) in enumerate(kota_brands.iterrows()):
                    with cols[i % 3]:
                        brand_name = brand_row["brand_name"]
                        logo_path = get_logo(brand_name)
                        st.markdown(f"""
                        <div style='background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);
                                    border-radius:14px;padding:16px;margin-bottom:12px;'>
                        """, unsafe_allow_html=True)
                        if logo_path:
                            st.image(logo_path, width=70)
                        else:
                            st.markdown("🍽️")
                        st.markdown(f"**{brand_name}**")
                        st.markdown(f"<p style='color:#94a3b8;font-size:13px;margin:2px 0;'>⭐ {brand_row['avg_rating']:.1f} &nbsp;·&nbsp; {int(brand_row['total_reviews'])} review</p>", unsafe_allow_html=True)
                        st.markdown(f"<p style='color:#86efac;font-size:12px;margin:2px 0;'>Positif: {brand_row['sentimen_pct']}%</p>", unsafe_allow_html=True)
                        branches = df_kota[df_kota["brand_name"] == brand_name]["branch_name"].unique()
                        with st.expander(f"📌 {len(branches)} cabang"):
                            for b in branches:
                                st.write(f"• {b}")
                        st.markdown("</div>", unsafe_allow_html=True)

                st.markdown("---")
                st.markdown(f"**📊 Ranking di {kota}**")
                display_df = kota_brands[["brand_name","avg_rating","total_reviews","sentimen_pct"]].copy()
                display_df.columns = ["Nama Restoran","Rating Rata-rata","Total Review","Sentimen Positif (%)"]
                display_df.index = range(1, len(display_df)+1)
                display_df.index.name = "Rank"
                st.dataframe(display_df, use_container_width=True, height=210)
            else:
                st.markdown("""
                <div style='text-align:center;padding:50px;color:#64748b;'>
                    <p style='font-size:36px;margin:0;'>🗺️</p>
                    <p style='margin:12px 0 0;font-size:14px;'>Pilih wilayah Jakarta di atas</p>
                </div>""", unsafe_allow_html=True)
