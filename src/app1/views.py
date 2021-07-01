import sys
import logging
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from app1.models import Contact_Us, PhoneBook
from app1.forms import ContactForm, LoginForm, PhoneBookForm

logger = logging.getLogger('app')


def home(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        pass
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return render(request,'index.html')


def about(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        pass
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return render(request,'about.html')


def contact(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        if request.method == 'POST':
            pDict = request.POST.copy()
            contact_form = ContactForm(pDict)
            if contact_form.is_valid(): 
                name = pDict['name']
                email = pDict['email']
                subject = pDict['subject']
                message = pDict['message']
            
                data = Contact_Us(name=name,email=email,subject=subject,message=message)
                data.save()

                data = {
                    'name' : name,
                    'email' : email,
                    'subject' : subject,
                    'message' : message
                }
                message = '''
                {}

                From: {}
                '''.format(data['message'], data['email'])
                send_mail(data['subject'], message, '',['lavanya00baskar@gmail.com'])
                info = "Thanks for submitting the form, we will be in touch soon"
                return render(request,'contact.html',{"content":info})
        else:
            contact_form = ContactForm()
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return render(request,'contact.html',locals())


def addContact(request):
    user = request.session['username']
    u = User.objects.get(username=user)

    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        if request.method=='POST':
            pDict = request.POST.copy()
            phonebook_form = PhoneBookForm(pDict)
            print(phonebook_form)
            if phonebook_form.is_valid():
                name = pDict['name']
                email = pDict['email']
                contact = pDict['contact']
                address = pDict['address']
                created_by = User.objects.get(id=u.id)
                data = PhoneBook(name=name,email=email,contact=contact,address=address,created_by=created_by)
                data.save()
                return redirect('phone_book')
        else:
            phonebook_form = PhoneBookForm()

    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return render(request,'add_contact.html', locals())

def register(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        content = dict()
        content.update({
            "error": False
        })
        if request.method == 'POST':
            firstName = request.POST['first_name']
            lastName = request.POST['last_name']
            userName = request.POST['username']
            password = request.POST['password1']
            confirmPassword = request.POST['password2']
            email = request.POST['email']
            if password == confirmPassword:
                if User.objects.filter(username=userName).exists():
                    content.update({
                        "error": True,
                        "userName": 'Username Already Taken'
                    })
                if User.objects.filter(email=email).exists():
                    content.update({
                        "error": True,
                        "email": 'Email Already Taken'
                    })
                else:
                    user = User.objects.create_user(username=userName, password=password, email=email,first_name=firstName,last_name=lastName)
                    user.save()
                    return redirect('login')
            else:
                content.update({
                    "error": True,
                    "password": 'password not matching'
                })
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return render(request,'register.html', locals())


def login(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        if request.method=='POST':
            pDict = request.POST.copy()
            login_form = LoginForm(pDict)
            if login_form.is_valid():
                username = pDict['username']
                password = pDict['password']
                user = auth.authenticate(username=username,password=password)
                auth.login(request,user)
                request.session['username'] = user.username
                request.session['id'] = user.id
                return redirect('home')
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    print(login_form)
    return render(request,'login.html', locals()) 


def logout(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        auth.logout(request)
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return redirect('home')


def phone_book(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        userId = request.session['id']
        phoneList = PhoneBook.objects.filter(created_by_id=userId).filter(datamode="A")
        return render(request,'phone_book.html',{'phoneListDict':phoneList})
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return render(request,'phone_book.html')

def show(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        id = request.GET['id']
        contactList = PhoneBook.objects.filter(id=id)
        return render(request,'show.html',{'contactList':contactList})
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return render(request,'show.html')

def edit(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        id = request.GET['id']
        contactList = PhoneBook.objects.filter(id=id)
        return render(request,'edit.html',{'contactData':contactList})
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return render(request,'show.html')
    

def delete(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        id = request.GET['id']
        deleteContact = PhoneBook.objects.get(id=id)
        deleteContact.datamode="D"
        deleteContact.save()
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return redirect('phone_book')

def update(request):
    fn = sys._getframe().f_code.co_name
    logger.info('{0} method is loading'.format(fn))
    try:
        if request.method == 'POST':
            pDict = request.POST.copy()
            name=pDict['name']
            email=pDict['email']
            contact=pDict['contact']
            address=pDict['address']


            updateId = request.POST['id']

            contactList = PhoneBook.objects.get(id=updateId)
            contactList.name = name
            contactList.email = email
            contactList.address = address
            contactList.contact = contact
            contactList.save()
            
    except Exception as e:
        logger.error(e)
    logger.info('{0} method is loading done'.format(fn))
    return redirect('phone_book')
        
def weather(request):
    return render(request,'weather.html')







