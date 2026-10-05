Nama: Ahmad Shanahan Zorya
NPM: 2506541894
Kelas: PBP D

## Tugas 3

buat ngambil JSON, bisa di /api/educations/ dan /api/experiences/

> Jujur ini pertama kali Vibecoding, HAHAHAHAH seru seru ngeri gimanaa gitu ngerjainnya

#### Pertanyaan Reflektif

1. Mengapa menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual? Mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut?

   Yaa, gampangnya, udah dikasih template, ngapain bikin sendiri, ada yang mudah, yang udah aman, udh ada validasi tiap field, better pake dibanding bikin sendiri.

   Token buat validation kalo input yg masuk di form itu dari Site yang sama, ga dari Site/web lain (Cross-Site)

2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

     - Native sama JavaScript, namanya aja JavaScript Object Notation
     - Simple (Key-Value pair), ga kayak XXML yg kek html, ada opening dan closing tag

3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

     - View menerima request
     - Query database, masih dalam bentuk object python/django
     - Object di-serialize biat bisa convert dari python object ke json
     - Data JSON di-return

     Perlu di-serialize biar bisa aconvert dari python object (yg strukturnya agak kompleks) ke JSON yg intuitive, readable, simple

---

## Tugas 4

#### Implementasi

- Grup Editor dibuat pake django admin, user yg ada di grup editor bisa ngedit data model
- buat helper function is_editor untuk ngecek apakah user termasuk editro
- Tombol yang gabisa dipake, ga ditampilkan (sesuai role)

#### AI Disclosure

Tools: Cline pake model MiniMax-M2.7-highspeed
Bagian yang dibantu AI:
- role-based aaccess
- django groups untuk role editor

---

## Tugas 5

#### Implementasi

- Halaman education dan experience ngambil data lewat AJAX (fetch) ke endpoint JSON /api/education/ dan /api/experience/
- Ada state loading, empty, dan error pas data lagi di-fetch
- Search pakai debouncing biar ga spam request tiap ketikan
- Form tambah data pake modal (popover), ga pindah halaman lagi
- Submit form lewat AJAX (POST) yang balikin JsonResponse + HTTP status (201/400/403)
- CSRF token dikirim lewat header X-CSRFToken
- Notifikasi sukses/gagal pake toast
- Data yang dirender di sisi klien di-escape (escapeHtml) biar aman dari XSS
- Helper getCookie dan escapeHtml dipindah ke static/js/utils.js biar ga duplikat

#### AI Disclosure

Tools: Cline pake model deepseek-v4.1-flash:netra
Bagian yang dibantu AI:
- perbaikan bug pada create_education_ajax dan create_experience_ajax
- perbaikan ID form modal dan fungsi close modal
- pemindahan getCookie dan escapeHtml ke utils.js
- penerapan escapeHtml pada rendering data via JS

#### Pertanyaan Reflektif
1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!
Intinya menunda execute search, biar ga terlalu sering proses/operasi yang jalan, biar ga overload. Dalam konteks searching ini, misal kalo kita ga pake debouncing, search bakal terjadi setiap selesai input. Literally every keystroke we do will trigger a search operation. Misal kalo kita cari di section Education "SMAN 67 Indonesia", itu aja udah ada 17 karakter, dengan asumsi kita ngetik itu tanpa typo, udah ada 17 karakter yang diketik = 17 search operation, in the bigger scale, ini bakal nambah jumlah operasi sangat banyak jadi berat di server yang menjalankan operasi search tersebut.
Dengan debouncing, search operation bakal terjadi **Paling Cepat** sesuai dengan konstanta waktu yang diberikan. Kalo kita tetapkan waktunya 300ms, maka jumlah search operation yang diketik **PALING CEPAT** bakal cuma 1 operation/300ms. Cara kerjanya, dengan konstanta yang kita set 300 ms, bakal ada timer yang di-set tiap keystroke, tiap keystroke bakal nge-set lagi jadi 0ms, kalo gada keystroke setelah timer nyampe 300ms, search operation bakal dijalanin, maka search operation bakal terjadi setiap kali ada gap 300ms tanpa input yang kita masukin, jadi realitanya nyaris gabakal secepet itu (1 operation/300ms). Misal kita ngetik "SMAN 67 Indonesia", dan kita jeda 300 ms abis ngetik "SMAN", maka search operation akan berjalan dengan query "SMAN", jadi search operation ga bakal terjadi untuk "S", "SM", ataupun "SMA", kalo kita ngetiknya emang cepet.
2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Jadi intinya await itu buat nunggu hasil dari fungsi yang dia wait, yang dia tunggu. Kalo misal dia langsung kek x = fetch(apapun.json), sedangkan apapun.json butuh waktu buat dijalanin, terus kita langsung ngejalanin operasi yang pake x sedangkan apapun.json itu belum nge-return hasilnya, bisa jadi error, karena yang di saat itu ada di x kasarannya cuma janji yang pending bahwa bakal ada jawaban, sedangkan jawabannya (return valuenya) belum tentu udah ada. Fungsi await adalah dia beneran nunggu sampe ada beneran hasilnya, sebelum kita bisa menjalankan operasi pake x
3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!

