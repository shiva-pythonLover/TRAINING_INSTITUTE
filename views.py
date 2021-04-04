from django.shortcuts import render,redirect
from softTech.forms import VideoForm
from TRAINING_INSTITUTE.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
from softTech.models import VideoModel
#from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"softech/index.html")

def contact(request):
    print("befor check post")
    if request.method == 'POST':
        name = request.POST['form_name']
        recepient = request.POST['form_email']
        phone = request.POST['form_phone']
        subject = request.POST['form_subject']
        message = request.POST['form_message']
        send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
        msg = "SUCCESSFULLY SENT"
        messages.success(request,msg)
        return render(request, "softech/contact.html",{'recepient': recepient})
    return render(request,"softech/contact.html")


# def index_2(request):
#     return render(request, "softech/index-2.html")
def sendQuote(request):
    if request.method == 'POST':
        name = request.POST['form_name']
        recepient = request.POST['form_email']
        subject = request.POST['form_subject']
        jobtitle = request.POST['form_jobtitle']
        message = request.POST['form_message']
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        msg = "SUCCESSFULLY SENT"
        messages.success(request, msg)
        return render(request, "softech/index.html", {'recepient': recepient})
    return render(request, "softech/index.html")


def aboutus(request):
    return render(request,"softech/about.html")


def service(request):
    return render(request, "softech/service.html")


def serviceDetails(request):
    return render(request, "softech/service-details.html")


def pricing(request):
    return render(request,"softech/pricing.html")


def testimonials(request):
    return render(request,"softech/testimonials.html")


def team(request):
    return render(request,"softech/team.html")


def terms_conditions(request):
    return render(request,"softech/terms-conditions.html")


def privacy_policy(request):
    return render(request,"softech/privacy-policy.html")


def sign_up(request):
    return render(request,"softech/sign-up.html")


def log_in(request):
    return render(request,"softech/log-in.html")


def coming_soon(request):
    return render(request,"softech/coming-soon.html")


def faq(request):
    return render(request,"softech/faq.html")

def blog(request):
    return render(request, "softech/blog.html")

def blog_grid(request):
    return render(request,"softech/blog-grid.html")


def blog_single(request):
    return render(request,"softech/blog-single.html")

def uploadvideo(request):
    form = VideoForm()
    if request.method=='POST':
        form = VideoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        # name = request.POST['name']
        # print(name)
        # video = request.FILES['video']
        #
        # content = VideoModel(name=name,videofile=video)
        # content.save()
        return redirect('uploadvideo')

    return render(request, "softech/upload.html",{'form':form})


def online_courses(request):
    # firstvideo = VideoModel.objects.last()
    # videofile_last = firstvideo.videofile.url
    x = VideoModel.objects.all()
    return render(request,"softech/online-courses.html",{ 'videos': x})

