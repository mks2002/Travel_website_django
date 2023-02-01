
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponseRedirect
from mainapp.models import Login
from bookings.models import Bookinghotel
import requests


# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def price(request):
    return HttpResponse('this is price page')


def staffs(request):
    return render(request, 'staffs.html')

# if we use this method we dont have the access of the username and password of the particular user in booking page when he goes from login page to booking page....

# def bookings(request):
#     data = {}
#     bool = False
#     if request.method == "POST":
#         name = request.POST.get('name')
#         last = request.POST.get('last')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         person = request.POST.get('person')
#         data = Booking(firstname=name, lastname=last,
#                        email=email, contact_no=contact, no_people=person)
#         data.save()
#         class_name = 'alert-success'
#         bool = True
#         n = 'your bookings has been done now'
#         data = {'cname': class_name,
#                 'bool': bool,
#                 'n': n}
#         return render(request, 'booking.html', data)
#     return render(request, 'booking.html', data)


# def login(request):
#     n = "for booking you need to login first !"
#     cname = "alert-warning"
#     bool = False
#     data = {'n': n,
#             'cname': cname,
#             'bool': bool}
#     if request.method == "POST":
#         un = request.POST.get('name')
#         pw = request.POST.get('password')
#         if Login.objects.filter(username=un, password=pw).exists():
#             return HttpResponseRedirect('/bookings/')
#         else:
#             n = "you are not registered create account to login "
#             cname = "alert-danger"
#             bool = 50
#             data = {'n': n,
#                     'cname': cname,
#                     'bool': bool}
#             return render(request, 'login.html', data)
#     return render(request, 'login.html', data)


def login(request):
    n = "for booking you need to login first !"
    cname = "alert-warning"
    bool = False
    data = {'n': n,
            'cname': cname,
            'bool': bool}
    if request.method == "POST":
        un = request.POST.get('name')
        pw = request.POST.get('password')
        if Login.objects.filter(username=un, password=pw).exists():

            url = '/bookings/?name={}&pw={}'.format(un, pw)
            return HttpResponseRedirect(url)

        else:
            n = "you are not registered create account to login "
            cname = "alert-danger"
            bool = 50
            data = {'n': n,
                    'cname': cname,
                    'bool': bool}
            return render(request, 'login.html', data)
    return render(request, 'login.html', data)


def bookings(request):
    data = {}
    data1 = {}
    bool = False
    if request.method == "GET":
        un = request.GET.get('name')
        password = request.GET.get('pw')
        # we use this url as a variable so that we can access this as a value in the page and by using this user can go to the dashboard page from the booking page...
        url = '/dashboard/?name={}&pw={}'.format(un, password)
        data = {'un': un, 'pw': password, 'url': url}
        return render(request, 'booking.html', data)
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            last = request.POST.get('last')
            email = request.POST.get('email')
            contact = request.POST.get('contact')
            person = request.POST.get('person')
            username = request.POST.get('username')
            password = request.POST.get('password')
            start = request.POST.get('startdate')
            end = request.POST.get('lastdate')
            data = Bookinghotel(firstname=name, lastname=last,
                                email=email, contact_no=contact, no_people=person, username=username, userpassword=password, start=start, end=end)
            data.save()
            class_name = 'alert-success'
            bool = True
            n = 'your bookings has been done now'
            url = '/dashboard/?name={}&pw={}'.format(username, password)
            data1 = {'cname': class_name,
                     'bool': bool,
                     'n': n, 'un': username, 'pw': password, 'url': url}
            return render(request, 'booking.html', data1)
    except Exception as e:
        pass
    return render(request, 'booking.html', data1)


def dashboard(request):
    data = {}
    if request.method == "GET":
        un = request.GET.get('name')
        password = request.GET.get('pw')
        tabel = Bookinghotel.objects.filter(username=un, userpassword=password)
        data = {'un': un, 'pw': password, 'maindata': tabel}
        return render(request, 'dashboard.html', data)

    return render(request, 'dashboard.html', data)


def delete(request):
    id1 = request.GET.get('id1')
    un = request.GET.get('name')
    pw = request.GET.get('pw')
    Bookinghotel.objects.filter(id=id1).delete()
    url = '/dashboard/?name={}&pw={}'.format(un, pw)
    return HttpResponseRedirect(url)


def signup(request):
    n = ''
    cname = ''
    bool = False
    data = {'n': n,
            'bool': bool, 'cname': cname}
    if request.method == "POST":
        un = request.POST.get('name')
        pw = request.POST.get('password')
        cpw = request.POST.get('cpassword')
        if pw != cpw:
            n = "password and confirm password must be same"
            cname = "alert-danger"
            bool = 50
            data = {'n': n,
                    'bool': bool, 'cname': cname}
        else:
            if Login.objects.filter(username=un).exists():
                n = "username already exist select another"
                cname = "alert-warning"
                bool = 40
                data = {'n': n,
                        'bool': bool, 'cname': cname}
            else:
                maindata = Login(username=un, password=pw)
                maindata.save()
                n = 'You have registerd succesfully! now you can login '
                bool = 30
                cname = "alert-success"
                data = {'n': n,
                        'bool': bool, 'cname': cname}
                return render(request, 'signup.html', data)

    return render(request, 'signup.html', data)


def blog(request):
    return render(request, 'blogs.html')


def travel(request):
    data = {}
    try:
        if request.method == "POST":
            id1 = request.POST.get('source')
            url = "https://trains.p.rapidapi.com/"

            payload = {"search": id1}
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "a78e10f741mshff5ec54a01b89afp1e0ae3jsnfdbc5239b4a0",
                "X-RapidAPI-Host": "trains.p.rapidapi.com"
            }

            response = requests.request(
                "POST", url, json=payload, headers=headers)
            datamain = response.json()
            data = {'datamain': datamain}
            return render(request, 'travel_details.html', data)
    except Exception as e:
        pass
    return render(request, 'travel_details.html', data)
