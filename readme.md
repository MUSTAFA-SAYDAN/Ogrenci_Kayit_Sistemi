#🎓 Flask Öğrenci Kayıt Sistemi (JWT ile)
Bu proje, kullanıcıların kayıt olup giriş yapabildiği ve JWT token ile korunan basit bir öğrenci yönetim API’sidir. Flask, SQLAlchemy, Flask-Bcrypt ve PyJWT kullanılarak geliştirilmiştir.

#✨ Özellikler
👤 Kullanıcı kayıt ve giriş sistemi

🔐 JWT ile güvenli kimlik doğrulama

📝 Öğrenci ekleme, listeleme, güncelleme ve silme

💾 SQLite veritabanı

🔒 Token korumalı API uç noktaları

#⚙️ Kurulum
Projeyi klonlayın veya indirin.

Komut satırında proje klasörüne gidin:

bash
Kopyala
Düzenle
cd Ogrenci_Kayit_Sistemi
Sanal ortam oluşturun ve aktif edin:

css
Kopyala
Düzenle
python -m venv venv
venv\Scripts\activate  (Windows için)
Gerekli kütüphaneleri yükleyin:

nginx
Kopyala
Düzenle
pip install -r requirements.txt
Uygulamayı başlatın:

nginx
Kopyala
Düzenle
python app.py
Uygulama 👉 http://localhost:5001 adresinde çalışacaktır.

🚀 API Kullanımı
🆕 Kayıt Olma
POST /kayit endpoint'ine aşağıdaki JSON verisi gönderilir:

json
Kopyala
Düzenle
{
  "kullanici_adi": "Mustafa",
  "sifre": "1234"
}
🔑 Giriş Yapma
POST /giris endpoint'ine aşağıdaki JSON verisi gönderilir:

json
Kopyala
Düzenle
{
  "kullanici_adi": "Mustafa",
  "sifre": "1234"
}
Başarılı girişte 🎫 JWT token döner. Bu token diğer API çağrılarında kullanılacaktır.

📚 Öğrenci İşlemleri
Aşağıdaki işlemler için her isteğin başlığında Authorization: Bearer <TOKEN> eklenmelidir.

👀 Öğrenci Listele:
GET /ogrenciler

➕ Öğrenci Ekle:
POST /ogrenciler
Gövde örneği:

json
Kopyala
Düzenle
{
  "isim": "Mustafa",
  "soyisim": "Saydan",
  "numara": 123456
}
🔎 Belirli Öğrenciyi Getir:
GET /ogrenciler/<id>

✏️ Öğrenci Güncelle:
PUT /ogrenciler/<id>
Gövde örneği (güncellenecek alanlar):

json
Kopyala
Düzenle
{
  "isim": "Mustafa"
}
🗑️ Öğrenci Sil:
DELETE /ogrenciler/<id>

#🛠️ Kullanılan Teknolojiler
🐍 Python 3.x

🌶 Flask

🐘 Flask SQLAlchemy

🔐 Flask Bcrypt

🔑 PyJWT

🗄 SQLite

👨‍💻 Geliştirici
Mustafa
GitHub: github.com/kullaniciadi

📄 Lisans
MIT Lisansı altında lisanslanmıştır.
