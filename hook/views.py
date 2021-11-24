from django.shortcuts import render
from .forms import register_user
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from twilio.rest import Client



def register(request):
        account_sid = 'AC6686a30c373e5badf67bef80d97ed84b'
        auth_token = 'ee78ad60f1d13ab8e90af37598129fac'
        client = Client(account_sid, auth_token)

        form =register_user(request.POST or None)
        if form.is_valid():

                user=form.save()
                print(request.POST.get("Prefered_Comminication"))
                form= register_user()
                if request.POST.get("Prefered_Comminication") == "P" :
                        message = client.messages.create(
                                        body=f'Hi {request.POST.get("Name")}, to complete your Competition entery follow this link below:  {"www.test.com"}',
                                        from_='+18454796568',
                                        to=request.POST.get("Cell_number")

                                    )
                return redirect("/")

        return render(request, "home.html" ,{ 'form': form})


# Create your views here.
def home_view(request, *args, **kwargs):
        print(request.user)
        return render(request, "index.html",{} ) 


