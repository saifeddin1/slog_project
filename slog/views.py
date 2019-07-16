from django.shortcuts import render
from .models import Post 



def home(request):
	context = {
		'posts' : Post.objects.all() 
		#importing posts from the database
	}
	return render(request, 'slog/home.html',context)


def about(request):
	return render(request, 'slog/about.html', {'title': 'About'})











