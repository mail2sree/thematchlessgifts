# import the standard Django Forms
# from built-in library
from django import forms 
    
# creating a form  
class InputForm(forms.Form): 
    phonenumber = forms.IntegerField( 
    )

class InputForm1(forms.Form): 
    phoneNumber = forms.IntegerField( 
    )    