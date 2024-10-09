# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.business_list, name='business_list'),
#     path('add/', views.add_business, name='add_business'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('https://www.amazon.in/ref=nav_logo', views.business_list, name='business_list'),  # Root URL for listings app
    path('add/', views.add_business, name='add_business'),  # URL to add a new business
]
