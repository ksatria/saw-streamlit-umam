import streamlit as st
import numpy as np
import pandas as pd

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

L = np.array(['benefit','benefit','benefit','cost','cost'])

W = np.array([0.3, 0.2, 0.2, 0.15, 0.15])

def click_button():
    st.session_state.clicked = True

def sample_norm(values, label):
    if not values.shape[1] == label.shape[0]:
        st.write('Jumlah kriteria dan label tidak sama')
        return

    norm_value = []
    norm_all = []

    for i in range(values.shape[0]):
        if label[i] == 'benefit':
            for j in range(values[i].shape[0]):
                norm_c = values[i][j] / np.max(values[i])
                norm_value.append(norm_c)
        elif label[i] == 'cost':
            for j in range(values[i].shape[0]):
                norm_c = np.min(values[i]) / values[i][j]
                norm_value.append(norm_c)

        norm_all.append(norm_value)
        norm_value = []

    return np.array(norm_all)

def calculate_saw(values, weight):
    if not values.shape[1] == weight.shape[0]:
        print('Jumlah kriteria dan bobot tidak sama')
        return

    alt_crit_value = []
    all_value = []
    all_saw = []

    values = np.transpose(values)

    for i in range(values.shape[0]):
        for j in range(values[i].shape[0]):
            val = values[i][j] * weight[j]
            alt_crit_value.append(val)

        all_value.append(alt_crit_value)
        alt_crit_value = []

        saw = np.sum(all_value)
        all_saw.append(saw)
        all_value = []

    return all_saw

def ranking(vector):
    temp = vector.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(vector))

    return len(vector) - ranks

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

    st.divider()

    st.write("## Input Nilai Kriteria")

    c1 = st.number_input("Nilai C1", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
    c2 = st.number_input("Nilai C2", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
    c3 = st.number_input("Nilai C3", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
    c4 = st.number_input("Nilai C4", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
    c5 = st.number_input("Nilai C5", min_value=0.0, max_value=1.0, value=0.0, step=0.1)

    if st.button("Simpan", type='primary', on_click=click_button):
        simpanData(c1,c2,c3,c4,c5)
    
    if st.session_state.clicked:
        data = st.session_state.nilai_kriteria
        df = pd.DataFrame(data, columns=('C1','C2','C3','C4','C5'))
        st.dataframe(df)

        if st.button("Proses"):
            prosesData()


def simpanData(c1,c2,c3,c4,c5):
    if 'nilai_kriteria' not in st.session_state:
        st.session_state.nilai_kriteria = np.array([[c1,c2,c3,c4,c5]])
    else:
        dataLama = st.session_state.nilai_kriteria
        dataBaru = np.append(dataLama, [[c1,c2,c3,c4,c5]], axis=0)
        st.session_state.nilai_kriteria = dataBaru

def prosesData():
    A = st.session_state.nilai_kriteria

    norm_a = sample_norm(A, L)
    saw = calculate_saw(norm_a, W)
    rank = ranking(np.asarray(saw))

    st.write("Nilai alternatif:")
    st.text(A)

    st.write("Normalisasi nilai alternatif:")
    st.text(norm_a)

    st.write("Perhitungan nilai SAW:")
    st.text(saw)

    st.write("Perankingan:")
    st.text(rank)


if __name__ == "__main__":
    run()
