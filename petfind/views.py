from django.shortcuts import render
from django.utils import timezone
from .models import Cat
from .models import Dog
from .models import Unique

# Create your views here.
def post_list(request):
    return render(request, 'petfind/post_list.html', {})

def cats(request):
    catlist = Cat.objects.filter(lastUpdate__lte=timezone.now()).order_by('lastUpdate')
    return render(request, 'petfind/cats.html', {'catlist': catlist})

def dogs(request):
    doglist = Dog.objects.filter(lastUpdate__lte=timezone.now()).order_by('lastUpdate')
    return render(request, 'petfind/dogs.html', {'doglist': doglist})

def unique(request):
    uniquelist = Unique.objects.filter(lastUpdate__lte=timezone.now()).order_by('lastUpdate')
    return render(request, 'petfind/unique.html', {'uniquelist': uniquelist})