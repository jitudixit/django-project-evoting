from turtle import setundobuffer
from django.shortcuts import render,redirect
from django.template import loader
from evotingapp.models import *
from django.http import HttpResponse
# Create your views here.

# Create your views for Users site
def uhome(request):
    return render(request,"users_site/users_login_page.html")
def ureg(request):
    return render(request,"users_site/users_registration_page.html")
def uvreg(request):
    return render(request,"users_site/users_voter_registration_page.html")
def userv(request):
    return render(request,"users_site/users_services_page.html")
def uabout(request):
    return render(request,"users_site/users_about_page.html")
def ucontact(request):
    return render(request,"users_site/users_contact_page.html")
def vot(request):
    return render(request,"users_site/users_voting_page.html")
def voted(request):
    return render(request,"users_site/users_voted_page.html")
def partynews(request):
    return render(request,"users_site/partynewspage.html")
def contactaction(request):
    msg=''
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']
        cn=Contact(fname=fname,lname=lname,email=email,message=message)
        cn.save()
        msg='feedback successful'
        
    else :
        msg='error occured'
    return render(request,"users_site/users_contact_page.html",{'msg':msg})
def candireg (request):
    return render(request,"party_site/party_candidate_registration_page.html")

def partyhome(request):
    return render(request,"party_site/party_home_page.html")
def partyloginaction(request):
    #msg=''
    if request.method == "POST":
        uname = request.POST['uname']
        psw = request.POST['psw']
        if uname=="bjp" and psw=="bjp":
            return render(request,"party_site/party_home_page.html")
        else:
            return render(request,"party_site/party_login_page.html",{'msg':"wrong username & password"})
        
    else :
        msg='error occured'
    return render(request,"party_site/party_login_page.html")
def adminloginaction(request):
    #msg=''
    if request.method == "POST":
        uname = request.POST['uname']
        psw = request.POST['psw']
        if uname=="admin" and psw=="admin":
            return redirect('/adminhome/')
        else:
            return render(request,"adminloginpage.html",{'msg':"wrong username & password"})
        
    else :
        msg='error occured'
    return render(request,"adminloginpage.html")
def uvregaction(request):
    msg=''
    if request.method == "POST":
       voterid=request.POST['voterid']
       issuedate=request.POST['isu']
       vname=request.POST['vname']
       fname=request.POST['fname']
       mname=request.POST['mname']
       dob=request.POST['dob']
       gender=request.POST['gender']
       category=request.POST['category']
       address=request.POST['address']
       state=request.POST['state']
       district=request.POST['district']
       vidname=request.POST['vidname']
       vid=VoterIds.objects.filter(voterid=voterid)
       if len(vid)>0:
            #return HttpResponse("<script>alert('if block');</script>")
            r=Regdetails.objects.filter(voterid=voterid)
            if len(r)>0:
                msg="already registered"
                return render(request,"users_site/users_voter_registration_page.html",{'msg':msg})
            else:
                reg=Regdetails(voterid=voterid,issuedate=issuedate,vname=vname,fname=fname,mname=mname,dob=dob,gender=gender,category=category,address=address,state=state,district=district,vidname=vidname)
                reg.save()
                msg="Successfully Registered Your voter id is your user id and dob is passward"
                u=Users(voterid=voterid,dob=dob)
                u.save()
                return render(request,"users_site/users_voter_registration_page.html",{'msg':msg})
       else:
           return render(request,"users_site/users_voter_registration_page.html",{'msg':"Invalid Record"})
def uregaction(request):
    msg=''
    if request.method == "POST":
        mobilenumber=request.POST['mobilenumber']
        otp=request.POST ['otp']
        v=Verification.objects.filter(mobilenumber=mobilenumber)
        if len(v)>0:
                return render(request,"users_site/users_registration_page.html",{'msg':"Mobile number allready registered"})
        elif otp=="1234":
            vr=Verification(mobilenumber=mobilenumber)
            vr.save()
            return redirect('/uvreg/')
def uregactionone(request):
    msg=''
    if request.method == "POST":
        aadharnumber=request.POST['aadharnumber']
        aotp=request.POST['aotp']
        ad=Verification.objects.filter(aadharnumber=aadharnumber)
        if len(ad)>0:
            return render(request,"users_site/users_registration_page.html",{'msg':"Aadhar number allready registered"})
        elif aotp=="5678":
            aad=Verification(aadharnumber=aadharnumber)
            aad.save()
            return redirect('/uvreg/')
    return render(request,"users_site/users_registration_page.html",{'msg':""})
#def regdetailsaction(request):
#    return render(request,"login.html")
def usersaction(request):
    msg = ''
    if request.method == "POST":
        voterid=request.POST['uname']
        dob=request.POST['psw']
        u=Users.objects.filter(voterid=voterid,dob=dob)
        if len(u)>0:
            return redirect("/vot/")
        else :
            return render(request,"users_site/users_login_page.html",{'msg':"Invalid userid and passward"})



#Create Views for Party  site

def partylogin(request):
    return render(request,"party_site/party_login_page.html")

#Create  Views for Admin site

def adminhome(request):
    return render(request,"admin_site/admin_home_page.html")
def adminlogin(request):
    return render(request,"admin_site/admin_login_page.html")
