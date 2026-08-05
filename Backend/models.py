from sqlalchemy import Column , Integer , String  , Float , DateTime 
from database   import Base 
import datetime 

class Kullanici(Base):
    __tablename__ = "Kullanicilar"

    id = Column(Integer, primary_key = True ,  index = True)
    ad_soyad = Column(String , index = True )
    email = Column(String , unique = True , index = True )

class ModelPerformans(Base):
    __tablename__ = "Model_performanslari"

    id= Column(Integer , primary_key = True , index = True)
    kullanilan_model = Column(String , index = True)
    islem_hizi_ms = Column(Float)
    fps_degeri = Column(Float)
    olcum_zamani = Column(DateTime,default=datetime.datetime.utcnow)

    # Veritabandaki tablolari python siniflari larak tuttuk
