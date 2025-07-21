# 🎓 Flask Öğrenci Kayıt Sistemi (JWT ile)

---

## 🚀 Kurulum

```bash
git clone https://github.com/kullaniciadi/Ogrenci_Kayit_Sistemi.git
cd Ogrenci_Kayit_Sistemi
python -m venv venv
venv\Scripts\activate       # Windows için
pip install -r requirements.txt
python app.py
**## 🔐 Kullanıcı Kayıt**
http
Kopyala
Düzenle
POST /kayit
Content-Type: application/json

{
  "kullanici_adi": "Mustafa",
  "sifre": "1234"
}
🔑 Giriş Yap
http
Kopyala
Düzenle
POST /giris
Content-Type: application/json

{
  "kullanici_adi": "Mustafa",
  "sifre": "1234"
}
Başarılı girişte dönen token örneği:

json
Kopyala
Düzenle
{
  "token": "eyJhbGc..."
}
📚 Öğrenci İşlemleri (Token Gerekli)
Her istekte header’a ekleyin:

makefile
Kopyala
Düzenle
Authorization: Bearer <JWT_TOKEN>
➕ Öğrenci Ekle
http
Kopyala
Düzenle
POST /ogrenciler
Content-Type: application/json
Authorization: Bearer <JWT_TOKEN>

{
  "isim": "Mustafa",
  "soyisim": "SAYDAN",
  "numara": 123456
}
👀 Öğrenci Listesi Getir
http
Kopyala
Düzenle
GET /ogrenciler
Authorization: Bearer <JWT_TOKEN>
🔎 Öğrenci Detayı
http
Kopyala
Düzenle
GET /ogrenciler/{id}
Authorization: Bearer <JWT_TOKEN>
✏️ Öğrenci Güncelle
http
Kopyala
Düzenle
PUT /ogrenciler/{id}
Content-Type: application/json
Authorization: Bearer <JWT_TOKEN>

{
  "isim": "Mustafa"
}
🗑️ Öğrenci Sil
http
Kopyala
Düzenle
DELETE /ogrenciler/{id}
Authorization: Bearer <JWT_TOKEN>
🛠 Kullanılan Teknolojiler
Python 3.x

Flask

Flask SQLAlchemy

Flask Bcrypt

PyJWT

SQLite

👨‍💻 Geliştirici
Mustafa
GitHub: github.com/MUSTAFA-SAYDAN

📄 Lisans
MIT Lisansı
