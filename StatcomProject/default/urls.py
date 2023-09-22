from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_page, name="homepage"),
    path('login/', views.login_page, name="loginpage"),
    path('gallery/', views.gallery_page, name="gallerypage"),
    path('about/', views.about_page, name="aboutpage"),
    path('home/', views.home, name="home"), #home page
    path('address/', views.address_page, name="addresspage"),
    path('contact/', views.contact_page, name="contactpage"),
    path('book/', views.book_page, name="bookpage"),
    path('index/', views.start_page, name="indexpage"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)