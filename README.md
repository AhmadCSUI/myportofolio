Nama: Ahmad Shanahan Zorya
NPM: 2506541894
Kelas: PBP D

## Tugas 3

buat ngambil JSON, bisa di /api/educations/ dan /api/experiences/

> Jujur ini pertama kali Vibecoding, HAHAHAHAH seru seru ngeri gimanaa gitu ngerjainnya

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

Tools: Cline
Bagian yang dibantu AI:
- perbaikan bug pada create_education_ajax dan create_experience_ajax
- perbaikan ID form modal dan fungsi close modal
- pemindahan getCookie dan escapeHtml ke utils.js
- penerapan escapeHtml pada rendering data via JS
