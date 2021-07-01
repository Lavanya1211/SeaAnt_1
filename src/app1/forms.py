from django import forms
from django.contrib.auth.models import User, auth
from app1.models import Contact_Us, PhoneBook



class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username:
            if not User.objects.filter(username=username).exists():
                raise forms.ValidationError(u"Username not avaiable in our system.")
        if username and password:
            user = auth.authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError(u"Username and Passwords do not match.")
            
        return self.cleaned_data
class ContactForm(forms.Form):
    name = forms.CharField(label='Full Name', required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Subject', required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message', required=True,widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean(self):
        super(ContactForm, self).clean()
        email = self.cleaned_data.get('email')
        if email:
            if Contact_Us.objects.filter(email=email).exists():
                raise forms.ValidationError(u"This mail id already send an mail.")

        return self.cleaned_data

class PhoneBookForm(forms.Form):
    name = forms.CharField(label="Name",required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contact = forms.IntegerField(label='Contact_No', required=True,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
   

    def clean(self):
            super(PhoneBookForm, self).clean()
            email = self.cleaned_data.get('email')
            contact_no = self.cleaned_data.get('contact')
            if email:
                if PhoneBook.objects.filter(email=email).exists():
                    raise forms.ValidationError(u"This mail id already Used.")
                
            if contact_no:
                if PhoneBook.objects.filter(contact=contact_no).exists():
                    raise forms.ValidationError(u"This Contact Number is already Used.")

            return self.cleaned_data


