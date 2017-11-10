# -*- coding: utf-8 -*-
import pymysql
import random

# MySQL Connection 연결
conn = pymysql.connect(host = 'localhost', user = 'user_name', password = 'user_password', db = 'DB_name', charset='utf8')

# Connection 으로부터 Dictoionary Cursor 생성
# 테이블에 저장된 값을 딕셔너리 형태로 생성해서 저장시킨다.
curs = conn.cursor()

def SQL():
    print('검색할 제조사의 번호를 입력해 주세요')
    print('P0001, P0002, P0003, P0004, P0005')
    data = input(">>>")
    # SQL문 실행
    sql = 'select * from manufacturer where Manu_num = \'%s\'' % data
    curs.execute(sql)
    rows = curs.fetchall()
    print('업체번호\t업체이름\t업체주소\t\t전화번호')
    for i in range(4):
        print(rows[0][i], end = '\t')

def Full_SQL():
    print('모든 정보를 출력해 줍니다.')
    sql = 'select * from manufacturer'
    curs.execute(sql)
    rows = curs.fetchall()
    for i in range(5):
        for j in range(4):
            if 0<=i<=2 and j ==1:
                print(end='       ')
                print(rows[i][j], end = '\t\t')
            else:
                print(rows[i][j], end = '\t')
            
        print()

def buyer_info_SQL():
    print('구매자의 정보를 출력해 줍니다.')
    sql = 'select * from Buyer'
    curs.execute(sql)
    rows = curs.fetchall()
    for a in range(len(rows)):
        print(rows[a])

def insert_SQL(data):
    return 'insert into buyer(Member_number, Name, Address, HP, ID_number, Driver_number) values(%s,%s,%s,%s,%s,%s)' % data

def buyer():
    buyer = ['이름','주소','전화번호','주민번홋','면허번호']
    buyer_info = list()
    max = 'select MAX(Member_number) from Buyer'
    # 쿼리문의 select문을 이용해서 최대값을 출력
    curs.execute(max)
    # mysql에 있는 쿼리문에 전송 및 입력
    
    max_num = curs.fetchall()
    # 찾아온 값을 max_num에 저장
    
    num = list(max_num[0])
    # mysql에서 가지고 올 때에는 튜플 형태로 만들어서 수정은 할 수 없으므로
    # list형태로 변환해서 값을 변경 가능하도록 한다.
    
    buyer_info.append(num[0]+1)
    
    print("  <<인적 사항을 입력해 주세요>>  ")
    for i in range(5):
        print(buyer[i]+' : ', end = '')
        user = input()
        if user == '종료' or user == '':
            print('입력을 종료합니다.')
            exit()
        buyer_info.append(user)   
    buyer_info = tuple(buyer_info)                   
    
    print(buyer_info)
    

    sql = 'insert into buyer(member_number, name, address,hp,id_number,driver_number) values(%d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'%buyer_info

    curs.execute(sql)
    # mysql에 전송 및 입력
    
    print('위의 데이터를 저장 하시겠습니까?\n1.데이터 입력\n2.취소')
    user = input(">>> ")
    # 데이터를 저장할 것인지 물어봄
    
    if user == '1':
        conn.commit()
        print('입력되었습니다!')
        # commit을 하면 값이 저장되고 하지 않으면 저장되지 않는다.
        
    elif user == '2':
        print('취소합니다.')
    else:
        print("잘못 입력하였습니다.")
    conn.close()
    # 연결 종료


    
def CarNumber():
    kor1 = '가 나 다 라 마 바 사 아 자 차 카 타 파 하 고 노 도 로 모 보 소 오 조 초 코 토 포 호'.split()
    kor2 = '거 너 더 러 머 버 서 어 저 처 커 터 퍼 허 구 누 두 루 무 부 수 우 주 추 쿠 투 푸 후'.split()
    kor3 = '그 느 드 르 므 브 스 으 즈 츠 크 트 프 흐 기 니 디 리 미 비 시 이 지 치 키 티 피 히'.split()
    
    kor = kor1 + kor2 + kor3
    
    kor_num = random.shuffle(kor)
    Car_Number = ''
    
    for i in range(7):
        a = str(random.randrange(0,10))
        if i == 2:
            Car_Number += kor[0]
        else:
            Car_Number += a
    
    return Car_Number


def main():
    print('검색을 원하십니까? (1.제조사 출력 / 2.제조사 검색 / 3.차량 주인 기록/ 4.사용자 정보)')
    user = int(input(">>> "))
    
    if user == 1:
        Full_SQL()
    elif user == 2:
        SQL()
    elif user == 3:
        buyer()
    elif user == 4:
        buyer_info_SQL()
    else:
        print('잘못 입력했습니다.')
    
    print(CarNumber())
        
if __name__ == '__main__':
    main()
