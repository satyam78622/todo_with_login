from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
  
## import todo form and models 
  
from .forms import TodoForm 
from .models import Todo
  
############################################### 
@login_required  
def index(request): 
  
    item_list = Todo.objects.order_by("-date") 
    if request.method == "POST": 
        form = TodoForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('http://127.0.0.1:8000/login/list/') 
    form = TodoForm() 
  
    page = { 
             "forms" : form, 
             "list" : item_list, 
             "title" : "TODO LIST", 
           } 
    return render(request, 'to_do/index.html', page) 
  
  
@login_required  
### function to remove item, it recive todo item id from url ## 
def remove(request, item_id): 
    item = Todo.objects.get(id=item_id) 
    item.delete() 
    messages.info(request, "item removed !!!") 
    return redirect('http://127.0.0.1:8000/login/list/')