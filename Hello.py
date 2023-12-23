import streamlit as st
import numpy as np

if 'data' not in st.session_state:
    st.session_state.data = np.array([0])

def run():
    st.set_page_config(
        page_title="Implementasi SAW",
        page_icon="👋",
    )

    st.write("# Implementasi Metode SAW")
    st.write("Dikembangkan oleh Khoirul Umam, S.Pd., M.Kom.")

    st.markdown(
        """
        Metode Simple Additive Weighting (SAW) merupakan salah satu metode dalam Sistem Pendukung Keputusan yang implementasinya sangat sederhana. Ide besarnya adalah mengalikan nilai kriteria dengan bobot kriteria yang telah ditentukan. Kemudian hasil perkalian tersebut ditotal untuk mendapatkan nilai akhir. Berdasarkan nilai akhir tersebut, sekumpulan alternatif dapat diranking untuk menentukan alternatif terbaik.
        
        Contoh kasus yang akan diimplementasikan pada aplikasi ini adalah sebagai berikut:

        Sebuah perusahaan akan melakukan rekrutmen kerja terhadap **5 calon pekerja** untuk posisi operator mesin. Posisi yang dibutuhkan hanya **2 orang**. Kriteria seleksi yang digunakan adalah sebagai berikut:

        - Pengalaman kerja (C1), semakin lama pengalaman kerjanya semakin baik
        - Pendidikan (C2), semakin tinggi pendidika terakhirnya semakin baik
        - Usia (C3), semakin dewasa usianya semakin baik
        - Status Perkawinan (C4), yang masih single lebih baik dari pada yang sudah menikah
        - Alamat (C5), yang dekat domisilinya dengan kantor semakin baik.

    """
    )

    c1 = st.number_input("Nilai C1", min_value=0.0, max_value=1.0, value=0.0, step=0.1)

    st.write("Nilai C1: ", c1)

    st.write("Data = ", st.session_state.data)

    st.button("Simpan", on_click=simpanData(c1), type='primary')


def simpanData(dataBaru):
    np.append(st.session_state.data, dataBaru)


if __name__ == "__main__":
    run()