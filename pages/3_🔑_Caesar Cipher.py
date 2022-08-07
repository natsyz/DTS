import streamlit as st

st.write("🔑 C A E S A R C I P H E R")

tab1, tab2= st.tabs(["Enkripsi", "Dekripsi"])

def encrypt(text, s):
    result = ""

    for i in range(len(text)):  
        char = text[i]  
        if (char.isupper()):  
            # encypt_func uppercase characters in plain txt  
            result += chr((ord(char) + s - 65) % 26 + 65)  
        else:  
            # encypt_func lowercase characters in plain txt  
            result += chr((ord(char) + s - 97) % 26 + 97) 

    return result

def decrypt(text, s):
    result = ""

    for i in range(len(text)):  
        char = text[i]  
        if (char.isupper()):  
            # encypt_func uppercase characters in plain txt  
            result += chr((ord(char) - s - 65) % 26 + 65)  
        else:  
            # encypt_func lowercase characters in plain txt  
            result += chr((ord(char) - s - 97) % 26 + 97) 

    return result

with tab1:
    text_en = st.text_input("Masukkan Plain Text: ")
    e = st.number_input("Encryption Shift: ", 0)
    st.write("**Hasil Enkripsi:** ", encrypt(text_en, e))

with tab2:
    text_de = st.text_input("Masukkan Cipher Text: ")
    d = st.number_input("Decryption Shift: ", 0)
    st.write("**Hasil Dekripsi:** ", decrypt(text_de, d))


st.markdown("""---""") 

st.header("Tentang Caesar Cipher")
st.write("""
Dikutip dari Wikipedia, dalam kriptografi, sandi Caesar, atau sandi geser, kode Caesar atau Geseran Caesar adalah salah satu teknik enkripsi paling sederhana dan paling terkenal.
Sandi ini termasuk sandi substitusi dimana setiap huruf pada teks terang (_plaintext_) digantikan oleh huruf lain yang memiliki selisih posisi tertentu dalam alfabet.

Misalnya, jika menggunakan geseran 3, W akan menjadi Z, I menjadi L, dan K menjadi N sehingga teks terang "wiki" akan menjadi "ZLNL" pada teks tersandi.
Nama Caesar diambil dari Julius Caesar, jenderal, konsul, dan diktator Romawi yang menggunakan sandi ini untuk berkomunikasi dengan para panglimanya.

Langkah enkripsi oleh sandi Caesar sering dijadikan bagian dari penyandian yang lebih rumit, seperti sandi Vigenère, dan masih memiliki aplikasi modern pada sistem ROT13.
Pada saat ini, seperti halnya sandi substitusi alfabet tunggal lainnya, sandi Caesar dapat dengan mudah dipecahkan dan praktis tidak memberikan kerahasiaan bagi pemakainya. 

""")

st.write("")
st.image("https://media.geeksforgeeks.org/wp-content/uploads/ceaserCipher.png")
st.caption("Ilustrasi Caesar Cipher")

st.header("Algoritma Caesar Cipher")
st.write("""
Enkripsi maupun dekripsi Caesar Cipher dapat direpresentasikan dengan menggunakan modular aritmetik dengan langkah awal mentransformasikan huruf ke angka, yaitu A → 0, B → 1, ..., Z → 25.

**Enkripsi** dari sebuah huruf _x_ dengan _shift n_ dapat ditulis secara matematis sebagai berikut:

$$E_{n}(x) = (x+n)\mod{26}$$

**Dekripsi** dari sebuah huruf _x_ dengan _shift n_ dapat ditulis secara matematis sebagai berikut:

$$D_{n}(x) = (x-n)\mod{26}$$
""")
