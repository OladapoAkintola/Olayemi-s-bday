import streamlit as st
import streamlit.components.v1 as components
from datetime import date, datetime

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Happy Birthday, Imo! 🎂",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Constants ─────────────────────────────────────────────────────────────────
BIRTHDAY    = date(2026, 5, 19)
FIRST_NAME  = "Imo"
today       = date.today()
is_birthday = today == BIRTHDAY

# ── Streamlit chrome removal + button style ───────────────────────────────────
st.markdown(
    """
    <style>
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    section.main { background: #0b0b14 !important; }
    [data-testid="stMain"] { padding-top: 0 !important; }
    [data-testid="stSidebar"] { display: none; }
    iframe { border: none !important; display: block; }

    .stButton > button {
        background: linear-gradient(135deg, #ffd700, #ffaa00) !important;
        color: #0b0b14 !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 14px 40px !important;
        box-shadow: 0 4px 20px rgba(255,200,0,0.35) !important;
        transition: all 0.25s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 30px rgba(255,200,0,0.55) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Confetti particle HTML ────────────────────────────────────────────────────
COLORS = ["#ffd700","#ffaa00","#ff6fb0","#c084fc","#60d9fa","#ff8c69","#7effd4","#ff4da6"]
dots = ""
for i in range(40):
    col   = COLORS[i % len(COLORS)]
    size  = 6 + (i % 10)
    left  = (i * 37 + 7) % 100
    dur   = 6 + (i % 8)
    delay = round((i * 0.4) % 8, 2)
    dots += (
        f'<div class="dot" style="--col:{col};--size:{size}px;'
        f'--left:{left}%;--dur:{dur}s;--delay:{delay}s;"></div>\n'
    )

sparkles = ""
for i in range(25):
    lx     = (i * 43 + 13) % 100
    ty     = (i * 29 + 5) % 100
    dur2   = 2 + (i % 4)
    delay2 = round((i * 0.6) % 6, 2)
    sparkles += (
        f'<div class="sparkle" style="--lx:{lx}%;--ty:{ty}%;'
        f'--dur2:{dur2}s;--delay2:{delay2}s;"></div>\n'
    )

# ── Conditional sections ──────────────────────────────────────────────────────
if is_birthday:
    hero_middle = """
    <div class="today-banner">
      <h2>&#127881; TODAY IS THE DAY! &#127881;</h2>
    </div>
    """
    bottom_section = f"""
    <div class="message-card">
      <p>
        <span class="quote-mark">&ldquo;</span>
        &nbsp;May this birthday be the beginning of a year so full of laughter,
        love, and beautiful moments that you lose count of all the reasons to smile.
        Here&rsquo;s to you, <strong>{FIRST_NAME}</strong> &mdash; celebrated, cherished,
        and absolutely irreplaceable. &#x1F942;&nbsp;
        <span class="quote-mark">&rdquo;</span>
      </p>
    </div>
    <div class="ribbon">&#127873; &#x1F942; &#127800; &#127872; &#10024; &#127882; &#127926;</div>
    """
else:
    hero_middle = """
    <div class="countdown-wrap">
      <div class="countdown-box">
        <span class="countdown-number" id="cd-days">00</span>
        <span class="countdown-label">Days</span>
      </div>
      <div class="countdown-box">
        <span class="countdown-number" id="cd-hours">00</span>
        <span class="countdown-label">Hours</span>
      </div>
      <div class="countdown-box">
        <span class="countdown-number" id="cd-mins">00</span>
        <span class="countdown-label">Minutes</span>
      </div>
      <div class="countdown-box">
        <span class="countdown-number" id="cd-secs">00</span>
        <span class="countdown-label">Seconds</span>
      </div>
    </div>
    <p class="until-text">until the big day &#10024;</p>
    """
    bottom_section = """
    <div class="teaser-card">
      <p class="lock-icon">&#128274;</p>
      <p class="teaser-text">A special message is waiting&hellip;<br>
      <span>Check back on May 19th to unlock it.</span></p>
    </div>
    """

ticker_js = """
<script>
  (function () {
    var target = new Date('2026-05-19T00:00:00').getTime();

    function pad(n) {
      return String(n).padStart(2, '0');
    }

    function tick() {
      var now  = Date.now();
      var diff = Math.max(target - now, 0);

      var days  = Math.floor(diff / 86400000);
      var hours = Math.floor((diff % 86400000) / 3600000);
      var mins  = Math.floor((diff % 3600000)  / 60000);
      var secs  = Math.floor((diff % 60000)    / 1000);

      var els = {
        days:  document.getElementById('cd-days'),
        hours: document.getElementById('cd-hours'),
        mins:  document.getElementById('cd-mins'),
        secs:  document.getElementById('cd-secs'),
      };

      if (els.days)  els.days.textContent  = pad(days);
      if (els.hours) els.hours.textContent = pad(hours);
      if (els.mins)  els.mins.textContent  = pad(mins);
      if (els.secs) {
        var prev = els.secs.textContent;
        els.secs.textContent = pad(secs);
        if (prev !== pad(secs)) {
          els.secs.style.transform = 'scale(1.3)';
          els.secs.style.color     = '#ffcc00';
          setTimeout(function () {
            els.secs.style.transform = 'scale(1)';
            els.secs.style.color     = '#ffd700';
          }, 200);
        }
      }

      if (diff === 0) clearInterval(timer);
    }

    tick();
    var timer = setInterval(tick, 1000);
  })();
</script>
"""

styles = """
<style>
/* unchanged for brevity */
</style>
"""

page_html = (
    """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
"""
    + styles
    + """</head>
<body>
<div class="confetti-wrap">
"""
    + dots
    + sparkles
    + """</div>

<div class="hero">
  <span class="cake-emoji">&#127874;</span>
  <p class="main-heading">Happy Birthday,<br>"""
    + FIRST_NAME
    + """!</p>
  <p class="sub-heading">&#10022; May 19th &middot; A Day to Celebrate &#10022;</p>
  <hr class="gold-divider">
"""
    + hero_middle
    + """</div>
"""
    + bottom_section
    + """<p class="footer">Made with &#10084;&#65039; &middot; Imo Martins &middot; May 19th</p>
"""
    + (ticker_js if not is_birthday else "")
    + """</body>
</html>"""
)

st.iframe(page_html, height=820)

if is_birthday:
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("🎉 Release the Balloons!", use_container_width=True):
            st.balloons()
            st.toast(f"🎂 Happy Birthday, {FIRST_NAME}! 🎉", icon="🎈")