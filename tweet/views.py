from django.shortcuts import render, redirect
from .models import TweetModel, TweetComment
from django.contrib.auth.decorators import login_required


def main(request): # 메인페이지 렌더 함수 main_view로 변경 생각중
    if request.method == 'GET':
        all_tweet = TweetModel.objects.all().order_by('-created_at')
        return render(request, 'index.html', {'tweet': all_tweet})


def tweet(request):  # 게시글
    if request.method == 'GET': # GET 렌더 함수
        return render(request, 'tweet/tweet.html')

    elif request.method == 'POST': # POST 게시글 작성
        user = request.user.is_authenticated
        title = request.POST.get('title', '')
        content = request.POST.get('my-content', '')

        if content == '' or title == '':  # 빈 칸일 시 validation
            return render(request, 'tweet/tweet.html', {'error': '다이어리를 입력해 주세요.'})
        else: # 로그인 안되어있을 시 validation
            if user:
                user = request.user # 여기서 is_authenticated 하면 ValueError Cannot assign "True" ~ must be a instance
                my_tweet = TweetModel.objects.create(author=user, title=title, content=content)
                my_tweet.save()
                return redirect('/tweet_list')
            else:
                return render(request, 'tweet/tweet.html', {'error': '다이어리 작성은 로그인이 필요해요.'})
        
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
    return redirect('/tweet_list')


@login_required  # 게시글 수정 페이지로 이동하는 함수
def edit_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request, 'tweet/tweet_edit.html', {'tweet': my_tweet, 'comment': tweet_comment})


@login_required  # 게시글 실제로 수정하여 업데이트 하는 함수
def update_tweet(request, id):
    if request.method == 'POST': # PUT
        update_tweet = TweetModel.objects.get(id=id)
        update_tweet.title = request.POST.get('title', '')
        update_tweet.content = request.POST.get('my-content', '')
        print(update_tweet.title, update_tweet.content) # 미해결

        if update_tweet.content == '' or update_tweet.title == '':
            return redirect('/tweet/edit/'+str(id)) # url이 /tweet/edit/48 이런식이라 안되는건가? 하는 예상..
            # return render(request, 'tweet/tweet_edit.html', {'error': '다이어리를 입력해 주세요.'})
        else:
            update_tweet.save()
            tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
            return render(request, 'tweet/tweet_detail.html', {'tweet': update_tweet, 'comment': tweet_comment})


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
