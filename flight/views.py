from django.shortcuts import render,redirect
from .models import flight_info,passengers
# Create your views here.
def home(request):
    return render(request,"flight/home.html",{
        "flights_info":flight_info.objects.all()
    })
def flight_infor(request,flight_id):
    flightinfo=flight_info.objects.get(pk=flight_id)
    return render(request,"flight/flight_detail.html",{
        "flight":flightinfo,
        "passengers":flightinfo.passenger.all(),
        "non_passenger":passengers.objects.exclude(flights=flightinfo).all()
    })

def book(request,flight_id):
    if request.method=='POST':
        flightinfo=flight_info.objects.get(id=flight_id)
        psgn=passengers.objects.get(id=int(request.POST['non_passenger']))
        psgn.flights.add(flightinfo)
        psgn.save()
        return redirect('flight-home')