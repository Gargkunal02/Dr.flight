from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib import messages

from UserLogin.models import Doctor, Lab, Patient, User

# Create your views here.

def home(request):
    return render(request,'Home/index.html')

def login_request(request):
    # return render(request,'Home/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_doctor:
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            elif request.user.is_lab:
                return redirect('home')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request = request,template_name = "Home/login.html",)


def register(request):
    
    p = Patient.objects.all()
    l= Lab.objects.all()
    d = Doctor.objects.all()
    context = {
        'patient' : p,
        'lab':l,
        'doctor':d,
        'message': 'Email already registered.'
    }
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['your_email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # Month_of_Pregnancy = request.POST['Month_of_Pregnancy']
        agee = request.POST['age']
        address = request.POST['address']
        lab = request.POST['lab']
        gender = request.POST['gender']
        password1 = request.POST['password']
        password2 = request.POST['comfirm_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'registration/Register.html', context)
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
            user.is_patient = True
            user.save()
            patient = Patient(user=user)
            # patient.pregnancy_month = Month_of_Pregnancy
            patient.age = agee
            patient.address = address
            # patient.lab = lab
            patient.gender = gender
            patient.save()
            return redirect('home')
            # return render(request, 'portal/patient_home.html')
    # return render(request, 'portal/index.html')
    return render(request,'registration/Register.html',context)
