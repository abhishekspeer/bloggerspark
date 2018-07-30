from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
'''
A view is a place where we put the "logic" of our application. It will request
information from the model you created before and pass it to a template
tells template how to use data from models
'''
def post_list(request):
    posts = Post.objects.filter(publised_date__lte=timezone.now()).order_by('publised_date')
    # posts <queryset>
    return render(request, 'blog/post_list.html', {'posts': posts})
    # {} stuff is used by the template
    # render == put together a template on request.
