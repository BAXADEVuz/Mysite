from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MypassordResetForm

urlpatterns = [
    path("", views.home),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),

    # Login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
    path('passwrod-reset/',auth_view.PasswordResetView.as_view(template_name='core/password_reset.html',form_class=MypassordResetForm),name='password_reset'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)