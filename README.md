## About Project
Projek ini menggunakan database chinook.db yang terdapat dalam dir /data. Dari API ini dapat diakses 3 jenis data hasil pengolahan dengan menggunakan python. Berikut ini merupakan list data yang dapat diakses beserta penjelasan singkatnya
___
## Dependencies : 
- Pandas    (pip install pandas)
- Flask     (pip install flask)
- Gunicorn  (pip install gunicorn)
___
'''
Berikut ini merupakan endpoint yang tersedia dalam API:
## Rata-rata umur pegawai berdasarkan jabatan
Data ini merupakan data rata-rata umur dari pegawai pada setiap jawabatan. Data .json dapat diakses pada alamat berikut >> /average_age_title

## Minat genre di setiap negara
Data ini merupakan data banyaknya penggemar dari suatu genre di suatu negara tertentu >> /fav_genre/country

## Data Invoice Total Negara
Pada data ini dapat diambil data invoices dari negara yang diinginkan dengan beberapa end point sebagai berikut:
-  /Argentina
-  /Australia
-  /Austria
-  /Belgium
-  /Spain
-  /Sweden
-  /USA
-  /United Kingdom
'''
___
We have deployed a simple example on : https://dashboard.heroku.com/apps/lugita-api

