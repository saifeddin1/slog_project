from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
	#submitting form
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		#validating form 
		if form.is_valid():
			#save the user actually
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Created for {username}!')
			return redirect('slog-home')
	else:
		form = UserRegisterForm()
	
	return render(request, 'users/register.html', {'form': form})