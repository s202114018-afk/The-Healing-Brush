import streamlit as st
import urllib.parse

# ==========================================
# 1. PAGE SETUP & CONFIDENT DARK THEME
# ==========================================
st.set_page_config(
    page_title="The Healing Brush - CASWCMC", 
    page_icon="🎨", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Premium CSS for Hackathon Standout UI
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #e0e0e0; font-family: 'Urbanist', Arial, sans-serif; }
    .title-text { font-weight: 700; color: #ffffff; text-align: center; margin-bottom: 5px; }
    .quote-text { font-style: italic; color: #deff9a; text-align: center; margin-bottom: 25px; font-size: 1.1rem; }
    .school-tag { text-align: center; color: #888888; font-size: 0.85rem; margin-top: -15px; margin-bottom: 30px; }
    .stProgress > div > div > div > div { background-color: #deff9a; }
    .custom-card {
        background-color: #141414; padding: 25px; border-radius: 16px; 
        border: 1px solid #262626; box-shadow: 0 4px 12px rgba(0,0,0,0.5); margin-bottom: 25px;
    }
    .accent-header { color: #deff9a; font-weight: 700; margin-top: 0; margin-bottom: 15px; font-size: 1.2rem; }
    .stButton>button {
        background-color: #1a1a1a; color: #deff9a; border: 1px solid #deff9a; 
        border-radius: 12px; padding: 12px 24px; font-weight: 600; width: 100%; transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #deff9a; color: #000000;
        box-shadow: 0 0 15px rgba(222, 255, 154, 0.6); transform: translateY(-2px);
    }
    .feedback-box {
        background-color: #0f1410; border-left: 4px solid #deff9a;
        padding: 15px 20px; border-radius: 0 12px 12px 0; margin: 20px 0;
    }
    .feedback-title { color: #deff9a; font-weight: bold; margin-bottom: 5px; font-size: 0.95rem; }
    .crisis-box { background-color: #1c1010; border: 1px solid #ff4b4b; padding: 15px; border-radius: 12px; margin-top: 30px; }
    </style>
""", unsafe_allow_html=True)

# 2. INITIALIZE THERAPEUTIC STATES
if "step" not in st.session_state: st.session_state.step = 1
if "emotion_label" not in st.session_state: st.session_state.emotion_label = ""
if "emotion_prompt" not in st.session_state: st.session_state.emotion_prompt = ""
if "metaphor_label" not in st.session_state: st.session_state.metaphor_label = ""
if "metaphor_prompt" not in st.session_state: st.session_state.metaphor_prompt = ""
if "hope_label" not in st.session_state: st.session_state.hope_label = ""
if "hope_prompt" not in st.session_state: st.session_state.hope_prompt = ""

# App Header Layout
st.markdown("<h1 class='title-text'>🎨 The Healing Brush</h1>", unsafe_allow_html=True)
st.markdown("<p class='quote-text'>\"When language reaches its limit, art begins to speak.\" — Paolo Knill</p>", unsafe_allow_html=True)
st.markdown("<p class='school-tag'>Christian Alliance SW Chan Memorial College | AI x HK OpenCup 2026</p>", unsafe_allow_html=True)

# Progress Indicator
progress_map = {1: 15, 2: 45, 3: 75, 4: 100}
st.progress(progress_map[st.session_state.step])
st.write("")

# STEP 1: EMOTIONAL EXTERNALIZATION
if st.session_state.step == 1:
    st.markdown("""
    <div class='custom-card'>
        <p class='accent-header'>Step 1: Emotional Externalization</p>
        <p>Many times, the heavy weight inside is hard to put into perfect words. Follow your intuition and tap an emotion button that closest represents your current state:</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("😫 Stressed / Anxious"):
            st.session_state.emotion_label = "Stressed"
            st.session_state.emotion_prompt = "overwhelming stress, heavy anxiety, suffocation, chaotic mind"
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("😔 Depressed / Lonely"):
            st.session_state.emotion_label = "Depressed"
            st.session_state.emotion_prompt = "deep depression, lonely sadness, empty chest, cold isolation"
            st.session_state.step = 2
            st.rerun()
    with col3:
        if st.button("😤 Angry / Frustrated"):
            st.session_state.emotion_label = "Angry"
            st.session_state.emotion_prompt = "burning anger, inner chaos, frustration, sharp resentment"
            st.session_state.step = 2
            st.rerun()

# STEP 2: PICK METAPHOR
elif st.session_state.step == 2:
    st.markdown(f"""
    <div class='custom-card'>
        <p class='accent-header'>Step 2: Pick an Environment Metaphor</p>
        <p>You have acknowledged feeling <span style='color:#deff9a; font-weight:bold;'>【{st.session_state.emotion_label}】</span>. If this pressure becomes a landscape or weather in your mind, what does it look like?</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌧️ Rainy Storm Night"):
            st.session_state.metaphor_label = "Rainy Storm Night"
            st.session_state.metaphor_prompt = "dark rainy stormy night, heavy ominous clouds, pouring rain, monochrome dark tones"
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("🌫️ Foggy Misty Forest"):
            st.session_state.metaphor_label = "Foggy Misty Forest"
            st.session_state.metaphor_prompt = "dense foggy misty forest, lost path, dead trees, cold desolation, muted grey colors"
            st.session_state.step = 3
            st.rerun()
    with col3:
        if st.button("🏜️ Barren Dry Desert"):
            st.session_state.metaphor_label = "Barren Dry Desert"
            st.session_state.metaphor_prompt = "barren dry endless desert, cracked earth, lonely vast emptiness, dusty pale atmosphere"
            st.session_state.step = 3
            st.rerun()

# STEP 3: VISUALIZATION
elif st.session_state.step == 3:
    st.markdown(f"""
    <div class='custom-card'>
        <p class='accent-header'>Step 3: Visualizing Your Inner Canvas (Externalization)</p>
        <p>Our system has translated your emotional input <b>【{st.session_state.emotion_label}】</b> and metaphor <b>【{st.session_state.metaphor_label}】</b> into abstract visual language:</p>
    </div>
    """, unsafe_allow_html=True)
    
    base_art_prompt = f"abstract expressionism emotional oil painting, representing {st.session_state.emotion_prompt}, set in a {st.session_state.metaphor_prompt}, highly atmospheric, surreal, psychological depth, masterpiece"
    encoded_base = urllib.parse.quote(base_art_prompt)
    first_image_url = f"https://image.pollinations.ai/p/{encoded_base}?width=800&height=480&seed=42"
    
    st.image(first_image_url, caption="Stage 1: Your Psychological Weight Externalized", use_container_width=True)
    
    st.markdown("""
    <div class='feedback-box'>
        <p class='feedback-title'>🎨 AI Art Therapist's Observation (Keeps it safe):</p>
        <p style='font-size: 0.95rem; color: #daffde; margin: 0;'>
            I am observing this painting. The heavy brushstrokes and suffocating tones vividly capture the raw weight that words fail to express. 
            Thank you for allowing this canvas to hold that heavy pressure for you. Remember, the canvas of art is always open to re-creation.
        </p>
    </div>
    <div class='custom-card' style='margin-top: 25px;'>
        <p class='accent-header'>Emotion Alchemy: What \"Hope Element\" would you like to introduce to transform this darkness?</p>
        <p>This active choice initiates your Cognitive Reframing process:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✨ Warm Morning Light"):
            st.session_state.hope_label = "Warm Morning Light"
            st.session_state.hope_prompt = "a bright brilliant ray of golden morning sun breaking through the dark clouds, glowing rays, illuminating hope"
            st.session_state.step = 4
            st.rerun()
    with col2:
        if st.button("🌱 Resilient New Sprout"):
            st.session_state.hope_label = "Resilient New Sprout"
            st.session_state.hope_prompt = "a tiny vibrant glowing green sprout pushing through the cracked ground, life force, resilience, hope"
            st.session_state.step = 4
            st.rerun()
    with col3:
        if st.button("🦋 Freedom Butterflies"):
            st.session_state.hope_label = "Freedom Butterflies"
            st.session_state.hope_prompt = "a swarm of glowing neon blue butterflies fluttering towards the horizon, scattering glowing dust, freedom"
            st.session_state.step = 4
            st.rerun()

# STEP 4: REFRAMING & REGENERATION
elif st.session_state.step == 4:
    st.markdown(f"""
    <div class='custom-card'>
        <p class='accent-header'>Step 4: Emotion Alchemy Complete (Cognitive Reframing)</p>
        <p>By introducing <b>【{st.session_state.hope_label}】</b>, you have actively commanded the AI to re-compose and heal the canvas:</p>
    </div>
    """, unsafe_allow_html=True)
    
    final_art_prompt = f"beautiful abstract expressionism painting, transitioning from darkness to healing, {st.session_state.emotion_prompt}, {st.session_state.metaphor_prompt}, into which {st.session_state.hope_prompt} is magnificently integrated, soft lighting, vibrant healing colors, peaceful atmosphere, hope and recovery"
    encoded_final = urllib.parse.quote(final_art_prompt)
    second_image_url = f"https://image.pollinations.ai/p/{encoded_final}?width=800&height=480&seed=99"
    
    st.image(second_image_url, caption="Stage 2: Your Transformed Canvas of Hope", use_container_width=True)
    
    st.markdown(f"""
    <div class='feedback-box' style='border-left-color: #deff9a; background-color: #121612;'>
        <p class='feedback-title'>🎉 The Healing Brush Empowerment Message:</p>
        <p style='font-size: 1rem; color: #ffffff; margin: 0; line-height: 1.6;'>
            Look at this brand new canvas! The light breaking through the darkness was not handed to you by anyone else—<b>it was your own choice</b>.<br>
            This transformation proves that no matter how heavy real-life pressure gets, you always hold the agency within yourself to invite light back into your story.<br>
            <span style='color:#deff9a; font-weight:bold; font-size:1.1rem;'>You just brought in the light yourself!</span>
        </p>
    </div>
    <div class='crisis-box'>
        <p style='color: #ff4b4b; font-weight: bold; margin-top:0; margin-bottom: 5px; font-size:0.9rem;'>⚠️ Campus Mental Health Safety Net (SDG 3):</p>
        <p style='font-size: 0.85rem; color: #cccccc; margin: 0;'>
            Artistic creation helps alleviate mild-to-moderate school and DSE pressures. If you or your peer are experiencing severe crisis or self-harm thoughts, seeking support is a sign of strength:<br>
            • The Samaritans HK: <b>2389 2222</b> | • Suicide Prevention Services: <b>2382 0000</b> | • HA Mental Health Hotline: <b>2466 7350</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🔄 Start a New Inner Art Journey"):
        st.session_state.step = 1
        st.session_state.emotion_label = ""
        st.session_state.emotion_prompt = ""
        st.session_state.metaphor_label = ""
        st.session_state.metaphor_prompt = ""
        st.session_state.hope_label = ""
        st.session_state.hope_prompt = ""
        st.rerun()
