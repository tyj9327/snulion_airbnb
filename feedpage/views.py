from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect

# Create your views here.


def new(request):
    return render(request, 'feedpage/new.html')


def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')


def show(request, id):
    if request.method == 'GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feedpage/show.html', {'feed': feed})
    elif request.method == 'POST':
        feed = Feed.objects.get(id=id)
        feed.title = request.POST['title']
        feed.content = request.POST['content']
        feed.save()
        feed.update_date()
        #return render(request, 'feedpage/show.html', {'feed': feed})
        return redirect('/feeds/' + str(id))

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')


def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed': feed})

