import streamlit as st

# Configuración visual de la página
st.set_page_config(
    page_title="Solicita tu DiDi Card | Sin Anualidad",
    page_icon="💳",
    layout="centered"
)

# Estilos visuales
st.markdown("""
    <style>
    .main {
        background-color: #FAFAFA;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF5E00;
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 12px;
        border-radius: 8px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💳 Tarjeta de Crédito DiDi Card")
st.caption("Solicitud rápida, digital y sin historial crediticio obligatorio.")

st.divider()

st.markdown("""
### 🔥 Beneficios Destacados:
* **Sin Anualidad de por vida:** Olvídate de cuotas de mantenimiento.
* **6% de Cashback:** Recibe reembolso de hasta 6% en la categoría que tú elijas.
* **Aprobación en minutos:** Proceso 100% en línea desde la app.
* **Tarjeta Digital Inmediata:** Compra en línea al instante tras la aprobación.
""")

st.divider()

# Tu enlace oficial
LINK_DIDICARD = "https://d.didiglobal.com/5dmuYbg?r=MGM_homepage_pop&c=M2"

st.info("💡 **Consejo:** Ten a la mano tu INE vigente para agilizar el registro.")

# Botón principal
st.link_button("👉 SOLICITAR MI DIDI CARD AHORA", LINK_DIDICARD, use_container_width=True)

st.caption("Proceso oficial y seguro a través de DiDi México.")
