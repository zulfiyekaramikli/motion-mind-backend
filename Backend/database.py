from sqlalchemy import create_engine # create_engine arada ki baglantiyi kuran ana köprü , tüm sorgular bundan geciyor 
from sqlalchemy.orm import sessionmaker # sessionmaker veritabaninda degisiklik yapmak istedigimizde bize temiz ve güvenli oturum acar 
#from models import Base # Base veritabani toblolarini tanimlamamizi saglar . postgresql kullanmaktan vazgectigimiz icin bu satiri kaldirdik 
from sqlalchemy.ext.declarative  import declarative_base # SQLLite kullandik ve bu kodda tablolarimizi olusturacak temel sinif tanimlamasi icin  

SQLALCHEMY_DATABASE_URL = "sqlite:///./spor_asistani.db" # veritabaninin tam adresi tanimlandi 

engine = create_engine( # Engine (Motor), SQLAlchemy'nin kalbidir. Veritabanı ile olan gerçek bağlantıyı o kurar ve SQL (yapısal sorgulama dili) komutlarını veritabanına iletir.
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False }
    )

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine ) # bu satirlarda ayarlar yapildi  autocemmit veritabanina veri ekledigimizde aninda kayit yapmaz bize sorar evet dersek ekleme yapar bu sekilde yarim yamalak veri kaydetmenin önüne gecilir 
Base = declarative_base() #Python sınıfları olarak yazacağız. Yazacağımız bu sınıfların hepsini Base sınıfından türeteceğiz

# Bu kodlar FastAPI uygulamamiz ile Sqlite  veritabanimiz arasindaki baglantiyi sagliyor 