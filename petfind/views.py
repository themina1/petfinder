from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Cat
from .models import Dog
from .models import UniqueAnimal

# Create your views here.
def animal_list(request):
    return render(request, 'petfind/animal_list.html', {})

def cats(request):
    catlist = Cat.objects.filter(firstSeen__lte=timezone.now()).order_by('firstSeen')
    catCount = catlist.count()
    sum = timedelta(days=0)
    for cat in catlist:
        timediff = cat.lastSeen - cat.firstSeen
        sum += timediff
    avg = sum/catCount
    print(avg)        
    return render(request, 'petfind/cats.html', {'catlist': catlist, 'catCount': catCount, 'avg': avg})

def cats_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'petfind/cats_detail.html', {'cat': cat})

def dogs(request):
    doglist = Dog.objects.filter(firstSeen__lte=timezone.now()).order_by('firstSeen')
    return render(request, 'petfind/dogs.html', {'doglist': doglist})

def dogs_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'petfind/dogs_detail.html', {'dog': dog})

def unique(request):
    uniquelist = UniqueAnimal.objects.filter(firstSeen__lte=timezone.now()).order_by('firstSeen')
    return render(request, 'petfind/unique.html', {'uniquelist': uniquelist})

def unique_detail(request, pk):
    unique = get_object_or_404(UniqueAnimal, pk=pk)
    return render(request, 'petfind/unique_detail.html', {'unique': unique})