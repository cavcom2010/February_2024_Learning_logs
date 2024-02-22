from django.shortcuts import render, redirect
from .import views
from .models import RSVP
from .forms import RSVPForm

# Create your views here.
def index_view(request):
    rsvp = RSVP.objects.all()
    return render(request, 'index.html', {'rsvp': rsvp})

def rsvp_view(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RSVPForm()

    context = {'form': form}
    return render(request, 'rsvp.html', context)

    


