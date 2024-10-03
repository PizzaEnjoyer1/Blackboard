import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Mi primer canvas")
st.write("¡Dibuja lo que quieras!")

with st.sidebar:

  st.title("Cambia los parámetros de tu canvas")
  
  drawing_mode = st.selectbox(
    "Selecciona el modo de dibujo",
    ("freedraw", "line", "transform", "rect", "circle")
  )


  stroke_width = st.slider("Grosor del pincel", 1, 100, 10)

  stroke_color = st.color_picker("Selecciona el color de linea", "#000000")

  fill_color = st.color_picker("Selecciona el color de relleno", "#000000")
  
  bg_color = st.color_picker("Selecciona el color del fondo", "#FFFFFF")

 
canvas_result = st_canvas(
    fill_color=fill_color,
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=720,
    width=1280,
    key="canvas",
    drawing_mode = drawing_mode,
)

