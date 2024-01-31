from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth  import authenticate, login, logout
from .forms import CustomUserForm, LekhForm
from django.contrib import messages
from .models import Lekh, Profile
from django.http import JsonResponse

# Create your views here.

# user signin
def signin(request):
    # if data is posted to signin and goes through authentication
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # authenticating user to login
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Wrong cred")
            return redirect('signin')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'pages/signin.html')

# register user and create a profile
def register(request):
    # if data is posted to register and goes through validation and saved
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        # checking the form is valid to be saved
        if form.is_valid():
            form.save()
            messages.success(request, "registration successful")
            return render(request, 'pages/register.html', {})
        else:
            messages.error(request, "registration not successful")
            return redirect('register')
    
    else:
        if request.user.is_authenticated:
            return redirect('index')
        form = CustomUserForm()
        return render(request, 'pages/register.html', {"form": form})

# home or index page if user logged
def index(request):
    if request.user.is_authenticated:
        form = LekhForm(request.POST or None)
        if form.is_valid():
            if(form.data.get("body") or request.FILES.get("file")):
                le = form.save(commit=False)
                le.profile = Profile.objects.get(user=request.user)
                le.save()
                if(request.FILES.get("file")):
                    le.file = request.FILES.get("file")
                    le.save()
                return redirect("index")
            else:
                return redirect("index")
        else:
            lekh = Lekh.objects.filter(parent__isnull=True).order_by('-date_created')
            return render(request, "pages/index.html", {"lekhs":lekh, "form":form})
    else:
        return redirect("signin")

# signout the user if logged in
def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("signin")

# profile viewing
def profile_view(request, id):
    if request.user.is_authenticated:
        form = LekhForm(request.POST or None)
        if form.is_valid():
            le = form.save(commit=False)
            le.profile = Profile.objects.get(user=request.user)
            le.save()
            if(request.FILES.get("file")):
                le.file = request.FILES.get("file")
                le.save()
            return redirect(request.META.get("HTTP_REFERER"))
        profile = get_object_or_404(Profile, id=id)
        lekhs = Lekh.objects.filter(profile=profile).order_by("-date_created")
        return render(request, 'pages/profile.html', {"profile":profile, "lekhs":lekhs, 'form':form})

# like_lekh
def like_lekh(request, lekh_id):
    if request.user.is_authenticated:
        lekh = get_object_or_404(Lekh, id=lekh_id)
        profile = get_object_or_404(Profile, user=request.user)
        response_data = {}
        if lekh.likes.filter(id=profile.id).exists():
            # If liked, remove the like
            lekh.likes.remove(profile)
            response_data = {'message': 'Unliked'}
        else:
            # If not liked, add the like
            lekh.likes.add(profile)
            response_data = {'message': 'Liked'}
        return JsonResponse(response_data)
    else:
        return redirect("signin")

# lekh_view
def lekh_view(request, lekh_id):
    if request.user.is_authenticated:
        lekh = get_object_or_404(Lekh, id=lekh_id)
        form = LekhForm(request.POST or None)
        if lekh:
            if (form.is_valid()):
                l = form.save(commit=False)
                l.profile = get_object_or_404(Profile, user=request.user)
                l.save()
                l.parent = lekh
                l.save()
                print(request.FILES.get("file"))
                if(request.FILES.get("file")):
                    l.file = request.FILES.get("file")
                    l.save()
                return redirect(request.META.get("HTTP_REFERER"))
            re_lekhs = Lekh.objects.filter(parent_id=lekh.id).order_by("-date_created")
            return render(request, "pages/lekh.html", {"lekh": lekh, 'form': form, "re_lekhs": re_lekhs})
    else:
        return redirect("signin")
    
# delete lekh
def delete_lekh(request, lekh_id):
    if request.user.is_authenticated:
        lekh = get_object_or_404(Lekh, id=lekh_id)
        response_data = {}
        if lekh and lekh.profile.user == request.user:
            lekh.file.delete()
            lekh.delete()
            response_data = {'message': 'Deleted'}
        else:
            response_data = {'message': 'error'}
        return JsonResponse(response_data)
    else:
        return redirect("signin")


# upload pp
def upload_pp(request):
    if (request.user.is_authenticated):
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            profile.profile_image.delete()
            profile.profile_image = request.FILES.get("pp")
            profile.save()
            return JsonResponse({'message': 'uploaded'})
        return JsonResponse({'message': 'error'})
    else:
        return redirect("signin")

# profile list
def profile_list(request):
    if (request.user.is_authenticated):
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'pages/profile_list.html', {'profiles':profiles})
    else:
        return redirect("signin")

# pany
def compain(request, id):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        comp_profile = get_object_or_404(Profile, id = id)
        response_data = {}
        if profile.companian.filter(id=comp_profile.id).exists():
            profile.companian.remove(comp_profile)
            response_data = {'message': 'uncompaining'}
        else:
            profile.companian.add(comp_profile)
            response_data = {'message': 'compaining'}
        return JsonResponse(response_data)
    return redirect("signin")

# search
def search_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            inp = request.POST.get("search")
            if(inp):
                search = Profile.objects.filter(user__username__contains=inp)
                search1 = Lekh.objects.filter(body__contains = inp)
                return render(request, "pages/search.html", {"search": search, "lekhs":search1})
        return render(request, "pages/search.html", {})
    else:
        return redirect("signin")