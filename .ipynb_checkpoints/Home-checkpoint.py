import streamlit as st

st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Portafolio web")


col1, col2 = st.columns(2)
with col1:
    st.image("images/image_home_1.jpeg")

with col2:
    st.write(
'''
# Luis Miguel Yances Castillo
## Ingeniero de sistemas

- :derelict_house_building: Bello-Antioquia
- :e-mail: luisyances1@gmail.com
- :smiley_cat: https://github.com/Luisyances1
- :bar_chart: Universidad de cordoba-colombia

'''
)
st.write('Como ingeniero de sistemas, poseo experiencia en el diseño, desarrollo, implementación y mantenimiento de sistemas informáticos y tecnologías de la información. Cuento con sólidos conocimientos en programación, bases de datos, redes, seguridad informática y gestión de proyectos, lo que me permite enfrentar desafíos complejos y encontrar soluciones innovadoras. Además, tengo una tendencia hacia la ciencia de datos, lo que me ha llevado a desarrollar habilidades en áreas como el análisis de datos, el aprendizaje automático y la visualización de datos. Estoy comprometido con la excelencia en el trabajo y en mantenerme actualizado en las últimas tendencias y tecnologías del sector, lo que me ha permitido desarrollar una carrera sólida y exitosa en este campo.')
st.sidebar.write('Contenido')
