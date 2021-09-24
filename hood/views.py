from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import RegistrationForm,EditProfileForm,RegisterBusinessForm,EditBusinessForm,PostMessageForm,NewsLetterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from itertools import chain
from .models import Profile,Neighborhood,Business,Meeting


# Create your views here.

def register_user(request):
    rgf =RegistrationForm()
    if request.method == 'POST':
        rgf = RegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            email = rgf.cleaned_data.get('email')
            # send_welcome_email(user,email)
            user_profile = Profile.objects.get(user = request.user)
            messages.success(request, 'Account was created for ' + user)
            return redirect("login_user")
            # return redirect(reverse('edit_profile',args=str(request.user.profile.id)))
            # return HttpResponseRedirect(reverse('edit_profile', args=[int(user.id)]))

    
    return render(request, 'registration/registration.html', {'rgf': rgf})

def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')
    
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
