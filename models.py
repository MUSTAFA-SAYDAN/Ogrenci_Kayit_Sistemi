from extensions import db, bcrypt

class Kullanici(db.Model):
    __tablename__ = "kullanicilar"

    id = db.Column(db.Integer, primary_key=True)
    kullanici_adi = db.Column(db.String(100), unique=True, nullable=False)
    sifre_hash = db.Column(db.String(100), nullable=False)

    def sifre_kontrol(self, sifre):
        return bcrypt.check_password_hash(self.sifre_hash, sifre)


class Ogrenci(db.Model):
    __tablename__ = "ogrenciler"

    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(100), nullable=False)
    soyisim = db.Column(db.String(100), nullable=False)
    numara = db.Column(db.String(20), nullable=False)
    kullanici_id = db.Column(db.Integer, db.ForeignKey("kullanicilar.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "isim": self.isim,
            "soyisim": self.soyisim,
            "numara": self.numara,
            "kullanici_id":self.kullanici_id
        }