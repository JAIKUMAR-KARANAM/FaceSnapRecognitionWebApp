from django.shortcuts import render,redirect
from .forms import information_form
from django.contrib import messages
from . import img_retrival
from django.contrib.sessions.models import Session
from .models import user_info
import os
#import pywhatkit as kit


target_path = 'C:\\Users\\User\\Desktop\\target\\'

def index(request):
    form=information_form()
    if request.method == 'POST':
        form=information_form(request.POST,request.FILES)
        if form.is_valid():
           
            user_name = form.cleaned_data['name']
            request.session['user_name'] = user_name
            saved_obj=form.save()
            current_id=saved_obj.id
            request.session['current_id'] = current_id
            messages.success(request,str(user_name)+" Success  Data is Saved..!")
            return redirect('/shwdt')
    return render(request,"client/index.html",{'form':form})
def shwdt(request):
    
        directory_name = request.session.get('user_name', None)
        id = request.session.get('current_id', None)
        print("--------------------",id)
        data_by_username = user_info.objects.filter(id=id)
        
        for data in data_by_username:
            image_name=data.image
            print("______________________________",image_name)
            phno=data.phone_number
            print("______________________________",phno)
        directory_name+=phno
        reference_path = "D:/project_j/static/"+str(image_name)
        res=img_retrival.image_retrival(target_path,reference_path,directory_name)
        sel_img_path="D:/project_j/static/images/prd_images/"+directory_name
    
        imgs_list_show=[]
        phone_num = str(phno)  
        #message = 'Check out this image!'
        
        for filename in os.listdir(sel_img_path):
            full_sel_image_path = os.path.join(sel_img_path, filename)
            imgs_list_show.append(full_sel_image_path)
            print(full_sel_image_path)
            #kit.sendwhats_image(phone_num, full_sel_image_path, message, 12, 0)
        return render(request,"client/showdata.html",{'res':'your pics are here !','imgs':imgs_list_show})
   