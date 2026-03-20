import streamlit as st

# Configuración de la página para modo ancho y título en pestaña
st.set_page_config(page_title="¿Puede un algoritmo entender tu tristeza?", layout="wide")

# Estilo CSS para emular la estética de s — o, io (Minimalismo, Tipografía y Navegación)
st.markdown("""
    <style>
    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Contenedor principal para simular Viewport 100% */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }

    /* Tipografía */
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

    /* Botones personalizados */
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

# Gestión de estado para la navegación por pasos
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

# --- SECCIONES DEL ARTÍCULO ---

# Paso 0: Título e Introducción
if st.session_state.step == 0:
    st.markdown("### Frida Rea / Gemini")
    st.title("¿Puede un algoritmo entender tu tristeza? El auge de la amistad con chatbots terapéuticos")
    st.markdown("
