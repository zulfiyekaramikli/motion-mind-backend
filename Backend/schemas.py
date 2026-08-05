from pydantic import BaseModel , EmailStr 

class KullaniciCreate(BaseModel):
    ad_soyad : str 
    email : str 

class KullaniciResponse(BaseModel):
    id : int 
    ad_soyad : str 
    email : str 
    
class Config : 
    from_attributes = True 
    # SQLAlchemy modellerini Pydantic modellerine dönüştürmeyi sağlar