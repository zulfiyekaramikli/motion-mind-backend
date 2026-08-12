from fastapi import FastAPI , Depends , HTTPException  # API olusturan kütüphane
from sqlalchemy.orm import Session 
import models # veritabani tablolarinin bulundugu dosya 
import schemas 
import security 
from database import engine , SessionLocal # engine SQLite veritabanina baglanan motor 

models.Base.metadata.create_all(bind=engine) # veritabani tablolarini fiziksel olarak olusturduk 

app = FastAPI(title="Spor ve Saglik Asistani API ")

# Her istek için veritabanı oturumu açıp iş bitince kapatan bağımlılık
def get_db():
    db = SessionLocal()
    try :
        yield db 
    finally :
        db.close()

# Yeni kullanıcı ekleme
@app.post("/Kullanicilar/", response_model= schemas.KullaniciResponse) # api rotasini tanimladik 
def Kullanici_olustur(Kullanici: schemas.KullaniciCreate, db : Session = Depends(get_db)):

    # Aynı email adresine sahip başka biri var mı diye kontrol edelim
    veritabanindaki_kullanici = db.query(models.Kullanici).filter(models.Kullanici.email == Kullanici.email).first()

    if veritabanindaki_kullanici:
        raise HTTPException(status_code =400 , detail = " Bu e-posta adresi zaten kayitli !")

    #Kullanıcının girdiği düz şifreyi motorumuzla hash'leyelim
    kriptolu_sifre = security.get_password_hash(Kullanici.sifre)

    # Yeni kullanıcı nesnesini oluşturalım
    yeni_kullanici = models.Kullanici(
        ad_soyad = Kullanici.ad_soyad ,
        email = Kullanici.email,
        hashed_password = kriptolu_sifre
        )
    
    # Veritabanına ekleyip kaydedelim
    db.add(yeni_kullanici)
    db.commit()
    db.refresh(yeni_kullanici)# Veritabanından gelen ID gibi otomatik alanları günceller

    return yeni_kullanici 

@app.get("/Kullanicilar/", response_model=list[schemas.KullaniciResponse])
def kullanicilari_getir(skip: int = 0 , limit: int =100 , db : Session = Depends(get_db)):
    kullanicilar = db.query(models.Kullanici).offset(skip).limit(limit).all()
   
    return kullanicilar  
