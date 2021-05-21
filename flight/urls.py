from django.urls import path
from .views import home,flight_infor,book
urlpatterns=[
    path("home",home,name='flight-home'),
    path("details/<int:flight_id>",flight_infor,name='flight-details'),
    path("book/<int:flight_id>",book,name='flight-book')
]