from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import RegistrationForm,EditProfileForm,RegisterBusinessForm,EditBusinessForm,PostMessageForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from itertools import chain
from .models import Profile,Neighborhood,Business,Meeting


# Create your views here.

def landing_page(request):
    '''
    This is just for the welcome page
    '''
    return render(request,'landing-page.html')

@login_required
def dashboard(request):
    neighborhoods= Neighborhood.objects.order_by("created_at")
    meetings = Meeting.objects.order_by("created_at")
    businesses = Business.objects.order_by("id")
    return render(request, "dashboard.html", {
        "news": neighborhoods,
        "events": meetings,
        "businesses": businesses
    })

def register_user(request):
    rgf =RegistrationForm()
    if request.method == 'POST':
        rgf = RegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            print(user)
            email = rgf.cleaned_data.get('email')
            # send_welcome_email(user,email)
            user_profile = Profile.objects.get(user = request.user)
            messages.success(request, 'Account was created for ' + user)
            return redirect("login_user")
            # return redirect(reverse('edit_profile',args=str(request.user.profile.id)))
            # return HttpResponseRedirect(reverse('edit_profile', args=[int(user.id)]))

    
    return render(request, 'registration/registration.html', {'rgf': rgf})

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('login_user')
    
    # Render the registration page template (GET request)
    return render(request, 'registration/registration2.html')

def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("login unsuccessful")

    return render(request, 'registration/register.html')
    
def logout_user(request):
    logout(request)
    return redirect('login_user')

def home(request):
    user_profile = Profile.objects.get(user=request.user)
    form = PostMessageForm()
    hoods = Neighborhood.objects.all()
    regform = RegisterBusinessForm()


    businesses = Business.objects.filter(neighbor = user_profile.hood).all()
    message = Meeting.objects.filter(hood = user_profile.hood).all()


    context = {
        'form':form,
        'profile': user_profile,
        'businesses':businesses,
        "reg_form":regform,
        "messages": message,
        "hoods": hoods,
    }

    return render(request,'index.html',context)

def neighbor_news(request):
    '''
    See neighborhub news
    '''
    return render(request,'hood_news.html')

def neighbor_events(request):
    '''
    See neighborhub events
    '''
    return render(request,'hood_events.html')

def create_hood(request):
    '''
    Registered Admins will be abale to create neighborhoods
    '''

    # if request.method == 'POST':

    return render(request,'post_hood.html')

def create_events(request):
    '''
    Registered Admins will be abale to create neighborhoods
    '''

    # if request.method == 'POST':

    return render(request,'post_events.html')

class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/edit-profile.html'


def edit_profile(request,id):
    editing_profile = Profile.objects.get(id=id)
    form = EditProfileForm()
    # current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = editing_profile.user.id
            post.save()
            return redirect(request.META.get('HTTP_REFERER'))

    title = 'BlockChain- Edit Profile'
    context = {
        "ed_form":form,
        "title":title,
    }

    return render(request,'profile/edit-profile.html',context)


def my_profile(request,id):
    user_profile = Profile.objects.get(user = id)
    user_profile_messages = Meeting.objects.filter(user = id).all()
    user_businesses = Business.objects.filter(user = id).all()

    regform = RegisterBusinessForm()

    current_user = request.user
    if request.method == 'POST':
        regform = RegisterBusinessForm(request.POST,request.FILES)
        print(regform)
        if regform.is_valid():
            post = regform.save(commit=False)
            post.user = current_user
            post.save()
            # return HttpResponseRedirect(reverse('home'))
            # return redirect('home')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = RegisterBusinessForm()


    form = EditProfileForm


    current_user = request.user.id

    context = {
        "profile":user_profile,
        "projects":user_profile_messages,
        'ed_form':form,
        "reg_form":regform,
        "current_user":current_user,
        "businesses":user_businesses,
    }

    return render(request,'profile/profile.html',context)


# def register_business(request):

#     return render(request,'profile/profile.html')

class BusinessEditView(UpdateView):
    model = Business
    form_class = EditBusinessForm

def post_message(request):
    user_profile = Profile.objects.get(user = request.user)
    hood = user_profile.hood

    form = PostMessageForm()

    if request.method == 'POST':
        form = PostMessageForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.hood = hood
            post.save()

            return redirect('home')



    # return render(request,'index.html',context)


def search_for_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        search_results = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"results":search_results,"message":message})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})




# User profile
