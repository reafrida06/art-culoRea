import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="¿Puede un algoritmo entender tu tristeza?",
    layout="wide"
)

# Estilos CSS
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 800px;
}

h1, h2, h3 {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    letter-spacing: -0.02em;
    text-align: center;
}

.content-text {
    font-family: 'Crimson Text', serif;
    font-size: 1.25rem;
    line-height: 1.6;
    text-align: justify;
}

.stButton>button {
    border-radius: 20px;
    padding: 10px 25px;
    border: 1px solid #ccc;
    background-color: transparent;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    border-color: #000;
    background-color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# Estado
if "step" not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1


# --- CONTENIDO ---

if st.session_state.step == 0:
    st.markdown("### Frida Rea / Gemini")
    st.title("¿Puede un algoritmo entender tu tristeza? El auge de la amistad con chatbots terapéuticos")
    st.markdown("---")

    st.info(
        "“La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites, incluso cuando el interlocutor es un reflejo de nuestra propia innovación.”"
    )

    st.markdown("""
    <div class="content-text">
    ¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas?
    Quizás parece una exageración, pero para miles de personas que buscan apoyo emocional
    en sus teléfonos, esta conexión es una realidad tangible.

    Imagina despertar a las tres de la mañana con una crisis de ansiedad y, en lugar de
    esperar semanas por una cita médica, recibir una respuesta cálida, empática y oportuna
    de un asistente virtual.

    Esto nos lleva a una pregunta que parece sacada de la ciencia ficción:
    ¿Es posible generar un vínculo emocional real con un programa de computadora?
    La ciencia actual dice que sí.
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.step == 1:
    st.header("1. De la terapia tradicional a la 'Alianza Digital'")

    st.markdown("""
    <div class="content-text">
    En la psicología clásica, existe un concepto fundamental llamado Alianza Terapéutica.
    Según Bordin (1979), este es el "pegamento" que une al paciente con su terapeuta.

    Hoy, con la evolución de la tecnología, los expertos hablan de una nueva dimensión:
    la Alianza Terapéutica Digital (ATD).

    Ya no vemos a la aplicación como una herramienta fría o estática; ahora establecemos
    una conexión subjetiva con ella que puede predecir el compromiso y el éxito del proceso.
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.step == 2:
    st.header("2. ¿Cómo nos 'enamora' un chatbot?")

    st.markdown("""
    <div class="content-text">
    Investigaciones han demostrado que chatbots pueden formar vínculos a "nivel humano"
    en muy poco tiempo.

    <ul>
        <li><b>Roles sociales:</b> mayor apertura emocional.</li>
        <li><b>Señales de calidez:</b> emojis y lenguaje personalizado.</li>
    </ul>

    No nos vinculamos con el código, sino con la "personalidad" que proyecta.
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.step == 3:
    st.header("3. Entre la eficacia y el riesgo")

    st.markdown("""
    <div class="content-text">
    La IA ofrece apoyo accesible, anónimo y 24/7.

    Pero también existe un riesgo:
    confundir una simulación con un profesional real.

    Puede haber dependencia hacia un sistema que no puede corresponder
    emocionalmente como un humano.
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.step == 4:
    st.header("4. ¿Por qué esto nos importa hoy?")

    st.markdown("""
    <div class="content-text">
    La tecnología intenta cerrar la brecha en salud mental.

    Las personas sí generan vínculos emocionales con chatbots.

    El reto no es evitarlo, sino asegurar que sea ético, seguro
    y beneficioso.
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.step == 5:
    st.header("Referencias y Bibliografía")
    st.write("Haz clic en cada referencia para ver su resumen:")

    refs = {
        "Corbella et al. (2025)": "Cuestiona ver chatbots como agentes de salud.",
        "D’Alfonso et al. (2020)": "Explora la alianza terapéutica digital.",
        "Darcy et al. (2021)": "Woebot genera vínculos comparables.",
        "Gómez Murcia (2024)": "IA más emocional.",
        "Nißen et al. (2022)": "El rol del chatbot importa.",
        "Rawat (2025)": "Beneficios vs límites éticos.",
        "Rivera Estrada (2016)": "IA no sustituye lo humano.",
        "Vowels (2024)": "Limitaciones emocionales.",
        "Xu et al. (2025)": "Empatía técnica clave."
    }

    for ref, summary in refs.items():
        with st.expander(ref):
            st.write(summary)


# --- NAVEGACIÓN ---
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.step > 0:
        st.button("Anterior", on_click=prev_step)

with col3:
    if st.session_state.step < 5:
        st.button("Siguiente", on_click=next_step)
    else:
        if st.button("Reiniciar"):
            st.session_state.step = 0
