from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,'book/home.html')

def create(request):
    # if request.method == 'POST':
    #     form = Booksform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     context = {'msg':'Book Added Successfully','form':form}
    # else:
    #     form = Booksform()
    #     context = {'msg': 'Add New Book','form':form}
    # return render(request,'book/create.html',{'context':context})

    form = Booksform()
    if request.method == 'GET':
        context = {'msg': 'Add New Movie','form':form}
    else:
        form = Booksform(request.POST)
        if form.is_valid():
            form.save()
            form = Booksform()
        context = {'msg':'Movie Added Successfully','form':form}
    return render(request,'book/create.html',{'context':context})

def retrieve(request):
    raws = library.objects.all()
    return render(request,'book/retrieve.html',{'rows':raws})

def viewbook(request,book_no):
    try:
        row = library.objects.get(no = book_no)
        return render(request,'book/viewbook.html',{'r':row})
    except library.DoesNotExist:
        row = 'Movie not available'
        return render(request,'book/retrieve.html',{'msg':row})

def search(request):
    if request.method == 'POST':
        form = searchbookform(request.POST)
        if form.is_valid():
            try:
                bid = form.cleaned_data['bno']
                library.objects.get(no=bid)
                return redirect("/view/" + str(bid))
            except library.DoesNotExist:
                rows = library.objects.all()
                msg = 'books levu'
                return redirect("/retrieve/", msg)         
    else:
        form = searchbookform()
    return render(request,'book/search.html',{'form':form})

def delete(request):
    if request.method == 'POST':
        form = deleteform(request.POST)
        if form.is_valid():
            bid = form.cleaned_data['bno']
            try:
                row = library.objects.get(no=bid)
                row.delete()
                msg = 'Movie deleted'
            except library.DoesNotExist:
                msg = 'Movie not found'            
            return redirect("/retrieve/" , msg)
    else:
        form = deleteform()
        msg = 'Enter No to Delete Movie'
    return render(request,'book/delete.html',{'form':form,'msg':msg})

def deleteb(request,book_no):
    row = library.objects.get(no = book_no)
    row.delete()
    msg = 'One Movie Deleted '
    return render(request,'book/deletebook.html',{'r':row,'msg':msg})


def update(request,book_no):
    b = library.objects.get(no = book_no)
    if request.method == 'POST':
        form = Booksform(request.POST , instance=b)
        if form.is_valid():
            form.save()
        return retrieve(request)
    else:
        form = Booksform(instance=b)
    return render(request,'book/update.html',{'form':form})

def updateb(request):
    return render(request,'book/updateb.html')