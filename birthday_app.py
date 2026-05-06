import streamlit as st
import streamlit.components.v1 as components
from datetime import date, datetime

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Happy Birthday, Olayemi! 🎂",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Constants ─────────────────────────────────────────────────────────────────
BIRTHDAY    = date(2026, 5, 11)
FIRST_NAME  = "Olayemi"
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
    # Countdown numbers start at 00 — JS fills them in immediately on load
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
      <span>Check back on May 11th to unlock it.</span></p>
    </div>
    """

# ── JS ticker — plain string, NOT inside the f-string below ──────────────────
# Kept separate to avoid Python f-string brace conflicts with JS { } syntax.
ticker_js = """
<script>
  (function () {
    var target = new Date('2026-05-11T00:00:00').getTime();

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

# ── CSS ───────────────────────────────────────────────────────────────────────
styles = """
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0b0b14;
    font-family: 'Lato', sans-serif;
    color: #f0e6d3;
    overflow-x: hidden;
    padding: 20px 16px 30px;
  }

  .confetti-wrap {
    position: fixed; inset: 0;
    pointer-events: none; z-index: 0; overflow: hidden;
  }
  .dot {
    position: absolute; border-radius: 50%; opacity: 0;
    animation: floatUp var(--dur) ease-in var(--delay) infinite;
    width: var(--size); height: var(--size);
    background: var(--col); left: var(--left); bottom: -10%;
  }
  @keyframes floatUp {
    0%   { transform: translateY(0) rotate(0deg);       opacity: 0; }
    10%  { opacity: 1; }
    90%  { opacity: 0.7; }
    100% { transform: translateY(-110vh) rotate(720deg); opacity: 0; }
  }
  .sparkle {
    position: absolute; width: 4px; height: 4px;
    background: #ffd700; border-radius: 50%;
    animation: twinkle var(--dur2) ease-in-out var(--delay2) infinite;
    left: var(--lx); top: var(--ty); opacity: 0;
  }
  @keyframes twinkle {
    0%, 100% { opacity: 0; transform: scale(0); }
    50%       { opacity: 1; transform: scale(3); }
  }

  .hero {
    position: relative; text-align: center;
    padding: 56px 36px 44px; max-width: 760px; margin: 0 auto;
    background: linear-gradient(135deg, #16142a 0%, #1e1a38 50%, #16142a 100%);
    border: 1px solid rgba(255,215,0,0.25); border-radius: 24px;
    box-shadow: 0 0 60px rgba(255,165,0,0.12), 0 0 120px rgba(180,0,120,0.08),
                inset 0 1px 0 rgba(255,255,255,0.07);
    overflow: hidden; z-index: 1;
  }
  .hero::before {
    content: ''; position: absolute; top: -80px; left: -80px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(255,180,0,0.15) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero::after {
    content: ''; position: absolute; bottom: -80px; right: -80px;
    width: 280px; height: 280px;
    background: radial-gradient(circle, rgba(200,0,180,0.12) 0%, transparent 70%);
    pointer-events: none;
  }

  .cake-emoji {
    font-size: 68px; display: block; margin-bottom: 12px;
    animation: bounceIn 0.8s cubic-bezier(0.36, 0.07, 0.19, 0.97) both,
               float 3s ease-in-out 0.8s infinite;
  }
  @keyframes bounceIn {
    0%   { transform: scale(0) rotate(-10deg); opacity: 0; }
    60%  { transform: scale(1.15) rotate(4deg); }
    80%  { transform: scale(0.95) rotate(-2deg); }
    100% { transform: scale(1) rotate(0deg); opacity: 1; }
  }
  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-10px); }
  }

  .main-heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 6vw, 3.4rem); font-weight: 900;
    background: linear-gradient(135deg, #ffd700 0%, #ffaa00 40%, #ff6fb0 80%, #ffd700 100%);
    -webkit-background-clip: text; background-clip: text; color: transparent;
    background-size: 200% 200%; animation: shimmer 3s ease infinite;
    line-height: 1.2; margin-bottom: 8px;
  }
  @keyframes shimmer {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  .sub-heading {
    font-family: 'Playfair Display', serif; font-size: 1.05rem;
    font-style: italic; color: rgba(255,220,160,0.7); letter-spacing: 2px;
  }

  hr.gold-divider {
    width: 80px; height: 2px;
    background: linear-gradient(90deg, transparent, #ffd700, transparent);
    border: none; margin: 22px auto;
  }

  .countdown-wrap {
    display: flex; justify-content: center;
    gap: 16px; margin: 28px 0 10px; flex-wrap: wrap;
  }
  .countdown-box {
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,215,0,0.2);
    border-radius: 14px; padding: 16px 22px; text-align: center; min-width: 76px;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .countdown-box:hover {
    transform: translateY(-4px); box-shadow: 0 8px 30px rgba(255,200,0,0.2);
  }
  .countdown-number {
    font-family: 'Playfair Display', serif; font-size: 2.4rem; font-weight: 700;
    color: #ffd700; display: block; line-height: 1;
    transition: transform 0.2s ease, color 0.2s ease;
  }
  .countdown-label {
    font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase;
    color: rgba(240,230,211,0.5); margin-top: 5px; display: block;
  }
  .until-text {
    font-size: 0.82rem; color: rgba(240,230,211,0.4);
    letter-spacing: 1px; margin-top: 8px;
  }

  .today-banner {
    background: linear-gradient(135deg, #ff6fb0, #ffaa00, #ffd700);
    border-radius: 16px; padding: 20px 28px; text-align: center;
    margin: 24px 0 8px; animation: pulse 2s ease-in-out infinite;
  }
  .today-banner h2 {
    font-family: 'Playfair Display', serif; font-size: 1.9rem;
    font-weight: 900; color: #0b0b14;
  }
  @keyframes pulse {
    0%, 100% { box-shadow: 0 0 20px rgba(255,180,0,0.5); }
    50%       { box-shadow: 0 0 50px rgba(255,100,180,0.7); }
  }

  .message-card {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,215,0,0.15);
    border-radius: 16px; padding: 28px 32px; margin: 20px auto 0;
    max-width: 760px; position: relative; z-index: 1;
  }
  .message-card p {
    font-size: 1.02rem; line-height: 1.85;
    color: rgba(240,230,211,0.88); text-align: center;
  }
  .quote-mark {
    font-family: 'Playfair Display', serif; font-size: 3.5rem;
    color: rgba(255,215,0,0.2); line-height: 0.5; vertical-align: -0.45em;
  }

  .teaser-card {
    background: rgba(255,255,255,0.03); border: 1px dashed rgba(255,215,0,0.2);
    border-radius: 16px; padding: 32px 28px; margin: 20px auto 0;
    max-width: 760px; text-align: center; z-index: 1; position: relative;
  }
  .lock-icon {
    font-size: 2.4rem; margin-bottom: 12px; opacity: 0.5;
    animation: sway 3s ease-in-out infinite;
  }
  @keyframes sway {
    0%, 100% { transform: rotate(-8deg); }
    50%       { transform: rotate(8deg); }
  }
  .teaser-text {
    font-size: 0.95rem; color: rgba(240,230,211,0.45);
    line-height: 1.8; letter-spacing: 0.5px;
  }
  .teaser-text span { color: rgba(255,215,0,0.45); font-style: italic; font-size: 0.88rem; }

  .ribbon {
    text-align: center; font-size: 1.7rem;
    letter-spacing: 8px; margin: 24px 0 10px; opacity: 0.65;
  }
  .footer {
    text-align: center; font-size: 0.75rem;
    color: rgba(240,230,211,0.28); letter-spacing: 1px; padding-top: 10px;
  }
</style>
"""

# ── Assemble full HTML — JS concatenated as plain string, not inside f-string ─
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
  <p class="sub-heading">&#10022; May 11th &middot; A Day to Celebrate &#10022;</p>
  <hr class="gold-divider">
"""
    + hero_middle
    + """</div>
"""
    + bottom_section
    + """<p class="footer">Made with &#10084;&#65039; &middot; Olayemi Martins &middot; May 11th</p>
"""
    + (ticker_js if not is_birthday else "")
    + """</body>
</html>"""
)

# ── Render ────────────────────────────────────────────────────────────────────
components.html(page_html, height=820, scrolling=False)

# ── Balloon button — only shown on the birthday ───────────────────────────────
if is_birthday:
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("🎉 Release the Balloons!", use_container_width=True):
            st.balloons()
            st.toast(f"🎂 Happy Birthday, {FIRST_NAME}! 🎉", icon="🎈")
