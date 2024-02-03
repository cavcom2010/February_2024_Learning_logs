from django.shortcuts import render
from .models import Topic, Entry

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
