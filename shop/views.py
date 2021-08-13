from django.core import paginator
from django.forms.widgets import Input
from django.shortcuts import redirect, render
from pyrebase.pyrebase import Database
from razorpay.resources import payment
from .models import Order, Product
from django.core.paginator import*
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import pyrebase
from .forms import*

# Create your views here.
def index(request):
    product_objects = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 20)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)


    return render(request, 'index.html', {'product_objects': product_objects})

def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'detail.html', {'product_object': product_object})

def checkout(request):
    if request.method == 'POST':
        total = request.POST.get('amount', "")
        items = request.POST.get('items', "")
        firstname = request.POST.get('firstName', "")
        lastname = request.POST.get('lastName', "")
        username = request.POST.get('username', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        address2 = request.POST.get('address2', "")
        country = request.POST.get('country', "")
        state = request.POST.get('state', "")
        city = request.POST.get('city', "")
        zip = request.POST.get('zip', "")
        total1 = total * 100
        order = Order(firstname=firstname, lastname=lastname, email=email, address=address, address2=address2, country=country, state=state, username=username, zip=zip, city="Dint Ask", items=items, orderstatus="Yet to be Dispatched", total=total)
        order.save()
        config = {

              "apiKey": "AIzaSyBanRhLGLaszhx509Lz8D2EvY28KDd98V0",

              "authDomain": "matchlessgifts2021-31-2021.firebaseapp.com",

              "projectId": "matchlessgifts2021-31-2021",

              "storageBucket": "matchlessgifts2021-31-2021.appspot.com",

              "messagingSenderId": "252095779446",

              "appId": "1:252095779446:web:fc2f859a67f5de0efb0557",

              "measurementId": "G-R03XFLTS7N",

              "databaseURL": "https://matchlessgifts2021-31-2021-default-rtdb.firebaseio.com/"

            }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()
        total1 = int(total) * (100)
        dict1 = {'total': total1, 'items': items, 'firstname': firstname, 'lastname': lastname, 'username': username, 'address': address, 'address2': address2, 'country': country, 'state': state, 'zip': request.POST.get('zip', ""), 'phone': request.POST.get('phone', ""), 'Order Status': 'Yet to be dispached'}
        database.child(request.POST.get('phone', "")).child('Details').set(dict1)

        return redirect('pay/')
        return render(request, 'checkout.html', {})

    return render(request, 'checkout.html', {})

@csrf_exempt
def success(request):
    return render(request, 'success.html')    

def pay(request):
    config = {

              "apiKey": "AIzaSyBanRhLGLaszhx509Lz8D2EvY28KDd98V0",

              "authDomain": "matchlessgifts2021-31-2021.firebaseapp.com",

              "projectId": "matchlessgifts2021-31-2021",

              "storageBucket": "matchlessgifts2021-31-2021.appspot.com",

              "messagingSenderId": "252095779446",

              "appId": "1:252095779446:web:fc2f859a67f5de0efb0557",

              "measurementId": "G-R03XFLTS7N",

              "databaseURL": "https://matchlessgifts2021-31-2021-default-rtdb.firebaseio.com/"

            }

    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    form = InputForm(request.POST)
    if form.is_valid():
        a = form.cleaned_data['phonenumber']
        print (a)
        total = database.child(a).child('Details').child('total').get().val()
        return render(request, 'pay.html', {'total': total, 'pay': pay, 'form': InputForm()})
    return render(request, 'pay.html', {})

def track(request):
    form = InputForm1(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            config = {

                "apiKey": "AIzaSyBanRhLGLaszhx509Lz8D2EvY28KDd98V0",

                "authDomain": "matchlessgifts2021-31-2021.firebaseapp.com",

                "projectId": "matchlessgifts2021-31-2021",

                "storageBucket": "matchlessgifts2021-31-2021.appspot.com",

                "messagingSenderId": "252095779446",

                "appId": "1:252095779446:web:fc2f859a67f5de0efb0557",

                "measurementId": "G-R03XFLTS7N",

                "databaseURL": "https://matchlessgifts2021-31-2021-default-rtdb.firebaseio.com/"

                }

            a = form.cleaned_data['phoneNumber']
            firebase = pyrebase.initialize_app(config)
            database = firebase.database()
            firstname = database.child(a).child('Details').child('firstname').get().val()
            lastname = database.child(a).child('Details').child('lastname').get().val()
            orderstatus = database.child(a).child('Details').child('Order Status').get().val()
            phone = database.child(a).child('Details').child('phone').get().val()
            address = database.child(a).child('Details').child('address').get().val()
            address2 = database.child(a).child('Details').child('address2').get().val()
            zipcode = database.child(a).child('Details').child('zip').get().val()
            return render(request, 'track.html', {'form': InputForm1(), 'fname': firstname, 'lname': lastname, 'ostatus': orderstatus, 'phone': phone, 'address': address, 'address2': address2, 'zip': zipcode})

    return render(request, 'track.html', {'form': InputForm1()})