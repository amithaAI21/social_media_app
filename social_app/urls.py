from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('user_management.urls')),
    path('interaction/',include('social_interactions.urls')),
]
