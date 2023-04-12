from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import GuestbookModel
from user.models import UserModel

@login_required
def guestbook(request):
    if request.method == 'GET':
        all_guestbook = GuestbookModel.objects.all().order_by('-created_at')
        return render(request, 'guestbook/guestbook.html', {'guestbook': all_guestbook, 'owner_username': request.user.username})
    elif request.method == 'POST':
        user = request.user
        my_guestbook = GuestbookModel()
        my_guestbook.author = user
        my_guestbook.author_nickname = user.username
        my_guestbook.content = request.POST.get('my-content', '')
        my_guestbook.created_at = request.POST.get('-created_at')
        my_guestbook.save()
        return render('/guestbook')

@login_required
def edit_guestbook(request, id):
    # 게시물의 작성자와 현재 로그인한 사용자가 같은 경우에만 수정이 가능하도록 합니다.
    guestbook = get_object_or_404(GuestbookModel, pk=id, author=request.user)

    if request.method == 'POST':
        guestbook.content = request.POST.get('my-content', '')
        guestbook.save()
        return redirect('guestbook')

    return render(request, 'guestbook/edit_guestbook.html', {'guestbook': guestbook})

@login_required
def delete_guestbook(request, id):
    # 게시물의 작성자와 현재 로그인한 사용자가 같은 경우에만 삭제가 가능하도록 합니다.
    my_guestbook = get_object_or_404(GuestbookModel, id=id, author=request.user)
    my_guestbook.delete()
    return redirect('guestbook')

@login_required
def view_guestbook(request, username):
    try:
        owner = UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        return redirect('login')

    guestbook_entries = GuestbookModel.objects.filter(author=owner)
    context = {'owner_username': owner.username, 'guestbook': guestbook_entries}
    return render(request, 'guestbook/guestbook.html', context)
