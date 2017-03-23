from django.shortcuts import render
from .models import Article
# Create your views here.
def post_list(request):
    posts = Article.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request,'blog/post_list.html',{'posts':posts})
