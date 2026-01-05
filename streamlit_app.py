import streamlit as st

st.set_page_config(
    page_title="Kalkulator Kimia Analisis",
    page_icon="⚗️",
    layout="centered"
)

st.title("🧪 Selamat datang di Kalkulator Kimia Analisis")
st.write("### Silahkan pilih menu di bawah ini")

menu = st.selectbox(
    "Pilih jenis perhitungan:",
    (
        "Faktor Pengenceran",
        "Normalitas",
        "Molaritas",
        "Mg/L",
        "% b/v",
        "% b/b",
        "% v/v"
    )
)

st.markdown("---")

# =========================
# MENU FAKTOR PENGENCERAN
# =========================
if menu == "Faktor Pengenceran":

    st.subheader("⚗️ Faktor Pengenceran")

    sub_menu = st.radio(
        "Pilih perhitungan:",
        (
            "Faktor pengenceran",
            "Volume yang harus diambil"
        )
    )

    st.markdown("---")

    # 1. Faktor Pengenceran
    if sub_menu == "Faktor pengenceran":
        st.write("### Faktor pengenceran")

        volume_labu = st.number_input(
            "Masukkan volume labu takar yang ingin digunakan (mL)",
            min_value=0.0,
            format="%.3f"
        )

        volume_pipet = st.number_input(
            "Masukkan volume yang dipipet (mL)",
            min_value=0.0,
            format="%.3f"
        )

        if st.button("Hitung Faktor Pengenceran"):
            if volume_pipet == 0:
                st.error("Volume yang dipipet tidak boleh 0.")
            else:
                faktor_pengenceran = volume_labu / volume_pipet
                st.success(f"✅ Faktor pengenceran = **{faktor_pengenceran:.3f}**")

    # 2. Volume yang Harus Diambil
    elif sub_menu == "Volume yang harus diambil":
        st.write("### Volume yang harus diambil")

        konsentrasi_awal = st.number_input(
            "Masukkan konsentrasi larutan yang ingin diambil",
            min_value=0.0,
            format="%.3f"
        )

        konsentrasi_akhir = st.number_input(
            "Masukkan konsentrasi larutan yang ingin dibuat",
            min_value=0.0,
            format="%.3f"
        )

        volume_akhir = st.number_input(
            "Masukkan volume larutan yang ingin dibuat (mL)",
            min_value=0.0,
            format="%.3f"
        )

        if st.button("Hitung Volume yang Harus Diambil"):
            if konsentrasi_awal == 0:
                st.error("Konsentrasi larutan yang ingin diambil tidak boleh 0.")
            else:
                volume_diambil = (volume_akhir * konsentrasi_akhir) / konsentrasi_awal
                st.success(
                    f"✅ Volume larutan yang harus diambil = **{volume_diambil:.3f} mL**"
                )
