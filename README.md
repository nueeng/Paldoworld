추억의 싸이월드

8° 월드

선선한 요즘날씨 봄을 맞아 다시 피어나는 꽃처럼 추억을 되살려보는 건 어떤가요
    내배캠 스파르타인들을 위한 서비스

회원 기능
회원 가입, 로그인 구현할 수 있다.
CRUD
c게시글 쓰기 기능 구현
r게시글 글 보여주기 구현
u게시글 글 수정 구현
d게시글 글 삭제 구현
GIT
git add / commit / push 활용
git 브랜치/ PR / merge 활용
github pull request에서 Code review 활용

app - user, tweet(게시글), guestbook(방명록)

역할 분담

Frontend

Backend

    로그인,회원가입 - 금방끝날것만안같습니다. 로그아웃도

    username
    password(password2와 같은지 검증)
    nickname
    introduce()-회원가입단계에서 프로필수정가능
    speech(한마디)
    site_address(git or blog 주소)
    tmi

    추후 프로필수정 같이

    게시글(base.html 중앙) 쓰기, 보여주기 -

    id
    title
    contents_text
    contents_photo (가능하면)
    created_at
    update_at

    게시글 수정&삭제

    방명록 쓰기,보여주기, 수정,삭제

    id
    profile_img (가능하면)
    contents_text
    created_at
    update_at

    follower / followee

어려울 것으로 예상됨

싸이월드 색감정하기

마이홈피 게시판 하얀색 파란색 회색
싸이월드 로고 주황색 하얀색
스파르타 빨간색 하얀색 노랑색

게더 사진찍어두고 어디 활용할지 선정

login / signup / tweet / guestbook 에러메세지 어떤식으로 띄울지

ERD 모델 명확히하기

웹 첫 페이지를 무엇으로 할건지? 로그인 창으로 해서 로그인해야 글도 볼 수 있게 할 건지 아니면 비로그인도 볼 수는 있게 해줄 것인지

로그인을 해야 다 볼수있도록

https://velog.io/@wiostz98kr/REST-API%EC%9D%98-%EA%B0%9C%EB%85%90%EA%B3%BC-%EB%94%94%EC%9E%90%EC%9D%B8-%EA%B0%80%EC%9D%B4%EB%93%9C
response에
key값 밸류값
결괏값 더 상세히쓰면
프론트 연결 시 편할 수 있음

response

profile, guestbook
url에 하이픈 언더바 하이픈을 선호
