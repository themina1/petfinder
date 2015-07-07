'''
Created on Jul 2, 2015

@author: aminm
'''

import tweepy
  
def updateTwitterStatus(animal, name, pet_id):
    """ Automatically tweets on the RockBridge Pet twitter page"""
    
    consumer_key = 'pzgRQNUrbgIIkphlnssurjaBa'
    consumer_secret = '0kswM3Uce9NwKvHRAKoZptBCX85QAFjBdwIIvGSpLyjYM4HEOV'
    access_token = '3355406643-8LM6r7tJosmkz5YRjhEFqH86Kpmf8zgsi14fsED'
    access_token_secret = '5as2sfqTt31d3JTY98vIxhWjgaoyiXSVWrcvt2Xq1itlT'
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
 
    # Sample method, used to update a status
    status= ('We have a new %s up for adoption. %s would love to be your friend. Visit https://www.petfinder.com/petdetail/%s' % (animal, name,pet_id))
    api.update_status(status=status)


    