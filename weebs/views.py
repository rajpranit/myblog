from django.shortcuts import render ,redirect
from .models import AllPost ,Comment ,Categories

def index(request):
 
   allpost = AllPost.objects.all()
   sliderpost = AllPost.objects.all().order_by('id')[:2]
   return render(request,'weebs/index.html',{
      'allpost':allpost,
      'sliderpost':sliderpost,
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

def comment(request,pk):
    if request.method == 'POST':
        posts = AllPost.objects.filter(pk = pk)
        for post in posts:
            post =post
            name = request.POST['cName']
            comment = request.POST['cMessage']
        comment = Comment(post = post,name=name,comment=comment)
        comment.save()

        return redirect('article-detail' ,pk)

def category(request):
    category = Categories.objects.all()

    return render(request,'weebs/category.html',{
        'category':category,
    })


def manhwa(request):
    return render(request,'weebs/manhwa.html')


def manhua(request):
    return render(request,'weebs/manhua.html')




def about(request):
    return render(request,'weebs/about.html')



def contact(request):
    return render(request,'weebs/contact.html')
