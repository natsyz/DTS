import streamlit as st

st.markdown("# Phising")

st.markdown(""" 
Kemajuan digital dan globalisasi membuat kita sebagai masyarakat umum dapat menggunakan aplikasi dan software tertentu untuk mempermudah kita mengerjakan sesuatu atau memperoleh apapun. Masa pandemi juga membuat kita semakin terbiasa untuk melakukan aktifitas jual beli secara digital, bukan lagi manual. Menyambungkan dompet digital (_e-wallet_) merupakan salah satu kemudahan yang disediakan  e-commerse dan marketplace untuk memudahkan proses pembayaran barang/jasa yang dibeli. Eitss, tapi hati-hati loh. Kemajuan teknologi ini juga membuat banyak “oknum nakal” mulai melakukan _cybercrime_.

Dikutip dari buku Pengantar Teknologi Informasi (2020) karya Darsil Aldo dkk, cyber crime adalah kejahatan yang ditimbulkan karena pemanfaatan teknologi internet. Bisa di maknai sebagai perbuatan melawan hukum yang dilakukan dengan menggunakan internet.
""")

st.image("images/image1.png")

st.markdown("""
Kalian pasti pernah membaca banyak judul berita seperti diatas kan? Yap, ini berupakan beberapa berita tentang cyber crime yang banyak dilakukan tapi sayangnya tidak semua orang menyadari kalau mereka mungkin adalah korban. Kegiatan cybercrime yang umumnya dilakukan untuk mengambil data korban atau detail akun bank/ e-wallet yang akan di retas adalah “Phising”.

Phising adalah upaya untuk mendapatkan informasi data seseorang dengan teknik pengelabuan. Data yang menjadi sasaran phising adalah data pribadi (nama, usia, alamat), data akun (username dan password), dan data finansial (informasi kartu kredit, rekening).

Istilah resmi phising adalah phishing, yang berasal dari kata fishing yaitu memancing.

Kegiatan phising memang bertujuan memancing orang untuk memberikan informasi pribadi secara sukarela tanpa disadari. Padahal informasi yang dibagikan tersebut akan digunakan untuk tujuan kejahatan.

Kenapa korban mau melakukan hal itu?

Pelaku phising biasanya menampakkan diri sebagai pihak atau institusi yang berwenang. Dengan menggunakan website atau email palsu yang tampak meyakinkan, banyak orang berhasil dikelabui.
""")

st.image("images/image2.png")

st.markdown("""
Informasi data phising yang diperoleh bisa langsung dimanfaatkan untuk menipu korban. Atau, bisa juga dijual ke pihak lain untuk melakukan tindakan tidak bertanggung jawab seperti penyalahgunaan akun.

Menurut sebuah laporan, 32% pencurian data selalu melibatkan kegiatan phising. Bahkan, di awal tahun 2020 saja, Anti Phishing Working Group mencatat sudah ada 165.772 website phising yang siap menjaring korban. Dan, sektor finansial masih menjadi sasaran utamanya:
""")

st.image("images/image3.png")


st.markdown("## Jenis Phising")

st.markdown("Untuk lebih mengenal tindakan phising, mari pelajari jenis phising yang paling banyak ditemui saat ini:")

st.markdown("""
1. **Email Phising**
    
    Sesuai namanya, email phising menggunakan media email untuk menjangkau calon korbannya.
    
    ![alt text](image3.png)

    Jumlah aksi email phising ini cukup banyak. Menurut data, terdapat 3,4 miliar email palsu yang dikirimkan setiap harinya. Anda bisa bayangkan, berapa banyak korban yang bisa terjerat aksi ini.

2. **Spear Phising**

    Spear phising adalah jenis dari email phising. Bedanya, alih-alih menggunakan pengiriman email secara masif dengan calon korban yang acak, spear phising menarget calon korban tertentu. Biasanya, teknik ini dilakukan setelah beberapa informasi dasar calon korban dimiliki, seperti nama dan alamat.

3. **Whaling**

    Whaling adalah langkah phising yang tidak hanya menarget individu secara spesifik, tapi juga individu yang memiliki kewenangan tinggi di suatu organisasi, misalnya pemilik bisnis, direktur perusahaan, manajer personalia, dan lainnya.

    Dengan demikian, jika tindakan whaling ini berhasil, akan banyak keuntungan yang bisa dimanfaatkan dari akses yang didapatkan.

4. **Web Phising**

    Web phising adalah upaya memanfaatkan website palsu untuk mengelabui calon korban. Website untuk phising akan terlihat mirip dengan website resmi dan menggunakan nama domain yang mirip. Hal ini disebut domain spoofing.
    
    Sebagai contoh, untuk menyerupai niagahoster.co.id, domain yang digunakan pelaku phising adalah niaga-hoster.my.id.
""")


st.markdown("## Bagaimana Sebuah Aksi Phising Dijalankan?")

st.markdown("Cara kerja phising adalah memanipulasi informasi dan memanfaatkan kelalaian korban. Di sini, kami akan menggunakan contoh web phising dengan memanfaatkan nama PayPal seperti ditemukan welivesecurity.com.")

st.markdown("""
1. **Pelaku Memilih Calon Korban**

    Tahap awal kegiatan web phising akan dimulai dengan menentukan siapa calon korbannya. Pada umumnya, korban yang disukai adalah pengguna platform pembayaran online seperti PayPal, Ovo, dan lainnya.

    ![alt text](images/image4.png)

    Tidak hanya itu saja, banyak pelaku phising yang mengincar pengguna platform yang memiliki celah keamanan. Kasus terbaru terjadi pada platform komunikasi Zoom. Tak kurang dari 1000 upaya phising terjadi hanya di bulan April 2020 saja.

2. **Pelaku Menentukan Tujuan Phising**

    Setelah mendapatkan calon korban yang potensial, pelaku akan mulai memikirkan apa yang akan dicapai dari kegiatan web phising yang dilakukan.

    Apakah akan menarget username dan password pengguna untuk menguasai akun. Apa malah mendapatkan semua informasi korban melalui sebuah prosedur yang disiapkan.

    Pada contoh aksi phising PayPal, pelaku menginginkan semua informasi dari pengguna platform tersebut. Seperti ditunjukkan welivescurity.com, pengguna akan menerima email untuk mengkonfirmasi data diri melalui sebuah link website palsu yang disediakan.

3. **Pelaku Membuat Website Phising**

    Untuk melancarkan aksinya, pelaku akan mulai menyiapkan website palsu untuk melakukan aksi phising. Mulai dari mendesain website palsu, memilih nama domain yang mirip dengan domain asli hingga menyiapkan konten dengan tulisan yang meyakinkan.

    ![alt text](images/image5.png)

    Pada prakteknya, pelaku kadang membuat website yang sangat menyerupai halaman website resmi tapi menggunakan nama domain yang jauh berbeda seperti terlihat di contoh atas.

    Namun, pada contoh kasus phishing Danamon Online beberapa waktu lalu, Anda akan langsung melihat bahwa domain yang digunakan mirip sekali dengan website resminya:

    ![alt text](images/image6.png)

4. **Calon Korban Mengakses Website Phising**

    Dengan tampilan website dan informasi yang meyakinkan, tak sedikit calon korban yang akhirnya mengakses website phising milik pelaku. Langkah ini biasanya didahului dengan mengajak calon korban melalui email phising atau link yang disebarkan via SMS atau akun media sosial.

    ![alt text](images/image7.png)

5. **Calon Korban Mengikuti Instruksi Pelaku**

    Inilah kunci dari terjadinya aksi phising. JIka calon korban melakukan instruksi yang diberikan pelaku, maka pelaku akan berhasil mencapai tujuannya.

    ![alt text](images/image8.png)

    Sebagai contoh, pada halaman website yang disediakan, calon korban diminta melakukan update informasi pribadi hingga data pembayaran pada akun yang digunakan. Pada saat selesai mengisi data dan melakukan submit, saat itulah semua informasi korban berhasil dimiliki.

6. **Data Korban akan Dimanfaatkan**

    Jika aksi web phising berhasil, pelaku akan memanfaatkan data yang telah diterima. Apa saja yang bisa dilakukan?

    * Menjual informasi yang didapatkan ke pihak ketiga yang membutuhkan data calon konsumen. Misalnya, untuk tujuan telemarketing atau kegiatan marketing online lainnya.
    * Menjual informasi data tersebut untuk kepentingan politik atau iklan penjualan produk.
    * Menjalankan aksi penipuan. Misalnya, dengan menyatakan seseorang memenangkan undian tertentu yang pada akhirnya meminta orang tersebut mengirimkan sejumlah uang.
    * Menggunakan data yang dimiliki untuk mencoba membobol akun yang dimiliki atau akun lain.
    * Melakukan pinjaman online mengatasnamakan korban dengan menggunakan data diri lengkap korban. Tentu saja, korban lah yang akan ditagih pelunasan atas pinjaman tersebut.
""")


st.markdown("## 9 Tips Agar Tidak Menjadi Korban Phising")

st.markdown("Agar sebagai pengguna platform tertentu, Anda bisa terhindar dari kejahatan phising, inilah beberapa tips yang perlu Anda lakukan:")

st.markdown("""
1. **Selalu Update Informasi terkait Phising**

    Anda sudah belajar tentang jenis phising. Namun, tidak menutup kemungkinan jenis kejahatan online akan terus berkembang. Baik dari media yang digunakan untuk phising ataupun jenis serangan yang dilakukan.

    ![alt text](images/image9.png)

    Oleh karena itu, selalu ikuti berita perkembangan phising dengan baik. Salah satunya dengan memiliki rasa ingin tahu apabila ada insiden keamanan yang terjadi seperti kebocoran data pengguna Tokopedia atau Bukalapak baru-baru ini.

    Apakah kejadian tersebut dimulai dari aksi phising? Bagaimana kejahatan online tersebut dilakukan? Atau, berbagai pertanyaan lainnya.

2. **Selalu Cek Siapa Pengirim Email**

    Email phising masih menjadi jenis kejahatan online yang marak. Untuk itu, Anda perlu berhati-hati ketika mendapatkan email dari pengirim yang mencurigakan.

    Anda sebaiknya tidak hanya melihat nama pengirim, tapi juga alamat email yang mengirimkannya pada bagian From field. Sebab, email tersebut bisa saja palsu.

    Anda bahkan harus extra waspada kalau email yang Anda terima terkait dengan perubahan informasi akun, pembayaran dan hal penting lainnya.

    Sebagai contoh, ketika Anda menerima email yang seolah berasal dari Niagahoster dan meminta Anda untuk melakukan pembaruan pesanan seperti di bawah ini, Anda bisa mengabaikannya:

    ![alt text](images/image10.png)

    Apa alasannya?

    Pertama, ketika menggunakan nama Niagahoster, maka email yang kami kirim akan menggunakan domain niagahoster.co.id, misalnya cs@niagahoster.co.id. Bukan @i-ob.co.uk atau domain lain yang tidak terkait Niagahoster.

    Kedua, pada bagian footer email, akan selalu ada kontak resmi Niagahoster yang bisa Anda gunakan melakukan pengecekan (verifikasi) apakah informasi yang Anda dapatkan itu benar. Pada email phising di atas, tidak ada, bukan?

    ![alt text](images/image11.png)

3. **Jangan Asal Klik Link yang Diterima**

    Meskipun Anda menjadi sasaran phising, Anda belum tentu menjadi korban. Kuncinya adalah apakah Anda melakukan klik pada link yang disiapkan oleh pelaku phising atau tidak.

    ![alt text](images/image12.png)

    Seperti Anda tahu, email dan website untuk phising dibuat mirip dengan aslinya. Namun, selalu ada hal yang membedakan sumber resmi dengan palsu. Bisa dari form pengisian data yang mencurigakan, bahasa konten yang bukan seperti biasa Anda terima, dan lain sebagainya.

    Jadi, sebelum meng-klik link apapun, pastikan link tersebut aman. 

    ![alt text](images/image13.png)

    Caranya, arahkan mouse ke link tersebut tanpa diklik (hover). Kemudian, akan muncul informasi URL dari link tersebut. Jika mengarah ke website asli, berarti aman. Jika mengarah ke website lain yang tidak dikenal, lebih baik urungkan niat Anda.

4. **Pastikan Keamanan Website yang Diakses**

    Jangan kunjungi website yang tidak aman, terutama website yang akan memproses data pribadi atau finansial. Hanya lakukan transaksi pada website yang menggunakan SSL saja, yaitu website yang ditandai dengan penggunaan protokol HTTPS.

    ![alt text](image14.png)

    Dengan memastikan aktivitas online Anda hanya pada website yang aman, maka kemungkinan Anda menjadi korban phising lebih kecil.

5. **Gunakan Browser Versi Terbaru**

    Sarana Anda untuk melakukan aktivitas online adalah browser. Jadi, selalu gunakan versi browser terbaru yang dapat melindungi keamanan data dan privasi Anda.

    ![alt text](images/image15.png)

    Langkah ini penting karena setiap browser merilis versi terbaru, selalu terkait dengan perbaikan pada celah keamanan dan fitur yang lebih efektif. Untuk memudahkan, Anda cukup mengaktifkan status automatic update di tiap browser yang Anda gunakan.

6. **Waspada Ketika Dimintai Data Pribadi**

    Pada dasarnya, jangan pernah memberikan data pribadi Anda ketika mengakses sebuah website. Kecuali, website tersebut memang resmi dan data Anda dibutuhkan untuk menjalankan proses transaksi.

    Sebagai contoh, terdapat beberapa toko online yang hanya melayani pembelian dari anggota yang sudah terdaftar. Namun, ada juga yang memperbolehkan transaksi pembelian tanpa harus login. Apapun pilihan Anda, lakukanlah yang paling memberikan dampak keamanan minimal.

7. **Cek Akun Online Anda secara Rutin**

    Tak jarang Anda melakukan registrasi ke berbagai platform atau situs dan kemudian tidak pernah menggunakannya lagi. Padahal, semua informasi Anda masih tersimpan di platform tersebut.

    Rekomendasi yang dapat kami berikan, lakukan penghapusan akun dan data jika sudah tidak digunakan. Atau, Anda bisa terus melakukan perubahan password secara berkala di akun tersebut jika masih ingin menggunakannya di waktu tertentu.

8. **Gunakan Two-Factor Authentication**

    Jika platform yang Anda gunakan menyediakannya, selalu aktifkan Two-Factor Authentication (2FA). Sistem ini menggunakan verifikasi 2 langkah, yaitu password dan ponsel Anda.

    ![alt text](images/image16.png)

    Pada saat pelaku phising sudah menemukan username dan password Anda tapi tidak dapat memasukan kode verifikasi 2FA, platform tidak akan melanjutkan proses. Artinya, akun Anda akan terlindungi dengan lebih baik.

9. **Lakukan Scan Malware secara Berkala**

    Salah satu serangan dalam phising adalah meminta Anda mendownload file tertentu melalui email palsu yang Anda terima. Pada saat melakukannya, bisa saja Anda sedang mengunduh malware yang akan bekerja di komputer Anda secara rahasia.

    Untuk menghindari hal ini, gunakanlah software anti-malware yang akan melakukan scan secara otomatis sesuai dengan setting yang Anda gunakan. Jangan lupa untuk segera menghapus script yang mencurigakan yang bisa saja mencuri informasi pribadi Anda.
""")

st.markdown("## 4 Cara Mengatasi Phising di Website WordPress")

st.markdown("Di sisi lain, jika Anda adalah seorang pemilik website yang menjadi sasaran kegiatan phising, inilah cara mengatasi kejahatan online tersebut di website WordPress Anda:")

st.markdown("""
1. **Gunakan Plugin untuk Membersihkan Malware Phising**

    Jangan sampai website Anda dimanfaatkan untuk sarana pencurian data pengunjung atau pelanggan toko online Anda. Maka, gunakanlah plugin anti malware di website WordPress Anda.

    ![alt text](images/image17.png)

    Apa saja pilihan plugin yang bisa Anda gunakan? Sebagian besar plugin security WordPress yang pernah kami bahas bisa Anda gunakan. Atau, Anda bisa menggunakan MalCare yang merupakan plugin anti malware dengan fitur instant removal. Malcare bisa mendeteksi adanya malware yang menyerang website dan lalu menghapusnya secara otomatis.

2. **Selalu Update WordPress**

    WordPress merupakan platform yang rutin melakukan update. Selain penambahan fitur, update juga digunakan untuk menambah celah keamanan yang kerap dimanfaatkan pelaku phishing.

    Untuk mencegah website Anda terserang malware, selalu gunakan versi WordPress terbaru. Jika versi WordPress Anda masih lama, Anda akan mendapatkan notifikasi di dashboard WordPress Anda agar segera melakukan update.

3. **Pasang Sertifikat SSL untuk Keamanan Website**

    Seperti telah dibahas sebelumnya, peran SSL sangat penting untuk menjamin keamanan transaksi di sebuah website. Jika belum menggunakannya, segera pasang sertifikat SSL di website WordPress Anda.

4. **Lakukan Manajemen Pengguna dengan Ketat**

    Jika website WordPress Anda dikelola banyak orang, lakukan manajemen pengguna dengan baik. Jangan berikan hak akses admin ke semua orang. Hak akses user harus disesuaikan dengan kewenangan dan kemampuannya dalam menjaga keamanan website dengan baik.
""")



