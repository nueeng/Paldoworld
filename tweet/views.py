from django.shortcuts import render, redirect
from .models import TweetModel, TweetComment
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
=======
from django.http import HttpResponse

>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4
# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/login')

def tweet(request):
    if request.method == 'GET':
        user=request.user.is_authenticated
        if user:
            all_tweet = TweetModel.objects.all().order_by('-created_at')
<<<<<<< HEAD
            return render(request, 'tweet/tweet.html', {'tweet':all_tweet})
=======
            return render(request, 'tweet/home.html', {'tweet':all_tweet})
>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4
        else:
            return redirect('/login')

    elif request.method == 'POST':
        user = request.user
<<<<<<< HEAD
        my_tweet = TweetModel()
        my_tweet.author = user
        my_tweet.content = request.POST.get('my-content','')
        my_tweet.save()
        return redirect('/tweet')
def main(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'index.html')
        else:
            return redirect('/login')

@login_required #사용자가 로그인이 되어있어야만 접근이 가능하다.라는 의미로 설정해준것
def delete_tweet(request, id):
=======
        content = request.POST.get('my-content','')

        if content == "": # 빈 칸일 시 if문 처리
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return HttpResponse("게시글이 빈칸 입니다.") # 이거 수정할 때 redirect로 할지 render로할지 정해서 게시글, 댓글 다 렌더 되도록해야함!
            return render(request, 'tweet/home.html') # 에러메세지 처리 뒤에
        else:
            my_tweet = TweetModel.objects.create(author=user, content=content)
            my_tweet.save()
            return redirect('/tweet')


@login_required # 사용자가 로그인이 되어있어야만 접근이 가능하다.라는 의미로 설정해준것
def delete_tweet(request, id): # 삭제
>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')

<<<<<<< HEAD
=======

>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4
@login_required # 상세 보기
def detail_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request,'tweet/tweet_detail.html',{'tweet':my_tweet,'comment':tweet_comment})

<<<<<<< HEAD
=======
@login_required # 트윗 수정 페이지로 이동하는 함수
def edit_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request,'tweet/tweet_edit.html',{'tweet':my_tweet,'comment':tweet_comment})

@login_required # 실제로 수정하여 업데이트 하는 함수
def update_tweet(request, id):
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')

    new_tweet = TweetModel.objects.get(id=id)
    new_tweet.content = request.POST.get("my-content","")

    if new_tweet.content == "":
        return HttpResponse("게시글이 빈칸 입니다.")
        return render(request,'tweet/tweet_detail.html') # 에러메세지 처리 뒤에
    else:
        new_tweet.save()
        return render(request,'tweet/tweet_detail.html',{'tweet':new_tweet,'comment':tweet_comment})

>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4

@login_required # 댓글 작성
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment","")
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/'+str(id))


@login_required # 댓글 삭제
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
<<<<<<< HEAD
    return redirect('/tweet/'+str(current_tweet))
=======
    return redirect('/tweet/'+str(current_tweet))
>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4
