from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post
import requests
import json

def contact (request):
    return render(request, 'blog/contact.html')

def about (request):
    return render(request, 'blog/about.html')    

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        # Recaptcha Stuff
            '''clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LdkHw0gAAAAAC3r52IX5ziNLq49M8m3xQp9b9O4'
            captchaData = {
                "secret": secretKey,
                "response": clientKey
            }
            r = requests.post("https://www.google.com/recaptcha/api/siteverify", data = captchaData)
            response = json.loads(r.text)
            verify = response["Success"]
            print("Your success is: ", verify)
            if verify:
                return HttpResponse('<script> alert("Success");</script>')
            else:
                return HttpResponse('<script> alert("Failed");</script>') '''   


        return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})