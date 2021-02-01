from django.shortcuts import render, get_object_or_404
from .models import Meeting
from django.forms import modelform_factory


def index(request):
    meetings = Meeting.objects.all()
    return render(request, 'app/index.html',
                  {"meetings": meetings})


def details(request, _id):
    meeting = get_object_or_404(Meeting, pk=_id)
    return render(request, 'app/details.html', {"meeting": meeting})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new_meeting(request):
    form = MeetingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'app/new_meeting.html',{"form":form})
