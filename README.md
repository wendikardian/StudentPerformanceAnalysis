# Latar Belakang Masalah
Jaya Jaya Institut menghadapi tingkat dropout siswa yang tinggi, yang dapat berdampak buruk pada reputasi institusi, efektivitas pembelajaran, dan pendapatan jangka panjang. Penurunan jumlah siswa yang menyelesaikan program studi juga mencerminkan kurangnya keberhasilan institusi dalam mendukung siswa untuk mencapai hasil akademik yang optimal.

Tantangan utama adalah mendeteksi siswa yang berisiko dropout sedini mungkin agar mereka dapat diberi bimbingan atau dukungan khusus. Pendekatan ini membutuhkan pemahaman yang mendalam tentang pola dan faktor yang berkontribusi terhadap kemungkinan siswa melakukan dropout.

## Tujuan Utama

### a. Permasalahan Bisnis
**Pertanyaan bisnis:**
- Apa faktor utama yang memengaruhi seorang mahasiswa untuk tidak menyelesaikan studinya (dropout)?
- Sejauh mana keterlibatan akademik mahasiswa (jumlah mata kuliah yang diambil, dievaluasi, atau diselesaikan) memengaruhi kelulusan mereka?
- Bagaimana pengaruh kondisi ekonomi makro (seperti tingkat pengangguran, inflasi, dan PDB) terhadap keberhasilan mahasiswa dalam menyelesaikan pendidikan?
- Bagaimana Membangun Model Prediksi untuk Mendeteksi Dropout?

### b. Cakupan Proyek
- **Membangun Model Machine Learning:**
    - Mengembangkan model prediksi untuk mengidentifikasi siswa yang berpotensi melakukan dropout berdasarkan data historis.
    - Menggunakan metrik evaluasi seperti akurasi, precision, recall, dan F1-score untuk menilai performa model.
    
- **Mencari Fitur yang Paling Penting:**
    - Melakukan analisis fitur untuk mengidentifikasi variabel yang paling memengaruhi prediksi dropout, seperti nilai rata-rata, status keuangan, dan beban kurikulum.
    
- **Mengembangkan Dashboard Otomatis:**
    - Membuat dashboard interaktif menggunakan business intelligence tools seperti public tableau untuk memvisualisasikan data performa siswa.
    - Dashboard akan menyajikan statistik dropout, analisis fitur penting, serta status siswa secara individual.
    
- **Mendeploy Model dengan Streamlit:**
    - Membangun aplikasi berbasis Streamlit untuk memungkinkan tim akademik melakukan prediksi secara langsung.
    - Aplikasi akan menyediakan antarmuka sederhana untuk memasukkan data siswa dan mendapatkan hasil prediksi dropout secara real-time.

## Persiapan Data
- **Sumber data:** [Data Source](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)
- **Struktur data:** 37 kolom, 4,424 baris data

### Kolom Utama:
- **Status (target variabel):** Mengindikasikan status kelulusan atau keberlanjutan mahasiswa, dengan kemungkinan seperti "Graduate", "Enrolled", atau "Dropout".

### Fitur Penting:
- **Marital_status:** Status pernikahan mahasiswa.
- **Application_mode:** Cara/kategori aplikasi penerimaan mahasiswa.
- **Previous_qualification:** Kualifikasi/tingkat pendidikan sebelumnya dari mahasiswa.
- **Previous_qualification_grade:** Nilai kualifikasi sebelumnya (float).
- **Nacionality:** Kode numerik untuk kebangsaan mahasiswa.
- **Admission_grade:** Nilai penerimaan yang diperoleh mahasiswa (float).
- **Tuition_fees_up_to_date:** Status pembayaran biaya kuliah mahasiswa.
- **Age_at_enrollment:** Usia mahasiswa saat mendaftar pertama kali.
- **Curricular_units_1st_sem_enrolled & Curricular_units_2nd_sem_enrolled:** Jumlah unit kurikulum yang diambil mahasiswa.
- **Curricular_units_1st_sem_approved & Curricular_units_2nd_sem_approved:** Jumlah unit yang disetujui atau diselesaikan mahasiswa.
- **Unemployment_rate:** Tingkat pengangguran (makro ekonomi).
- **Inflation_rate:** Tingkat inflasi (makro ekonomi).
- **GDP:** Produk Domestik Bruto, sebagai indikator ekonomi makro.

## Tugas Awal:
- **Visualisasi Distribusi Status**
- **Analisis Korelasi**
- **Analisis Fitur Kategorikal**

### Setup Environment
Untuk mempersiapkan lingkungan kerja Anda, gunakan perintah berikut:

#### Langkah installasi
```bash
pip install -r requirements.txt
pip list
```

#### Langkah Menjalankan Skrip
Gunakan perintah berikut di terminal:
```bash
streamlit run app.py
```

Untuk mengakses link streamlit online untuk mengecek prototype, bisa akses link berikut: [Streamlit Prototype](https://wendistudentanalysis.streamlit.app/)

### Dashboard
Akses link tableau dalam link berikut: [Tableau Dashboard](https://public.tableau.com/views/StudentPerformanceAnalysis_17331387560340/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


## Temuan Utama:
### Faktor Utama untuk Dropout:
- Mahasiswa dengan skor keterlibatan rendah lebih cenderung mengalami dropout.
- Lebih banyak pria yang dropout dibandingkan wanita.

### Pengaruh Keterlibatan Akademik:
- Mahasiswa yang mengambil dan menyelesaikan lebih banyak unit kurikulum lebih cenderung lulus.

### Pengaruh Kondisi Ekonomi Makro:
- **GDP:** Tidak ada korelasi langsung terlihat, tetapi umumnya kondisi ekonomi yang lebih baik dapat mendukung kelulusan.
- **Tingkat Pengangguran:** Tingkat pengangguran tinggi mungkin berhubungan dengan kenaikan dropout.
- **Inflasi:** Tingkat inflasi tinggi dapat mempengaruhi keberhasilan dengan menambahkan tekanan ekonomi pada mahasiswa.

## Conclusion:
- Keterlibatan akademik rendah berkontribusi pada dropout.
- Pria lebih banyak mengalami dropout dibandingkan wanita.
- Mahasiswa yang menyelesaikan lebih banyak unit kurikulum cenderung lulus.
- Tingkat pengangguran tinggi dan inflasi dapat meningkatkan risiko dropout.
- Kondisi ekonomi makro yang lebih baik cenderung mendukung kelulusan.
- Random Forest Algorithm menghasilkan akurasi terbaik dibandingkan Logistic Regression.

## Recommender Action:
- **Mentoring:** Implementasikan program bimbingan akademik.
- **Workshops:** Adakan lokakarya keterampilan belajar.
- **Tracking:** Gunakan sistem untuk memantau keterlibatan mahasiswa.
- **Gender Initiatives:** Kembangkan inisiatif khusus untuk pria.
- **Peer Support:** Bentuk kelompok dukungan mahasiswa pria.
- **Financial Aid:** Tingkatkan akses beasiswa dan bantuan keuangan.
- **Industry Partnerships:** Sediakan magang berbayar.
- **Flexible Learning:** Perkenalkan jadwal fleksibel dan opsi online.
- **Modular Courses:** Implementasikan kursus modular.
- **Counseling:** Pastikan akses ke layanan konseling.
- **Balance Workshops:** Selenggarakan lokakarya keseimbangan hidup.