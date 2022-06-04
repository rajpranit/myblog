from django.shortcuts import render
from .models import AllPost

def index(request):
   allpost = AllPost.objects.all()
   sliderpost = AllPost.objects.all().order_by('id')[:2]
   return render(request,'weebs/index.html',{
      'allpost':allpost,
      'sliderpost':sliderpost,
    })

def top_article(request,pk ):
    toppost = AllPost.objects.filter(pk=pk)
    return render(request,'weebs/top-article.html',{
        "toppost":toppost,
    })

def manhua_article(request,pk ):
    manhuapost = AllPost.objects.filter(pk = pk)
    return render(request,'weebs/manhua-article.html',{
        "manhuapost":manhuapost,
    })

def manhwa_article(request,pk ):
    
    manhwapost = AllPost.objects.filter(pk = pk)
    count = 0
    for post in manhwapost:
        for comment in post.comments.all():
            count += 1  


        
    return render(request,'weebs/manhwa-article.html',{
        "manhwapost":manhwapost,
        "count":count
    })

def article_detail(request,pk ):
    
    posts = AllPost.objects.filter(pk = pk)
    count = 0
    for post in posts:
        for comment in post.comments.all():
            count += 1  


        
    return render(request,'weebs/article-detail.html',{
        "posts":posts,
        "count":count
    })






def category(request):
    return render(request,'weebs/category.html')


def manhwa(request):
    return render(request,'weebs/manhwa.html')


def manhua(request):
    return render(request,'weebs/manhua.html')




def about(request):
    return render(request,'weebs/about.html')



def contact(request):
    return render(request,'weebs/contact.html')
