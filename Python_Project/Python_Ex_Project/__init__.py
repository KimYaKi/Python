# -*- coding: utf8 -*-
import pymysql

conn = pymysql.connect(host='localhost', user='kimjiha', password='9509', db='kimjihadb', charset='utf8') 
# mysql에 연결

def insert_SQL():
    
    number = list()
    curs = conn.cursor()
    # 커서를 제어하기 위한 생성자 curs 선언
    
    max = 'select MAX(num) from TEST2'
    # 쿼리문의 select문을 이용해서 최대값을 출력
    curs.execute(max)
    # mysql에 있는 쿼리문에 전송 및 입력
    
    max_num = curs.fetchall()
    # 찾아온 값을 max_num에 저장
    
    num = list(max_num[0])
    # mysql에서 가지고 올 때에는 튜플 형태로 만들어서 수정은 할 수 없으므로
    # list형태로 변환해서 값을 변경 가능하도록 한다.
    
    number.append(num[0]+1)
    # 찾아온 값에서 1을 더한 뒤 number리스트에 입력
    name = input(">>> ")
    number.append(name)
    # 이름을 입력한 뒤 number리스트에 입력
    
    number = tuple(number)
    # 쿼리문을 다시 적을 때에는 list의 형태인 [ ] 형태가 아닌
    # tuple의 형태 ( )의 형태로 입력되어야 하기 때문에 tuple로 형 변환
    
    print(number)
    sql = 'insert into TEST2(num,name) values (%d, \'%s\')' % number
    # 값을 저장하기 위한 insert문
    
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
    

def select_SQL():
    curs = conn.cursor()
    # 값을 
    sql = 'select * from TEST2'
    curs.execute(sql)
    row = curs.fetchall()
    print("-번호-\t-이름-")
    for i in range(len(row)):
        print(' %d\t %s'%(row[i][0],row[i][1]))
    conn.close()

def main_sql():
    print(" <<<< 연동 테스트 >>>>")
    print("어떤 작업을 하시겠습니까?\n1.데이터 입력\n2.데이터 출력")
    user = input(">>>")
    if user == '1':
        insert_SQL()
    elif user =='2':
        select_SQL()
    else:
        print("잘못 입력하였습니다!")


if __name__ == '__main__':
    main_sql()
    