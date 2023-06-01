# Mebuat kelas Mahasiswa
class Mahasiswa:
    # Constructor untuk kelas Mahasiswa
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    # Method untuk menampilkan informasi mahasiswa
    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)

# Membuat kelas Jurusan
class Jurusan:
    # Constructor untuk kelas Jurusan
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
     # Method untuk menambahkan objek mahasiswa
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)
    
     # Method untuk menampilkan daftar mahasiswa
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        print("==============================================")
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)
            print("Jurusan:", mahasiswa.jurusan.NamaJurusan)
            print()

# Membuat kelas Universitas
class Universitas:
     # Constructor untuk kelas Universitas
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    # Method untuk menambahkan objek Jurusan 
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)
    
    # Method untuk menampilkan daftar jurusan
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)
            print()
            
# Langkah-langkah berikut menjawab pertanyaan yang diberikan:

# 1. Implementasi kelas Mahasiswa, Jurusan, dan Universitas
# (Implementasi sudah diberikan di atas)

# 2. Buat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# 3. Buat objek Jurusan dengan nama "Teknik Informatika" dan tambahkan ke dalam Universitas XYZ
jurusan_TI = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_TI)

# 4. Buat objek Mahasiswa dengan nama "Kalian masing", NIM "Kalian masing", dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa = Mahasiswa("Imelda Cyntia", "G1A022022", jurusan_TI)
jurusan_TI.tambah_mahasiswa(mahasiswa)
mahasiswa1 = Mahasiswa("Attiya Dianti Fadli", "G1A022002", jurusan_TI)
jurusan_TI.tambah_mahasiswa(mahasiswa1)
mahasiswa2 = Mahasiswa("Tiesya Adriani Ramadhanti", "G1A022014", jurusan_TI)
jurusan_TI.tambah_mahasiswa(mahasiswa2)
mahasiswa3 = Mahasiswa("Merly Yuni Purnama", "G1A022006", jurusan_TI)
jurusan_TI.tambah_mahasiswa(mahasiswa3)
mahasiswa4 = Mahasiswa("Dian Ardianti", "G1A022084", jurusan_TI)
jurusan_TI.tambah_mahasiswa(mahasiswa4)
mahasiswa5 = Mahasiswa("Ahmad Radesta", "G1A022086", jurusan_TI)
jurusan_TI.tambah_mahasiswa(mahasiswa5)

# 5. Tampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# 6. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_TI.tampilkan_daftar_mahasiswa()
