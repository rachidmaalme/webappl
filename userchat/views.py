from django.shortcuts import render
from django.http import HttpResponseRedirect ,HttpResponse
from .forms import LoginForm , UserProfilForm,AddFriendForm
from .models import Personne,Message
from django.utils import timezone
from django.core import exceptions
from django import forms
# Create your views here.

def login(request) :
    if request.method=="POST":
       form = LoginForm(request.POST)
       if form.is_valid():
           user_email = form.cleaned_data['email']
           logged_user = Personne.objects.get(courriel=user_email)
           request.session['logged_user_id'] = logged_user.id
           return HttpResponseRedirect('/welcome')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form' :form ,})



def register(request) :
    if len(request.GET) >0:
        form = UserProfilForm(request.GET)
        if form.is_valid():
             form.save(commit=True)
             return HttpResponseRedirect('/login')
        else:
             return render(request,'login.html', {'form' : form})
    else:
         form = UserProfilForm()
         return render(request,'user_profile.html ', {'form' : form})


    # looking up a person 
def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        if len(Personne.objects.filter(id=logged_user_id))==1:
          return Personne.objects.get(id=logged_user_id)
    else :
        return None




def welcome(request) :
      logged_user = get_logged_user_from_request(request)
      if not logged_user is None:
          if 'newMessage' in request.GET and request.GET['newMessage'] != '':
              newMessage = Message(auteur=logged_user,contenu=request.GET['newMessage'],date_de_publication = timezone.now())
              newMessage.save()
          friendMessages = Message.objects.filter(auteur__amis= logged_user).order_by('-date_de_publication')
          return render(request,'welcome.html',{'logged_user': logged_user,'friendMessages': friendMessages})
      else:
         return HttpResponseRedirect('/login')



def addfriend(request):
    logged_user=get_logged_user_from_request(request)
    if logged_user:
        #Test if the form was sent
        if len(request.GET)>0:
            form = AddFriendForm(request.GET)
            if form.is_valid():
                new_freind_email=form.cleaned_data['email']
                NewFriend = Personne.objects.get(courriel=new_freind_email)
                logged_user.amis.add(NewFriend)
                logged_user.save()
                return HttpResponseRedirect('/welcome')
            else:
                return render (request,'addFriend.html' , {'form' : form})
        else: #the form wasn't newMessagelnput
            form =AddFriendForm()
            return render (request,'addFriend.html' , {'form' : form})
    else:
        return HttpResponseRedirect('/login')


def showProfile(request):
    logged_user=get_logged_user_from_request(request)
    if logged_user:
        #test if the expected settings is good
        if 'userToshow' in request.GET and request.GET['userToshow'] !='':
             result=Personne.objects.filter(id=request.GET['userToshow'])
             if result==1:
                 user_to_show=Personne.objects.get(id=request['userToshow'])
                 return render(request,'showProfile.html',{'user_to_show':user_to_show})
        else:
            return render(request,'showProfile.html',{'user_to_show':logged_user})
    else:
        return HttpResponseRedirect('/login')



def modifyP(request):
        logged_user=get_logged_user_from_request(request)
        if logged_user:
            if len(request.GET) > 0:
                 form =UserProfilForm(request.GET,instance=logged_user)
                 if form.is_valid():
                     form.save(commit=True)
                     return HttpResponseRedirect('/welcome')
                 else:
                    return render(request,'modify_profile.html', {'form' : form})
            else:
                form =UserProfilForm(instance=logged_user)
                return render(request,'modify_profile.html', {'form' : form})
        else:
            return HttpResponseRedirect('/login')



def ajax_check_email_field(request):
    HTML_to_return = ''
    if 'value' in request.GET:
        field = forms.EmailField()
        try:
            field.clean(request.GET['value'])
        except exceptions.ValidationError as ve:
                HTML_to_return = '<ul class="errorlist">'
                for message in ve.messages:
                    HTML_to_return += '<li>' + message + '</li>'
                    HTML_to_return += '</Ul>'
    return HttpResponse(HTML_to_return)
