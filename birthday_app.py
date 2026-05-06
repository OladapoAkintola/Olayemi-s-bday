import streamlit as st
from datetime import date, datetime
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Happy Birthday, Olayemi! 🎂",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Constants ─────────────────────────────────────────────────────────────────
BIRTHDAY       = date(2026, 5, 11)
NAME           = "Olayemi Martins"
FIRST_NAME     = "Olayemi"
today          = date.today()
days_left      = (BIRTHDAY - today).days
is_birthday    = today == BIRTHDAY

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Lato:wght@300;400;700&display=swap');

    /* ── Reset / base ── */
    html, body, [data-testid="stAppViewContainer"] {
        background: #0b0b14 !important;
    }

    [data-testid="stMain"], section.main {
        background: transparent !important;
        padding-top: 0 !important;
    }

    /* Hide default Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none; }

    /* ── Typography ── */
    * { font-family: 'Lato', sans-serif; color: #f0e6d3; }

    /* ── Floating confetti ── */
    .confetti-wrap {
        position: fixed; top: 0; left: 0;
        width: 100vw; height: 100vh;
        pointer-events: none; z-index: 0; overflow: hidden;
    }
    .dot {
        position: absolute;
        border-radius: 50%;
        opacity: 0;
        animation: floatUp var(--dur) ease-in var(--delay) infinite;
        width: var(--size); height: var(--size);
        background: var(--col);
        left: var(--left);
    }
    @keyframes floatUp {
        0%   { transform: translateY(110vh) rotate(0deg);   opacity: 0; }
        10%  { opacity: 1; }
        90%  { opacity: 0.7; }
        100% { transform: translateY(-10vh) rotate(720deg); opacity: 0; }
    }

    /* ── Star sparkles ── */
    .sparkle {
        position: absolute;
        width: 4px; height: 4px;
        background: #ffd700;
        border-radius: 50%;
        animation: sparkle var(--dur2) ease-in-out var(--delay2) infinite;
        left: var(--lx); top: var(--ty);
        opacity: 0;
    }
    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0); }
        50%       { opacity: 1; transform: scale(3); }
    }

    /* ── Hero card ── */
    .hero {
        position: relative;
        text-align: center;
        padding: 60px 40px 50px;
        margin: 30px auto 0;
        max-width: 780px;
        background: linear-gradient(135deg, #16142a 0%, #1e1a38 50%, #16142a 100%);
        border: 1px solid rgba(255, 215, 0, 0.25);
        border-radius: 24px;
        box-shadow:
            0 0 60px rgba(255, 165, 0, 0.12),
            0 0 120px rgba(180, 0, 120, 0.08),
            inset 0 1px 0 rgba(255,255,255,0.07);
        overflow: hidden;
        z-index: 1;
    }
    .hero::before {
        content: '';
        position: absolute;
        top: -80px; left: -80px;
        width: 300px; height: 300px;
        background: radial-gradient(circle, rgba(255,180,0,0.15) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero::after {
        content: '';
        position: absolute;
        bottom: -80px; right: -80px;
        width: 280px; height: 280px;
        background: radial-gradient(circle, rgba(200,0,180,0.12) 0%, transparent 70%);
        pointer-events: none;
    }

    /* ── Cake emoji ── */
    .cake-emoji {
        font-size: 72px;
        display: block;
        margin-bottom: 10px;
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

    /* ── Main heading ── */
    .main-heading {
        font-family: 'Playfair Display', serif !important;
        font-size: clamp(2.2rem, 5vw, 3.6rem) !important;
        font-weight: 900 !important;
        color: transparent !important;
        background: linear-gradient(135deg, #ffd700 0%, #ffaa00 40%, #ff6fb0 80%, #ffd700 100%) !important;
        -webkit-background-clip: text !important;
        background-clip: text !important;
        background-size: 200% 200% !important;
        animation: shimmer 3s ease infinite !important;
        line-height: 1.15 !important;
        margin-bottom: 6px !important;
    }
    @keyframes shimmer {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* ── Sub heading ── */
    .sub-heading {
        font-family: 'Playfair Display', serif !important;
        font-size: 1.15rem !important;
        font-style: italic !important;
        color: rgba(255,220,160,0.75) !important;
        letter-spacing: 2px !important;
        margin-bottom: 0 !important;
    }

    /* ── Divider ── */
    .gold-divider {
        width: 80px;
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffd700, transparent);
        margin: 22px auto;
        border: none;
    }

    /* ── Countdown section ── */
    .countdown-wrap {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 30px 0 10px;
        flex-wrap: wrap;
    }
    .countdown-box {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,215,0,0.2);
        border-radius: 14px;
        padding: 18px 28px;
        text-align: center;
        backdrop-filter: blur(4px);
        min-width: 90px;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .countdown-box:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(255,200,0,0.2);
    }
    .countdown-number {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        font-weight: 700;
        color: #ffd700;
        display: block;
        line-height: 1;
    }
    .countdown-label {
        font-size: 0.72rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: rgba(240,230,211,0.55);
        margin-top: 5px;
        display: block;
    }

    /* ── Message card ── */
    .message-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,215,0,0.15);
        border-radius: 16px;
        padding: 28px 36px;
        margin: 24px auto 0;
        max-width: 680px;
        position: relative;
        z-index: 1;
    }
    .message-card p {
        font-size: 1.05rem;
        line-height: 1.85;
        color: rgba(240,230,211,0.88);
        text-align: center;
        margin: 0;
    }
    .message-card .quote-mark {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        color: rgba(255,215,0,0.2);
        line-height: 0.5;
        vertical-align: -0.5em;
    }

    /* ── Birthday today banner ── */
    .today-banner {
        background: linear-gradient(135deg, #ff6fb0, #ffaa00, #ffd700);
        border-radius: 16px;
        padding: 22px 32px;
        text-align: center;
        margin-bottom: 20px;
        animation: pulse 2s ease-in-out infinite;
    }
    .today-banner h2 {
        font-family: 'Playfair Display', serif !important;
        font-size: 2rem;
        font-weight: 900;
        color: #0b0b14 !important;
        margin: 0;
    }
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 20px rgba(255,180,0,0.5); }
        50%       { box-shadow: 0 0 50px rgba(255,100,180,0.7); }
    }

    /* ── Launch button ── */
    .stButton > button {
        background: linear-gradient(135deg, #ffd700, #ffaa00) !important;
        color: #0b0b14 !important;
        font-family: 'Lato', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 14px 40px !important;
        cursor: pointer !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 20px rgba(255,200,0,0.35) !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 30px rgba(255,200,0,0.55) !important;
        background: linear-gradient(135deg, #ffe44d, #ffbb22) !important;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        padding: 30px 0 20px;
        font-size: 0.78rem;
        color: rgba(240,230,211,0.3);
        letter-spacing: 1px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Confetti particles (CSS only) ─────────────────────────────────────────────
confetti_colors = [
    "#ffd700", "#ffaa00", "#ff6fb0", "#c084fc",
    "#60d9fa", "#ff8c69", "#7effd4", "#ff4da6",
]
dots_html = '<div class="confetti-wrap">'
for i in range(40):
    col   = confetti_colors[i % len(confetti_colors)]
    size  = 6 + (i % 10)
    left  = (i * 37 + 7) % 100
    dur   = 6 + (i % 8)
    delay = (i * 0.4) % 8
    dots_html += (
        f'<div class="dot" style="'
        f'--col:{col};--size:{size}px;--left:{left}%;'
        f'--dur:{dur}s;--delay:{delay}s;"></div>'
    )

# Sparkles
for i in range(25):
    lx    = (i * 43 + 13) % 100
    ty    = (i * 29 + 5)  % 100
    dur2  = 2 + (i % 4)
    delay2= (i * 0.6) % 6
    dots_html += (
        f'<div class="sparkle" style="'
        f'--lx:{lx}%;--ty:{ty}%;'
        f'--dur2:{dur2}s;--delay2:{delay2}s;"></div>'
    )
dots_html += '</div>'
st.markdown(dots_html, unsafe_allow_html=True)

# ── Compute countdown values ──────────────────────────────────────────────────
now       = datetime.now()
bday_dt   = datetime(2026, 5, 11, 0, 0, 0)
delta     = bday_dt - datetime.now()
total_sec = max(int(delta.total_seconds()), 0)
cd_days   = total_sec // 86400
cd_hours  = (total_sec % 86400) // 3600
cd_mins   = (total_sec % 3600)  // 60
cd_secs   = total_sec % 60

# ── Hero card ─────────────────────────────────────────────────────────────────
hero_html = f"""
<div class="hero">
    <span class="cake-emoji">🎂</span>
    <p class="main-heading">Happy Birthday,<br>{FIRST_NAME}!</p>
    <p class="sub-heading">✦ May 11th · A Day to Celebrate ✦</p>
    <hr class="gold-divider">
"""

if is_birthday:
    hero_html += """
    <div class="today-banner">
        <h2>🎉 TODAY IS THE DAY! 🎉</h2>
    </div>
    """
else:
    hero_html += f"""
    <div class="countdown-wrap">
        <div class="countdown-box">
            <span class="countdown-number">{cd_days:02d}</span>
            <span class="countdown-label">Days</span>
        </div>
        <div class="countdown-box">
            <span class="countdown-number">{cd_hours:02d}</span>
            <span class="countdown-label">Hours</span>
        </div>
        <div class="countdown-box">
            <span class="countdown-number">{cd_mins:02d}</span>
            <span class="countdown-label">Minutes</span>
        </div>
        <div class="countdown-box">
            <span class="countdown-number">{cd_secs:02d}</span>
            <span class="countdown-label">Seconds</span>
        </div>
    </div>
    <p style="font-size:0.85rem;color:rgba(240,230,211,0.45);letter-spacing:1px;margin-top:6px;">
        until the big day ✨
    </p>
    """

hero_html += "</div>"
st.markdown(hero_html, unsafe_allow_html=True)

# ── Message card ──────────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="message-card">
        <p>
            <span class="quote-mark">"</span>
            &nbsp;May this birthday be the beginning of a year so full of laughter,
            love, and beautiful moments that you lose count of all the reasons to smile.
            Here's to you, <strong>{FIRST_NAME}</strong> — celebrated, cherished, and
            absolutely irreplaceable. 🥂&nbsp;
            <span class="quote-mark">"</span>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Spacer + button ───────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    if is_birthday:
        label = "🎉 Release the Balloons!"
    else:
        label = "🎈 Send Early Wishes!"

    if st.button(label, use_container_width=True):
        st.balloons()
        st.toast(f"🎂 Happy Birthday, {FIRST_NAME}! 🎉", icon="🎈")

# ── Emoji ribbon ──────────────────────────────────────────────────────────────
st.markdown(
    """
    <p style="text-align:center;font-size:1.8rem;
               letter-spacing:8px;margin:30px 0 10px;opacity:0.7;">
        🎁 🥂 🌸 🎀 ✨ 🎊 🎶
    </p>
    """,
    unsafe_allow_html=True,
)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    '<p class="footer">Made with ❤️ · Olayemi Martins · May 11th</p>',
    unsafe_allow_html=True,
)
