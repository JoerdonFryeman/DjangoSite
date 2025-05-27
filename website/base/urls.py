from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('category/<slug:cat_slug>/', views.CategoryPage.as_view(), name='category'),
    path('content/<slug:slug>/', views.ContentPage.as_view(), name='content'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('terms/', views.TermsPage.as_view(), name='terms'),
    path('privacy/', views.PrivacyPage.as_view(), name='privacy'),
    path('email_was_sent/', views.EmailWasSent.as_view(), name='email_was_sent'),
    path('error_404/', views.page_not_found, name='error_404'),
]
