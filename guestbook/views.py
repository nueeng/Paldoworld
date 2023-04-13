from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import GuestbookModel, UserModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import GuestbookModel
from user.models import UserModel
from django.utils import timezone

@login_required
def guestbook(request):
    if request.method == 'GET':
        all_guestbook = GuestbookModel.objects.all().order_by('-created_at')
        return render(request, 'guestbook/guestbook.html', {'guestbook': all_guestbook, 'owner_username': request.user.username})
    elif request.method == 'POST':
        user = request.user
        my_guestbook = GuestbookModel()
        my_guestbook.author = user
        my_guestbook.author_nickname_id = user.id
        my_guestbook.content = request.POST.get('my-content', '')
        my_guestbook.created_at = timezone.now()  # 유효한 값을 할당합니다.
        my_guestbook.save()
        return redirect('guestbook')




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

# ...

from django.http import Http404

@login_required
def view_guestbook(request, author):
    try:
        owner = UserModel.objects.get(nickname=author)
    except UserModel.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        content = request.POST.get('my-content', '')
        author_nickname = request.user.nickname
        guestbook = GuestbookModel.objects.create(content=content, author=request.user, author_nickname=author_nickname)
        owner.guestbook.add(guestbook)

    guestbook = owner.guestbook.all().order_by('-created_at')
    context = {
        'owner': owner,
        'guestbook': guestbook,
    }
    return render(request, 'guestbook/guestbook.html', context=context)




