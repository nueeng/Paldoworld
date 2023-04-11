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
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        nickname = request.POST.get('nickname', None)
        speech = request.POST.get('speech', None)
        site_address = request.POST.get('site_address', None)
        tmi = request.POST.get('tmi', None)

        if password != password2:
            return render(request, 'user/sign-up.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/sign-up.html')
            else:
                UserModel.objects.create_user(username=username, password=password, speech=speech, nickname=nickname, site_address=site_address, tmi=tmi)
                return redirect('/login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)  # get메서드안에 네임은 login html에 있는 input의 name="데이터"값이다.
        password = request.POST.get('password', None)

        # 유저모델은 이미 db와 연결돼있는 class다
        # 빨강색 username은 우리가만든 username이아니라 models에있던 클래스UserModel()의 username이다.
        # authenticate 암호화된 password를 연결해줌
        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/login')

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/login.html')



@login_required #사용자가 로그인이 되어있어야만 접근이 가능하다.라는 의미로 설정해준것
def logout(request):
    auth.logout(request)
    return redirect('/')
