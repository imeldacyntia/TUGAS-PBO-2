# TUGAS-PBO-2
Kode program yang telah dibuat merupakan implementasi dari beberapa kelas yang saling terkait, yaitu kelas Mahasiswa, Jurusan, dan Universitas. Berikut ini adalah penjelasan rinci mengenai setiap kelas dan metode yang ada dalam program tersebut:

1. Kelas Mahasiswa:

   Pada kelas Mahasiswa memiliki atribut:
    - nama: Menyimpan nama mahasiswa.
    - nim: Menyimpan NIM (Nomor Induk Mahasiswa) mahasiswa.
    -jurusan: Menyimpan objek jurusan tempat mahasiswa tersebut terdaftar.
    
   Pada kelas Mahasiswa memiliki metode:
    - init(self, nama, nim, jurusan): Merupakan constructor yang digunakan untuk menginisialisasi objek Mahasiswa dengan nama, nim, dan jurusan.
    - tampilkan_info(self): Metode ini digunakan untuk menampilkan informasi mahasiswa seperti nama, nim, dan nama jurusan tempat mahasiswa tersebut terdaftar.

2. Kelas Jurusan:

   Pada kelas Jurusan memiliki atribut:
   
     - NamaJurusan: Menyimpan nama jurusan.
     - DaftarMahasiswa: Menyimpan daftar objek Mahasiswa yang terdaftar dalam jurusan tersebut.

   Pada kelas Jurusan memiliki metode:
     - init(self, nama_jurusan): Merupakan constructor yang digunakan untuk menginisialisasi objek Jurusan dengan nama jurusan.
     - tambah_mahasiswa(self, mahasiswa): Metode ini digunakan untuk menambahkan objek Mahasiswa ke dalam daftar mahasiswa pada jurusan tersebut.
     - tampilkan_daftar_mahasiswa(self): Metode ini digunakan untuk menampilkan daftar mahasiswa yang terdaftar dalam jurusan tersebut.

3. Kelas Universitas:

   Pada kelas Universitas memiliki atribut:
    - NamaUniversitas: Menyimpan nama universitas.
    - DaftarJurusan: Menyimpan daftar objek Jurusan yang ada di universitas.
    
   Pada kelas  Universitas memiliki metode:
  
    - init(self, nama_universitas): Merupakan constructor yang digunakan untuk menginisialisasi objek Universitas dengan nama universitas.
    - tambah_jurusan(self, jurusan): Metode ini digunakan untuk menambahkan objek Jurusan ke dalam daftar jurusan pada universitas tersebut.
    - tampilkan_daftar_jurusan(self): Metode ini digunakan untuk menampilkan daftar jurusan yang ada di universitas.
    
   Berikut ini merupakan hasil outputan pada kode program yang telah dibuat: 
   <img width="297" alt="image" src="https://github.com/imeldacyntia/TUGAS-PBO-2/assets/95126142/bb7b7490-e497-42a4-bdee-bb6b16e0df9d">
