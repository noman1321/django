# from django.contrib.auth import views as auth_views
# from django.urls import path

# urlpatterns = [
#     path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
#     path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),            # Admin URL
    path('', include('listings.urls')),         # Root URL that includes listings app URLs
]
