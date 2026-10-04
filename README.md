# Minpro-2-DDP-PendataanKoleksiTenun

Nama  :  Raihanum Athaya Rana Insyra<br>
NIM   :  2609116014<br>
Kelas :  A<br>
Tema  :  Sistem Pendataan Koleksi Tenun Samarinda<br>
---
## **Penjelasan Program**<br>
Sistem Pendataan Koleksi Tenun Samarinda berfungsi untuk memudahkan pencatatan, pemantauan, dan pengelolaan data kain Tenun Samarinda secara terstruktur dengan fitur sederhana yang mampu menambahkan data, menampilkan data, mengubah data, serta menghapus data kain tenun yang telah tersimpan.<br>

Pada mini project 2, saya telah mengembangkan program ini dengan tambahan dua role (admin & user). Role admin memiliki akses penuh (CRUD) untuk menambahkan data baru, menampilkan data, mengubah, dan menghapus data kain tenun dari sistem. Sedangkan user disini memiliki akses hanya untuk menampilkan daftar koleksi tenun.<br>

Di program ini saya tidak hanya menggunakan tuple & list, saya menggunakan dictionary untuk menyimpan informasi akun dan sekelompok tuple. Selain itu, saya juga menggunakan library prettytable agar tampilan lebih rapi, pwinput agar menyamarkan password yang dimasukkan, pembersih layar otomatis menggunakan os.system, library sys agar dapat menghentikan prgram yang tidak berada di dalam looping, dan library time agar otomatis kembali ke menu utama ketika password yang dimasukkan salah. Terakhir, dilengkapi dengan validasi looping untuk mencegah adanya error yang muncul dikarenakan kesalahan input.<br>

## **Gambar Flowchart**<br>
### 1. Flowchart Halaman Utama/Login<br>
<img width="850" height="1100" alt="flowchart halaman login" src="https://github.com/user-attachments/assets/3b3e5eb1-8e05-44c4-8333-e7f443c94070" /><br>
Di halaman utama, pengguna akan diberikan 3 pilihan yaitu login bagi yang sudah memiliki akun, registrasi untuk membuat akun baru, dan keluar atau menghentikan program. Jika pengguna memilih login, maka menu yang akan ditampilkan akan meneysuaikan role dari akun tersebut (admin/user), bagi pengguna yang registrasi dapat membuat username dan password baru sebagai user saja, dan dipastikan tidak dapat memasukkan username dan password yang sudah ada.<br>
### 2. Flowchart Menu Admin
<img width="1609" height="1120" alt="halaman admin dan user tenun-halaman admin" src="https://github.com/user-attachments/assets/45032dff-ff5f-4004-a111-034167b26bee" /> <br>
Bagi pengguna yang memiliki role akun sebagai admin, maka akan ditampilkan menu admin. Di dalam menu admin, terdapat 6 fitur yaitu membuat, menampilkan, mengubah, menghapus, logout (kembali ke halaman utama), dan keluar (menghentikan program)<br>
### 3. Flowchart Menu User
<img width="777" height="490" alt="halaman admin dan user tenun-halaman user drawio" src="https://github.com/user-attachments/assets/e5a047a5-cca3-4f32-bfa9-74e565e41c7b" /> <br>
Bagi akun pengguna yang tercatat memiliki role sebagai user, akan diarahkan ke menu user. Di dalam menu user terdiri dari 3 pilihan yaitu menampilkan data, logout (kembali ke halaman utama), serta keluar (menghentikan program)<br>

## Input dan Output Beserta Penjelasan
### Inisialisasi Data<br>
<img width="1184" height="742" alt="image" src="https://github.com/user-attachments/assets/b68e3912-91cf-4dc3-b2a6-8b4bc9473495" /><br>
Saya menggunakan library seperti os, time, prettytable, sys, dan pwinput yang sekiranya sesuai dengan kebutuhan program saya. Kemudian untuk persiapan data, saya menyediakan data_user dan koleksi_tenun sebagai permulaannya.<br>
### Function Membersihkan Layar<br>
<img width="902" height="194" alt="image" src="https://github.com/user-attachments/assets/97c06fce-b26c-4257-8dae-5b0d37ef3c00" /><br>
Saya memulai dengan mendefinisikan fungsi bersih_layar() yang berfungi untuk membersihkan tampilan terminal secara otomatis agar terlihat rapi denga menggunakan os.system agar bisa memperintah langsung ke sistem komputernya melalui terminal.<br>
### Function Menu Admin 1 : Masukkan Data Baru<br>
<img width="1060" height="790" alt="image" src="https://github.com/user-attachments/assets/e92dd35d-9e81-4df2-aa82-6d090bd91527" /><br>
Saya mendefinisikan fungsi untuk tambah data yang dimulai dengan input kode kain (strip dan upper untuk mencegah error dari kesalahan input pengguna dari penulisannya. Jika kode yang diinput telah tersedia, makan akan tampil "sudah terdaftar". Namun, jika belum tersedia, admin bisa melanjutkan memasukkan detail kain. Dengan menggunakan validasi looping, saya memastikan admin hanya dapat memasukkan angka agar programnya berlanjut dengan menambahkan .isdigit() <br>
### Function Menu Admin 2 : Menampilkan Data<br>
<img width="1108" height="518" alt="image" src="https://github.com/user-attachments/assets/545cc681-3154-4c55-b9ce-452cc9c4b667" /> <br>
Saya mendefinikan fungsi tampilkan_data dengan mengecek apakah list ada isinya, jika tidak ada tampil "data kosong" jika ada, maka akan ditampilkan table yang menggunakan prettytable yang berisi data tentang kain tenun.<br>
### Function Menu Admin 3 : Mengubah Data<br>
<img width="1326" height="1126" alt="image" src="https://github.com/user-attachments/assets/8795292f-1a73-4a43-9e57-1c7d7f819af2" /><br>
Saya mendeifinisikan fungsi ubah_data yang dimulai dengan cek apakah data tersedia? jika tersedia lanjut untuk memasukkan kode, kemudian di-cek apakah kode ada? jika kode sudah ada, maka admin bisa lanjut memasukkan detail tambahan. namun jika kode tidak tersedia, maka akan tampil tidak ditemukan. Dipastikan dalam input tahun pembuatannya juga memuat angka.<br>
### Function Menu Admin 4 : Menghapus Data<br>
<img width="1246" height="736" alt="image" src="https://github.com/user-attachments/assets/257f205c-3559-4570-8d68-d5cdad872943" /><br>
Saya mendefinisikan fungsi hapus_data dengan dengan mengecek apakah data tersedia? jika memang sudah kosong dari awal, maka akan tampil "data kosong" namun jika tersedia, admin memilih kode kain yang mana yang akan dihapus, kemudian dicek apakah kode tersedia? jika tersedia data kain tersebut akan dihapus, namun jika tidak maka akan tampil "kode tidak ditemukan"<br>
### Function menu admin 5 dan 6 : Keluar dan Logout
<img width="594" height="568" alt="image" src="https://github.com/user-attachments/assets/1a5b1231-2a14-4730-b795-607497dd4936" /><br>
Jika admin ingin langsung menghentikan program, maka saya telah mendefinisikan fungsi keluar dengan langsung menghentikan program yaitu dengan menggunakan sys.exit(). bagi admin yang ingin mengubah akunnya, dapat logout dengan function logout yang akan diarahkan kembali ke menu utama<br>
### Halaman Admin
<img width="1088" height="1012" alt="image" src="https://github.com/user-attachments/assets/2f950c6d-c227-41e8-aa76-f432d77c5e23" /><br>
saya mendefinisikan fungsi untuk menu admin kemudian menggunakan while True untuk perulangan, saya menampilkan data dari 1-6 dan memanggil function-function yang sudah dibuat sesuai dengan pilihan fitur yang ada. Dan jika admin tidak memasukkan input yang valid, akan tertulis "pilihan tidak valid".<br>
### Halaman User
<img width="944" height="820" alt="image" src="https://github.com/user-attachments/assets/ec4df641-db63-4257-8378-fddeda2f519c" /><br>
Saya mendefinisikan fungsi untuk menu user dengan menggunakan pengulangan while True yang menampilkan 3 pilihan (tmampilkan, logout, keluar) kemudian memanggil function-function yang sudah tersedia. Jika user memasukkan input selain dari 1-3 maka akan muncul "pilihan tidak valid"<br>
### Halaman Login
<img width="1088" height="450" alt="image" src="https://github.com/user-attachments/assets/627ca5dd-403f-45ec-a8c7-6206dc13fa9c" /><br>
saya mendefinisikan menu utama sebagai main() yang berisikan perulangan while True saat menampilkan pilihan menu untuk menu utamanya.<br>
### Pilihan 1 Halaman Login
<img width="1058" height="778" alt="image" src="https://github.com/user-attachments/assets/649ff052-0740-4a36-a81c-c14dc6c4a289" /><br>
saya menggunakan if-else saat menampilkan pilihan untuk login. Dimulai dengan memastikan apakah username yang dimasukkan tersedia? jika tersedia, apakah password tersebut cocok dengan milik pengguna? Jika sudah benar, maka akan ditentukan apakah akun tersebut memiliki role admin atau user, dan diarahkan ke menu yang sesuai dengan function menu_admin dan menu_user. Jika salah, akan ditampilkan "password atau username salah". <br>
### Pilihan 2 (registrasi) Halaman Login<br>
<img width="1132" height="644" alt="image" src="https://github.com/user-attachments/assets/0883068d-42ab-44bc-b2cc-6f79939460a7" /><br>
saya menggunakan elif untuk pengguna yang memilih pilihan 2. Dimulai dengan memasukkan username dan password baru untuk mendaftarkan akun. Kemudian dicek, jika username sudah ada, maka akan tampil "username sudah terdaftar". Jika tidak, maka user dapat melanjutkan memasukkan password baru dan terdaftar sebagai user. Hal tersebut agar dapat mencegah user yang bukan admin dengan mudah mengubah data yang sudah ada. Ketika regis berhasil, saya menggunakan time.sleep(3) agar dalam 3 detik langsung kembali ke menu utama.
### Pilihan 3 (keluar) Halaman Login<br
<img width="814" height="388" alt="image" src="https://github.com/user-attachments/assets/c1a3525c-61d0-4d2d-b860-e22dfddf982f" /><br>
saya menggunkaakan sys.exit untuk langsung menghentikan program, dan print pilihan tidak valid jika user memasukkan selain angka 1-3.
### Memanggil function halaman login untuk tampil pertamakali memasuki program
<img width="468" height="136" alt="image" src="https://github.com/user-attachments/assets/a567fbd9-5cf2-4970-8345-739e2b9eecc5" /><br>
---
## Output dan Skenarionya
### 1. Tampilan menu utama (main())<br> 
<img width="854" height="276" alt="image" src="https://github.com/user-attachments/assets/63edc57d-8d42-40db-ae65-5fb4f355129c" /><br>
### 2. Login - Input tidak valid<br>
<img width="1112" height="654" alt="image" src="https://github.com/user-attachments/assets/4f94e2c9-9105-4641-8791-17a7d01ef8b5" /><br>
### 3. LOgin - Input sesuai, password benar<br>
<img width="678" height="506" alt="image" src="https://github.com/user-attachments/assets/2c8c9067-d5e9-4a9a-b650-22e5f64328f3" /><br>
### 4. Login - Input sesuai password/username salah<br>
<img width="716" height="426" alt="image" src="https://github.com/user-attachments/assets/0efcc520-3f1a-4636-9b8f-f7578819ac0f" /><br>
### 5. Regis - Input sesuai <br>
<img width="706" height="436" alt="image" src="https://github.com/user-attachments/assets/2559f910-696e-4586-934a-15d0949225cc" /><br>
### 6. regis - Input sudah terdaftar<br>
<img width="792" height="416" alt="image" src="https://github.com/user-attachments/assets/0d7e0bd6-6e8c-4a69-9447-a11501379e35" /><br>
### 7. Keluar dari program<br>
<img width="1030" height="144" alt="image" src="https://github.com/user-attachments/assets/42c633fb-7f73-48ea-b4cb-c9e27e02b8fe" /><br>
### 8. Tampilan Halaman admin
<img width="564" height="284" alt="image" src="https://github.com/user-attachments/assets/f49e0327-8070-491f-86cc-2ad7baba158a" /><br>
### 9. Pilihan tidak sesuai<br>
<img width="626" height="592" alt="image" src="https://github.com/user-attachments/assets/04ab6fb5-1dad-43ae-a094-79c5c461eed1" /><br>
### 10. Masukkan data baru - input sudah terdaftar<br>
<img width="568" height="432" alt="image" src="https://github.com/user-attachments/assets/06fad251-8511-434d-8b49-ab8127a8b540" /><br>
### 11. Data baru - input sesuai - tahun bukan angka - tahun adalah angka
<img width="660" height="612" alt="image" src="https://github.com/user-attachments/assets/a2894a1f-873a-4c3b-835f-482313d3cbce" /><br>
### 12. Tampilkan data<br>
<img width="1208" height="690" alt="image" src="https://github.com/user-attachments/assets/cb69783b-47ed-42f9-a46f-90d3eeb8d605" /><br>
### 13. Ubah data - kode tidak terdaftar
<img width="706" height="438" alt="image" src="https://github.com/user-attachments/assets/cbff8e61-c2cb-4f0b-8f84-5cdf6cea7f0a" /><br>
### 14. Ubah data - kode terdaftar - tahun bukan angka - tahun adalah angka<br>
<img width="1178" height="1250" alt="image" src="https://github.com/user-attachments/assets/66a3855a-96c2-48a3-bc82-1ee57864d097" /><br>
### 15. hapus data - kode tidak ditemukan<br>
<img width="752" height="424" alt="image" src="https://github.com/user-attachments/assets/cc5ff4cd-2540-4f5e-955d-3241bc153e2e" /><br>
### 16. hapus data - kode ditemukan
<img width="1184" height="1134" alt="image" src="https://github.com/user-attachments/assets/8366a610-e15a-45af-bc83-b016e0375e9a" /><br>
### 17. Logout<br>
<img width="726" height="310" alt="image" src="https://github.com/user-attachments/assets/68f652a6-e726-4e2a-bf1b-461eee45ac17" /><br>
### 18. keluar<br>
<img width="1160" height="214" alt="image" src="https://github.com/user-attachments/assets/693628b6-96c1-438c-bb3f-0e183b048658" /><br>
### 19. Tampilan halaman user<br>
<img width="590" height="220" alt="image" src="https://github.com/user-attachments/assets/73db2b4a-d541-435b-af74-f9b9dfcc21d1" /><br>
### 20. Tampilkan data - input sesuai<br>
<img width="1168" height="610" alt="image" src="https://github.com/user-attachments/assets/baa69fc4-d5a7-44f5-ae66-02514b4e2bb2" /><br>
### 21. Tampilan halaman - input tidak sesuai<br>
<img width="634" height="324" alt="image" src="https://github.com/user-attachments/assets/7c40bf9b-d056-44df-af41-4a52138f574c" /><br>
### 22. logout<br>
<img width="802" height="578" alt="image" src="https://github.com/user-attachments/assets/21de8aff-0038-47f8-8304-88d4cb8831ca" /><br>
### 23. keluar<br>
<img width="1068" height="422" alt="image" src="https://github.com/user-attachments/assets/04ad4546-de77-407b-aed8-597e3916fb19" /><br>
---
### Penjelasan Nilai Tambah
1. Program memiliki validasi input menggunakan error handling, sehingga input yang salah tidak menyebabkan program langsung berhenti/error.<br>
-> berdasarkan percobaan yang telah dilakukan, ketika saya menghapus seluruh data, dan coba untuk menampilkan data, outputnya akan seperti ini <br>
<img width="618" height="472" alt="image" src="https://github.com/user-attachments/assets/cbc1a1b8-63fa-4178-9045-677d5eb9682c" /><br>

dikarenakan :<br>

<img width="632" height="150" alt="image" src="https://github.com/user-attachments/assets/c0fbf5a8-d57b-4d11-be94-00bb24a706b6" /><br>

2. Menerapkan 3 library atau lebih sesuai dengan kebutuhan program.<br>
-> Saya menerapkan 5 library, yaitu library prettytable agar tampilan lebih rapi, pwinput agar menyamarkan password yang dimasukkan, pembersih layar otomatis menggunakan os.system, library sys agar dapat menghentikan prgram yang tidak berada di dalam looping, dan library time agar otomatis kembali ke menu utama ketika password yang dimasukkan salah.








































  








