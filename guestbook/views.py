from django.shortcuts import render, redirect, get_object_or_404
from .models import GuestbookModel, UserModel
from django.contrib.auth.decorators import login_required


def guestbook(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_guestbook = GuestbookModel.objects.all().order_by('-created_at')
            return render(request, 'guestbook/guestbook.html', {'guestbook': all_guestbook})
        else:
            return redirect('/login')

    elif request.method == 'POST':
        user = request.user
        my_guestbook = GuestbookModel()
        my_guestbook.author = user
        my_guestbook.content = request.POST.get('my-content', '')
        my_guestbook.created_at = request.POST.get('-created_at')
        my_guestbook.save()
        return redirect('/guestbook')


def edit_guestbook(request, id):
    # 로그인한 사용자인 경우에만 뷰 함수를 실행합니다.
    if not request.user.is_authenticated:
        raise PermissionDenied

    guestbook = get_object_or_404(GuestbookModel, id=id)
    if request.method == 'GET':
        return render(request, 'guestbook/edit_guestbook.html', {'guestbook': guestbook})
    elif request.method == 'POST':
        guestbook.content = request.POST.get('my-content', '')
        guestbook.save()
        return redirect('/guestbook')

@login_required # 방명록 삭제
def delete_guestbook(request, id):
    my_guestbook = GuestbookModel.objects.get(id=id)
    my_guestbook.delete()
    return redirect('/guestbook')

def view_guestbook(request):
    if request.method == 'GET': # GET 렌더 함수
        owner = UserModel.objects.all()
        # guestbook_entries = Guestbook.objects.filter(owner=owner)
        # context = {'owner_username': owner.username, 'guestbook_entries': guestbook_entries}
        return render(request, 'guestbook/view_guestbook.html', {'owner':owner})
