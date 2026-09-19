import streamlit as st

# Configuración de la pestaña del navegador
st.set_page_config(page_title="Para mis mejores amigas 💛", page_icon="🌻", layout="centered")

# Estilos visuales estéticos (Cajas de diseño personalizadas sin usar imágenes externas)
st.markdown("""
    <style>
    /* Fondo de la aplicación */
    .stApp {
        background-color: #fffef2;
    }
    
    /* Caja principal estilo Sticker interactivo */
    .main-card {
        background-color: #ffffff;
        border: 4px solid #1a1a1a;
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        box-shadow: 8px 8px 0px #1a1a1a;
        max-width: 500px;
        margin: auto;
    }
    
    /* Títulos principales */
    .title-text {
        font-family: 'Comic Sans MS', sans-serif;
        color: #1a1a1a;
        font-size: 28px;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    
    .subtitle-text {
        font-family: 'Comic Sans MS', sans-serif;
        color: #4a4a4a;
        font-size: 18px;
        margin-bottom: 25px;
    }
    
    /* Contenedor circular animado para los emojis principales */
    .emoji-avatar {
        background-color: #fff9db;
        border: 3px solid #1a1a1a;
        border-radius: 50%;
        width: 130px;
        height: 130px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 70px;
        margin: 0 auto 25px auto;
        box-shadow: 4px 4px 0px #1a1a1a;
    }
    
    /* Caja especial estilo pergamino para la letra de la canción */
    .lyrics-box {
        background-color: #fffdf0;
        border: 2px dashed #ffde4d;
        border-radius: 16px;
        padding: 22px;
        margin: 20px 0;
        font-family: 'Georgia', serif;
        font-style: italic;
        color: #444444;
        line-height: 1.8;
        font-size: 16px;
        box-shadow: inset 0px 0px 10px rgba(0,0,0,0.01);
        text-align: center;
    }
    
    /* Tarjetas de flores interactivas dibujadas digitalmente */
    .flower-box {
        background: linear-gradient(135deg, #fff9db 0%, #fff3b3 100%);
        border: 3px solid #1a1a1a;
        border-radius: 20px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 5px 5px 0px #1a1a1a;
        text-align: center;
    }
    
    .flower-icon {
        font-size: 65px;
        margin-bottom: 10px;
    }
    
    .final-text {
        font-family: 'Comic Sans MS', sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: #1a1a1a;
        margin-top: 30px;
        letter-spacing: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# Controlar el cambio de pantallas en la sesión
if "mostrar_sorpresa" not in st.session_state:
    st.session_state.mostrar_sorpresa = False

# --- PANTALLA 1: La Invitación Inicial ---
if not st.session_state.mostrar_sorpresa:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # Dibujo de avatar con Snoopy y flores representado en combinación de Emojis estéticos
    st.markdown('<div class="emoji-avatar">🐶💐</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="title-text">¡HOLA PRECIOSA! ✨</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">¿Te gustaría recibir tu detalle del 21 de septiembre? 💛</div>', unsafe_allow_html=True)
    
    # Columnas para los botones interactivos
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("NO GRACIAS", use_container_width=True):
            st.toast("❌ ¡Esa opción no existe hoy! Intenta con la otra, jaja. 🌻😜")
            
    with col2:
        if st.button("SI POR FAVOR", type="primary", use_container_width=True):
            st.session_state.mostrar_sorpresa = True
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: La Sorpresa (Flores Amarillas Virtuales) ---
else:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # EFECTO ESPECIAL: Dispara una lluvia de globos y confeti en la pantalla
    st.balloons() 
    
    st.markdown('<div class="title-text">🌻 ¡TUS FLORES AMARILLAS! 🌻</div>', unsafe_allow_html=True)
    
    # Dibujo digital de Snoopy celebrando con su flor amarilla
    st.markdown('<div class="emoji-avatar">🕺💛</div>', unsafe_allow_html=True)
    
    # Tu hermoso mensaje personalizado para tus amigas
    st.markdown("""
    <div style='font-family: "Comic Sans MS", sans-serif; font-size: 16px; color: #222222; text-align: justify; margin-bottom: 10px; line-height: 1.5;'>
    Hice esto especialmente para ti porque <b>te quiero un chingo</b>. Gracias por ser una amiga tan increíble, 
    por estar siempre conmigo y por hacer mis días mucho más felices. ¡Te mereces todas las flores amarillas del mundo hoy y siempre! 💛✨
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # SECCIÓN DE LA LETRA: Tu fragmento exacto solicitado de Floricienta
    st.markdown('<div style="font-family: \'Comic Sans MS\', sans-serif; font-weight: bold; color: #1a1a1a; text-align: left;">🎵 Flores Amarillas 🌸</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="lyrics-box">
        "Ella sabía que él sabía<br>
        Que algún día pasaría<br>
        Que vendría a buscarla<br>
        Con sus flores amarillas... 💛"<br>
        <br>
        "No te apures, no te detengas<br>
        Al instante del encuentro<br>
        Está dicha que es hecho, no la pierdas<br>
        No hay derecho..."<br>
        <br>
        "No te olvides que la vida<br>
        Casi nunca está dormida..."✨
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # SECCIÓN INTERACTIVA: Selección manual de su ramo de flores
    st.markdown('<div style="font-family: \'Comic Sans MS\', sans-serif; font-weight: bold; margin-bottom: 10px; color: #1a1a1a;">👇 Elige qué ramo de flores amarillas quieres que dibuje para ti hoy:</div>', unsafe_allow_html=True)
    
    opcion_flor = st.selectbox(
        "Selecciona tus flores:",
        ["Un ramo gigante de Girasoles 🌻", "Un ramo elegante de Tulipanes Amarillos 🌷", "Un ramo hermoso de Rosas Amarillas 🌹"],
        label_visibility="collapsed"
    )
    
    # Renderizar las flores dinámicamente según la selección
    if "Girasoles" in opcion_flor:
        st.markdown("""
            <div class="flower-box">
                <div class="flower-icon">🌻🌻🌻</div>
                <b style="font-family: 'Comic Sans MS', sans-serif; font-size: 16px; color: #1a1a1a;">¡Ramo de Girasoles Brillantes!</b><br>
                <span style="font-family: 'Comic Sans MS', sans-serif; font-size: 14px; color: #4a4a4a;">Tan radiantes y únicos como tu hermosa sonrisa. 😊💛</span>
            </div>
        """, unsafe_allow_html=True)
    elif "Tulipanes" in opcion_flor:
        st.markdown("""
            <div class="flower-box">
                <div class="flower-icon">🌷🌷🌷</div>
                <b style="font-family: 'Comic Sans MS', sans-serif; font-size: 16px; color: #1a1a1a;">¡Ramo de Tulipanes Perfectos!</b><br>
                <span style="font-family: 'Comic Sans MS', sans-serif; font-size: 14px; color: #4a4a4a;">Elegantes, llenos de luz y de buena vibra para ti. ✨☀️</span>
            </div>
        """, unsafe_allow_html=True)
    elif "Rosas" in opcion_flor:
        st.markdown("""
            <div class="flower-box">
                <div class="flower-icon">🌹🌹🌹</div>
                <b style="font-family: 'Comic Sans MS', sans-serif; font-size: 16px; color: #1a1a1a;">¡Ramo de Rosas Amarillas!</b><br>
                <span style="font-family: 'Comic Sans MS', sans-serif; font-size: 14px; color: #4a4a4a;">El símbolo de la amistad más sincera, chingona y pura que existe. 🤝💛</span>
            </div>
        """, unsafe_allow_html=True)
        
    st.write("---")
    
    # Despedida solicitada
    st.markdown('<div class="final-text">FIN 🌻</div>', unsafe_allow_html=True)
    
    # Botón de reinicio
    if st.button("Volver a empezar", use_container_width=True):
        st.session_state.mostrar_sorpresa = False
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)