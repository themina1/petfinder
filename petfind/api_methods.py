# Required imports

from urllib.request import urlopen
from json import load
import codecs
import os
import django
from django.utils import timezone
from petfind.rockBridgetwitter import updateTwitterStatus
import pprint

# To access Django Models in our script
os.environ.__setitem__("DJANGO_SETTINGS_MODULE", "petsite.settings")
django.setup()
from petfind.models import Animal
# Defining the constants:
KEY = "6d3a2622c9ee34420afe02206d1cee12"
URL = "http://api.petfinder.com/"
URL_JSON_KEY = "key=" + KEY + "&format=json"
SHELTER_ID = "&id=VA321"
LOCATION = "&location=24450"


# To make the json readable in utf-8

reader = codecs.getreader("utf-8")

# Main method:
def petExist(animal, pet_id):
    """ Returns True if pet exists"""
    return Animal.objects.filter(pk = pet_id).exists()

    
def getStatus(url, URL_JSON_KEY,pet_id):
    """Returns the json object containing all the pet info from a particular shelter"""
    
    method = "pet.get?"
    petId = "&id="+pet_id
    url+= method + URL_JSON_KEY + petId
    petJson = urlopen(url)
    petsInfo = load(reader(petJson))
    message = petsInfo['petfinder']['header']['status']['code']['$t']
    if message == '100':
        status = petsInfo['petfinder']['pet']['status']['$t']
        return status
    elif message =='201':
        status = "Animal Removed"
        return status
    else:
        print("Something went wrong. Sorry.")

def changePetStatus():
    animals = Animal.objects.all()
    for animal in animals:
        if animal.match== "No" and animal.petStatus!='X' and animal.petStatus!='Animal Removed':
            pet_id = animal.petId
            status = getStatus(URL,URL_JSON_KEY, pet_id)
            animal.petStatus = status
            animal.save()
            print(pet_id+"'s status has been changed to "+status)
        animal.match = "No"
        animal.save()

def shelterGetPets(url, URL_JSON_KEY, shelter_id):
    """Returns the json object containing all the pet info from a particular shelter"""
    
    method = "shelter.getPets?"
    count = "&count=100"
    url+= method + URL_JSON_KEY + shelter_id + count
    petJson = urlopen(url)
    petInfo = load(reader(petJson))
    return petInfo

def addAnimalsToDb(petsInfo):
    """ This function takes a json file as an input and parses it. It collects info about
    the pet and creates and saves the pet in their corresponding database table. """
    
    for pet in petsInfo['petfinder']['pets']['pet']:        
        
        #Parsing the json file to get individual information
         
        animal = pet['animal']['$t']    
        name = pet['name']['$t']
        pet_id = pet['id']['$t']
        desc = pet['description']['$t']
        age = pet['age']['$t']
        breeds = pet['breeds']['breed']
        breed = ""
        # because some pets have multiple breed stored in a list
        try:                          
            breed = breeds['$t']
        except TypeError:
            for x in breeds:
                breed += x['$t'] + ", "
                        
        status = pet['status']['$t']
        sex = pet['sex']['$t']
        size = pet['size']['$t']
        mix = pet['mix']['$t']
        match = "Yes"
        features = pet['options']['option']
        feature = ""
        # because some pets have multiple breed stored in a list
        try:
            feature = features['$t']
        except TypeError:             
            for x in features:
                feature += x['$t'] + ", "
        photo = pet['media']['photos']['photo'][2]['$t']
        if petExist(animal, pet_id):  
            firstSeen = Animal.objects.get(pk = pet_id).firstSeen
            pet =  Animal(animal = animal, petId = pet_id, petName = name, 
                        petDescription = desc, petAge = age, 
                        petBreed = breed, petStatus = status, 
                        petSex = sex, petSize = size, 
                        petMix = mix, petFeatures = feature, 
                        lastSeen = timezone.now(), 
                        firstSeen = firstSeen,match = match, petPhoto = photo) 
                
            pet.save()
                
# if the pet doesn't exist, add the pet.            
        else:                                           
            pet = Animal(animal = animal, petId = pet_id, petName = name, 
                      petDescription = desc, petAge = age, 
                      petBreed = breed, petStatus = status, 
                      petSex = sex, petSize = size, 
                      petMix = mix, petFeatures = feature, 
                      lastSeen = timezone.now(), 
                      firstSeen = timezone.now(), match = match, petPhoto = photo)   
                
            pet.save()
            updateTwitterStatus(animal, name, pet_id)

            print("A new %s has been added.", animal)
    
    #pprint.pprint(petsInfo)        
    print("Pet information added to database.")

##########################################################################################################################

if __name__ == "__main__":

    petsInfo = shelterGetPets(URL, URL_JSON_KEY, SHELTER_ID)
    addAnimalsToDb(petsInfo)
    changePetStatus()

