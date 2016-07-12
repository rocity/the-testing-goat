from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item

# Create your views here.
def home_page(request):

    # user wants to add a new item in the list
    if request.method == 'POST':

        # create an object to be saved into the database
        Item.objects.create(text=request.POST['item_text'])

        # redirect back to the form
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'lists/home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})