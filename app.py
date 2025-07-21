from flask import Flask, request, jsonify
from models import db, bcrypt, Kullanici, Ogrenci
from functools import wraps
import jwt
import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ogrenciler.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "gizli_anahtar"  

db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    db.create_all()


def token_gerekli(f):
    @wraps(f)
    def sarici(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"hata": "Token gerekli!!!"}), 401
        try:
            token = token.replace("Bearer ", "")  
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            kullanici_id = data["kullanici_id"]
        except jwt.ExpiredSignatureError:
            return jsonify({"hata": "Token süresi bitmiş"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"hata": "Geçersiz token!!!"}), 401

        return f(kullanici_id, *args, **kwargs)
    return sarici


@app.route("/kayit", methods=["POST"])
def kayit():
    data = request.json
    kullanici_adi = data.get("kullanici_adi")
    sifre = data.get("sifre")

    if Kullanici.query.filter_by(kullanici_adi=kullanici_adi).first():
        return jsonify({"hata": "Bu kullanıcı adı zaten alınmış"}), 400

    sifre_hash = bcrypt.generate_password_hash(sifre).decode("utf-8")
    yeni_kullanici = Kullanici(kullanici_adi=kullanici_adi, sifre_hash=sifre_hash)
    db.session.add(yeni_kullanici)
    db.session.commit()

    return jsonify({"mesaj": "Kayıt başarılı"}), 201


@app.route("/giris", methods=["POST"])
def giris():
    data = request.json
    kullanici_adi = data.get("kullanici_adi")
    sifre = data.get("sifre")

    kullanici = Kullanici.query.filter_by(kullanici_adi=kullanici_adi).first()
    if not kullanici or not kullanici.sifre_kontrol(sifre):
        return jsonify({"hata": "Geçersiz kullanıcı adı veya şifre"}), 401

    token = jwt.encode(
        {
            "kullanici_id": kullanici.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({"token": token})


@app.route("/ogrenciler", methods=["POST"])
@token_gerekli
def ogrenci_ekle(kullanici_id):
    data = request.json
    isim = data.get("isim")
    soyisim = data.get("soyisim")
    numara = data.get("numara")

    if not (isim and soyisim and numara):
        return jsonify({"hata": "Eksik öğrenci bilgisi"}), 400

    yeni_ogrenci = Ogrenci(
        isim=isim,
        soyisim=soyisim,
        numara=numara,
        kullanici_id=kullanici_id
    )

    db.session.add(yeni_ogrenci)
    db.session.commit()

    return jsonify({"mesaj": "Öğrenci eklendi"}), 201


@app.route("/ogrenciler", methods=["GET"])
@token_gerekli
def ogrencileri_listele(kullanici_id):
    ogrenciler = Ogrenci.query.all()
    return jsonify({"ogrenciler": [k.to_dict() for k in ogrenciler]})


@app.route("/ogrenciler/<int:id>", methods=["GET"])
@token_gerekli
def ogrenci_getir(kullanici_id, id):
    ogrenci = Ogrenci.query.filter_by(id=id, kullanici_id=kullanici_id).first()
    if not ogrenci:
        return jsonify({"hata": "Öğrenci bulunamadı"}), 404
    return jsonify(ogrenci.to_dict())


@app.route("/ogrenciler/<int:id>", methods=["PUT"])
@token_gerekli
def ogrenci_guncelle(kullanici_id, id):
    ogrenci = Ogrenci.query.filter_by(id=id, kullanici_id=kullanici_id).first()
    if not ogrenci:
        return jsonify({"hata": "Öğrenci bulunamadı"}), 404

    data = request.json
    ogrenci.isim = data.get("isim", ogrenci.isim)
    ogrenci.soyisim = data.get("soyisim", ogrenci.soyisim)
    ogrenci.numara = data.get("numara", ogrenci.numara)

    db.session.commit()
    return jsonify({"mesaj": "Öğrenci güncellendi", "ogrenci": ogrenci.to_dict()})


@app.route("/ogrenciler/<int:id>", methods=["DELETE"])
@token_gerekli
def ogrenci_sil(kullanici_id, id):
    ogrenci = Ogrenci.query.filter_by(id=id, kullanici_id=kullanici_id).first()
    if not ogrenci:
        return jsonify({"hata": "Öğrenci bulunamadı"}), 404

    db.session.delete(ogrenci)
    db.session.commit()
    return jsonify({"mesaj": "Öğrenci silindi"})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
