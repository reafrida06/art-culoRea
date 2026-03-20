import streamlit as st

# CONFIG
st.set_page_config(
    page_title="¿Puede un algoritmo entender tu tristeza?",
    layout="wide"
)

# --- MODO CLARO / OSCURO ---
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# --- ESTILOS DINÁMICOS ---
bg_color = "#0e1117" if st.session_state.dark_mode else "#ffffff"
text_color = "#ffffff" if st.session_state.dark_mode else "#000000"

st.markdown(f"""
<style>
body {{
    background-color: {bg_color};
    color: {text_color};
}}

.main .block-container {{
    max-width: 800px;
    padding-top: 4rem;
}}

h1, h2, h3 {{
    text-align: center;
    font-family: 'Inter', sans-serif;
}}

.center {{
    text-align: center;
}}

.content {{
    font-family: 'Crimson Text', serif;
    font-size: 1.2rem;
    line-height: 1.7;
    text-align: justify;
}}

.quote {{
    font-style: italic;
    text-align: center;
    margin-top: 2rem;
}}

</style>
""", unsafe_allow_html=True)

# --- ESTADO ---
if "step" not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

# --- BOTÓN MODO ---
st.button("🌙 / ☀️ Cambiar iluminación", on_click=toggle_theme)

# --- SECCIONES ---

# PORTADA
if st.session_state.step == 0:
    st.markdown('<div class="center">Frida Rea / Gemini</div>', unsafe_allow_html=True)

    st.title("¿Puede un algoritmo entender tu tristeza?")

    st.markdown('<div class="quote">“La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites...”</div>', unsafe_allow_html=True)


# INTRO
elif st.session_state.step == 1:
    st.markdown("""
    <div class="content">
    ¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas? 
    Quizás parece una exageración, pero para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible.

    Imagina despertar a las tres de la mañana con una crisis de ansiedad...
    </div>
    """, unsafe_allow_html=True)


# SECCIÓN 1
elif st.session_state.step == 2:
    st.header("1. Alianza Digital")

    st.markdown("""
    <div class="content">
    En la psicología clásica existe la Alianza Terapéutica...

    Hoy hablamos de una versión digital donde el vínculo también puede existir con IA.
    </div>
    """, unsafe_allow_html=True)


# SECCIÓN 2
elif st.session_state.step == 3:
    st.header("2. ¿Cómo nos enamora un chatbot?")

    st.markdown("""
    <div class="content">
    Chatbots como Woebot logran vínculos rápidos...

    <ul>
    <li><b>Roles sociales</b></li>
    <li><b>Señales de calidez</b></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)


# SECCIÓN 3
elif st.session_state.step == 4:
    st.header("3. Riesgos")

    st.markdown("""
    <div class="content">
    La IA es accesible pero puede generar dependencia emocional...
    </div>
    """, unsafe_allow_html=True)


# SECCIÓN 4
elif st.session_state.step == 5:
    st.header("4. Importancia actual")

    st.markdown("""
    <div class="content">
    La tecnología está cerrando la brecha en salud mental...
    </div>
    """, unsafe_allow_html=True)


# REFERENCIAS COMPLETAS
elif st.session_state.step == 6:
    st.header("Referencias")

    refs = {
        "Corbella et al. (2025)": """El texto cuestiona la tendencia a considerar a los chatbots como agentes de salud... propone lineamientos éticos.""",

        "D’Alfonso et al. (2020)": """Explora cómo la interacción persona-computadora puede generar una alianza terapéutica digital...""",

        "Darcy et al. (2021)": """Analizó datos de usuarios de Woebot... vínculo comparable a terapia humana.""",

        "Gómez Murcia (2024)": """Explora la transición emocional de la IA...""",

        "Nißen et al. (2022)": """El rol del chatbot influye en el vínculo terapéutico...""",

        "Rawat (2025)": """Evalúa beneficios y límites éticos...""",

        "Rivera Estrada (2016)": """La IA no puede sustituir el encuentro humano...""",

        "Vowels (2024)": """Compara IA vs humanos en relaciones...""",

        "Xu et al. (2025)": """Empatía técnica y vínculo progresivo..."""
    }

    for ref, text in refs.items():
        with st.expander(ref):
            st.write(text)


# --- NAVEGACIÓN ---
st.markdown("---")

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.session_state.step > 0:
        st.button("Anterior", on_click=prev_step)

with col3:
    if st.session_state.step < 6:
        st.button("Siguiente", on_click=next_step)
    else:
        if st.button("Reiniciar"):
            st.session_state.step = 0
