# -*- coding: utf-8 -*-
import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host = 'localhost', user = 'kimjiha', password = '9509', db = 'school', charset='utf8')

# Connection 으로부터 Dictoionary Cursor 생성
# 테이블에 저장된 값을 딕셔너리 형태로 생성해서 저장시킨다.
curs = conn.cursor(pymysql.cursors.DictCursor)
 
 # SQL문 실행
sql = "select * from buyer"
curs.execute(sql)
 
 # 데이타 Fetch
rows = curs.fetchall()

print(rows)
    
conn.close()
