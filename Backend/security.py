from passlib.context import CryptContext # passlib = python dünyasinda en iyi sifreleme kütüphanesi , CryptContext = sifreleme yöntemlerini yönetmemizi saglar 

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated ="auto")  # schemes=["bcrypt"]: Sistemimize şifreleri şifrelerken Bcrypt algoritmasını kullanmasını söylüyoruz. Bcrypt, siber güvenlikte altın standartlardan biridir. deprecated="auto": İleride Bcrypt'in daha yeni ve güvenli bir versiyonu çıkarsa, eski şifreleri otomatik olarak yeni standarda yükseltmek için bir açık kapı bırakır.

def get_password_hash(password : str):
    return pwd_context.hash(password) 

# bu satirlarla sifreyi veritabanina kaydettik 

def verify_password(plain_password , hashed_password):
    return pwd_context.verify(plain_password , hashed_password)

#bu satirlarla yeniden sayfaya girdigimizde sifrenin dogrulugunu kontrol ettik 