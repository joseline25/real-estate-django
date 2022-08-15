from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.

#  List + CRUD (Create, Retrieve, Update, Delete)

# list
@login_required(login_url='login')
def listing_list(request):
    listings = Listing.objects.all()
    locations = Listing.objects.values('address').distinct()
    context = {
        'listings': listings,
        'locations': locations,
    }
    return render(request, 'list.html', context)


# retrieve

@login_required(login_url='login')
def listing_retrieve(request, id):
    listing = Listing.objects.get(id=id)
    context = {
        'listing': listing,
    }
    return render(request, 'listing.html', context)


# create

@login_required(login_url='login')
def listing_create(request):
    form = ListingForm()

    context = {
        'form': form,
    }
    
    user = request.user.profile

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            num_bedrooms = form.cleaned_data['num_bedrooms']
            num_bathrooms = form.cleaned_data['num_bathrooms']
            square_footage = form.cleaned_data['square_footage']
            address = form.cleaned_data['address']
            image = form.cleaned_data['image']
            #status = form.cleaned_data['status']
            owner = user
            
            obj = Listing(title=title, price=price, num_bedrooms=num_bedrooms, num_bathrooms=num_bathrooms, square_footage=square_footage, address=address, image=image, owner=owner)
            obj.save()
            #form.save()
        return redirect('list')

    return render(request, 'listing_create.html', context)


@login_required(login_url='login')
def listing_update(request, id):

    listing = Listing.objects.get(id=id)
    form = ListingForm(instance=listing)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
        return redirect('list')

    return render(request, 'listing_update.html', context)


# delete
@login_required(login_url='login')
def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    listing.delete()
    return redirect('list')


# create booking
@login_required(login_url='login')
def booking_create(request, id):
    listing = Listing.objects.get(id=id)
    form = BookingForm()

    context = {
        'form': form,
    }

    if request.method == 'POST':
        
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid(): 
            listing.status = Listing.statuss[1][1]
            listing.save()
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            obj = Booking(listing=listing,start_date=start_date, end_date=end_date)
            obj.save()
        return redirect('list')

    return render(request, 'booking_create.html', context)


# recherche d'un listing
@login_required(login_url='login')
def search_listing(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        location = request.POST.get('location')
        listings = Listing.objects.filter(title__contains=search).order_by('price') & Listing.objects.filter(address=location)
        return render(request, 'list.html', {'listings_search': listings, 'search_value': search})

# page d'enregistrement

def registerPage(request):
    form = CreateUserForm()
    form_profile = UserProfileForm()    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form_profile = UserProfileForm(request.POST)
        if form.is_valid() and form_profile.is_valid():
            user = form.save() #form.save()
            profile = form_profile.save(commit=False)
            print(form)
            
            profile.user = user # the user has to be saved before the profile
            form_profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Le compte de ' + username + ' a été crée avec succès!')
            return redirect('login')
    context = {'form': form, 'form_profile': form_profile}
    return render(request, 'register.html', context)



# page login

def loginPage(request):
            
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            messages.info(request, "Le nom d'utilisateur ou le mot de passe est incorrect!")
    context = {}        
    return render(request, 'login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'user.html', context)