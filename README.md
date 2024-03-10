# Instagram Clone
Bu proje, Django kullanılarak oluşturulmuş bir Instagram klonudur. Kullanıcılar fotoğraf yükleyebilir, yorum yapabilir, beğenebilir ve diğer kullanıcıları takip edebilirler.

# Kurulum
1. Sanal ortamı oluşturun ve etkinleştirin:
   python -m venv venv
   source venv/bin/activate  # Windows için: venv\Scripts\activate
2. Gerekli bağımlılıkları yükleyin:
   pip install -r requirements.txt
3. Veritabanını oluşturun ve migrate edin:
   python manage.py migrate
4. Yönetici hesabı oluşturun:
   python manage.py createsuperuser
5. Sunucuyu çalıştırın:
   python manage.py runserver
6. Tarayıcınızda http://localhost:8000 adresine giderek uygulamayı görüntüleyin.

# Kullanılan Teknolojiler
-Django
-HTML
-CSS
-Bootstrap

# Özellikler:
**Kayıt Olma:** Kullanıcılar için benzersiz bir e-posta adresi ve kullanıcı adı girmeleri gerekmektedir. Şifre en az 3 karakterden oluşmalıdır.

**Giriş Yapma:** Kayıt olduktan sonra kullanıcılar giriş yapabilirler.

**Ana Sayfa:** Kullanıcıların paylaştığı gönderileri görebileceği bir ana sayfa bulunmaktadır. Gönderilere yorum yapabilir, beğenebilir ve paylaşabilirler.

**Profil Sayfası:** Kullanıcıların kendi profil bilgilerini ve paylaştıkları gönderileri görebileceği bir profil sayfası vardır.

**Keşfet Sayfası:** Popüler veya önerilen gönderilerin bulunduğu bir keşfet sayfası bulunmaktadır.

**Takip Etme:** Kullanıcılar diğer kullanıcıları takip edebilirler.

**Beğenme:** Kullanıcılar gönderilere beğeni verebilirler.

**Yorum Ekleme:** Kullanıcılar gönderilere yorum yapabilirler. Yorumlar gönderinin alt kısmında görüntülenir.



![Ana Sayfa Ekran Görüntüsü](screenshots/screenshot1.png)
