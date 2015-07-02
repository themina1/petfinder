from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Animal

# Create your views here.
def animal_list(request):
    return render(request, 'petfind/animal_list.html', {})

# Formating function for timedelta 
def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

def cats(request):
    catlist = Animal.objects.filter(animal='Cat', petStatus='A')
    catCount = catlist.count()
    sumT = timedelta(days=0)
    for cat in catlist:
        timediff = cat.lastSeen - cat.firstSeen
        sumT += timediff
    avg = sumT/catCount
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes") 
    return render(request, 'petfind/cats.html', {'catlist': catlist, 'catCount': catCount, 'averageTime': averageTime})

def cats_detail(request, pk):
    cat = get_object_or_404(Animal, pk=pk)
    return render(request, 'petfind/cats_detail.html', {'cat': cat})

def cats_adopted_list(request):
    catlist = Animal.objects.filter(animal='Cat', petStatus='X')
    catCount = catlist.count()
    sumT = timedelta(days=0)
    for cat in catlist:
        timediff = cat.lastSeen - cat.firstSeen
        sumT += timediff
    if catCount != 0:
        avg = sumT/catCount
    else: 
        avg = timedelta(days=0)
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes")
    return render(request, 'petfind/cats_adopted_list.html', {'catlist': catlist, 'catCount': catCount, 'averageTime': averageTime})

def cats_removed_list(request):
    catlist = Animal.objects.filter(animal='Cat', petStatus='Animal Removed')
    catCount = catlist.count()
    sumT = timedelta(days=0)
    for cat in catlist:
        timediff = cat.lastSeen - cat.firstSeen
        sumT += timediff
    if catCount != 0:
        avg = sumT/catCount
    else: 
        avg = timedelta(days=0)
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes")
    return render(request, 'petfind/cats_removed_list.html', {'catlist': catlist, 'catCount': catCount, 'averageTime': averageTime})

def dogs(request):
    doglist = Animal.objects.filter(animal = 'Dog', petStatus='A')
    dogCount = doglist.count()
    sumT = timedelta(days=0)
    for dog in doglist:
        timediff = dog.lastSeen - dog.firstSeen
        sumT += timediff
    avg = sumT/dogCount
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes") 
    return render(request, 'petfind/dogs.html', {'doglist': doglist, 'dogCount': dogCount, 'averageTime': averageTime})

def dogs_detail(request, pk):
    dog = get_object_or_404(Animal, pk=pk)
    return render(request, 'petfind/dogs_detail.html', {'dog': dog})

def dogs_adopted_list(request):
    doglist = Animal.objects.filter(animal='Dog', petStatus='X')
    dogCount = doglist.count()
    sumT = timedelta(days=0)
    for dog in doglist:
        timediff = dog.lastSeen - dog.firstSeen
        sumT += timediff
    if dogCount != 0:
        avg = sumT/dogCount
    else: 
        avg = timedelta(days=0)
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes")
    return render(request, 'petfind/dogs_adopted_list.html', {'doglist': doglist, 'dogCount': dogCount, 'averageTime': averageTime})

def dogs_removed_list(request):
    doglist = Animal.objects.filter(animal='Dog', petStatus='Animal Removed')
    dogCount = doglist.count()
    sumT = timedelta(days=0)
    for dog in doglist:
        timediff = dog.lastSeen - dog.firstSeen
        sumT += timediff
    if dogCount != 0:
        avg = sumT/dogCount
    else: 
        avg = timedelta(days=0)
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes")
    return render(request, 'petfind/dogs_removed_list.html', {'doglist': doglist, 'dogCount': dogCount, 'averageTime': averageTime})

def unique(request):
    uniquelist = Animal.objects.filter(animal='UniqueAnimal', petStatus='A')
    uniqueCount = uniquelist.count()
    sumT = timedelta(days=0)
    for unique in uniquelist:
        timediff = unique.lastSeen - unique.firstSeen
        sumT += timediff
    if uniqueCount != 0:
        avg = sumT/uniqueCount
    else: 
        avg = timedelta(days=0)
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes") 
    return render(request, 'petfind/unique.html', {'uniquelist': uniquelist, 'uniqueCount': uniqueCount, 'averageTime': averageTime})

def unique_detail(request, pk):
    unique = get_object_or_404(animal='UniqueAnimal', pk=pk)
    return render(request, 'petfind/unique_detail.html', {'unique': unique})

def unique_adopted_list(request):
    uniquelist = Animal.objects.filter(animal='Unique', petStatus='X')
    uniqueCount = uniquelist.count()
    sumT = timedelta(days=0)
    for unique in uniquelist:
        timediff = unique.lastSeen - unique.firstSeen
        sumT += timediff
    if uniqueCount != 0:
        avg = sumT/uniqueCount
    else: 
        avg = timedelta(days=0)
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes")
    return render(request, 'petfind/unique_adopted_list.html', {'uniquelist': uniquelist, 'uniqueCount': uniqueCount, 'averageTime': averageTime})

def unique_removed_list(request):
    uniquelist = Animal.objects.filter(animal='Unique', petStatus='Animal Removed')
    uniqueCount = uniquelist.count()
    sumT = timedelta(days=0)
    for unique in uniquelist:
        timediff = unique.lastSeen - unique.firstSeen
        sumT += timediff
    if uniqueCount != 0:
        avg = sumT/uniqueCount
    else: 
        avg = timedelta(days=0)
    averageTime=strfdelta(avg, "{days} days, {hours} hours, and {minutes} minutes")
    return render(request, 'petfind/unique_removed_list.html', {'uniquelist': uniquelist, 'uniqueCount': uniqueCount, 'averageTime': averageTime})
