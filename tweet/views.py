from django.shortcuts import render, redirect
from .models import TweetModel, TweetComment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def main(request): # 메인페이지 렌더 함수 main_view로 변경 생각중
    return render(request, 'index.html')


def tweet(request):  # 게시글
    if request.method == 'GET': # GET 렌더 함수
        all_tweet = TweetModel.objects.all().order_by('-created_at')
        return render(request, 'tweet/tweet.html', {'tweet': all_tweet})

    elif request.method == 'POST': # POST 게시글 작성
        user = request.user
        content = request.POST.get('my-content', '')

        if content == "":  # 빈 칸일 시 if문 처리
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            # 이거 수정할 때 redirect로 할지 render로할지 정해서 게시글, 댓글 다 렌더 되도록해야함!
            return HttpResponse("게시글이 빈칸 입니다.")
            return render(request, 'tweet/tweet.html')  # 에러메세지 처리 뒤에
        else:
            my_tweet = TweetModel.objects.create(author=user, content=content)
            my_tweet.save()
            return redirect('/tweet_list')
        
def tweet_list(request):
    if request.method == 'GET': # GET 렌더 함수
        all_tweet = TweetModel.objects.all().order_by('-created_at')
        return render(request, 'tweet/tweet_list.html', {'tweet': all_tweet})


def detail_tweet(request, id):  # 게시글 상세페이지 렌더 함수
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request, 'tweet/tweet_detail.html', {'tweet': my_tweet, 'comment': tweet_comment})


@login_required
def delete_tweet(request, id): # 게시글 삭제함수
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')


@login_required  # 게시글 수정 페이지로 이동하는 함수
def edit_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(
        tweet_id=id).order_by('-created_at')
    return render(request, 'tweet/tweet_edit.html', {'tweet': my_tweet, 'comment': tweet_comment})


@login_required  # 게시글 실제로 수정하여 업데이트 하는 함수
def update_tweet(request, id):
    tweet_comment = TweetComment.objects.filter(
        tweet_id=id).order_by('-created_at')

    new_tweet = TweetModel.objects.get(id=id)
    new_tweet.content = request.POST.get("my-content", "")

    if new_tweet.content == "":
        return HttpResponse("게시글이 빈칸 입니다.")
        return render(request, 'tweet/tweet_detail.html')  # 에러메세지 처리 뒤에
    else:
        new_tweet.save()
        return render(request, 'tweet/tweet_detail.html', {'tweet': new_tweet, 'comment': tweet_comment})


@login_required  # 댓글 작성 함수
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/'+str(id))


@login_required  # 댓글 삭제 함수
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/'+str(current_tweet))
