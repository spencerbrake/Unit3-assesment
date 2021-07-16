from django.shortcuts import render, redirect
from .models import Wishlist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
def home(request):    
    wl = Wishlist.objects.all()
    return render(request, 'home.html', {'wl': wl})

class add_item(CreateView):
    model = Wishlist
    fields = ['definition'] 
    def form_valid(self, form):
        return super().form_valid(form)
    
def delete(request, item_definition):
    Wishlist.objects.filter(definition=item_definition).delete()
    return redirect('home')
