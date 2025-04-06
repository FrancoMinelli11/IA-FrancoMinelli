# 🏀 Generador de Jugadas de Básquet con IA

Este proyecto es una aplicación web desarrollada con Streamlit que permite generar jugadas ofensivas de básquetbol asistidas por inteligencia artificial. Está pensada para entrenadores, jugadores o entusiastas que deseen recibir sugerencias estratégicas en tiempo real, considerando el contexto del partido.

## 🚀 Objetivo

Crear una herramienta interactiva que, a partir de datos tácticos proporcionados por el usuario (tipo de defensa, tiempo restante, situación de juego), proponga una jugada estructurada paso a paso, acompañada de representaciones visuales generadas automáticamente.

## 🛠️ Tecnologías Utilizadas

- **Python + Streamlit**: Para la construcción de la aplicación web.
- **Gemini (Google Generative AI)**: Para generar la jugada en formato de texto paso a paso.
- **Hugging Face + Stable Diffusion**: Para generar imágenes representativas de cada paso táctico.

## 🧠 ¿Cómo Funciona?

1. El usuario proporciona:
   - Tipo de defensa del rival (Zona, Hombre a hombre, etc.)
   - Tiempo restante en la posesión
   - Situación de juego (texto libre)

2. Se genera un prompt con esa información y se envía a **Gemini**, que devuelve una lista de pasos detallados para una jugada ofensiva.

3. Cada paso se transforma en una descripción visual en inglés, usada como prompt para generar una imagen usando **Stable Diffusion** a través de Hugging Face.

4. La app muestra los pasos de la jugada y las imágenes correspondientes.

## 📸 Ejemplo de Uso

- Defensa seleccionada: `Zona 2-3`
- Tiempo restante: `14 segundos`
- Situación: `Estamos perdiendo por 2 puntos, última posesión.`

Resultado: una jugada ofensiva compuesta por movimientos tácticos como cortes, pantallas e intentos de tiro, ilustrados paso a paso.

## ⚠️ Limitaciones

- **Imágenes poco eficaces**: Las imágenes generadas con IA no representan con precisión las posiciones y movimientos tácticos, lo que limita su utilidad como herramienta visual principal.
- **Cuotas de uso**: El uso gratuito de Gemini es limitado y puede resultar en errores como `RESOURCE_EXHAUSTED`, lo que impide generar contenido si se superan los límites.

## ✅ Recomendaciones

- Usar las jugadas generadas como base y complementarlas con diagramas hechos a mano o en herramientas como **FastDraw** o **KlipDraw**.
- Explorar el desarrollo de un sistema propio de diagramación táctica más estructurado.

## 🧩 Conclusión

Este proyecto demuestra cómo la inteligencia artificial puede asistir en la toma de decisiones estratégicas en el deporte. La generación textual ofrece gran valor, aunque la parte visual todavía necesita mejoras para representar con precisión jugadas tácticas complejas.

---

> Desarrollado como proyecto final del curso, combinando IA generativa, diseño web y pasión por el básquetbol 🏀.


El usuario selecciona:

Tipo de defensa del rival (Zona, Hombre a hombre, etc.)

Tiempo restante en la posesión

Situación del juego (campo de texto libre)

A partir de esa información, se genera un prompt que es enviado a Gemini para obtener una lista de pasos detallados que conforman una jugada.

Cada paso generado es convertido en una descripción visual en inglés, que se utiliza como prompt para generar una imagen usando Stable Diffusion a través de la API de Hugging Face.

La aplicación muestra tanto los pasos de la jugada como las imágenes generadas para facilitar la comprensión.

Ejemplo de Uso

Defensa seleccionada: Zona 2-3

Tiempo restante: 14 segundos

Situación de juego: "Estamos perdiendo por 2 puntos, última posesión"

La app genera una jugada ofensiva que responde a esa situación y sugiere movimientos de los jugadores numerados del 1 al 5, incluyendo cortes, pantallas y el tiro final.

Limitaciones

Generación de imágenes: Las imágenes generadas por los modelos de difusión no son suficientemente precisas ni detalladas para representar movimientos tácticos complejos o ubicaciones específicas de los jugadores. Por lo tanto, no resultan eficaces como herramienta visual principal.

Cuotas de uso de Gemini: La API de Gemini tiene un límite de uso gratuito que puede ser fácilmente superado, lo que genera errores (por ejemplo, "RESOURCE_EXHAUSTED") y limita el uso continuo de la aplicación.

Recomendaciones

Complementar las imágenes generadas con diagramas hechos a mano o herramientas específicas como FastDraw o KlipDraw.

Considerar el uso de otros modelos para la parte visual o incorporar un sistema de diagramación propio.

Conclusión

Este proyecto demuestra cómo se puede integrar inteligencia artificial generativa en un contexto deportivo para asistir la toma de decisiones estratégicas. Si bien la parte textual ofrece gran utilidad, la generación visual aún presenta desafíos que deberán ser resueltos en futuras iteraciones del sistema.

