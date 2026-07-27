from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from .forms import RoomForm
from .models import Room , Topic


# Create your views here.
# rooms = [
#     {'id' : 1, 'name' : 'lets Start the adventure'},
#     {'id' : 2, 'name' : 'Arise'},
#     {'id' : 3, 'name' : 'im gonna be the pirate king'}
# ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(topic__name__icontains = q)
    topics = Topic.objects.all()

    context = {'rooms' : rooms , 'topics' : topics}
    return render(request , 'basic/home.html' , context)

def room(request , pk):
    room = Room.objects.get(id = pk)            
    context = {'room':room}
    return render(request,'basic/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'basic/room_form.html', context)

def updateRoom(request , pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance = room)

    if request.method == 'POST':
        form = RoomForm(request.POST , instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'basic/room_form.html', context)


def deleteRoom(request , pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request , 'basic/delete.html',{"obj":room})



