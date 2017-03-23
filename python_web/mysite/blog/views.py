from django.shortcuts import render
from .models import Article
from django.shortcuts import render,get_object_or_404
# Create your views here.
def post_list(request):
    posts = Article.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Article,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})
