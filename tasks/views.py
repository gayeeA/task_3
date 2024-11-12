import base64
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate

# Create your views here.
# def home(request):
#     return render(request, 'home_page.html')
# def login(request):
#     return render(request, 'login.html')
# def signup(request):
#     return render(request, 'signup.html')

# Create your views here.
def home(request):
    # request is used to navgate the command to our html page
    # for navigation we need to use a keyword called as "render"
    return render(request,'home_page.html')
 
def login(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if(request.method == "POST"):
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request,username=un,password=pw)
        #authenticate() used to check for the valid statements given or not by linking with database automatically.
        #if the values are matched, then it will return the username
        #if the values are not matched, then it will return the 'None'
        if(user is not None):
            return redirect('/profile')
        else:
            msg = 'Error in login. Invalid username/password'
            form = AuthenticationForm()
            # used to create a basic login page with username and password conditions
            return render(request,'login.html',{'form':form,'msg':msg})
    else:
        form = AuthenticationForm()
        # used to create a basic login page with username and password conditions
        return render(request,'login.html',{'form':form})
 
def register(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            un = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            user = authenticate(username=un,password=pw)
            return redirect('/login')
        else:
            return render(request,'signup.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(request,'signup.html', {'form':form})
 
def profile(request):
    if(request.method=="POST"):
        if(request.FILES.get('abd')):
            img_name = request.FILES['abd'].read()
            #encode the file to base64 concept
            #base64 concept will have a separate charset
            encode = base64.b64encode(img_name).decode('utf-8')
            #create a url for the image
            img_url = f"data:image/jpeg;base64,{encode}"
            #return the url to the page
            return render(request,'profile.html',{'img':img_url})
    else:
        return render(request,'profile.html')
