import streamlit as st

st.write("👧 K E Y L O G G E R L A D I E S B L O G")
tab1, tab2= st.tabs(["Beranda", "Tentang Kami"])

with tab1:
    st.image("https://blog.cloudflare.com/content/images/2021/01/Hybrid-WAF-keys.png")
    st.write("""
    Holla sis, gan 👋

    Pernah gak sih kalian melihat atau membaca tulisan “ percakapan anda telah terenkripsi secara end-to-end, atau percakapan anda telah terlindungi secara enkripsi” saat menggunakan aplikasi pesan online yang biasa kita gunakan?.
    Enkripsi dalam bidang kriptologi merupakan salah satu proses pengamanan yang dapat memperkecil kemungkinan kejahatan cybercrime menimpa kita.
    Eits, BTW kalian tahu gak sih enkripsi atau end-to-end itu apa? yuk kita bahas bareng-bareng :D
    """)

    st.header("Apa itu Enkripsi?")
    st.image("https://www.egnyte.com/sites/default/files/inline-images/hsVNCfELzr2R0D2YOOBUbXcBgYYXHhcY7lUKrkw9e7vEq8zFQN.png")
    st.write("""
    _Encryption_ atau enkripsi adalah proses untuk membuat suatu susunan acak dari teks yang dapat dibaca oleh manusia (_human-readable plaintext_) menjadi teks yang tidak dapat dibaca oleh manusia dan hanya dimengerti oleh sistem saja (_incomprehensible text_).
    Teks hasil dari enkripsi disebut dengan “_ciphertext_”.

    _Encryption_ ini memang sering digunakan untuk mengamankan data yang berupa informasi atau pesan, hal itu memiliki tujuan yaitu untuk menjaga keamanan dan mencegah pihak tidak bertanggung jawab mengetahui isi dari pesan yang kamu kirimkan.
    Saat pihak yang tidak bertanggung jawab berusaha untuk mengetahui isi pesanmu, mereka hanya akan melihat teks acak yang tidak dapat dimengerti.

    Tapi tenang saja, lawan bicara kamu akan melihat teks tersebut sama seperti yang kamu kirimkan.
    Sebelum disampaikan teks akan melewati proses yang dinamakan dekripsi atau _decrypt_.
    Proses tersebut adalah proses yang mengubah teks acak menjadi teks biasa atau plaintext.
    Dekripsi ini hanya bisa terjadi jika orang memiliki atau diberi akses untuk melihat data yang dienkripsi.
    """)

    st.header("Bagaimana Cara Kerja Enkripsi?")
    st.write("Enkripsi dibedakan dari _encryption key_ yang digunakan, yaitu enkripsi simetris dan enkripsi asimetris. Berikut ini adalah penjelasan keduanya:")

    st.subheader("Enkripsi Simetris")
    st.write("""
    Enkripsi simetris adalah jenis enkripsi yang proses penguncian data dan proses pembukaan datanya dilakukan menggunakan satu kunci yang sama.

    Karena menggunakan satu kunci yang sama, maka algoritma enkripsi pada jenis ini terlihat tidak terlalu kompleks dan cenderung lebih mudah untuk dieksekusi.
    Jenis enkripsi ini adalah pilihan yang tepat untuk membawa transmisi data dalam jumlah besar.
    """)

    st.subheader("Enkripsi Asimetris")
    st.write("""
    Enkripsi asimetris dikenal juga dengan _public-key cryptography_ atau _public-key encryption_.
    Hal ini karena enkripsi jenis ini menggunakan dua kunci yang saling berhubungan, yaitu kunci publik dan kunci pribadi.

    Kunci publik berfungsi untuk mengenkripsi pesan dan dapat diakses oleh semua orang.
    Sedangkan kunci pribadi berfungsi untuk mendekripsi pesan dan hanya dapat diakses oleh pemilik kunci untuk menjaga privasi.

    Jenis enkripsi asimetris lebih kompleks dan memakan lebih banyak waktu.
    Tapi, keamanannya lebih kuat jika dibandingkan dengan enkripsi simetris
    """)

    st.markdown("""---""")

    st.write("""
    Itu adalah beberapa informasi seputar enkripsi atau _encrypt_.
    Secara singkat, _encryption_ memastikan bahwa data atau teksmu tersimpan aman dari _hacker_.
    
    Adapun hasil data atau teks yang terenkripsi disebut sebagai _ciphertext_ yang tidak bisa dipecahkan tanpa _cryptographic key_.
    """)

with tab2:
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")
    with col2:
        st.image("https://aptika.kominfo.go.id/wp-content/uploads/2019/09/digitalent-e1568964668804.jpg")
    with col3:
        st.write("")

    st.write("""
    Keylogger Ladies Blog ini merupakan halaman yang kami persembahkan sebagai platform edukasi mengenai keamanan siber dan informasi khususnya mengenai enkripsi dalam kriptogafi.
    Pembuatan blog ini juga ditujukan untuk memenuhi tugas akhir dalam pelatihan **Women in Tech: Cybersecurity and Python** yang diselenggarakan oleh Program Digital Talen Scholarship Kementerian Komunikasi dan Informatika.
    """)

    st.write("")
    st.write("")
    st.write("Made with ❤,\n\n Ajeng, Nata, dan Zischa.")