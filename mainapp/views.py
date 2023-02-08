
from datetime import datetime as dt
from hotellist.models import Hotellist
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


# ______________________________________________________________________________________
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

# ______________________________________________________________________________________________

# here after login we send the user to booking form page but in the below one we create one hotellist page and after login we send user to that hotellist page from there he can go to bookings form page...

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

#             url = '/bookings/?name={}&pw={}'.format(un, pw)
#             return HttpResponseRedirect(url)

#         else:
#             n = "you are not registered create account to login "
#             cname = "alert-danger"
#             bool = 50
#             data = {'n': n,
#                     'cname': cname,
#                     'bool': bool}
#             return render(request, 'login.html', data)
#     return render(request, 'login.html', data)

# ____________________________________________________________________________________________________

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
        hl = 'all'
        if Login.objects.filter(username=un, password=pw).exists():

            url = '/hotellist/{}/{}/{}'.format(un, pw, hl)
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

# this page is for changing the password...
def update(request):
    n = 'enter your new password here'
    cname = 'alert-warning'
    bool = False
    data = {'n': n, 'bool': bool, 'cname': cname}
    if request.method == "POST":
        name = request.POST.get('name')
        new = request.POST.get('newpassword')
        if Login.objects.filter(username=name).exists():
            Login.objects.filter(username=name).update(
                username=name, password=new)
            n = 'your password is updated successfully now you can login !'
            cname = 'alert-success'
            bool = True
            data = {'n': n, 'bool': bool, 'cname': cname}
        else:
            n = 'No such account is exist'
            cname = 'alert-danger'
            bool = 50
            data = {'n': n, 'bool': bool, 'cname': cname}
        return render(request, 'update_password.html', data)
    return render(request, 'update_password.html', data)


def hotellist(request, username, password, hotelstate):
    if hotelstate == 'all':
        data = Hotellist.objects.all()
    elif hotelstate == 'others':
        data = Hotellist.objects.filter(
            state='gujrat') | Hotellist.objects.filter(state='laddakh')
    else:
        data = Hotellist.objects.filter(state=hotelstate)

    url = '/dashboard/?name={}&pw={}'.format(username, password)

    datamain = {'un': username, 'pw': password,
                'url': url, 'data': data}
    return render(request, 'hotellist.html', datamain)


def bookings(request):
    data = {}
    data1 = {}
    bool = False
    # this get values are come from the hotellist page..
    if request.method == "GET":
        un1 = request.GET.get('name')
        password1 = request.GET.get('pw')
        hname1 = request.GET.get('hname')
        hcity1 = request.GET.get('hcity')
        hstate1 = request.GET.get('hstate')
        hcost1 = request.GET.get('hcost')
        # we use this url as a variable so that we can access this as a value in this  page as well as we can use this to take this value to dashboard page and by using this user can go to the dashboard page from the booking page...
        url = '/dashboard/?name={}&pw={}'.format(un1, password1)
        data = {'un1': un1, 'pw1': password1, 'hname1': hname1,
                'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1, 'url': url}
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
            hotelname = request.POST.get('hotelname')
            hotelcity = request.POST.get('hotelcity')
            hotelstate = request.POST.get('hotelstate')
            hotelcost = request.POST.get('hotelcost')

            #  this are all the get method variable....
            un1 = request.GET.get('name')
            password1 = request.GET.get('pw')
            hname1 = request.GET.get('hname')
            hcity1 = request.GET.get('hcity')
            hstate1 = request.GET.get('hstate')
            hcost1 = request.GET.get('hcost')

            if end < start:
                class_name = 'alert-warning'
                bool = 50
                n = 'your starting date must be less than ending date'

                # url = '/dashboard/?name={}&pw={}'.format(username, password)
                url = '/dashboard/?name={}&pw={}'.format(un1, password1)
                data1 = {'cname': class_name,
                         'bool': bool,
                         'n': n, 'un': username, 'pw': password, 'url': url, 'un1': un1, 'pw1': password1, 'hname1': hname1,
                         'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
                return render(request, 'booking.html', data1)
            else:
                data = Bookinghotel(firstname=name, lastname=last,
                                    email=email, contact_no=contact, no_people=person, username=username, userpassword=password, start=start, end=end, hotelname=hotelname, city=hotelcity, state=hotelstate, current_cost=hotelcost)
                data.save()
                class_name = 'alert-success'
                bool = True
                n = 'your bookings has been done now'
                url = '/dashboard/?name={}&pw={}'.format(username, password)
                data1 = {'cname': class_name,
                         'bool': bool,
                         'n': n, 'un': username, 'pw': password, 'url': url, 'un1': un1, 'pw1': password1, 'hname1': hname1,
                         'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
                return render(request, 'booking.html', data1)
    except Exception as e:
        pass
    # if there is no post request which means user does not do any booking then it will render and by using this user can also go to the dashboard page...
    # this is not neccesary because if the request is not post then it must be get and we already handle get request....
    return render(request, 'booking.html', data1)


def dashboard(request):
    data = {}
    if request.method == "GET":
        un = request.GET.get('name')
        password = request.GET.get('pw')
        tabel = Bookinghotel.objects.filter(username=un, userpassword=password)
        hotelurl = '/hotellist/{}/{}/{}'.format(un, password, 'all')
        data = {'un': un, 'pw': password,
                'maindata': tabel, 'hotelurl': hotelurl}
        return render(request, 'dashboard.html', data)

    return render(request, 'dashboard.html', data)


def details(request):
    data = {}
    if request.method == "GET":
        un = request.GET.get('name')
        password = request.GET.get('pw')
        id = request.GET.get('id1')
        url = '/dashboard/?name={}&pw={}'.format(un, password)
        maindata = Bookinghotel.objects.get(id=id)
        start = str(maindata.start)
        end = str(maindata.end)
        res = (dt.strptime(end, "%Y-%m-%d") -
               dt.strptime(start, "%Y-%m-%d")).days
        total_cost = res*maindata.current_cost
        data = {'un': un, 'pw': password,
                'maindata': maindata, 'url': url, 'cost': total_cost}
        return render(request, 'order_details.html', data)
    return render(request, 'order_details.html', data)

# this page is for deleting the order...
def delete(request):
    id1 = request.GET.get('id1')
    un = request.GET.get('name')
    pw = request.GET.get('pw')
    Bookinghotel.objects.filter(id=id1).delete()
    url = '/dashboard/?name={}&pw={}'.format(un, pw)
    return HttpResponseRedirect(url)


def blog(request):
    return render(request, 'blogs.html')

# this is the traindetails page ...
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
