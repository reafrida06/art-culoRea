import streamlit as st

# Configuración de la página
st.set_page_config(page_title="¿Puede un algoritmo entender tu tristeza?", layout="wide")

# Estilo CSS para minimalismo y navegación 100vh
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital@0;1&family=Inter:wght@300;400&display=swap');
    
    .main { background-color: #fafafa; color: #1a1a1a; }
    h1 { font-family: 'Playfair Display', serif; font-size: 3rem; text-align: center; }
    p, li { font-family: 'Inter', sans-serif; font-size: 1.2rem; line-height: 1.6; }
    .quote { font-style: italic; text-align: center; color: #555; margin: 2rem 0; }
    
    /* Simulación de secciones de pantalla completa */
    .section-container {
        height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 2rem;
    }
    
    /* Botones de navegación */
    .stButton>button {
        border-radius: 20px;
        padding: 10px 25px;
        border: 1px solid #1a1a1a;
        background-color: transparent;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #1a1a1a; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de navegación
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- CONTENIDO DE LAS SECCIONES ---
secciones = [
    # 0. Título
    {"tipo": "portada"},
    # 1. Introducción
    {"titulo": "¿Alguna vez has sentido que Siri o Alexa te 'entienden'?", "cuerpo": "Imagina despertar a las tres de la mañana con una crisis de ansiedad y, en lugar de esperar semanas por una cita, recibir una respuesta cálida de un asistente virtual. ¿Es posible generar un vínculo emocional real con un código?"},
    # 2. Alianza Digital
    {"titulo": "De la terapia tradicional a la 'Alianza Digital'", "cuerpo": "En la psicología clásica, la Alianza Terapéutica es el 'pegamento' entre paciente y terapeuta (Bordin, 1979). Hoy, la Alianza Terapéutica Digital (ATD) permite una conexión subjetiva con la app que predice el éxito del tratamiento."},
    # 3. El secreto del vínculo
    {"titulo": "¿Cómo nos 'enamora' un chatbot?", "cuerpo": "Sistemas como Woebot logran niveles de alianza similares a la terapia presencial en solo cinco días. El secreto está en el diseño: roles de 'compañero' y señales de calidez como emojis y personalización."},
    # 4. Eficacia y Riesgo
    {"titulo": "Entre la eficacia y el riesgo", "cuerpo": "La IA ofrece apoyo 24/7, vital ante la falta de atención global. Sin embargo, existe el riesgo de 'deshumanización': un algoritmo no puede corresponder al afecto de la misma forma que un humano."},
    # 5. Cierre
    {"titulo": "Conclusión", "cuerpo": "El reto del futuro no será evitar que nos encariñemos con la tecnología, sino asegurar que esa conexión sea segura, ética y realmente beneficiosa para nuestra salud mental."},
    # 6. Referencias
    {"tipo": "referencias"}
]

current = secciones[st.session_state.step]

# --- RENDERIZADO ---
with st.container():
    if current.get("tipo") == "portada":
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.write("---")
        st.markdown("<h1>¿Puede un algoritmo entender tu tristeza?</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Por: Frida Rea / Gemini</p>", unsafe_allow_html=True)
        st.markdown("<p class='quote'>“La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites...”</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    elif current.get("tipo") == "referencias":
        st.markdown("<h3>Referencias Bibliográficas</h3>", unsafe_allow_html=True)
        st.info("Haz clic en cada referencia para leer su resumen científico.")
        
        with st.expander("Corbella, S., et al. (2025)"):
            st.write("Cuestiona la tendencia a considerar a los chatbots como agentes de salud y analiza el peligro de deshumanizar el vínculo terapéutico.")
        with st.expander("D’Alfonso, S., et al. (2020)"):
            st.write("Explora cómo el diseño de la interfaz permite al usuario sentir una 'colaboración' en su tratamiento.")
        with st.expander("Darcy, A., et al. (2021)"):
            st.write("Hallazgo principal: los usuarios de Woebot reportaron niveles de alianza comparables a terapeutas humanos en solo 5 días.")
        # Se pueden agregar todas las demás siguiendo este formato

    else:
        st.markdown(f"<div class='section-container'>", unsafe_allow_html=True)
        st.markdown(f"<h2>{current['titulo']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p>{current['cuerpo']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- BOTONES ---
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.session_state.step > 0:
        st.button("Anterior", on_click=prev_step)
with col3:
    if st.session_state.step < len(secciones) - 1:
        st.button("Siguiente", on_click=next_step)
