import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide",
                  page_title="Carrera_universitaria",
                  page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png")

imageUrls = ["https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/Certificado_mintic.png",
             "https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/curso_platzi1.png",
             "https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/curso_platzi2.PNG",
             "https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/curso_platzi3.PNG",
             "https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/curso_platzi4.png",
             "https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/curso_platzi5.PNG",
             "https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/curso_platzi6.PNG",
             "https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/curso_platzi7.png",
             "https://raw.githubusercontent.com/Luisyances1/Certificaciones/main/curso_platzi8.png"
    ]

 # reemplaza con la ruta a tus imágenes

st.write('''
# Estudios complementarios
''')

with st.spinner("Cargando imágenes..."):
    imageCarouselComponent = components.declare_component(
        "image-carousel-component",
        path="./frontend/public")
    selectedImageUrl=imageCarouselComponent(imageUrls=imageUrls, height=200)
    if selectedImageUrl is not None:
        st.image(selectedImageUrl, use_column_width='always')
