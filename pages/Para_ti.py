import streamlit as st
import base64

st.set_page_config(layout="wide",
                  page_title="Carrera_universitaria",
                  page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png")


st.sidebar.image("images/felicidades.jpeg")
st.sidebar.markdown("<h3 style='color: white;'> La suegrita que mas quiero Jajajajaj </h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'> SOFIA </h1>", unsafe_allow_html=True)
st.write('''
<h2 style='text-align: center; color: white;'> ¡Felicidades! </h2>

Tenia bastante tiempo que no escribia algo para alguien, se siente un poco raro jajajaaj, pero lo hago de corazon y
con mucho cariño.
De todas las cosas que te quiero decir, comenzare por felicitarte, mira hasta donde has llegado, mira todo lo que has conocido, todo lo que has aprendido, a tan corta edad. eres el vivo ejemplo de lo que significa la frase "*Querer es poder*", estoy seguro que aun te faltan muchas cosas para ti estoy mas que seguro, por todo lo que trabajas, por todo lo que te esfuerzas y por todo el empeño que siempre pones en las cosas que haces, por que siempre le pones corazon,.

Tienes tantas cualidades que tal ves me cansaria primero entes que escribirlas todas :smile: te dire algo que ya sabes, pero es bueno que lo recuerdes y lo sepas, YO CREO Y CONFIO EN TI, nunca lo olvides, siempre vas a poder contar conmigo
dire algo relacionado a tu padre con todo el respeto que el merece, siempre te quizo y estoy seguro que donde quiera que se encuentre, te sigue queriendo, sus sentimientos seran imborrables en ti, tu papa fue mi gran amigo en el poco tiempo que convivi con el, en ese tiempo logre ver todo lo que te queria, y los grandes deseos de exito que tenia sobre ti, por eso recuerdalo siempre con alegria, con esperanzas, cuando sientas angustia o miedo, recuerda que tu padre creeia y confiaba en ti, eres una guerrera como tu madre que nunca se ha rendido apesar de todo por lo que ha podido pasar
asi que animo, animo, ¡ANIMO!

Sofia hoy en estas fecha tan especial, yo quiero desearte, desde el fondo de mi corazon, con alegria y con mucho mucho cariño para ti un feliz FELIZ CUMPLEAÑOS 
Tus fortalezas son mas grandes que tus miedos nunca lo olvides
sin mas que decir, la quiero mucho y que cumplas muchos años y logros mas

''', unsafe_allow_html=True)

st.image('images/fondo.jpeg')

c1,c2,c3 = st.columns(3)
with c2:
    st.write('Presiona el boton')
    if st.button('¡FELICIDADES!'):
        st.balloons()
