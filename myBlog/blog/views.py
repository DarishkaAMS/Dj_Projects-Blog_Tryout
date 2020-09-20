from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  blog.models import Post

# Create your views here.

def home(request):
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 4)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)
 
    context = {
        "postList": postList,
        "title": "Blog Main Page",
        "desc": "Description of the Main Page",
        "key": "Key Words",
    }
    return render(request, "partial/home.html")

def single(request, id=None):
    return render(request, "partial/single.html")

