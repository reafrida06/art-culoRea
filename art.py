import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="¿Puede un algoritmo entender tu tristeza?",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS (Minimalismo y Modos) ---
st.markdown("""
    <style>
    /* Estilo para simular secciones de 100% de alto */
    .section-container {
        min-height: 70vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 2rem;
    }
    .main-title {
        font-family: 'serif';
        font-size: 3rem;
        font-weight: bold;
    }
    .content-text {
        font-family: 'serif';
        font-size: 1.25rem;
        line-height: 1.6;
        max-width: 800px;
        margin: auto;
    }
    .quote {
        font-style: italic;
        color: #555;
        border-left: 4px solid #ccc;
        padding-left: 20px;
        margin: 20px 0;
    }
    /* Estilo de botones */
    .stButton>button {
        border-radius: 20px;
        padding: 10px 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN ---
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

# --- CONTENIDO DE LAS SECCIONES ---
sections = [
    # SECCIÓN 0: Título e Intro
    {
        "title": "¿Puede un algoritmo entender tu tristeza?",
        "subtitle": "El auge de la amistad con chatbots terapéuticos",
        "content": f"**Por: Frida Rea / Gemini** \n\n > “La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites, incluso cuando el interlocutor es un reflejo de nuestra propia innovación.”"
    },
    # SECCIÓN 1: Introducción
    {
        "title": "La Conexión Invisible",
        "content": "¿Alguna vez has sentido que Siri o Alexa te 'entienden' mejor que algunas personas? Para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible. Imagina despertar a las tres de la mañana con una crisis de ansiedad y recibir una respuesta cálida de un asistente virtual. ¿Es posible generar un vínculo emocional real con un programa?"
    },
    # SECCIÓN 2: Punto 1 - Alianza Digital
    {
        "title": "1. De la terapia tradicional a la 'Alianza Digital'",
        "content": "En la psicología clásica, la **Alianza Terapéutica** es el 'pegamento' basado en confianza y cariño (Bordin, 1979). Hoy hablamos de la **Alianza Terapéutica Digital (ATD)**. Ya no vemos la app como una herramienta fría; establecemos una conexión subjetiva que predice el éxito del tratamiento (Xu et al., 2025)."
    },
    # SECCIÓN 3: Punto 2 - Fronteras Socioemocionales
    {
        "title": "2. Fronteras Socioemocionales",
        "content": "Al usar lenguaje natural, las máquinas operan en nuestras 'fronteras socioemocionales', el espacio donde guardamos sentimientos profundos (Gómez Murcia, 2024). No nos vinculamos con el código, sino con la 'personalidad' que la IA proyecta (Vowels, 2024)."
    },
    # SECCIÓN 4: Punto 3 - El Secreto del Diseño
    {
        "title": "3. ¿Cómo nos 'enamora' un chatbot?",
        "content": "Chatbots como **Woebot** forman vínculos a nivel humano en solo cinco días (Darcy et al., 2021). El secreto es el diseño estratégico: Roles sociales (compañero o guía) y señales de calidez (emojis y lenguaje personalizado) que refuerzan la confianza (Nißen et al., 2022)."
    },
    # SECCIÓN 5: Punto 4 - Eficacia vs. Riesgo
    {
        "title": "4. Entre la eficacia y el riesgo",
        "content": "La IA ofrece apoyo accesible y anónimo 24/7 (Rawat, 2025). Sin embargo, existe el riesgo de una 'deshumanización'. No debemos confundir una simulación técnica con un profesional real; un algoritmo no puede corresponder al afecto como un humano (Corbella et al., 2025)."
    },
    # SECCIÓN 6: Punto 5 - El Futuro
    {
        "title": "5. ¿Por qué esto nos importa hoy?",
        "content": "La brecha en salud mental es inmensa. Aunque faltan estudios a largo plazo, la evidencia sugiere que las personas sí generan vínculos emocionales con estos sistemas (D’Alfonso et al., 2020). El reto es asegurar que esta conexión sea segura y ética."
    },
    # SECCIÓN 7: Ideas Clave y Cierre
    {
        "title": "Conclusión",
        "content": "Los 'compañeros algorítmicos' ya son parte de nuestra realidad. El reto no es evitar el cariño hacia la tecnología, sino garantizar que sea beneficiosa para nuestra vida diaria. \n\n --- \n\n ### 📚 Referencias Principales \n * **D’Alfonso (2020)**: Concepto de Alianza Digital. \n * **Darcy (2021)**: Vínculo humano con Woebot. \n * **Corbella (2025)**: Riesgos de deshumanización."
    }
]

# --- RENDERIZADO ---
current_data = sections[st.session_state.step]

st.markdown(f"""
    <div class="section-container">
        <div class="main-title">{current_data['title']}</div>
        <div style="font-size: 1.5rem; margin-bottom: 20px;">{current_data.get('subtitle', '')}</div>
        <div class="content-text">{current_data['content']}</div>
    </div>
""", unsafe_allow_html=True)

# --- CONTROLES DE NAVEGACIÓN ---
cols = st.columns([1, 1, 1])

with cols[0]:
    if st.session_state.step > 0:
        st.button("← Anterior", on_click=prev_step, use_container_width=True)

with cols[2]:
    if st.session_state.step < len(sections) - 1:
        st.button("Siguiente →", on_click=next_step, use_container_width=True)

# Barra de progreso discreta
progress = (st.session_state.step + 1) / len(sections)
st.progress(progress)
