from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
from django.contrib.auth import authenticate
from .models import user_profile , post_details , likePost , follower
from django.contrib.auth.decorators import login_required
from itertools import chain
# Create your views here.
def checkemail(mail,UserName):
    try: 
        user_name = User.objects.get(username=UserName)
        return False
    except:
        return True


@login_required(login_url='/')
def index(request):
    user_d = user_profile.objects.get(user=request.user)
    P_details = post_details.objects.filter(user=request.user)
    context = {'detail':user_d,'post':P_details}
    # print(context['post'])
    return render(request,'index.html',context)
@login_required(login_url='/')

def createPost(request):
    if request.method == 'POST':
        post_user = request.user.username
        post_title = request.POST.get('post_title')
        post_body = request.POST.get('post_body')
        post_img = request.FILES.get('post_img')
        post = post_details.objects.create(user=post_user,title = post_title,description = post_body , postImg=post_img)
        post.save()
        return redirect('/home')
    user_d = user_profile.objects.get(user=request.user)
    context = {'detail':user_d}
    return render(request,'post.html',context)
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/main')
        else:
            print('Authentication failed')
    return render(request,'login.html')


def Sign(request):
    if 'signin' in request.POST:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password!=confirmpassword:
            print("Password not matched")
        elif(checkemail(mail,username)):
            print(fname,lname,username,password,mail,confirmpassword)
            user = User.objects.create_user(username=username, email = mail, password = password , first_name=fname.capitalize() , last_name=lname.capitalize())
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request,user)
            user_d = User.objects.get(username=username)
            prof_save = user_profile.objects.create(user=user_d,id_user = user_d.id)
            prof_save.save()
            return redirect('/account')
    # if 'login' in request.POST:
    #     return redirect(request , 'Login.html')
    return render(request,'Sign.html')


@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='/')
def accountsettings(request):
    user_d = user_profile.objects.get(user=request.user)
    context = {'detail':user_d}
    # detail = user_profile.objects.get(user=request.user)
    # context = {'user_detail': detail} 
    if request.method == 'POST':
        img_prof = request.FILES.get('img_prof')
        status = request.POST.get('status')
        bio = request.POST.get('bio')
        print(img_prof, status, bio)
        if  img_prof is None:
            # user_d.prof_img = img_prof
            user_d.status = status
            user_d.bio = bio
            user_d.save()
        else:
            user_d.prof_img = img_prof
            user_d.status = status
            user_d.bio = bio
            user_d.save()
    return render(request,'accountsettings.html',context)

@login_required(login_url='/')
def like_post(request):
    username = request.user.username
    post_id  = request.GET.get('post_id')
    post_ob = post_details.objects.get(id=post_id)
    like_filter = likePost.objects.filter(post_id=post_id,username=username).first()
    if like_filter is None:
        like_save = likePost.objects.create(post_id=post_id,username=username)
        like_save.save()
        post_ob.likes = post_ob.likes + 1 
        post_ob.save()
        # context = {'outline': 'btn btn-dark'}
        return redirect('/main')
    else:
        like_filter.delete() 
        post_ob.likes = post_ob.likes - 1
        post_ob.save()
        context = {'outline': 'btn'}
        return redirect('/main')

@login_required(login_url='/')
def profile(request,pk):
    details = User.objects.get(username=pk)
    # print(details.username,request.user)
    user_posts = post_details.objects.filter(user=details.username)
    user_prof = user_profile.objects.get(user=details)
    # print(len(user_posts))
    u_f = follower.objects.filter(user_to_whom =details)
    followers = len(u_f)
    print(followers)
    if follower.objects.filter(user_to_whom =details.username,user_who_follow=request.user.username).first():
        but_type = 'btn-outline-secondary'
    else:
        but_type = 'btn-dark'
    context = { 
                'u_s' : user_prof, 
                'u_p' : user_posts,
                'd' : details,
                'len': len(user_posts),
                'but_type' : but_type,
                'no_of_followers' : followers,
                'p_d_img' :user_profile.objects.get(user=request.user)
                }
    # print(context['current_user'],context['prof_user'])
    if 'follow' in request.POST :
        follow_models = follower.objects.filter(user_to_whom =details.username,user_who_follow=request.user.username).first()
        if follow_models is None:
            follow_save = follower.objects.create(user_to_whom =details.username,user_who_follow=request.user.username)
            follow_save.save()
            return redirect(f'/profile/{details}')
        else:
            follow_models_delete = follower.objects.get(user_to_whom =details,user_who_follow=request.user)
            follow_models_delete.delete() 
            return redirect(f'/profile/{details}')
    return render(request, 'profile_page.html' , context)
@login_required(login_url='/')
def main_page(request):
    u_d = user_profile.objects.get(user=request.user)
    f_d = follower.objects.filter(user_who_follow=request.user)
    f_d_2 = follower.objects.filter(user_to_whom=request.user)
    l_post = likePost.objects.filter(username = request.user)
    l_like_post_id = []
    for i_d in l_post:
        l_like_post_id.append(i_d.post_id)
    print(l_like_post_id)
    # print(type(l_like_post_id)) --> list
    followings_list = [x for x in f_d]
    feeds = []
    fellow_ppl = []
    for i in range (len(followings_list)):
        u = User.objects.get(username=followings_list[i])
        u_f_ppl = user_profile.objects.filter(user=u)
        u_p = post_details.objects.filter(user=u) 
        feeds.append(u_p)
        fellow_ppl.append(u_f_ppl)

    context = {'u_d' : u_d , 'length_f_d':len(f_d),'length_f_d_2':len(f_d_2) , 'feeds':feeds , 'fellow_ppl' : fellow_ppl , 'l_p_id': l_like_post_id}
    return render(request, 'main_page.html',context)
@login_required(login_url='/')
def del_post(request):
    del_id = request.GET.get('del_id')
    print(del_id)
    del_ob = post_details.objects.get(user = request.user , id=del_id)
    del_ob.delete()
    return redirect('/home')
@login_required(login_url='/')
def search (request):
    u_d = user_profile.objects.get(user=request.user)
    if request.method == 'POST':
        u_name = request.POST.get('search_name')
        try:
            u_User = User.objects.get(username=u_name)
            u_d_s = user_profile.objects.get(user=u_User)
            u_f = follower.objects.filter(user_to_whom = u_User)
            u_f_f = follower.objects.filter(user_who_follow = u_User)
            p_d_l = len(post_details.objects.filter(user=u_User))
            follow = len(u_f)
            follow_1 = len(u_f_f)
            context = {'u_d_s': u_d_s , 'u_d': u_d ,'u_User': u_User , 'follow': follow , 'follow_1': follow_1 , 'p_d_l':p_d_l , 'noone':""}
            return render(request, 'search.html',context)
        except:
            context = {'noone':'No such user exists','u_User':"",'u_d': u_d}
            return render(request, 'search.html',context)
