from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib import messages
from contacts.models import createcontact

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return render(request, '')
def create(request):  
    return render(request, 'createcontacts.html')
def contacts(request):
    # return render(request, 'phonedirectory.html')
    contact = None
    print("start")
    if request.method == "POST":
        firstName = request.POST.get('firstname')
        middleName = request.POST.get('middlename')
        lastName = request.POST.get('lastname')
        nickName = request.POST.get('nickname')
        phoneno = request.POST.get('mobileno')
        workno = request.POST.get('workno')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        anniversary = request.POST.get('anniversary')
        bloodgroup = request.POST.get('bloodgroup')
        hstreet = request.POST.get('hstreet')
        hcity = request.POST.get('hcity')
        hstate = request.POST.get('hstate')
        hcountry = request.POST.get('hcountry')
        hpostcode = request.POST.get('hpostcode')
        wstreet = request.POST.get('wstreet')
        wcity = request.POST.get('wcity')
        wstate = request.POST.get('wstate')
        wcountry = request.POST.get('wcountry')
        wpostcode = request.POST.get('wpostcode')

        store = createcontact(firstName=firstName, middleName=middleName, lastName=lastName,
        nickName=nickName,
        phoneno=phoneno,
        workno=workno,
        email=email,
        birthday=birthday,
        anniversary=anniversary,
        bloodgroup=bloodgroup,
        hstreet = hstreet, 
        hcity = hcity, 
        hstate = hstate, 
        hcountry = hcountry, 
        hpostcode = hpostcode, 
        wstreet = wstreet, 
        wcity = wcity, 
        wstate = wstate, 
        wcountry = wcountry, 
        wpostcode = wpostcode
        )
        # print("Save karo")
        store.save()
        # print("save ho gaya")
        # messages.success(request, "finally ho gaya bhai")
        
    data = createcontact.objects.all()
    contact = {
        "contact": data
    }

    return render(request, 'phonedirectory.html', contact)
        
    # return render(request, 'phonedirectory.html')

# def show(request):
    
    
