from django import forms
from learning_logs.models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            "text"
        ]
        labels = {"text": ""}
