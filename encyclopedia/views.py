from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseNotFound
from . import util
import markdown
import random
from django.contrib import messages

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_detail(request,title):  
    if util.get_entry(title)==None:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(request,'encyclopedia/entry_detail.html',{
        "entry":util.get_entry(title), "title":title
        })
    
def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('q', None)
        if search_query in util.list_entries():
            return render(request,'encyclopedia/entry_detail.html',{
            "entry":util.get_entry(search_query), "title":search_query
            }) 
        else:
            lst=[]
            for i in util.list_entries():
                if search_query.lower() in i.lower():
                    lst.append(i)
            if lst:        
                return render(request,'encyclopedia/search.html',{
                    "lst":lst,
                })
        return HttpResponseNotFound('<h1>No such entry</h1>')

def new_page(request):
    if request.method=='POST' :
        search_query = request.POST.get('q', None)
        if search_query in util.list_entries():
            messages.error(request, 'An entry already exists')
        else:
            util.save_entry(search_query,request.POST.get('content',None),)
            return render(request,'encyclopedia/entry_detail.html',{
            "entry":util.get_entry(search_query), "title":search_query
            }) 
    return render(request,'encyclopedia/new_page.html')

def edit_page(request,title): 
    content=util.get_entry(title)
    if request.method=='POST' :
        util.save_entry(title,request.POST.get('content',None),)
        return render(request,'encyclopedia/entry_detail.html',{
        "entry":util.get_entry(title), "title":title
        })
    return render(request,'encyclopedia/edit_page.html',{'content':content,
    })

def random_entry(request):
    title=random.choice(util.list_entries())
    return render(request,'encyclopedia/entry_detail.html',{
        "entry":util.get_entry(title),"title":title
    })