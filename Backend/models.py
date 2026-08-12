from sqlalchemy import Column , Integer , String  , Float , DateTime , ForeignKey
from sqlalchemy.orm import relationship 
from database   import Base 
import datetime 

class Kullanici(Base):
    __tablename__ = "Kullanicilar"

    id = Column(Integer, primary_key = True ,  index = True)
    ad_soyad = Column(String , index = True )
    email = Column(String , unique = True , index = True )
    hashed_password = Column(String)
    
    ruh_halleri = relationship("RuhHaliGecmisi" , back_populates = "sahip")
    oyunlastirma_verisi = relationship("Oyunlastirma" , back_populates="sahip",uselist= False)

class RuhHaliGecmisi(Base):
    __tablename__="ruh_hali_gecmisi"

    id = Column(Integer, primary_key= True , index = True)
    Kullanici_id = Column(Integer, ForeignKey("Kullanicilar.id")) # hangi kullaniciya ait oldugunu belirttik 
    ruh_hali = Column(String)
    onerilen_antrenman=Column(String)
    tarih = Column( DateTime , default=datetime.datetime.utcnow)

    sahip = relationship("Kullanici",back_populates="ruh_halleri") # kullanici tablosuyla baglanti kurdurduk 


class Oyunlastirma(Base):
    __tablename__="oyunlastirma"

    id = Column(Integer , primary_key=True, index= True)
    Kullanici_id= Column(Integer , ForeignKey("Kullanicilar.id"),unique=True)
    puan = Column(Integer , default=0)
    rozetler=Column(String , default ="")
    günlük_seri = Column(Integer ,  default =0)

    sahip=relationship("Kullanici",back_populates="oyunlastirma_verisi")


class ModelPerformans(Base):
    __tablename__ = "Model_performanslari"

    id= Column(Integer , primary_key = True , index = True)
    kullanilan_model = Column(String , index = True)
    islem_hizi_ms = Column(Float)
    fps_degeri = Column(Float)
    olcum_zamani = Column(DateTime,default=datetime.datetime.utcnow)

    # Veritabandaki tablolari python siniflari larak tuttuk
