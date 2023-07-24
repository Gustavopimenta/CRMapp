from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # check to see if loggin in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # autentificação 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home') #atenção nessa parte
        else:
            messages.success(request, "There was an Error loggin In, Please Try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register_user(request):
    return render(request, 'home.html',{})