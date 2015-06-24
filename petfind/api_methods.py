__author__ = 'shnoudahm'

from urllib.request import urlopen
from json import load
from .models import *
import codecs
import pprint

aType = input('What kind of animal do you want to search for? (dog or cat)')
if aType != 'dog' and aType != 'cat':
    aType = 'unique'

URL = 'http://api.petfinder.com/'
#METHOD = 'pet.find?'
KEY = 'key=6d3a2622c9ee34420afe02206d1cee12'
ID = '&id=VA321'
LOC = '&location=24450'
OFFSET = '&offset=0'
COUNT = '&count=10'
ANIMAL = '&animal=' + aType
OUTPUT = '&output=basic'
FORMAT = '&format=json'

reader = codecs.getreader('utf-8')

def shelter_getPets(URL, KEY, ID, FORMAT, COUNT):
    METHOD = 'shelter.getPets?'
    URL += METHOD + KEY + ID + FORMAT + COUNT
    response = urlopen(URL)
    json_obj = load(reader(response))
    return json_obj

def add_pet(json_obj):
    for pet in petinfo['petfinder']['pets']['pet']:

        age = pet['age']['$t']
        animal = pet['animal']['$t']
        breeds = pet['breeds']['$t']
        address1 = pet['contact']['address1']['$t']
        address2 = pet['contact']['address2']['$t']
        city = pet['contact']['city']['$t']
        email = pet['contact']['email']['$t']
        fax = pet['contact']['fax']['$t']
        phone = pet['contact']['phone']['$t']
        state = pet['contact']['state']['$t']
        zip = pet['contact']['zip']['$t']
        description = pet['description']['$t']
        id = pet['id']['$t']
        lastUpdate = pet['lastUpdate']['$t']
        media = pet['media']['photos']['photo']['$t']
        mix = pet['mix']['$t']
        name = pet['name']['$t']
        options = pet['options']['$t']
        sex = pet['sex']['$t']
        shelterId = pet['shelterId']['$t']
        shelterPetId = pet['shelterPetId']['$t']
        size = pet['size']['$t']
        status = pet['status']['$t']

        if animal == 'dog':
            dog = models.Dog(age = age,
                             animal = animal,
                             breeds = breeds,
                             address1 = address1,
                             address2 = address2,
                             city = city,
                             email = email,
                             fax = fax,
                             phone = phone,
                             state = state,
                             zip = zip,
                             description = description,
                             id = id,
                             lastUpdate = lastUpdate,
                             media = media,
                             mix = mix,
                             name = name,
                             options = options,
                             sex = sex,
                             shelterId = shelterId,
                             shelterPetId = shelterPetId,
                             size = size,
                             status = status)
            dog.save()

        if animal == 'cat':
            cat = models.Cat(age = age,
                             animal = animal,
                             breeds = breeds,
                             address1 = address1,
                             address2 = address2,
                             city = city,
                             email = email,
                             fax = fax,
                             phone = phone,
                             state = state,
                             zip = zip,
                             description = description,
                             id = id,
                             lastUpdate = lastUpdate,
                             media = media,
                             mix = mix,
                             name = name,
                             options = options,
                             sex = sex,
                             shelterId = shelterId,
                             shelterPetId = shelterPetId,
                             size = size,
                             status = status)
            cat.save()

        else:
            unique = models.Unique(age = age,
                             animal = animal,
                             breeds = breeds,
                             address1 = address1,
                             address2 = address2,
                             city = city,
                             email = email,
                             fax = fax,
                             phone = phone,
                             state = state,
                             zip = zip,
                             description = description,
                             id = id,
                             lastUpdate = lastUpdate,
                             media = media,
                             mix = mix,
                             name = name,
                             options = options,
                             sex = sex,
                             shelterId = shelterId,
                             shelterPetId = shelterPetId,
                             size = size,
                             status = status)
            unique.save()

petinfo = shelter_getPets(URL, KEY, ID, FORMAT, COUNT)
pprint.pprint(petinfo)
add_pet(petinfo)

"""
URL += METHOD + KEY + LOC + ANIMAL + COUNT + OUTPUT + OFFSET + FORMAT

response = urlopen(URL)
json_obj = load(reader(response))
pprint.pprint(json_obj)
"""
