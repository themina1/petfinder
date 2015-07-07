'''
Created on Jul 6, 2015

@author: aminm
'''

import json
import requests
import os
import django

# To access Django Models in our script
os.environ.__setitem__("DJANGO_SETTINGS_MODULE", "petsite.settings")
django.setup()

from petfind.models import RedditPost

def postExist(post_id):
    """ Returns True if pet exists"""
    return RedditPost.objects.filter(pk = post_id).exists()

def getCatReddit():
    url = "https://www.reddit.com/r/cats/hot/.json"
    r = requests.get(url)
    j = json.loads(r.text)

    for post in j['data']['children']:
        post_id = post['data']['id']
        up_votes = post['data']['ups']
        link = post['data']['url']
        title = post['data']['title']
        #img = post['data']["preview"]['images'][0]['resolutions'][0]['url']
       
        
        # If post does not exist, make a new post
        if not postExist(post_id):   
            reddit_post = RedditPost(post_id = post_id, link = link, title = title, up_votes = up_votes)
            reddit_post.save()
        # Else, just update up_votes
        else:
            reddit_post = RedditPost.objects.get(pk = post_id)
            reddit_post.up_votes = up_votes
            reddit_post.save()
            
    print("Posts added")

if __name__ == '__main__':
    getCatReddit()