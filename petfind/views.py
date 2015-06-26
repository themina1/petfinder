from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Cat
from .models import Dog
from .models import UniqueAnimal

# Create your views here.
def animal_list(request):
    return render(request, 'petfind/animal_list.html', {})

def cats(request):
    catlist = Cat.objects.filter(timeInShelter__lte=timezone.now()).order_by('timeInShelter')
    return render(request, 'petfind/cats.html', {'catlist': catlist})

def cats_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'petfind/cats_detail.html', {'cat': cat})

def dogs(request):
    doglist = Dog.objects.filter(timeInShelter__lte=timezone.now()).order_by('timeInShelter')
    return render(request, 'petfind/dogs.html', {'doglist': doglist})

def dogs_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'petfind/dogs_detail.html', {'dog': dog})

def unique(request):
    uniquelist = UniqueAnimal.objects.filter(timeInShelter__lte=timezone.now()).order_by('timeInShelter')
    return render(request, 'petfind/unique.html', {'uniquelist': uniquelist})

def unique_detail(request, pk):
    unique = get_object_or_404(UniqueAnimal, pk=pk)
    return render(request, 'petfind/unique_detail.html', {'unique': unique})