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
  
  bg_color = st.color_picker("Enter background color", "#FFFFFF")

 
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)"
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
