import streamlit as st
from streamlit_modal import Modal

# --- CONFIG ---
st.set_page_config(page_title="¿Puede un algoritmo entender tu tristeza?", layout="wide")

# --- ESTADO ---
if "page" not in st.session_state:
    st.session_state.page = 0

# --- FUNCIONES ---
def next_page():
    if st.session_state.page < len(sections) - 1:
        st.session_state.page += 1

def prev_page():
    if st.session_state.page > 0:
        st.session_state.page -= 1

# --- ESTILOS ---
st.markdown("""
<style>
.block {
    height: 85vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    max-width: 900px;
    margin: auto;
}

.title {
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    font-size: 22px;
    margin-top: 10px;
}

.text {
    font-size: 18px;
    line-height: 1.7;
    margin-top: 20px;
    text-align: justify;
}

.quote {
    font-style: italic;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# --- SECCIONES ---
sections = [

# PORTADA
lambda: st.markdown("""
<div class="block">
<div class="title">¿Puede un algoritmo entender tu tristeza?</div>
<div class="subtitle">El auge de la amistad con chatbots terapéuticos</div>
<div class="subtitle">Por: Frida Rea / Gemini</div>
<div class="quote">
“La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites, incluso cuando el interlocutor es un reflejo de nuestra propia innovación.”
</div>
</div>
""", unsafe_allow_html=True),

# INTRO
lambda: st.markdown("""
<div class="block">
<div class="title">Introducción</div>
<div class="text">
¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas? Quizás parece una exageración, pero para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible. Imagina despertar a las tres de la mañana con una crisis de ansiedad y, en lugar de esperar semanas por una cita médica, recibir una respuesta cálida, empática y oportuna de un asistente virtual.

Esto nos lleva a una pregunta que parece sacada de la ciencia ficción: ¿Es posible generar un vínculo emocional real con un programa de computadora? La ciencia actual dice que sí.
</div>
</div>
""", unsafe_allow_html=True),

# ALIANZA
lambda: st.markdown("""
<div class="block">
<div class="title">De la terapia tradicional a la "Alianza Digital"</div>
<div class="text">
En la psicología clásica, existe un concepto fundamental llamado Alianza Terapéutica. Según Bordin (1979), este es el "pegamento" que une al paciente con su terapeuta: se basa en la confianza mutua, el cariño y el acuerdo sobre los objetivos del tratamiento (citado en D’Alfonso et al., 2020).

Hoy, con la evolución de la tecnología, los expertos hablan de una nueva dimensión: la Alianza Terapéutica Digital (ATD). Ya no vemos a la aplicación como una herramienta fría o estática; ahora establecemos una conexión subjetiva con ella que puede predecir qué tanto nos comprometeremos con el proceso y qué tan exitoso será el resultado (Xu et al., 2025). Al usar lenguaje natural, estas máquinas han dejado de realizar solo tareas lógicas para operar en nuestras "fronteras socioemocionales", ese espacio donde guardamos nuestros sentimientos más profundos (Gómez Murcia, 2024).
</div>
</div>
""", unsafe_allow_html=True),

# CHATBOT
lambda: st.markdown("""
<div class="block">
<div class="title">¿Cómo nos "enamora" un chatbot?</div>
<div class="text">
Parece increíble, pero investigaciones han demostrado que chatbots como Woebot pueden formar vínculos a "nivel humano" en un tiempo récord. Mientras que a las personas nos puede tomar semanas ganar la confianza de alguien, estos sistemas logran niveles de alianza similares a la terapia presencial en tan solo cinco días (Darcy et al., 2021).

¿Cuál es el secreto? No es magia, es diseño estratégico:

Roles sociales: Cuando el bot asume un papel de "compañero" o "guía", las personas muestran una mayor apertura emocional y ganas de seguir usando la app, a diferencia de las interfaces que se sienten puramente técnicas (Nißen et al., 2022).

Señales de calidez: El uso de emojis, la personalización del lenguaje y la capacidad de ofrecer consejos rápidos y eficaces refuerzan nuestra confianza en el sistema (Vowels, 2024; Xu et al., 2025).

En palabras simples: No nos vinculamos con el código de programación, sino con la "personalidad" que la IA proyecta. Si se siente atento y nos ayuda, nuestro cerebro tiende a procesarlo como un apoyo real.
</div>
</div>
""", unsafe_allow_html=True),

# RIESGOS
lambda: st.markdown("""
<div class="block">
<div class="title">Entre la eficacia y el riesgo</div>
<div class="text">
A pesar de estos avances, no todo es sencillo. Existe una tensión ética importante. Por un lado, la IA ofrece apoyo accesible, anónimo y disponible las 24 horas, algo vital ante la falta de atención en salud mental a nivel global (Rawat, 2025).

Por otro lado, expertos como Corbella et al. (2025) advierten que no debemos confundir una simulación técnica con un profesional de la salud real. Existe el riesgo de una "deshumanización" del proceso clínico, donde el usuario podría desarrollar una dependencia hacia un algoritmo que, por su naturaleza, no puede corresponder al afecto de la misma forma que un humano (Rivera Estrada & Sánchez Salazar, 2016).
</div>
</div>
""", unsafe_allow_html=True),

# CONCLUSIÓN
lambda: st.markdown("""
<div class="block">
<div class="title">Conclusión</div>
<div class="text">
En conclusión, estos "compañeros algorítmicos" ya son parte de nuestra realidad. El reto del futuro no será evitar que nos encariñemos con la tecnología, sino asegurar que esa conexión sea segura, ética y realmente beneficiosa para nuestra salud mental en la vida diaria.
</div>
</div>
""", unsafe_allow_html=True),

# REFERENCIAS INTERACTIVAS
lambda: references_section()
]

# --- REFERENCIAS INTERACTIVAS ---
def references_section():
    st.markdown("<div class='block'><div class='title'>Referencias</div></div>", unsafe_allow_html=True)

    refs = {
        "Corbella et al. (2025)": "El texto cuestiona la tendencia a considerar a los chatbots como 'agentes de salud'...",
        "D’Alfonso et al. (2020)": "Explora cómo la interacción persona-computadora puede generar una alianza terapéutica digital...",
        "Darcy et al. (2021)": "Los usuarios de Woebot reportaron niveles de alianza comparables a terapeutas humanos...",
        "Gómez Murcia (2024)": "Analiza la transición hacia una IA más emocional y su aceptación social...",
        "Nißen et al. (2022)": "La personalidad del chatbot influye directamente en el vínculo terapéutico...",
        "Rawat (2025)": "Evalúa la accesibilidad 24/7 y sus implicaciones éticas...",
        "Rivera Estrada & Sánchez (2016)": "Cuestiona si una máquina puede realizar el acto psicoterapéutico...",
        "Vowels (2024)": "Compara empatía entre IA y humanos en relaciones...",
        "Xu et al. (2025)": "La 'empatía técnica' es clave para mantener al usuario en tratamiento..."
    }

    for i, (title, content) in enumerate(refs.items()):
        modal = Modal(title, key=f"modal_{i}")

        if st.button(title):
            modal.open()

        if modal.is_open():
            with modal.container():
                st.write(content)

# --- RENDER ---
sections[st.session_state.page]()

# --- BOTONES DINÁMICOS ---
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.session_state.page > 0:
        st.button("⬅ Anterior", on_click=prev_page)

with col3:
    if st.session_state.page < len(sections) - 1:
        st.button("Siguiente ➡", on_click=next_page)
