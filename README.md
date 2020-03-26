# Flask-Blog-API
Školica Flaska by LVH-27

Blog API

  Implementirajte API koji ima endpointove za:
- dohvat svih blog postova
- dohvat pojedinog blog posta (s nekim ID-em; vratit 404 ako ga ne nađe)
- upload novog blog posta (vratit 400 ako request body (onaj JSON) nije ispravno formatiran)
- editiranje postojećeg blog posta (vratit 400 ako request body (onaj JSON) nije ispravno formatiran)
- dohvat svih blog postova koji sadrže neki string (predan kao parametar u GET requestu)
- dohvat svih blog postova koje je napisao neki član
