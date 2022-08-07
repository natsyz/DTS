import streamlit as st

st.write("📚 A R T I K E L")
tab1, tab2, tab3 = st.tabs(["Tipe Enkripsi", "Pros & Cons", "Hashing?"])

with tab1:
    st.title("Tipe Enkripsi")
    st.caption("Minggu, 07 Agustus 2022")
    st.write("""
    Selain dibedakan berdasarkan jenisnya yaitu enkripsi simetris dan asimetris, enkripsi juga memiliki beberapa tipe yang dilihat dari kebutuhan penggunaan, infrastruktur, maupun parameter lainnya.
    
    * **Encryption as a service (EaaS)**, menyewakan enkripsi bagi pengguna dengan sumber daya yang sedikit dan tidak mampu membuat enkripsi sendiri. Pada enkripsi tipe ini, pengguna perlu mematuhi segala peraturan yang berlaku dan selalu menjaga data mereka di lingkungan penyewa.
    * **Bring your own encryption (BYOE)**, enkripsi tipe ini cocok untuk pengguna layanan _cloud_ yang ingin mengelola perangkat lunak dan kunci enkripsi mereka sendiri.
    * **Cloud storage encryption**, merupakan tipe enkripsi yang disediakan oleh penyedia layanan cloud. Mereka mengenkripsi data menggunakan algoritma dan penyimpanan mereka sendiri, sehingga pengguna hanya perlu menyewanya.
    * **Deniable encryption**, adalah tipe enkripsi yang memungkinkan data terenkripsi untuk didekripsi dalam dua cara atau lebih berdasarkan kunci enkripsi yang digunakan oleh suatu pihak
    * **Column-level encryption**, cocok digunakan untuk enkripsi basis data. Di mana setiap sel dalam kolom data tertentu dapat diakses dengan kata sandi yang sama.
    * **Field-level encryption**, enkripsi jenis ini mengelola suatu enkripsi data pada bidang tertentu dari halaman web. Misalnya, mengenkripsi nomor KTP, nomor kartu kredit, dll.
    * **End-to-end encryption (E2EE)**, adalah tipe enkripsi yang banyak digunakan oleh aplikasi _chatting_. Enkripsi E2EE memastikan komunikasi antara dua pihak tidak dapat dibaca oleh pihak lain.
    * **Full-disk encryption (FDE)**, enkripsi jenis ini bekerja pada tingkat _hardware_ dan mengubah semua data pada disket menjadi bentuk yang tidak bisa dipahami. FDE hanya dapat diakses oleh orang tertentu yang memiliki kunci autentikasi.
    * **Network-level encryption**, merupakan tipe enkripsi yang mengandalkan jaringan internet melalui Internet Protocol Security (IPSec). Enkripsi tipe ini memastikan komunikasi yang aman di level transfer jaringan.
    * **Link-level encryption**, tipe enkripsi ini ada pada level tautan atau _link_. Di mana data dienkripsi saat dikirim dari _host_, dan didekripsi saat mencapai tautan selanjutnya.
    * **Hypertext Transfer Protocol Secure (HTTPS)**, mengenkripsi setiap konten yang dikirim oleh _web server_ dan melakukan verifikasi apakah public-key encryption telah terinstall.
    * **Homomorphic encryption**, adalah tipe enkripsi yang mengubah data menjadi _ciphertext_ yang dapat diproses, sehingga memungkinkan pengguna untuk melakukan operasi kompleks pada data yang terenkripsi.

    """)

with tab2:
    st.title("Keuntungan dan Kerugian Menggunakan Enkripsi")
    st.caption("Minggu, 07 Agustus 2022")

    st.subheader("Keuntungan menggunakan enkripsi")
    st.write("""
    Dalam penggunaannya, enkripsi memberikan banyak keuntungan. Berikut ini adalah keuntungan dalam menggunakannya:
    * Memberikan rasa aman kepada pengguna.
    * Kerahasiaan suatu informasi terjamin.
    * Meminimalisir terjadinya penyadapan.
    * Mencegah kebocoran data.
    """)

    st.subheader("Kerugian menggunakan enkripsi")
    st.write("Selain enkripsi dapat menjaga data penggunanya, ternyata ia juga memiliki kekurangan. Jika penerima informasi kehilangan kunci atau (_decryptor_) untuk melakukan dekripsi, maka pesan informasi tersebut tidak dapat dibaca dan informasi tidak dapat dipulihkan seperti semula lagi.")

    st.subheader("Kegunaan enkripsi sehari-hari")
    st.write("""
    Nah, ada beberapa kegunaan encryption yang sering kita temukan sehari-hari menurut [Learning Hub](https://learn.g2.com/what-is-encryption), yaitu:
    1. **Data Encryption**
        
        Enkripsi data adalah metode perlindungan informasi untuk _database_, _data warehouse_, dan _backup server_.

        Untuk data dalam jumlah besar seperti _data warehouse_, dibutuhkan peran [_security engineer_](https://glints.com/id/lowongan/security-engineer/) dan profesional di bidang IT lainnya untuk memastikan keamanannya menggunakan teknologi enkripsi.

    2. **File Encryption**

        Enkripsi juga bisa digunakan untuk _file_. Ada _software_ khusus untuk membantu menjaga keamanan _file_ dan _folder_ di komputer atau dalam sistem _cloud_.
        Dengan begitu, _hacker_ akan kesulitan untuk mengakses data pentingmu.
    
    3. **Encryption Messaging**

        Aplikasi _messenger_ seperti WhatsApp, Telegram, dan lain-lain biasanya juga menggunakan teknologi keamanan siber ini.
        
        Pasalnya, informasi yang dibagikan seringkali rawan peretasan.
        Oleh karena itu, enkripsi merupakan salah satu pertimbangan penting ketika harus memilih aplikasi _messenger_ untuk digunakan sehari-hari, khususnya jika untuk urusan pekerjaan.

    4. **Endpoint Encryption**

        _Endpoint encryption_ adalah perlindungan operating system dari serangan [_keylogger_](https://glints.com/id/lowongan/keylogger/) atau _corrupt boot files_ yang bisa mengakses data tanpa izin.
        Ini sering dibutuhkan untuk laptop, _server_, tablet, dan lain-lain.

    """)

    st.markdown("""---""") 
    st.write("""
    Sudah paham, kan, tentang enkripsi dan betapa pentingnya bagi keamanan datamu?

    Pada dasarnya, teknologi ini diciptakan untuk tujuan yang positif.
    Akan tetapi, kadang memang ada kesulitan atau tantangan yang terjadi akibat kerumitan dekripsinya, khususnya pada situasi tertentu.    
    Misalnya, karena proses dekripsi data semakin kompleks, backup data ketika dibutuhkan bisa jadi lebih sulit dan membutuhkan waktu yang lama.
    Bahkan, di beberapa kasus, pemilik data justru jadi tidak bisa mengaksesnya karena kesalahan tertentu.
    """)


with tab3:
    st.title("Perbedaan Enkripsi dengan Hashing")
    st.caption("Minggu, 07 Agustus 2022")
    st.write("")

    st.image("images/image20.jpg")
    st.caption("© Pexels.com")

    st.write("""
    Dalam bidang _data security_, enkripsi dan _hashing_ adalah dua praktik yang sering dianggap sama.
    Padahal, menurut [Encryption Consulting](https://www.encryptionconsulting.com/education-center/encryption-vs-hashing/), berikut adalah perbedaan _encrpyt_ dengan _hashing_.
    
    1. **Fungsi**

        Fungsi enkripsi berjalan dua arah, sedangkan, _hashing_ berjalan satu arah saja.
        Maksudnya, hasil data atau teks dari enkripsi dapat diubah dan dikembalikan lagi.
        Sedangkan, data atau teks yang diubah menggunakan _hashing_ tidak bisa dikembalikan lagi.

    2. **Jenis Algoritma**

        Algoritma yang digunakan enkripsi memiliki dua jenis, _symmetric_ dan _asymmetric_.
        Sedangkan, _hashing_ hanya memiliki satu jenis algoritma saja, yaitu algoritma _hashing_.
    
    3. **Kegunaan**

        Enkripsi digunakan untuk melindungi data atau teks yang sedang atau telah terkirim.
        Sedangkan, _hashing_ digunakan untuk menghindari duplikasi data.
        
        Enkripsi umumnya terdapat dalam aplikasi atau fitur _chatting_ di media sosial.
        Di sisi lain, _hashing_ digunakan untuk melindungi hal-hal penting seperti tanda tangan digital hingga _password_.
    """)


