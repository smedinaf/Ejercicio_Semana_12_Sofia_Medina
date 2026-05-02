import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ─────────────────────────────
# CONFIG
# ─────────────────────────────
st.set_page_config(page_title="Wireframe Studio 💖", layout="wide")

# 🎀 GIRLY STYLE
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Fondo */
.stApp {
    background: linear-gradient(135deg, #fff0f5, #ffe4ec);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 2px solid #fbcfe8;
}

/* Títulos */
h1 {
    color: #be185d !important;
    font-weight: 700 !important;
}
h2, h3 {
    color: #9d174d !important;
}

/* Botones */
.stButton > button {
    background: linear-gradient(135deg, #f472b6, #ec4899) !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.2rem !important;
}

/* Canvas card */
.canvas-card {
    background: white;
    border-radius: 20px;
    padding: 20px;
    border: 1px solid #fbcfe8;
    box-shadow: 0 6px 18px rgba(236,72,153,0.15);
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────
# UI
# ─────────────────────────────
st.title("🎀 Wireframe Studio")
st.subheader("Dibuja ideas rápidas de páginas web ✨")

# ─────────────────────────────
# SIDEBAR
# ─────────────────────────────
with st.sidebar:
    st.subheader("💖 Propiedades")

    st.markdown("### 📐 Tamaño del lienzo")
    canvas_width = st.slider("Ancho", 300, 1000, 800, 50)
    canvas_height = st.slider("Alto", 200, 800, 500, 50)

    st.markdown("### 🛠 Herramientas")
    drawing_mode = st.selectbox(
        "Modo de dibujo",
        ("freedraw", "line", "rect", "circle"),
    )

    stroke_width = st.slider('Grosor de línea', 1, 20, 3)

    st.markdown("### 🎨 Estilo UI")
    preset = st.selectbox(
        "Tipo de elemento",
        ["Texto", "Botón", "Navbar", "Card", "Input"]
    )

    colores_ui = {
        "Texto": "#9d174d",
        "Botón": "#ec4899",
        "Navbar": "#be185d",
        "Card": "#f472b6",
        "Input": "#f9a8d4"
    }

    stroke_color = colores_ui[preset]

    st.markdown("### 💡 Ideas rápidas")
    st.markdown("""
    - 🧭 Navbar arriba  
    - 🔲 Cards en grid  
    - 🔘 Botones CTA  
    - 📝 Formularios  
    - 📦 Secciones  
    """)

# ─────────────────────────────
# CANVAS
# ─────────────────────────────
st.markdown('<div class="canvas-card">', unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="rgba(255, 192, 203, 0.2)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="#ffffff",
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key="canvas",
)

st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────
# EXTRA UI
# ─────────────────────────────
col1, col2 = st.columns(2)

with col1:
    if st.button("🧹 Limpiar lienzo"):
        st.rerun()

with col2:
    st.button("💾 Guardar idea (demo)")

st.markdown("### ✨ Tips de diseño")
st.markdown("""
- Usa rectángulos para representar secciones  
- Mantén jerarquía visual (tamaños distintos)  
- Piensa en mobile primero 📱  
- No detalles demasiado, es solo wireframe  
""")
