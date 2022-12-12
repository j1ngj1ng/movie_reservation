rows = 10 #이차원 리스트를 선언하기 위한 행 변수
cols = 10 #이차원 리스트를 선언하기 위한 열 변수
seat = [[0 for j in range(cols)] for i in range(rows)]  #이차원 리스트를 만드는 변수로 10x10 리스트를 만들어 출력 한다.
totalPay =0 #영화를 예매한 금액을 출력하기 위한 변수 
cnt = 0 #좌석을 그려줄때 몇번째 행과 몇번째 열인지를 알려주기 위한 카운트 변수
selectCol = 0 #좌석을 선택하는 변수
selectRow = 0 #좌석을 선택하는 변수

def seatCondition(): #좌석의 현황 출력을 위한 함수
    print('  ', end ='') #앞부분을 띄워주기 위한 단순 출력문이다.
    cnt =0 #다음 호출에서 다시 사용될 수 있기 때문에 항상 초기화를 위하여 사용한다.
    print(' ',end ='') #띄워주기 위한 단순 출력문 
    while cnt<10 : #1부터 10까지 출력하기 위하여 10번 반복한다
        cnt+=1 #반복하면서 숫자를 1씩 증가 시켜준다.
        print('%3d' %cnt, end ='') #3자리를 차지하는 cnt변수를 출력해주고 엔터키를 치지 않기 위하여 end를 사용한다.
    print() #엔터를 위한 출력문
    cnt =1 #행이 몇번째 인지 알려주기 위한 변수 
    print('-----------------------------------') #구분자 출력을 해준다.
    for a in seat: #a부터 seat변수 까지 반복
        print('%-2d' %cnt, end ='|') #1부터 10까지 몇번째 열인지 알려주기위해서 구분자 |와 숫자를 출력한다
        for b in a: #b부터 a까지 반복한다
            print(' ',b, end='') #공백과 b를 출력함 엔터키를 치지 않음.
        print() #줄바꿈 출력
        cnt+=1 #카운트변수에 1씩 더한다
    return ' '

def inputSeat(person): #좌석 예약을 위한 함수로 입력받은 사람 수 만큼 반복하는 함수이다.
    i = 1
    total =0 #금액을 저장하기 위한 변수 이다.
    stop = 1 #-1을 입력받으면 좌석을 종료하려면 저장하기 위한 변수 이다.
    while  (i <= person): #i는 그냥1 person은 예약하려던 사람 수 이다. i가 예약하는 사람 수 보다 작거나 같을때 까지 아래의 예약하는 코드를 반복한다.
        seatCondition() #좌석 현황을 출력해준다.
        print("원하시는 좌석의 행번호를 입력하세요(종료는 -1)") #예약하고 싶은 좌석의 행번호를 입력하라는 안내 문구이다.
        global selectCol #위에서 선언한 변수를 사용하기 위해 선언을 해주는 것이다. 아래도 같은 이유이다.
        global selectRow
        selectCol=int(input()) #행 번호를 선택하기 위해서 정수로 입력해준다.
        if selectCol == -1: #만약 입력한 행번호가 -1이라면 종료를 뜻하기 때문에 아래의 코드를 실행하게 된다.
            stop = 0 #stop변수를 0으로 설정해주고 메인 함수로 가서 바로 종료해주기 위해 미리 변수에 판단할 수 있는 값을 넣어준다.
            break #입력을 받지 않고 종료 할거기 때문에 무한 반복문을 멈춘다.
        print("원하시는 좌석의 열번호를 입력하세요(종료는 -1)") #위에 행번호를 설명한 내용과 같다.
        selectRow=int(input())
        if selectRow == -1:
            stop = 0
            break
        if selectCol >=1 and selectCol <=10 and selectRow >=1 and selectRow <=10: #만약 위에서 입력한 행번호와 열번호 모두 1과 10사이의 수라면 아래의 코드를 실행한다.
            if seat[selectRow-1][selectCol-1]=="1": #만약 좌석이 이미 선택된 좌석인 1로 되어 있다면 예약된 좌석이기 때문에 아래의 코드를 실행한다
                print("이미 예약된 좌석이니, 다른 좌석을 선택하세요") #이미 선택한 좌석이기 때문에 다른 좌석을 선택하라는 안내 메시지를 출력한다.
            else:
                seat[selectRow-1][selectCol-1]="1" #좌석이 1이 아니라면 이미 위에서 초기화 한 대로 0으로 초기화 되어있기 때문에 입력한 자리를 1로 변경해준다. 이때 -1을 해주는 이유는 리스트는 0부터 시작했기 때문에 입력한 수보다 하나 작다.
                print("좌석이 예약되었습니다") #좌석이 예약 되었다는 안내문구를 출력한다
                print("예약하신 좌석") #안내 문구를 출력한다.
                seatCondition() #좌석 현황을 출력해주는 용도
                    #Number.append(select)
                i += 1 #위의 코드가 잘 작동했다면 한명에 대한 예약이 끝났기 때문에 i에 1을 더해준다.
                total += 9000 #위의 코드가 잘 작동했다면 영화 금액에 대하여 9천원을 더해준다.
        else: #만약 좌석 입력이 이상하다면 아래 코드를 실행한다.
            print("1-10번 좌석 중 선택하세요!!") #1번부터 10번 사이의 좌석을 입력하라는 안내메시지를 출력한다.
    return total, stop #리턴값으로 영화 가격과 예약을 그만둘건지에 대한 여부를 반환해준다.
    
def title(): #영화 제목 및 날짜, 상영시간을 고르는 함수이다.
    mtitle=["올빼미", "그래비티","매드맥스","프레이 포 더 데블", "크리스마스 캐럴","아바타"] #리스트로 mtitle이라는 변수에 영화제목을 순서대로 저장한다.
    mtime=["9:00-11:00", "12:30-14:30","16:00-18:00","19:30-21:30"] #리스트로 mtime이라는 변수에 시간을 순서대로 저장한다.
    while True: #잘못 입력할 경우 다시 입력을 요구하기 위하여 무한 반복문을 사용한다.
        print("영화제목 선택-번호를 입력해주세요") # 영화제목 선택하라는 안내문을 출력한다.
        print("1. 올빼미 2.그래비티 3.매드맥스 4.프레이 포 더 데블 5.크리스마스 캐럴 6.아바타") #영화 제목을 순서대로 보여준다.
        movieTitle = int(input()) #정수형으로 입력을 받는다.
        if movieTitle >= 1 and movieTitle<=6: #만약 위에서 입력받은 값이 1부터 6사이라면 아래의 코드를 실행한다.
            break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
        else: #만약 입력받은 값이 이상하다면 아래의 코드를 실행한다.
            print("잘못 입력하셨습니다.") #잘못 입력했다는 것을 출력해준다
            continue #잘못 입력하였기때문에 다시 처음 무한반복문의 처음으로 돌아가서 다시 코드를 실행한다.
    while True: #잘못 입력할 경우 다시 입력을 요구하기 위하여 무한 반복문을 사용한다.
        print("날짜를 입력해 주세요 *입력예시: 03 15") #날짜를 입력해 달라는 안내 메시지 출력
        date = input() #date에 날짜를 입력해준다.
        if " " in date: #만약 date 사이에 공백이 있다면 아래 코드를 실행한다. 공백이 있는지 확인하는 이유는 입력 예시에 공백으로 월, 날짜 를 구분했기 때문에 공백이 있는지 확인해준다.
            month, day = date.split() #잘 입력 받았다면 date를 띄어쓰기 기준으로 잘라서 앞에 있는 문자를 month에 저장하고 date를 띄어쓰기 기준으로 나누었을때 뒤에 있는 문자는 day에 저장해준다.
            break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
        else : #만약 date사이에 공백이 없다면 아래 코드를 실행한다.
            print("잘못 입력하셨습니다.") #잘못 입력했다는 안내 메시지 출력
            continue #잘못 입력하였기때문에 다시 처음 무한반복문의 처음으로 돌아가서 다시 코드를 실행한다.
    while True: #잘못 입력할 경우 다시 입력을 요구하기 위하여 무한 반복문을 사용한다.
        print("영화 시간대") #영화 시간대 메시지 출력
        print("1. 9:00-11:00   2. 12:30-14:30   3. 16:00-18:00   4. 19:30-21:30") #시간대 순서대로 출력
        time = int(input()) #time변수에 정수형으로 입력받는다.
        if time >=1 and time <=4: #만약 입력받은 수가 1부터 4 사이라면 아래 코드 실행
            break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
        else: #위의 조건이 잘못되었을 경우 아래코드를 실행한다.
            print("잘못 입력하셨습니다.")#잘못 입력했다는 안내 메시지 출력
            continue #잘못 입력하였기때문에 다시 처음 무한반복문의 처음으로 돌아가서 다시 코드를 실행한다.
    return month, day, mtitle[movieTitle-1], mtime[time-1] #몇월 며칠에 예약을 한건지, 영화 제목, 영화 상영시간 을 반환한다. 이때 영화 제목과 영화 시간을 -1 해주어 리스트를 출력하는 이유는
    #리스트는 0부터 시작하는 성질을갖기때문에 그냥 movieTitle을 할 경우 리스트의 n원소가 아니라 n+1의 원소가 되어버리기 때문에 -1을 해준다.
   
def snack(): #간식을 구매하는 함수
    print("구매할 간식을 선택해 주세요") #구매할 간식을 선택하라는 안내 메시지 출력
    while True: #잘못 입력할 경우 다시 입력을 요구하기 위하여 무한 반복문을 사용한다.
        print("1. 팝콘(m)+탄산(m) 6,000원  2. 팝콘(L)+탄산2(m) 10,000원  3. 핫도그+탄산(m) 7,000원") #간식의 종류 출력
        ans=int(input()) #답변 입력받기
        if ans==1: #만약 대답이 1이라면 아래 코드 실행
            print("팝콘의 맛을 골라주세요") #팝콘의 맛을 골라달라는 안내 문구 출력
            print("1.오리지널  2.달콤(+1000) 3.치즈(+1000) 4.어니언(+1000)") #팝콘의 맛에 대하여 출력
            taste=int(input()) #맛을 입력받는 대답 입력받기
            if taste==1: #만약 입력받은 값이 1 이라면 아래 코드 출력
                total = 6000 #추가되는 가격이 없으므로 값에 6000저장
                break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
            elif taste<=4 and taste >= 2 : #만약 입력받은 대답이 2와 4 사이의 수라면 아래 코드 실행
                total = 7000 #2와 4 사이의 값은 1000이 추가 되기때문에 값에 7000저장
                break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
            else: #만약 1과 4 사이의 값이 아니라면 아래코드 실행
                print("잘못 입력하셨습니다.") #잘못 입력했다는 안내 메시지 출력
            continue #잘못 입력하였기때문에 다시 처음 무한반복문의 처음으로 돌아가서 다시 코드를 실행한다.
        elif ans==2: #만약 간식의 종류에 대한 대답이 2라면 아래코드 실행
            print("팝콘의 맛을 골라주세요") #팝콘의 맛을 골라달라는 안내 문구 출력
            print("1.오리지널  2.달콤(+1000) 3.치즈(+1000) 4.어니언(+1000)") #팝콘의 맛에 대하여 출력
            taste=int(input()) #맛을 입력받는 대답 입력받기
            if taste==1: #만약 입력받은 값이 1 이라면 아래 코드 출력
                total = 10000 #추가되는 가격이 없으므로 값에 10000저장
                break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
            elif taste<=4 and taste >= 2 : #만약 입력받은 대답이 2와 4 사이의 수라면 아래 코드 실행
                total = 11000 #2와 4 사이의 값은 1000이 추가 되기때문에 값에 11000저장
                break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
        elif ans == 3: #만약 간식의 종류에 대한 대답이 3이라면 아래코드 실행
            total = 7000 #핫도그와 탄산의 가격이 7000원 이므로 7000저장
            break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
        else :
            print("잘못 입력하셨습니다.") #잘못 입력했다는 안내 메시지 출력
            continue #잘못 입력하였기때문에 다시 처음 무한반복문의 처음으로 돌아가서 다시 코드를 실행한다.
    return total  #반환값으로 구매하려는 간식의 값을 반환한다.

def paymentMethod(): #결제 방식 및 할인혜택을 선택하는 함수
    while True: #잘못 입력할 경우 다시 입력을 요구하기 위하여 무한 반복문을 사용한다.
        print("결제 방식 및 할인 혜택을 선택해주세요") #결제 방식 및 할인 혜택을 선택하라는 안내 메시지
        print("1. 계좌이체  2. 카드결제   3.문화상품권이용") #계좌 이체 카드결제 문화상품권 사용
        card = input() #어떤 결제 방식을 선택할것인지에 대한 입력을 받는다.
        print("할인 방법을 선택해주세요") #할인 방법을 선택하라는 메시지를 출력한다.
        print("1. 통신사 할인 40%  2. 나의 할인쿠폰  3. 할인 선택 안함") #할인방법에 대해 출력한다
        discount = int(input()) #discount변수에 입력을 받는다.
        if discount == 1: #만약 변수의 값이 1 이라면
            discount = 0.6 #할인률은 40% 로 원래 영화 금액에서 0.6을 곱하면 된다.
            break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
        elif discount == 2: #만약 변수의 값이 2라면 다음 코드를 실행한다.
            cupon = int(input("1. 영화 30%할인   2. 매점 2000원 할인 ")) #쿠폰 변수에서 영화를 30%할인을 받을것인지 매점에서 2000원을 할인받을것인지 선택한다
            if cupon == 1: #만약 쿠폰의 값이 1 이라면 아래 코드 실행
                discount =0.7 #할인률은 30% 로 원래 영화 금액에서 0.7을 곱하면 된다.
                break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
            elif cupon == 2: #만약 쿠폰의 값이 2라면 아래 코드 실행
                discount = 2000 #팝콘에서 2000원을 빼주기때문에 변수에 2000을 저장한다.
                break #잘못 입력한 경우 다시 입력을 요구하기 위해 무한반복문을 실행하였는데 위에서 잘 입력했을경우 무한반복문을 종료한다.
            else: #만약 쿠폰 값이 1, 2가 아니라면 아래 코드를 실행한다. 잘못 입력된 값이다.
                print("잘못 입력하셨습니다. 결제 방식선택으로 돌아갑니다.") #잘못 입력했다는 안내 메시지와 결제방식으로 돌아간다는 메시지 출력
        elif discount == 3: #만약 discount변수가 3이라면 할인을 선택하지 않는다 다음 코드를 실행한다.
            discount = 1 #할인은 따로 받지 않기 때문에 원래 영화 금액에서 1을 곱하면 결국 다를게 없다.
            break #잘못 입력하는 경우 다시 입력을 요구하기 위해 무한반복문을 실행하는데 반대로 잘 입력할 경우 무한반복문을 종료하기 위하여 break를 사용한다.
        else: #만약 discount변수가 1,2,3이 아니라면 잘못 입력한 것으로 아래 코드를 실행한다.
            print("잘못 입력하셨습니다.") #잘못 입력했다는 안내 메시지 출력
            continue #잘못 입력하였기때문에 다시 처음 무한반복문의 처음으로 돌아가서 다시 코드를 실행한다.
    return discount #반환값으로 disount를 반환한다.
    

while True: #잘못 입력할 경우 다시 입력을 요구하기 위하여 무한 반복문을 사용한다.
    answer = input("영화 예매 프로그램입니다. 좌석을 예약하시겠습니까? (yes/no)") #영화 예매를 할것인지에 대하여 묻는 메시지를 출력헌다.
    if answer == "YES" or answer == "yes": #만약 위의 대답이 yes이거나 YES일 경우 아래의 코드를 실행한다.
        month, day, movieTitle, time=title() #title함수를 호출하고 함수의 리턴값을 차례대로 month, day, movieTitle, time에 저장한다.
        print("예약할 인원수를 입력하세요") #예약할 인원수를 입력하라는 메시지를 출력한다.
        person= int(input()) #person에 예약할 인원수를 입력 받는다 이때 정수형으로 입력 받도록 한다.
        totalPay, stop = inputSeat(person) #inputSeat함수를 i값과 person을 넣으면서 함수의 반환값은 totalPay와 stop에 저장한다.
        if stop == 0: #만약 stop의 값이 0이라면 아래 코드를 실행한다.
            print("예약을 취소합니다.") #예약을 취소하겠다는 메시지를 출력한다.
            break #예약을 취소하기 때문에 무한반복문을 탈출한다.
        popAns = input("팝콘이나 핫도그를 드시겠습니까? (yes/no)") #팝콘이나 핫도그를 먹을것인지에 대해 입력 받는다.
        if popAns == "y"or popAns=="yes": #위에서 받은 입력값이 y이거나 yes일 경우 아래 코드를 실행한다.
            pop=snack() #snack함수를 호출하고 반환값을 pop에 저장한다. 
        else: #만약 popAns가 y이거나 yes가 아니라면 아래 코드를 실행한다.
            pop=0 #간식을 먹는것이 아니기 때문에 pop에 0을 저장한다.
        print("예약하신 영화는", movieTitle, month,"월", day,"일",time,"입니다.") #예약한 영화의 제목, 보려는 날짜, 시간 을 다시 확인하게끔 출력해준다.
        check = input("예약을 취소하시겠습니까? 계속 진행하시려면 0 취소하려면 1을 처음부터 예약하시려면 2를 입력하세요.") #예약을 취소할것인지, 계속 진행할것인지, 처음부터 예약할것인지에 대해 선택받는다.
        if check == "1": #1을 입력할 경우 아래의 코드를 실행한다.
            print("예약을 취소합니다.") #예약을 취소한다는 안내 메시지를 출력한다.
            break #예약을 취소하기 때문에 무한 반복문을 종료하고 프로그램을 종료한다.
        elif check =="2": #2를 입력할경우 처음부터 돌아가야하는 코드이다 2를 입력하면 아래의 코드를 실행한다.
            seat[selectRow-1][selectCol-1]=0 #정했던 좌석을 0으로 만드는 코드 이다.
            print("예약을 다시 진행합니다") #예약을 다시 진행한다는 메시지를 출력한다.
            continue #예약을 처음부터 진행하고 싶다고 입력받았기 때문에 처음 무한반복문의 처음으로 돌아가서 다시 코드를 실행한다.
        discount = paymentMethod() #pymentMethod함수를 실행하고 반환값을 discount에 저장한다.
        if discount <=1: #discount가 1 이하의 값이라면 아래 코드를 실행한다.
            print("영화금액:",int(totalPay*discount)," 간식 금액: ",int(pop)," 총 금액:", int(totalPay*discount)+int(pop)) #discount의 값이 1보다 작다면 영화를 할인 받는것이기 때문에 할인받은 영화금액, 간식금액, 총금액을 출력한다.
        elif discount > 1 and pop != 0: #만약 discount가 1보다 크고 pop값이 0이 아니라면 아래 코드를 실행한다.
            print("영화금액:",int(totalPay)," 간식 금액: ",int(pop-discount)," 총 금액:", int(totalPay)+int(pop-discount)) #discount의 값이 1보다 크다면 매점 할인을 받느것 이기 때문에 영화금액, 할인받은 간신금액, 총금액을 출력한다.
        else: #위의 조건이 만족하지 않다면 간식을 먹지 않는데 간식 할인을 받은것이다. 아래 코드를 실행한다.
            print("매점 할인이 적용되지 않습니다.") #매점 할인이 적용되지 않는다고 메시지를 출력한다.
            print("영화금액:",int(totalPay)," 간식 금액: ",int(pop)," 총 금액:", (int(totalPay)+int(pop))) #영화금액, 간식금액, 총 금액을 출력한다.
        print("예약이 완료 되었습니다. 감사합니다.") #예약 완료 안내 메시지 출력
    elif answer == "NO" or answer =="no": #대답이 만약 NO또는 no라면 아래 코드를 실행한다.
        print("예약을 취소합니다.") #예약을 취소한다는 메시지를 출력한다.
        break #예약을 취소하기 때문에 무한반복문을 끝내고 프로그램또한 종료 시킨다.
    else: #만약 대답이 YES, NO가 아니라면 아래 코드를 실행한다
        print("다시 입력하세요") #다시 입력하라는 메시지를 출력한다.
        continue #잘못 입력하였기때문에 다시 처음 무한반복문의 처음으로 돌아가서 다시 코드를 실행한다.