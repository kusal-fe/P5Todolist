from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = TodoList.objects.get(id=id)
    
    if ls in response.user.todolist.all():
        if response.method=="POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id))=="clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid Input")

        return render(response, 'main/list.html', {"ls":ls})
    else:
        return redirect("/view")

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response.method=="POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" % t.id)
        
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {"form":form})

def view(response):
    return render(response, "main/view.html", {})