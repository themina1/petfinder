# Required imports

from urllib.request import urlopen
from json import load
import codecs
import pprint
import os
import django

os.environ.__setitem__("DJANGO_SETTINGS_MODULE", "petsite.settings")

import petfind.models
# To access Django Models in our script

django.setup()

# Defining the constants:
KEY = "6d3a2622c9ee34420afe02206d1cee12"
URL = "http://api.petfinder.com/"
URL_JSON_KEY = "key=" + KEY + "&format=json"
SHELTER_ID = "&id=VA321"
LOCATION = "&location=24450"


# To make the json readable in utf-8

reader = codecs.getreader("utf-8")

# Main method:


def shelterGetPets(url, URL_JSON_KEY, shelter_id):
    """Returns the json object containing all the pet info from a particular shelter"""
    
    method = "shelter.getPets?"
    count = "&count=50"
    url+= method + URL_JSON_KEY + shelter_id + count
    petJson = urlopen(url)
    petInfo = load(reader(petJson))
    return petInfo

def addAnimalsToDb(petsInfo):
    """ This function takes a json file as an input and parses it. It collects info about
    the pet and creates and saves the pet in their corresponding database table. """
    
    for pet in petsInfo['petfinder']['pets']['pet']:        
        
        #Parsing the json file to get individual information
           
        name = pet['name']['$t']
        pet_id = pet['id']['$t']
        desc = pet['description']['$t']
        age = pet['age']['$t']
        breeds = pet['breeds']['breed']
        breed = ""
        try:                           # because some pets have multiple breed stored in a list
            breed = breeds['$t']
        except TypeError:
            for x in breeds:
                breed += x['$t'] + ", "
                        
        status = pet['status']['$t']
        sex = pet['sex']['$t']
        size = pet['size']['$t']
        mix = pet['mix']['$t']
        features = pet['options']['option']
        feature = ""
        try:
            feature = features['$t']
        except TypeError:             # because some pets have multiple breed stored in a list
            for x in features:
                feature += x['$t'] + ", "
        
        if pet['animal']['$t']=="Cat":
            cat = petfind.models.Cat(petId = pet_id, petName = name, petDescription = desc, petAge = age, petBreed = breed, petStatus = status, petSex = sex, petSize = size, petMix = mix, petFeatures = feature)
            cat.save()
            
        elif pet['animal']['$t']=="Dog":
            dog = petfind.models.Dog(petId = pet_id, petName = name, petDescription = desc, petAge = age, petBreed = breed, petStatus = status, petSex = sex, petSize = size, petMix = mix, petFeatures = feature)
            dog.save()
        else:
            uniqueAnimal = petfind.models.UniqueAnimal(petId = pet_id, petName = name, petDescription = desc, petAge = age, petBreed = breed, petStatus = status, petSex = sex, petSize = size, petMix = mix, petFeatures = feature)
            uniqueAnimal.save()
    print("Pet information added to database")
    print(features)

##########################################################################################################################

if __name__ == "__main__":

    petsInfo = shelterGetPets(URL, URL_JSON_KEY, SHELTER_ID)
    addAnimalsToDb(petsInfo)
    pprint.pprint(petsInfo)