from django import forms
from .models import Personne

class LoginForm(forms.Form):
    email=forms.EmailField(label='courriel')
    password = forms.CharField(label ='mot_de_passe')
    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        #check that 2 champ are valide 
        if email and password:
            result = Personne.objects.filter(mot_de_passe=password,courriel=email)
            if len(result)!=1:
                raise forms.ValidationError(" Your email or password wrong ")
        return cleaned_data


class UserProfilForm(forms.ModelForm):
    class Meta :
        model= Personne
        exclude = ( 'amis',)


class AddFriendForm(forms.Form):

     email = forms.EmailField(label='Courriel : ')
     def clean(self) :
        cleaned_data = super(AddFriendForm , self).clean()
        email = cleaned_data.get("email")
        #Vérifie que le champ est valide
        if email:
            result=Personne.objects.filter(courriel=email)
            if len(result) !=1:
                raise forms.ValidationError("Address not found")
            return cleaned_data
