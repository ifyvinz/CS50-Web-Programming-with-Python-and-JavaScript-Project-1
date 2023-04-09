<<<<<<< HEAD
from django.shortcuts import render

from . import util

=======
from re import U
import secrets
from turtle import title
from attr import Attribute
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

from . import util
import markdown

class NewForm(forms.Form):
    title = forms.CharField(label= "Title", widget= forms.TextInput(attrs= {'class': 'form-control'}))
    body = forms.CharField(widget= forms.Textarea(attrs={'class': 'form-control'}))
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required = False)
>>>>>>> 377c1a4 (modified views, urls and templates)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

<<<<<<< HEAD
=======
def entry(request, name):
    titleName = util.get_entry(name)

    if titleName is None:
        return render(request, "encyclopedia/noEntry.html", {
            "content": name
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": name,
            "content": markdown.markdown(titleName)
        })

def search(request):
    if request.method == 'GET':
       query = request.GET.get('q')
       entry = util.get_entry(query)

       if entry:
          return HttpResponseRedirect(reverse("entry", kwargs={"name" : query}))
       else:
          subName = []
          for entry in util.list_entries():
              if query.lower() in entry.lower():
                 subName.append(entry)
    
       return render(request, "encyclopedia/search.html", {
             "entries": subName,
        
    })

def createEntry(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]

            if util.get_entry( title) is None or form.cleaned_data["edit"] is True :
                util.save_entry( title,body)
                return HttpResponseRedirect(reverse("entry", kwargs={"name": title}))

            else:
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                     "errorMessage": "Error " + title + " exist already, put in a different entry.",
                     "title": title
                   })
        else:
            return render(request,"encyclopedia/create.html", {
                "form":form,
               } )
    else:
        return render(request,"encyclopedia/create.html", {
                "form":NewForm(),
               } )

def edit(request, name):
    entry = util.get_entry(name)
    if entry is None:
         return render(request, "encyclopedia/noEntry.html", {
            "content": name
        })
    else:
        form = NewForm()
        form.fields["title"].initial = name
        form.fields["title"].widget.attrs['readonly'] = True
        form.fields["body"].initial = entry
        form.fields["edit"].initial = True

        return render(request, "encyclopedia/create.html", {
             "form": form,
             
        } )

def randomPage(request):
    entries = util.list_entries()
    randomise = secrets.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={"name":randomise}))
       

>>>>>>> 377c1a4 (modified views, urls and templates)
