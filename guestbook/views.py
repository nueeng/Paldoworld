from django.shortcuts import render, redirect, get_object_or_404
from .models import GuestbookModel
from django.contrib.auth.decorators import login_required


def guestbook(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_guestbook = GuestbookModel.objects.all().order_by('-created_at')
            return render(request, 'guestbook_1/guestbook.html', {'guestbook': all_guestbook})
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

@login_required # 방명록 수정
def edit_guestbook(request, id):
    guestbook = get_object_or_404(GuestbookModel, id=id)
    if request.method == 'GET':
        return render(request, 'guestbook_1/edit_guestbook.html', {'guestbook': guestbook})
    elif request.method == 'POST':
        guestbook.content = request.POST.get('my-content', '')
        guestbook.save()
        return redirect('/guestbook')

@login_required # 방명록 삭제
def delete_guestbook(request, id):
    my_guestbook = GuestbookModel.objects.get(id=id)
    my_guestbook.delete()
    return redirect('/guestbook')

