from django.shortcuts import render, redirect
from myapp.forms import AppointmentForm
from myapp.models import Appointment, Contact,Member

# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            members = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'members': members})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
        

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def appointment(request):
    if request.method == 'POST':
       makeappointment = Appointment(
              name = request.POST['name'],
              email = request.POST['email'],
              phone = request.POST['phone'],
              date = request.POST['date'],
              department = request.POST['department'],
              doctor = request.POST['doctor'],
              message = request.POST['message']
       )
       makeappointment.save()
       return redirect('/show')
    else:
        return render(request, 'appointment.html')
def contact(request):
    if request.method == 'POST':
       makecontact = Contact(
              name = request.POST['name'],
              email = request.POST['email'],
              subject = request.POST['subject'],
              message = request.POST['message']
       )
       makecontact.save()
       return redirect('contact')
    else:
        return render(request, 'contact.html')

def show(request):
    appointments = Appointment.objects.all()
    return render(request, 'show.html', {'appointments': appointments})

def delete(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('/show')

def edit(request, id):
    appointment = Appointment.objects.get(id=id)
    return render(request, 'edit.html', {'appointment': appointment})

def update(request, id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'appointment': updateinfo})
    
def register(request):
    if request.method == 'POST':
         member = Member(
                  name = request.POST['name'],
                  username = request.POST['username'],
                  password = request.POST['password']
         )
         member.save()
         return redirect('/login')
    else:
        return render(request, 'register.html')

             
def login(request):
    return render(request, 'login.html')
 
      

   


    







       
       
   








