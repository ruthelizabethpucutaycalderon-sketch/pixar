import streamlit as st
import random
      st.tittle
st.Ruth_Pucutay_Calderón
# Diccionario de preguntas, opciones, respuestas y personajes
preguntas = [
    {
        "pregunta": "¿Cómo se llama el pez protagonista en 'Buscando a Nemo'?",
        "opciones": ["Dory", "Marlin", "Nemo", "Bubbles"],
        "respuesta": "Nemo",
        "personaje_bueno": "nemo.jpg",
        "villano": "dentista.jpg"
    },
    {
        "pregunta": "¿Cuál es el nombre de la princesa en 'La Bella y la Bestia'?",
        "opciones": ["Aurora", "Bella", "Ariel", "Elsa"],
        "respuesta": "Bella",
        "personaje_bueno": "bella.jpg",
        "villano": "gastón.jpg"
    },
    {
        "pregunta": "¿Quién es el villano en 'El Rey León'?",
        "opciones": ["Mufasa", "Timon", "Scar", "Zazú"],
        "respuesta": "Scar",
        "personaje_bueno": "simba.jpg",
        "villano": "scar.jpg"
    },
    {
        "pregunta": "¿Cómo se llama la sirena protagonista en 'La Sirenita'?",
        "opciones": ["Úrsula", "Ariel", "Flounder", "Vanessa"],
        "respuesta": "Ariel",
        "personaje_bueno": "ariel.jpg",
        "villano": "ursula.jpg"
    },
    {
        "pregunta": "¿Quién entrena a Hércules en la película?",
        "opciones": ["Zeus", "Hades", "Filoctetes", "Pegaso"],
        "respuesta": "Filoctetes",
        "personaje_bueno": "hercules.jpg",
        "villano": "hades.jpg"
    }
]

# Selecciona una pregunta aleatoria al inicio
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = random.choice(preguntas)
    st.session_state.respondido = False

st.title("🎬 Quiz Disney: ¿Cuánto sabes?")

q = st.session_state.pregunta_actual
st.subheader(q["pregunta"])
respuesta = st.radio("Elige tu respuesta:", q["opciones"])

if st.button("Responder"):
    st.session_state.respondido = True
    if respuesta == q["respuesta"]:
        st.success("¡Correcto! 🎉")
        st.image("images/" + q["personaje_bueno"], caption="¡Es el personaje correcto!", use_column_width=True)
    else:
        st.error("Incorrecto 😢")
        st.image("images/" + q["villano"], caption="¡Oh no! Apareció el villano...", use_column_width=True)

if st.session_state.respondido:
    if st.button("Siguiente pregunta"):
        st.session_state.pregunta_actual = random.choice(preguntas)
        st.session_state.respondido = False
