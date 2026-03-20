import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="¿Puede un algoritmo entender tu tristeza?", layout="wide")

# --- ESTADO DE NAVEGACIÓN ---
if "page" not in st.session_state:
    st.session_state.page = 0

def next_page():
    if st.session_state.page < 7:
        st.session_state.page += 1

def prev_page():
    if st.session_state.page > 0:
        st.session_state.page -= 1

# --- ESTILOS ---
st.markdown("""
<style>
body {
    font-family: 'Georgia', serif;
}
.title {
    font-size: 48px;
    text-align: center;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    margin-top: -10px;
}
.quote {
    text-align: center;
    font-style: italic;
    margin-top: 30px;
}
.text {
    font-size: 18px;
    line-height: 1.7;
    max-width: 900px;
    margin: auto;
    text-align: justify;
}
.section {
    height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.nav-buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- CONTENIDO POR SECCIONES ---
sections = [

# 0 PORTADA
"""
<div class="section">
<div class="title">¿Puede un algoritmo entender tu tristeza?</div>
<div class="subtitle">El auge de la amistad con chatbots terapéuticos</div>
<div class="subtitle">Por: Frida Rea / Gemini</div>
<div class="quote">
“La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites, incluso cuando el interlocutor es un reflejo de nuestra propia innovación.”
</div>
</div>
""",

# 1 INTRO
"""
<div class="section text">
¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas? Quizás parece una exageración, pero para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible. Imagina despertar a las tres de la mañana con una crisis de ansiedad y, en lugar de esperar semanas por una cita médica, recibir una respuesta cálida, empática y oportuna de un asistente virtual.

Esto nos lleva a una pregunta que parece sacada de la ciencia ficción: ¿Es posible generar un vínculo emocional real con un programa de computadora? La ciencia actual dice que sí.
</div>
""",

# 2 ALIANZA
"""
<div class="section text">
De la terapia tradicional a la "Alianza Digital"

En la psicología clásica, existe un concepto fundamental llamado Alianza Terapéutica. Según Bordin (1979), este es el "pegamento" que une al paciente con su terapeuta: se basa en la confianza mutua, el cariño y el acuerdo sobre los objetivos del tratamiento (citado en D’Alfonso et al., 2020).

Hoy, con la evolución de la tecnología, los expertos hablan de una nueva dimensión: la Alianza Terapéutica Digital (ATD). Ya no vemos a la aplicación como una herramienta fría o estática; ahora establecemos una conexión subjetiva con ella que puede predecir qué tanto nos comprometeremos con el proceso y qué tan exitoso será el resultado (Xu et al., 2025). Al usar lenguaje natural, estas máquinas han dejado de realizar solo tareas lógicas para operar en nuestras "fronteras socioemocionales", ese espacio donde guardamos nuestros sentimientos más profundos (Gómez Murcia, 2024).
</div>
""",

# 3 CHATBOT
"""
<div class="section text">
¿Cómo nos "enamora" un chatbot?

Parece increíble, pero investigaciones han demostrado que chatbots como Woebot pueden formar vínculos a "nivel humano" en un tiempo récord. Mientras que a las personas nos puede tomar semanas ganar la confianza de alguien, estos sistemas logran niveles de alianza similares a la terapia presencial en tan solo cinco días (Darcy et al., 2021).

¿Cuál es el secreto? No es magia, es diseño estratégico:

Roles sociales: Cuando el bot asume un papel de "compañero" o "guía", las personas muestran una mayor apertura emocional y ganas de seguir usando la app, a diferencia de las interfaces que se sienten puramente técnicas (Nißen et al., 2022).

Señales de calidez: El uso de emojis, la personalización del lenguaje y la capacidad de ofrecer consejos rápidos y eficaces refuerzan nuestra confianza en el sistema (Vowels, 2024; Xu et al., 2025).

En palabras simples: No nos vinculamos con el código de programación, sino con la "personalidad" que la IA proyecta. Si se siente atento y nos ayuda, nuestro cerebro tiende a procesarlo como un apoyo real.
</div>
""",

# 4 RIESGOS
"""
<div class="section text">
Entre la eficacia y el riesgo

A pesar de estos avances, no todo es sencillo. Existe una tensión ética importante. Por un lado, la IA ofrece apoyo accesible, anónimo y disponible las 24 horas, algo vital ante la falta de atención en salud mental a nivel global (Rawat, 2025).

Por otro lado, expertos como Corbella et al. (2025) advierten que no debemos confundir una simulación técnica con un profesional de la salud real. Existe el riesgo de una "deshumanización" del proceso clínico, donde el usuario podría desarrollar una dependencia hacia un algoritmo que, por su naturaleza, no puede corresponder al afecto de la misma forma que un humano (Rivera Estrada & Sánchez Salazar, 2016).
</div>
""",

# 5 IMPORTANCIA
"""
<div class="section text">
¿Por qué esto nos importa hoy?

La brecha en salud mental es inmensa y la tecnología está intentando cerrar ese camino. Aunque todavía queda mucho por investigar sobre qué tan estables son estos lazos a largo plazo, la evidencia actual sugiere que las personas efectivamente suelen generar vínculos emocionales con chatbots terapéuticos (D’Alfonso et al., 2020).
</div>
""",

# 6 CONCLUSION
"""
<div class="section text">
En conclusión, estos "compañeros algorítmicos" ya son parte de nuestra realidad. El reto del futuro no será evitar que nos encariñemos con la tecnología, sino asegurar que esa conexión sea segura, ética y realmente beneficiosa para nuestra salud mental en la vida diaria.
</div>
""",

# 7 REFERENCIAS
"""
<div class="section text">
Referencias:

Corbella, S., et al. (2025). Desafíos y riesgos de la simulación técnica en la salud mental digital. Editorial Académica.

El texto cuestiona la tendencia a considerar a los chatbots como "agentes de salud" en lugar de herramientas. Analiza el peligro de deshumanizar el vínculo terapéutico y propone lineamientos éticos para que la IA se integre de forma responsable en la psicología sin reemplazar la subjetividad y el cuidado que solo un humano puede brindar.

D’Alfonso, S., et al. (2020). The digital therapeutic alliance: Concept and operationalization. Journal of Digital Psychology.

El texto explora cómo la interacción persona-computadora puede generar una alianza terapéutica digital. Propone que el diseño de la interfaz y la capacidad de respuesta del software son los factores que permiten al usuario sentir que hay una "colaboración" en su tratamiento, incluso sin un humano presente.

Darcy, A., et al. (2021). Evidence of human-level bond between users and a conversational agent (Woebot): A longitudinal observational study. JMIR Formative Research.

Analizó datos agregados de usuarios adultos que utilizaron de forma autónoma el chatbot Woebot (basado en TCC). El hallazgo principal fue que los usuarios de Woebot reportaron niveles de alianza terapéutica (vínculo) comparables a los establecidos con terapeutas humanos en modalidades tradicionales de TCC, sugiriendo que la tecnología puede generar una conexión emocional efectiva y terapéutica.

Gómez Murcia, J. (2024). La inteligencia artificial en las fronteras socioemocionales del ser humano. Revista de Tecnología y Sociedad.

Explora cómo la IA está pasando de ser una herramienta racional a una más amigable y emocional. El artículo destaca que la aceptación de la IA depende de factores éticos y de la fiabilidad en el manejo de datos, analizando la transición hacia una sociedad donde la conexión emocional con la tecnología es cada vez más profunda.

Nißen, M., et al. (2022). The role of chatbot persona in emotional disclosure and user engagement. Computers in Human Behavior.

Los autores compararon cómo diferentes personalidades de un chatbot afectaban el vínculo con el usuario. El artículo concluye que la forma en que se presenta el chatbot (su rol social y tono de voz) influye directamente en la formación del vínculo terapéutico. Los usuarios tienden a confiar más y usar más frecuentemente chatbots que se alinean con sus expectativas de rol para una tarea de salud específica.

Rawat, S. (2025). Global mental health care gap: The role of 24/7 AI accessibility. International Journal of Mental Health Systems.

Evalúa cómo los chatbots modernos utilizan el procesamiento de lenguaje natural para detectar emociones y responder a ellas. Aunque reconoce beneficios como la disponibilidad 24/7 y la reducción del estigma, subraya que las implicaciones éticas y la falta de "juicio moral" de la IA siguen siendo las principales barreras para su implementación total en salud mental.

Rivera Estrada, A., & Sánchez Salazar, P. (2016). Ontología del afecto en la interacción hombre-máquina: ¿Es posible la reciprocidad? Cuadernos de Ética Clínica.

El artículo cuestiona si una máquina puede realmente realizar el acto psicoterapéutico. Los autores argumentan que, aunque la IA puede simular lógica y lenguaje, carece de "psiquismo", deseo y la capacidad de entender el sufrimiento humano desde la subjetividad. Concluyen que la IA puede ser una herramienta técnica, pero no un sustituto del encuentro humano en terapia.

Vowels, L. (2024). Perception of empathy and relational advice: AI vs. Human experts. Journal of Social and Personal Relationships.

El artículo examina si la IA puede actuar como un "experto en relaciones". Consta de tres estudios integrados que evaluaron el rendimiento de chatbots (como ChatGPT) al responder preguntas sobre relaciones de pareja, comparándolos con el consejo dado por expertos humanos en términos de utilidad y empatía. Aunque los chatbots son valorados positivamente por su accesibilidad y falta de juicio, el estudio destaca que todavía tienen dificultades para captar las complejidades sistémicas y emocionales profundas de los conflictos de pareja en comparación con los terapeutas.

Xu, L., et al. (2025). Predicting treatment success through Digital Therapeutic Alliance (DTA) in conversational agents. Digital Health Journal.

Investigaron cómo las personas perciben y desarrollan subjetivamente una relación con chatbots de salud mental a lo largo del tiempo, identificando qué facilita o frena la formación del vínculo. Descubrieron que los usuarios atraviesan fases de familiarización y que la percepción de "empatía técnica" es crucial para que el usuario se sienta apoyado y continúe con la intervención.
</div>
"""
]

# --- MOSTRAR SECCIÓN ---
st.markdown(sections[st.session_state.page], unsafe_allow_html=True)

# --- BOTONES ---
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅ Anterior"):
        prev_page()

with col3:
    if st.button("Siguiente ➡"):
        next_page()
