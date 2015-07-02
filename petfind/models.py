from django.db import models


# Common info for all models.
class Animal(models.Model):
    animal = models.CharField(max_length = 20, blank = True)
    petId = models.CharField(max_length = 20, primary_key=True, verbose_name = 'ID', blank = True )
    firstSeen = models.DateTimeField("First Seen", null = True)
    lastSeen = models.DateTimeField("Last seen ", null = True)
    petName = models.CharField(max_length = 50, verbose_name = 'Name: ', blank = True)
    petDescription = models.TextField(verbose_name = 'Description', blank = True)
    petBreed = models.CharField(max_length = 100, verbose_name = 'Breed', blank = True)
    petStatus = models.CharField(max_length = 10, verbose_name = 'Status', blank = True)
    petAge = models.CharField(max_length = 10, blank = True, verbose_name ='Age')
    petSex = models.CharField(max_length = 10, blank = True, verbose_name = 'Sex')
    petSize = models.CharField(max_length = 10, blank = True, verbose_name ='Size')
    petMix = models.CharField(max_length = 10, blank = True, verbose_name ='Mixed?')
    petFeatures = models.CharField(max_length = 200, verbose_name ='Features', blank = True)
    petPhoto = models.TextField(blank = True, verbose_name = 'Picture')
    address = models.CharField(max_length = 200, blank = True, default = '10 Animal Place')
    city = models.CharField(max_length = 50, blank = True, default = 'Lexington')
    email = models.CharField(max_length = 200, blank = True, default = 'shelter@rockbridgespca.net' ) 
    fax = models.CharField(max_length = 200, blank = True, default = '540-464-8847')
    phone = models.CharField(max_length = 200, blank = True, default = '540-463-5123')
    state = models.CharField(max_length = 2,default = 'VA')
    zip = models.CharField(max_length = 10,default = '24450')
    match = models.CharField(max_length = 5, default = "No")

    class Meta:
        ordering = ['petId']
    
    def __str__(self):
        return "Id: " + self.petId  + "Animal: " + self.animal + "Name: " + self.petName