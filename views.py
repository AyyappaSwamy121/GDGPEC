from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import  logout,login
from django.http import *
from .models import *
import random
from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
def member(request):
    return render(request,'index2.html')

def login2(request):
    return render(request,"login2.html")

def gallery2(request):
    return render(request,"gallery2.html")

def perks(request):
    return render(request,"perks.html")

def home(request):
    return render(request,"index2.html")

def a(request):
    return render(request,"a.html")

def contact(request):
    return render(request,"contact.html")

def registration(request):
    return render(request,"registration.html")

def after_login(request):
    return render(request,"after_login.html")

def quiz_instruction(request):
    return render(request,"quiz_instruction.html")


def registration_adding(request):
    if request.method == "POST":            
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')

        if password != cpassword:
            messages.error(request, "Passwords do not match!")
            return redirect("registration")  

        if Registration.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("registration")  

        if Registration.objects.filter(contact=contact).exists():
            messages.error(request, "Phone number already exists!")
            return redirect("registration") 

        
        user = Registration(name=name, contact=contact, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful!")
        return redirect("home")  

    return redirect("registration")  

            
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        request.session['email'] = email

        if Registration.objects.filter(email=email).exists():
            member = Registration.objects.get(email=email)
     

            if member.password == password:
               return redirect("after_login")

            else:
                 messages.error(request, "Invalid Password")
        else:
             messages.error(request, "Email does not exists ")

    return render(request, 'login2.html')


def kaggle(request):
    email = request.session.get('email')
    data=Registration.objects.get(email=email)
    if request.method == 'POST':
        email = request.session.get('email')
        data=Registration.objects.get(email=email)
        score = 0
        for question in kaggle_questions.objects.all():
                    selected_answer = request.POST.get('question' + str(question.id))
                    print("the selected answer is",selected_answer)
                    if selected_answer == question.answer:
                        score += 1
                    data.kaggle_result=score
                    data.save()
                    print("score is",data.kaggle_result)
    context={}
    questions =list(kaggle_questions.objects.all())
    print("the questions arre",questions)
    random.shuffle(questions)
    context = {
        'questions': questions
        }
    return render(request, 'quiz_template.html', context)
    
def quiz_view(request, quiz_name):
    email = request.session.get('email')
    data = Registration.objects.get(email=email)
    try:
        QuizModel = apps.get_model('GDG', f"{quiz_name}_questions")
    except LookupError:
        return render(request, 'error.html', {'message': 'Quiz not found'})

    if request.method == 'POST':
        score = 0
        for question in QuizModel.objects.all():
            selected_answer = request.POST.get(f'question{question.id}')
            if selected_answer == question.answer:
                score += 1
        
        setattr(data, f"{quiz_name}_result", score)  
        data.save()
        return redirect("after_login")
    
    questions = list(QuizModel.objects.all())
    random.shuffle(questions)

    context = {
        'questions': questions,
        'quiz_name': quiz_name,
    }
    return render(request, 'quiz_template.html', context)

def view_score(request):
    email=request.session['email']
    task=Registration.objects.get(email=email)
    context={
        'task':task,
    }
    return render(request,'view_score.html',context)