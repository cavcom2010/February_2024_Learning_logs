from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# the homepage view
def home(request):
    """in the form a function that returns the website"""
    return render(request, "index.html")

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

def new_entry(request, topic_id):
    """add a new entry for a particular topic """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # an empty form
        form = EntryForm()
        """an entry will be inputed from this."""
    form = EntryForm(data=request.POST)
    """from a post request with information to save."""
    if form.is_valid():
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.save()
        return redirect('topic', topic_id=topic_id)
    
    return render(request, 'learning_logs/new_entry.html', {'form': form, 'topic': topic})

def edit_entry(request, entry_id):
    """a view to edit the entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        """prefill form with the current entry"""
        form = EntryForm(instance=entry)
    else:
        # post data submitted and process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic', topic_id=topic.id)
    
    context = {'entry':entry, 'form': form, 'topic': topic}
    return render(request, 'learning_logs/edit_entry.html', context )




    


