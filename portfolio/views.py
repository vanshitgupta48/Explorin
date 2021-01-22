from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def projects(request):
	return render(request,'projects.html')

def contact(request):
	return render(request,'contact.html')

def flexbox(request):
    return render(request,'flexbox.html')

def bonus(request):
	return render(request,'bonus.html')

def advance(request):
	return render(request,'advance.html')

def week2bonus(request):
	return render(request,'week2bonus.html')

def video(request):
	return render(request,'video.html')

def project1(request):
	return render(request,'project1.html')