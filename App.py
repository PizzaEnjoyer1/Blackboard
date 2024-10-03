import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("My first canvas")
st.write("Draw anything you want!")

with st.sidebar:

  st.title("Cambia los parámetros de tu canvas")
  
  drawing_mode = st.selectbox(
    "Selecciona el modo de dibujo",
    ("freedraw", "line", "transform", "rect", "circle")
  )


  stroke_width = st.slider("Grosor del pincel", 1, 100, 10)

  stroke_color = st.color_picker("Selecciona un color", "#000000")

  fill_color = st.color_picker("Selecciona el color de relleno, "#FFFFFF")
  
  bg_color = st.color_picker("Enter background color", "#FFFFFF")

 
canvas_result = st_canvas(
    fill_color=fill_color  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=720,
    width=1280,
    key="canvas",
    drawing_mode = drawing_mode
)

if canvas_result is not None:
    st.image(canvas_result)
