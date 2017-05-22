from django.shortcuts import render
# from .models import Message
from .models import Post

from django.utils import timezone
from config.settings.base import DJANGO_ROOT
#from blog.dataread import json_dsort
from operator import itemgetter
from blog.forms import PostForm
from django.utils.text import slugify

import datetime
import json
import os
import sqlite3

json_file_path= os.path.join(DJANGO_ROOT, "data", "blogs_11.json")
def json_read():
    with open(json_file_path) as json_file:
        json_data = json.load(json_file)
    json_file.close()
    return json_data


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute('SELECT * FROM starter_app_post ORDER BY date')
rows = cur.fetchall()
db_data = ?????

def json_write(lista):
    with open(json_file_path,'w') as outfile:
        json.dump(lista,outfile) 
    outfile.close()    
    return    
def look(slug):
    item={}
    json_datar = json_read()
    
    for item in json_datar:
        if item["slug"] == slug:
            return item
     

def home(request):
    json_datar = json_read()
    json_dsort=sorted(json_datar,key=itemgetter('date'),reverse=True) 
    for dat_e in json_dsort:
        dat_str = dat_e['date'][0:10]
        dat_e.update({'date': dat_str}) 

    context_dict  = {'messages' : json_dsort}
    return render(request, 'starter_app/blog.html',context_dict)

def post_detail(request,slug):
    post_detail = {}
    post_detail = look(slug)
   
    dat_str = post_detail['date'][0:10]
    post_detail.update({'date': dat_str}) 
    if not post_detail:
        return render (request,'starter_app/blog.html',{})
           
    context_dict  = {'pos' : post_detail}
    return render (request,'starter_app/post_detail.html',
        context_dict)    

def post_new(request):      
    post = PostForm
    sent = False
    if request.method == 'POST':        # Form was submitted   
        form = PostForm(request.POST)      
        if form.is_valid():
        ###           # Form fields passed validation 
            cd = form.cleaned_data 
            post.date = datetime.datetime.utcnow().isoformat()                
            elem = {'title': cd['title'],'slug':slugify(cd['title']),
            'content':cd['content'],'date':post.date }
            #store new post
            json_datar = json_read()
            json_datar.append(elem)
            json_write(json_datar)
            sent = True
    else:
        form = PostForm()
    return render(request, 'starter_app/post_new.html', 
            {'post': post,'form': form,'sent': sent})   

def post_list(request):
    '''
    json_datar = json_read()
    json_dsort=sorted(json_datar,key=itemgetter('date'),reverse=True) 
    '''
    json_dosort=[]
    for row in rows:
        json_dsort = jsort_dsort.append(['title',row[0]])
       


    context_dict  = {'messages' : json_dsort}
    return render(request,'starter_app/post_list.html',context_dict)

def post_menu(request):
    json_datar = json_read()
    json_dsort=sorted(json_datar,key=itemgetter('date'),reverse=True)


    dat_str = json_dsort[0]['date'][0:10]

    json_dsort[0].update({'date': dat_str}) 

    right = {'post_t': json_dsort[0]}
    context_dict  = {'messages' : json_dsort}
    context_dict.update(right)
    return render(request,'starter_app/total.html',context_dict)
def post_menu_d(request,slug):
   # print slug
    json_datar = json_read()
    json_dsort=sorted(json_datar,key=itemgetter('date'),reverse=True) 
    post_detail = {}
    json_datar = json_dsort
    
    for item in json_datar:
        if item["slug"] == slug:
            post_detail = item   

    dat_str = post_detail['date'][0:10]
    post_detail.update({'date': dat_str}) 

    right = {'post_t': post_detail}
    context_dict  = {'messages' : json_dsort}
    context_dict.update(right)
    return render(request,'starter_app/total.html',context_dict)

