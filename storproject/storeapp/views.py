from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Application


def base(request):
    return render(request, 'navbar.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def faculty(request):
    return render(request, 'faculty.html')


def contact(request):
    return render(request, 'contact.html')


def fill(request):
    return render(request, 'fill.html')


def success(request):
    return render(request, 'success.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('fill')
        else:
            messages.info(request, "invalid fruits")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)

            user.save();
            return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        date_of_birth = request.POST.get('bdate')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        mailing_address = request.POST.get('mailing_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        course = request.POST.get('course')
        degree = request.POST.get('degree')
        year = request.POST.get('year')
        reason_to_join = request.POST.get('reason_to_join')
        checklist = request.POST.getlist('checklist')
        agree_terms = request.POST.get('agree_terms') == 'on'

        application = Application(
            name=name,
            date_of_birth=date_of_birth,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            mailing_address=mailing_address,
            city=city,
            state=state,
            postal_code=postal_code,
            course=course,
            degree=degree,
            year=year,
            reason_to_join=reason_to_join,
            checklist=','.join(checklist),
            agree_terms=agree_terms
        )
        application.save()

        return redirect('success')
    return render(request, "form.html")
