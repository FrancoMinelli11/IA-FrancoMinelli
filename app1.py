import streamlit as st
import google.genai as genai
import random
from PIL import Image
from io import BytesIO
import base64
import time
import requests

# Configura tus claves de API
client = genai.Client(api_key="AIzaSyAR-2L1q6_ubtD8QIvjOhaRxCm_kgJXNzA")
HUGGINGFACE_TOKEN = st.secrets["HUGGINGFACE_TOKEN"]

modelos = client.models.list()
for modelo in modelos:
    print(modelo.name)


# Configuración de la página
st.set_page_config(page_title="Generador de Jugadas de Básquet con IA", layout="centered")
st.title("🏀 Generador Inteligente de Jugadas de Básquet")

st.markdown("""
Este generador usa inteligencia artificial para ayudarte a planear jugadas estratégicas en tiempo real. 
Solo ingresa el contexto del partido, y la IA te sugerirá una jugada con una visualización animada.
""")

# Entradas del usuario
defensa = st.selectbox("Tipo de defensa del rival:", ["Zona 2-3", "Hombre a hombre", "Presión a toda cancha", "Mixta"])
tiempo = st.slider("Tiempo restante (segundos):", min_value=1, max_value=24, value=14)
situacion = st.text_area("Situación de juego:", "Estamos perdiendo por 2 puntos, última posesión.")

# Función para traducir paso a prompt visual con Gemini
def generar_prompt_visual(paso):
    prompt_conversion = f"""
Eres un asistente de IA especializado en generar descripciones visuales para diagramas tácticos de básquetbol. 
Dado el siguiente paso de una jugada, crea un prompt en inglés para una imagen estilo diagrama (vista desde arriba) que represente claramente el movimiento o situación.

Paso táctico: "{paso}"

Ejemplo de salida:
"A top-down basketball tactical diagram showing player 1 at the top of the key, player 2 setting a screen on the right wing, player 3 cutting to the basket with movement arrows."

Solo responde con el prompt visual en inglés.
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt_conversion,
            config={"temperature": 0.6}
        )
        return response.text.strip().replace('"', '')
    except Exception as e:
        st.warning(f"No se pudo generar prompt visual con Gemini: {e}")
        return f"Top-down basketball tactical diagram showing basic player positions for: {paso}"

# Función para generar imagen en Hugging Face
def generar_imagen_hf(paso):
    modelos = [
        "runwayml/stable-diffusion-v1-5",
        "stabilityai/stable-diffusion-2-1",
        "CompVis/stable-diffusion-v1-4"
    ]
    prompt = generar_prompt_visual(paso)
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

    for modelo in modelos:
        api_url = f"https://api-inference.huggingface.co/models/{modelo}"
        data = {"inputs": prompt}
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            try:
                return Image.open(BytesIO(response.content))
            except Exception as e:
                st.warning(f"Error al procesar la imagen del modelo {modelo}: {e}")
        else:
            st.warning(f"No se pudo generar imagen con {modelo} (código {response.status_code})")
            time.sleep(1.5)  # pequeña pausa antes del siguiente intento

    st.error("No se pudo generar la imagen con ninguno de los modelos.")
    return None

# Botón para generar jugada
if st.button("Generar jugada"):
    with st.spinner("Generando jugada..."):
        prompt = f"""
Actúa como un entrenador profesional de básquetbol. Dado el siguiente contexto:

- Tipo de defensa: {defensa}
- Tiempo restante: {tiempo} segundos
- Situación del juego: {situacion}

Diseña una jugada ofensiva clara, efectiva, nombrando a los jugadores por número (1 al 5) e indicando el movimiento de cada uno paso a paso. Finaliza con un intento de anotación lógico. 
Devuelve el resultado en formato de lista de pasos.
"""
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt,
            config={
                'temperature': 0.7,
                'top_p': 0.9
            }
        )

        jugada = response.text
        st.subheader("📋 Jugada Sugerida")
        st.markdown(jugada)

        # Extraer pasos
        pasos = [line.strip() for line in jugada.split("\n") if line.strip() and (line.startswith("Paso") or line[0].isdigit())]

        st.subheader("🎞️ Visualización de la Jugada Paso a Paso")
        for i, paso in enumerate(pasos):
            st.markdown(f"**{paso}**")
            imagen = generar_imagen_hf(paso)
            if imagen:
                st.image(imagen, caption=f"{paso}")
            else:
                st.error("No se pudo generar la imagen para este paso.")
            time.sleep(0.5)

        st.markdown("*Imágenes generadas automáticamente por IA (Stable Diffusion en Hugging Face).*")

# Información adicional
st.markdown("---")
st.markdown("""
### ℹ️ ¿Cómo funciona?
Esta app recibe información táctica y usa Gemini de Google para generar una jugada sugerida. Luego muestra los pasos estratégicos y una imagen generada por IA por cada uno (vía Stable Diffusion).
""")

