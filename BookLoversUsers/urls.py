
from django.contrib import admin
from django.urls import path
from users.views import UserView
from django.contrib.auth import views as auth_views
from users.views import user, register, register_1, register_2, home, profile
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="homepage"),
    # path('user/<int:user_id>', UserView.as_view),
    path('user/<int:user_id>', user, name="user_view"),
    path('register', register, name="register_user_view"),
    path('register_1', register_1, name="register_user_view_1"),
    path('register_2', register_2, name="register_user_view_2"),
    path('profile', profile, name="profile"),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),

]

# urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)