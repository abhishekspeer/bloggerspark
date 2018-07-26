from django.shortcuts import render

# Create your views here.
'''
A view is a place where we put the "logic" of our application. It will request
information from the model you created before and pass it to a template
tells template how to use data from models
'''
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    # render == put together a template on request.
