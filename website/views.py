from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'teams.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')

def appointment(request):
    email = None
    firstname = None
    lastname = None
    if request.user.is_authenticated:
        email = request.user.email
        firstname = request.user.first_name
        lastname = request.user.last_name

    if request.method == "POST":
        ap_date = request.POST['ap-date']
        ap_phone = request.POST['ap-phone']
        ap_message = request.POST['ap-message']
        ap_doctor = request.POST['ap-doctor']
        messages.success(request, "Appointment Booked Successfully")
        send_mail('Appointment Confirmation' , 'Dear ' + firstname + ' '  + lastname + ', your appointment with ' + ap_doctor + ' has been scheduled for ' + ap_date + '. We will send you a link for the Duo Call via SMS on the date of appointment' , 'raghavsoni331@gmail.com', [email])
        send_mail('New Appointment Booked' ,firstname + ' '  + lastname + ', has booked an appointment with ' + ap_doctor + ' for ' + ap_date + '. Please send a link for the Duo Call via SMS on ' + ap_phone , 'raghavsoni331@gmail.com', ['sparsh.singh1000@gmail.com'])
        return render(request, 'appointment.html', context={"firstname": firstname, "lastname": lastname, "date":ap_date, "email":email, "doctor": ap_doctor})
        # datatuple=(
        # ('Appointment Confirmation' , 'Dear' + firstname + ' '  + lastname + ', your appointment with ' + doctor + 'has been scheduled for ' + date + 'We wil send you a link for the Duo Call via SMS on the date of appointment' , 'raghavsoni331@gmail.com', [email])
        # ('New Appointment request' , 'An appointment has been booked by ' + firstname + ' ' + lastname 'for ' + doctor + 'on ' + date + '. Kindly  connect with the patient via email: ' + email + ' phone: ' + phone, 'raghavsoni331@gmail.com', ['sparsh.singh1000@gmail.com'])
        # )
        # send_mass_mail(datatuple)

    else:
        return render(request, 'appointment.html', {"firstname": firstname, "lastname": lastname, "email":email})
def join(request):
    return render(request, 'join.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registered Successfully!")
            return redirect('home')
        messages.error(request, "Error while regsitering, please try again")
    form = NewUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid Username or password.")
        else:
            messages.info(request, "Invalid Username of Password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
	# 	if form.is_valid():
	# 		username = form.cleaned_data.get('username')
	# 		password = form.cleaned_data.get('password')
	# 		user = authenticate(username=username, password=password)
	# 		if user is not None:
	# 			login(request, user)
	# 			messages.info(request, f"You are now logged in as {username}.")
	# 			return redirect("main:homepage")
	# 		else:
	# 			messages.error(request,"Invalid username or password.")
	# 	else:
	# 		messages.error(request,"Invalid username or password.")
	# form = AuthenticationForm()
	# return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.success(request, "Logged out Successful")
    return redirect('home')