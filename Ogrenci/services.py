from extensions import db
from models import Ogrenci

def ogrenci_ekle(isim,numara,kullanici_id):
    yeni_ogrenci=Ogrenci(isim=isim,numara=numara,kullanici_id=kullanici_id)
    db.session.add(yeni_ogrenci)
    db.session.commit()
    return yeni_ogrenci

def ogrenci_getir(ogrenci_id):
    return Ogrenci.query.get(ogrenci_id)

def ogrenci_guncelle(ogrenci,isim=None,numara=None,kullanici_id=None):
    if isim is not None:
        ogrenci.isim=isim
    if numara is not None:
        ogrenci.numara=numara
    if kullanici_id is not None:
        ogrenci.kullanici_id=kullanici_id
    
    db.session.commit()
    return ogrenci

def ogrenci_sil(ogrenci):
    db.session.delete(ogrenci)
    db.session.commit()