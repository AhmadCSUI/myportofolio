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
