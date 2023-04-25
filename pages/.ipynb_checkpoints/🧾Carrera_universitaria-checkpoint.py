import streamlit as st

st.set_page_config(layout="wide",
                  page_title="Carrera_universitaria",
                  page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png")


col1_1, col2_1 = st.columns(2)
with col1_1:
    st.image('images/Certificados/diploma.png')

with col2_1:
    st.write('Soy graduado de la Universidad de Córdoba, ubicada en la hermosa ciudad de Montería, donde completé la carrera de Ingeniería de Sistemas. Durante mi carrera universitaria, adquirí conocimientos sólidos en áreas como la programación, las bases de datos, las redes, la seguridad informática y la gestión de proyectos, lo que me ha permitido enfrentar desafíos complejos y encontrar soluciones innovadoras. Además, tuve la oportunidad de participar en proyectos y programas extracurriculares que me permitieron desarrollar habilidades en liderazgo, trabajo en equipo y comunicación efectiva, lo que me ha sido de gran utilidad en mi carrera profesional. Estoy muy agradecido por la educación de calidad que recibí, y estoy comprometido a seguir aprendiendo y creciendo como profesional en el campo de la ingeniería de sistemas.')

col1_2,col2_2 = st.columns(2)
with col2_2:
    st.image('images/Certificados/diplomado.png')
    
with col1_2:
    st.write('Culminé mis estudios universitarios en la carrera de Ingeniería de Sistemas en la Universidad de Córdoba, pero mi pasión por la tecnología y los datos me llevó a continuar mi educación y adquirir nuevas habilidades en el campo de la ciencia de datos. Fue así como decidí participar en un diplomado en ciencia de datos con Python, donde aprendí a utilizar herramientas de análisis de datos, aprendizaje automático y visualización de datos. Este diplomado fue un punto de inflexión en mi carrera profesional, ya que me permitió combinar mi pasión por la tecnología con mi interés por el análisis de datos. Desde entonces, he estado enfocado en desarrollar habilidades en áreas como el análisis de datos, la estadística y el aprendizaje automático, lo que me ha permitido trabajar en proyectos emocionantes y desafiantes en el campo de la ciencia de datos. Estoy entusiasmado por las oportunidades que me esperan en este campo en constante evolución y comprometido a seguir aprendiendo y creciendo como profesional.')
    