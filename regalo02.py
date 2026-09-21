import streamlit as st

# ==================================================
# CONFIGURACIÓN
# ==================================================

st.set_page_config(
    page_title="Para una amiga especial 💛",
    page_icon="🌻",
    layout="centered"
)

# ==================================================
# DISEÑO
# ==================================================

st.markdown("""
<style>

.stApp {
    background-color: #fffdf0;
    color: #222222;
}

/* Todo el texto */
.stApp p,
.stApp label,
.stApp span,
.stApp div {
    color: #222222;
}

/* Títulos */
h1, h2, h3 {
    color: #222222 !important;
}

/* Botones */
.stButton > button {
    color: #222222 !important;
    background-color: #fff4a8;
    border: 2px solid #222222;
    border-radius: 15px;
    font-size: 17px;
    font-weight: bold;
}

/* Texto de las cajas */
.caja {
    background-color: white;
    border: 2px solid #222222;
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    color: #222222;
}

.flores {
    text-align: center;
    font-size: 60px;
}

.gatitos {
    text-align: center;
    font-size: 80px;
}

.cancion {
    background-color: #fff8d6;
    border: 2px solid #e0b800;
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    color: #222222;
}

.carta {
    background-color: #fff8d6;
    border: 2px solid #e0b800;
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    color: #222222;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# CONTROL DE PÁGINAS
# ==================================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"


# ==================================================
# PÁGINA PRINCIPAL
# ==================================================

if st.session_state.pagina == "inicio":

    st.title("🌻 Feliz Día de las Flores Amarillas 🌻")

    st.subheader("21 de septiembre 💛")

    st.markdown(
        '<div class="flores">🌻💛🌼💛🌻</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.header("✨ Tengo una sorpresa para ti ✨")

    st.write(
        "Hice esta pequeña página especialmente para ti, "
        "porque eres una persona muy especial para mí. 💛"
    )

    st.write(
        "Aunque nuestra historia haya cambiado, siempre voy "
        "a guardar con cariño los momentos bonitos que vivimos."
    )

    st.write(
        "Por eso quise hacerte este pequeño detalle por "
        "el Día de las Flores Amarillas. 🌻"
    )

    st.write("")

    st.subheader("💛 Elige una sorpresa")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎵 Música", use_container_width=True):
            st.session_state.pagina = "musica"
            st.rerun()

    with col2:
        if st.button("💐 Flores", use_container_width=True):
            st.session_state.pagina = "flores"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        if st.button("💌 Carta", use_container_width=True):
            st.session_state.pagina = "carta"
            st.rerun()

    with col4:
        if st.button("🐱 Abrazo", use_container_width=True):
            st.session_state.pagina = "abrazo"
            st.rerun()


# ==================================================
# MÚSICA
# ==================================================

elif st.session_state.pagina == "musica":

    st.title("🎵 Música para ti")

    st.markdown(
        '<div class="flores">🎶🤎🎶</div>',
        unsafe_allow_html=True
    )

    st.header("Te Amo y Más")

    st.write(
        "Quise poner esta canción porque me recuerda a "
        "una persona que fue muy especial para mí."
    )

    st.write(
        "Aunque nuestra historia cambió, hay recuerdos que "
        "siempre voy a guardar con mucho cariño. 💛"
    )

    st.write("")

    st.markdown("""
    <div class="cancion">

    <h3>🎵 Te Amo y Más</h3>

    <p>
    "Amor más que amor es el nuestro..."
    </p>

    <p>
    Una canción para recordar los momentos bonitos
    que alguna vez compartimos. 🤎
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎧 Escuchar canción")

    st.write(
        "Si tienes el archivo de audio que puedes utilizar, "
        "guárdalo en la misma carpeta que tu programa."
    )

    # EJEMPLO:
    # st.audio("te_amo_y_mas.mp3")

    st.write("")

    st.info(
        "Para reproducirla, coloca tu archivo MP3 en la carpeta "
        "del programa y utiliza: st.audio(\"te_amo_y_mas.mp3\")"
    )

    st.write("")

    if st.button("← Regresar al inicio", use_container_width=True):
        st.session_state.pagina = "inicio"
        st.rerun()


# ==================================================
# FLORES
# ==================================================

elif st.session_state.pagina == "flores":

    st.title("💐 Elige tus flores")

    st.write(
        "Ahora puedes elegir las flores amarillas que más te gusten. 💛"
    )

    st.write("")

    opcion = st.selectbox(
        "🌻 ¿Qué flores quieres?",
        [
            "🌻 Girasoles",
            "🌷 Tulipanes amarillos",
            "🌼 Gerberas",
            "🌹 Rosas amarillas",
            "🌼 Margaritas"
        ]
    )

    st.write("")

    if opcion == "🌻 Girasoles":

        st.markdown(
            '<div class="flores">🌻🌻🌻🌻🌻</div>',
            unsafe_allow_html=True
        )

        st.header("🌻 Girasoles")

        st.write(
            "Un hermoso ramo de girasoles para llenar "
            "tu día de luz y alegría. 💛"
        )

    elif opcion == "🌷 Tulipanes amarillos":

        st.markdown(
            '<div class="flores">🌷🌷🌷🌷🌷</div>',
            unsafe_allow_html=True
        )

        st.header("🌷 Tulipanes amarillos")

        st.write(
            "Un ramo de tulipanes amarillos para una "
            "persona muy especial. 💛"
        )

    elif opcion == "🌼 Gerberas":

        st.markdown(
            '<div class="flores">🌼🌼🌼🌼🌼</div>',
            unsafe_allow_html=True
        )

        st.header("🌼 Gerberas")

        st.write(
            "Gerberas llenas de color, alegría y mucho cariño. 💛"
        )

    elif opcion == "🌹 Rosas amarillas":

        st.markdown(
            '<div class="flores">🌹🌹🌹🌹🌹</div>',
            unsafe_allow_html=True
        )

        st.header("🌹 Rosas amarillas")

        st.write(
            "Rosas amarillas como símbolo de nuestra amistad. 💛"
        )

    else:

        st.markdown(
            '<div class="flores">🌼🌼🌼🌼🌼</div>',
            unsafe_allow_html=True
        )

        st.header("🌼 Margaritas")

        st.write(
            "Margaritas para hacer tu día un poquito más bonito. 💛"
        )

    st.write("")

    if st.button("← Regresar al inicio", use_container_width=True):
        st.session_state.pagina = "inicio"
        st.rerun()


# ==================================================
# CARTA
# ==================================================

elif st.session_state.pagina == "carta":

    st.title("💌 Una carta para ti")

    st.markdown(
        '<div class="flores">💛💌🌻💌💛</div>',
        unsafe_allow_html=True
    )

    st.header("Para una amiga muy especial 💛")

    st.write(
        "Quería hacerte este pequeño detalle porque, aunque "
        "nuestra historia haya cambiado, sigues siendo una "
        "persona muy importante para mí."
    )

    st.write(
        "Fuimos parte importante de la vida de la otra y "
        "compartimos momentos que siempre voy a recordar "
        "con mucho cariño."
    )

    st.write(
        "Gracias por las risas, las pláticas, los recuerdos "
        "y por todos esos pequeños momentos que hicieron "
        "especial nuestra historia."
    )

    st.write(
        "Tal vez las cosas cambiaron, pero eso no borra "
        "todo lo bonito que vivimos."
    )

    st.write(
        "Hoy quise regalarte flores amarillas como un pequeño "
        "detalle para decirte gracias por haber formado parte "
        "de mi vida. 🌻"
    )

    st.write(
        "Espero que estés bien, que sonrías mucho y que "
        "vengan para ti muchos momentos bonitos."
    )

    st.write("")

    st.subheader("🌻 Feliz 21 de septiembre 🌻")

    st.write("Con mucho cariño. 💛")

    st.write("")

    if st.button("← Regresar al inicio", use_container_width=True):
        st.session_state.pagina = "inicio"
        st.rerun()


# ==================================================
# ABRAZO
# ==================================================

elif st.session_state.pagina == "abrazo":

    st.title("🐱💛 Un abrazo para ti 💛🐱")

    st.markdown(
        '<div class="gatitos">🐱🫂🐱</div>',
        unsafe_allow_html=True
    )

    st.header("Un abrazo de gatitos 🤗")

    st.write(
        "Porque hay momentos en los que no hacen falta "
        "muchas palabras..."
    )

    st.write(
        "Solo un abrazo. 💛"
    )

    st.write("")

    if st.button("🤗 Dar abrazo", use_container_width=True):

        st.balloons()

        st.markdown(
            '<div class="gatitos">🐱💛🫂💛🐱</div>',
            unsafe_allow_html=True
        )

        st.success(
            "¡Abrazo enviado! Espero que te llegue con mucho cariño. 💛"
        )

    st.write("")

    st.write(
        "Aunque sea un abrazo virtual, está hecho especialmente para ti."
    )

    st.write("")

    if st.button("← Regresar al inicio", use_container_width=True):
        st.session_state.pagina = "inicio"
        st.rerun()
