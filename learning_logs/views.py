from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm

# the homepage view
def home(request):
    """in the form a function that returns the website"""
    return render(request, "home.html")

def topics(request):
    """show all the topics"""
    topics = Topic.objects.all()
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html', context)

def topic(request, topic_id):
    """show all entries for a particu;lar topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """a view for the new topic"""

    if request.method != 'POST':
        # create an empty form
        form = TopicForm()
        """this is blank with no data."""
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

