from django.shortcuts import render, get_object_or_404
from .models import Accident, Events, Tag
from django.shortcuts import redirect
from django.db.models import Max
from .forms import PostForm, EventForm, LinkForm, PostFormEdit
from datetime import datetime


def accident_list(request):
    accident = Accident.objects.select_related().order_by('created_date')
    tags = Tag.objects.all()
    user = request.user
    context = {'accident': accident, 'tags': tags, 'user': user}
    return render(request, 'accident/accident_list.html', context)


def accident_detail(request, pk):
    accident = get_object_or_404(Accident, pk=pk)
    events = Events.objects.filter(accident=pk).order_by('date_time')
    tag = Tag.objects.filter(accident=pk)
    last_date = events.aggregate(Max('date_time'))
    context = {'events': events, 'tag': tag,
               'accident': accident, 'last_date': last_date}
    return render(request, 'accident/accident_detail.html', context)


def accident_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            accident = form.save(commit=False)
            accident.author = request.user
            try:
                request.POST['public']
                date_time = request.POST['datetime']
                date_time_obj = datetime.strptime(date_time, "%d.%m.%Y %H:%M")
                accident.created_date = date_time_obj
            except:
                pass
            accident.save()
            return redirect('accident_detail', pk=accident.id)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'accident/accident_edit.html', context)


def event_new(request, pk):
    accident = get_object_or_404(Accident, id=pk)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = Events()
            event.event = form.cleaned_data['event_text']
            event.accident = accident
            try:
                request.POST['public']
                date_time = request.POST['datetime']
                date_time_obj = datetime.strptime(date_time, "%d.%m.%Y %H:%M")
                event.date_time = date_time_obj
            except:
                pass
            event.save()
            return redirect('accident_detail', pk=accident.pk)
    else:
        form = EventForm()
    context = {'form': form, 'accident': accident}
    return render(request, 'accident/event_edit.html', context)


def link_new(request, pk):
    accident = get_object_or_404(Accident, id=pk)
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = Tag()
            link.tag_text = form.cleaned_data['tag_text']
            link.accident = accident
            link.link = form.cleaned_data['link']
            link.save()
            event = Events()
            event.event = 'Прикреплен тикет ' + form.cleaned_data['tag_text']
            event.accident = accident
            try:
                request.POST['public']
                date_time = request.POST['datetime']
                date_time_obj = datetime.strptime(date_time, "%d.%m.%Y %H:%M")
                event.date_time = date_time_obj
            except:
                pass
            event.save()
            return redirect('accident_detail', pk=accident.pk)
    else:
        form = LinkForm()
    context = {'form': form, 'accident': accident}
    return render(request, 'accident/link_edit.html', context)


def accident_edit(request, pk):
    accident = get_object_or_404(Accident, id=pk)
    old_status = str(accident.status)
    if request.method == "POST":
        form = PostFormEdit(request.POST, instance=accident)
        if form.is_valid():
            accident = form.save()
            new_status = str(form.cleaned_data['status'])
            event = Events()
            event.event = old_status + '->' + new_status
            event.accident = accident
            event.save()
            return redirect('accident_detail', pk=accident.id)
    else:
        form = PostFormEdit(instance=accident)
    context = {'form': form}
    return render(request, 'accident/accident_edit_form.html', context)
