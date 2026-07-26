from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .forms import RoomForm
from .models import Room


# Create your views here.
# rooms = [
#     {'id' : 1, 'name' : 'lets Start the adventure'},
#     {'id' : 2, 'name' : 'Arise'},
#     {'id' : 3, 'name' : 'im gonna be the pirate king'}
# ]

def home(request):
    rooms = Room.objects.all()
    return render(request , 'basic/home.html' , {'rooms' : rooms})

def room(request , pk):
    room = Room.objects.get(id = pk)            
    context = {'room':room}
    return render(request,'basic/room.html', context)

def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'basic/room_form.html', context)
