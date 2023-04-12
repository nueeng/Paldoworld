from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):  # 회원가입 함수
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign-up.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        nickname = request.POST.get('nickname', '')
        speech = request.POST.get('speech', '')
        site_address = request.POST.get('site_address', '')
        tmi = request.POST.get('tmi', '')

        if password != password2:
            return render(request, 'user/sign-up.html', {'error':'비밀번호를 확인해 주세요'})
        else:
            if username == '' or password == '':
                return render(request, 'user/sign-up.html', {'error':'아이디와 비밀번호는 필수 값입니다.'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/sign-up.html',{'error':'사용자가 존재합니다.'})
            else:
                UserModel.objects.create_user(username=username, password=password, speech=speech, nickname=nickname, site_address=site_address, tmi=tmi)
                return redirect('/login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # get메서드안에 네임은 login html에 있는 input의 name="데이터"값이다.
        password = request.POST.get('password', '')

        # 유저모델은 이미 db와 연결돼있는 class다
        # 빨강색 username은 우리가만든 username이아니라 models에있던 클래스UserModel()의 username이다.
        # authenticate 암호화된 password를 연결해줌
        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error': '아이디 혹은 비밀번호를 확인해 주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/login.html')


@login_required # 사용자가 로그인이 되어있어야만 접근이 가능하다.라는 의미로 설정해준것
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        user = request.user
        user.nickname = request.POST.get('nickname',None)
        user.speech = request.POST.get('speech',None)
        user.site_address = request.POST.get('site_address',None)
        user.tmi = request.POST.get('tmi',None)
        user.save()
        return redirect('/')
    else:
        return render(request, 'user/profile_edit.html')

def userlist_view(request): # 유저리스트 띄우기 함수 / 이런식으로 할지 아니면 팔로우하고 있는 유저만 띄울지
    if request.method == 'GET':
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/follow.html', {'user_list':user_list})


@login_required
def follow_view(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.follower.all():
        click_user.follower.remove(request.user)
    else:
        click_user.follower.add(request.user)
    return redirect('/follow')

