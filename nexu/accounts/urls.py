from django.urls import path
from .views import signup
from .views import logout_view
from .views import login_view

urlpatterns=[
    path('signup/', signup),
    path('logout/', logout_view),
    path('login/', login_view),
]