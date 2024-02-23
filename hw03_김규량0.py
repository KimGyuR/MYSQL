import pymysql

def create_table(conn, curs):
    try:
        query1 = "drop table if exists customer"

        query2 = """
        create table user_table
		(userID CHAR(8),
		userName VARCHAR(10),
		birthYear INT,
		addr CHAR(2),
		mobile1 CHAR(3),
		mobile2 CHAR(8),
		height smallint,
		mDate DATE,
		constraint id_userID primary key (userID));"""

        query3 = """create table buy_table
		(num INT,
		userID CHAR(8),
		prodName CHAR(6),
		groupName CHAR(4),
		price INT,
		amount SMALLINT,
		constraint nums primary key (num));"""

        curs.execute(query1)
        curs.execute(query2)
        curs.execute(query3)
        conn.commit()
        print('Table 생성 완료')

    except Exception as e:
        print(e)

def insertD(conn, cur):
    sql1 = """insert into user_table (userID, userName, birthYear,
    						addr, mobile1, mobile2, height, mDate)
    						values ('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'),
    						('KJD', '김제동', 1974, '경남', NULL, NULL, 173, '2013-03-03'),
    						('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
    						('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-05-05'),
    						('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
    						('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
    						('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
    						('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-05-05'),
    						('SDY', '신동엽', 1971, '경기', NULL, NULL, 176, '2008-10-10'),
    						('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08');"""

    sql2 = """insert into buy_table (num, userID, prodName, groupName,
						price, amount)
						values (1, 'KHD', '운동화', NULL, 30, 2),
							   (2, 'KHD', '노트북', '전자', 1000, 1),
							   (3, 'KYM', '모니터', '전자', 200, 1),
							   (4, 'PSH', '모니터', '전자', 200, 5),
							   (5, 'KHD', '청바지', '의류', 50, 3),
							   (6, 'PSH', '메모리', '전자', 80, 10),
							   (7, 'KJD', '책', '서적', 15, 5),
							   (8, 'LHJ', '책', '서적', 15, 2),
							   (9, 'LHJ', '청바지', '의류', 50, 1),
							   (10, 'PSH', '운동화', NULL, 30, 2),
							   (11, 'LHJ', '책', '서적', 15, 1),
							   (12, 'PSH', '운동화', NULL, 30, 2);"""

    cur.execute(sql1)
    cur.execute(sql2)
    conn.commit()
    print('데이터 입력 완료')

def no1(conn, cur):
    sql = """select u.userName, b.prodName, u.addr, concat(u.mobile1, u.mobile2) 연락처
from user_table as u inner join buy_table as b
on u.userID = b.userID;"""

    cur.execute(sql)
    print('문제 1번')
    print('-'*30)
    print('userName prodName  addr     연락처')
    print('-' * 30)
    rows = cur.fetchall()
    for row in rows:
        print(row)
def no2(conn, cur):
    sql = """select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1, u.mobile2) 
from user_table u inner join buy_table b
on u.userID = b.userID
where u.userID = 'KYM';"""

    cur.execute(sql)
    print('문제 2번')
    print('-' * 30)
    print('userID userName prodName  addr     연락처')
    print('-' * 30)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def no3(conn, cur):
    sql = """select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1, u.mobile2) 연락처
    from user_table u inner join buy_table b
    on u.userID = b.userID
    order by u.userID;
    """

    cur.execute(sql)
    print('문제 3번')
    print('-' * 30)
    print('userID userName prodName  addr     연락처')
    print('-' * 30)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def no4(conn, cur):
    sql = """select distinct u.userID, u.userName, u.addr
from user_table as u inner join buy_table as b
on u.userID = b.userID
order by u.userID;
"""

    cur.execute(sql)
    print('문제 4번')
    print('-' * 30)
    print('userID  userName addr')
    print('-' * 30)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def no5(conn, cur):
    sql = """
select u.userID, u.userName, u.addr, concat(u.mobile1, u.mobile2) 연락처
from user_table as u inner join buy_table as b
on u.userID = b.userID
where u.addr = '경북' or u.addr = '경남'
order by u.userID;
"""

    cur.execute(sql)
    print('문제 5번')
    print('-' * 30)
    print('userID  userName  addr    연락처')
    print('-' * 30)
    rows = cur.fetchall()
    for row in rows:
        print(row)
def main():
    # 데이터베이스(shoppingmall) 연결
    conn = pymysql.connect(host='localhost', user='root', password='1234',
                           db='shoppingmall', charset='utf8')

    curs = conn.cursor()

    create_table(conn, curs)
    insertD(conn, curs)
    print()
    no1(conn, curs)
    print()
    no2(conn, curs)
    print()
    no3(conn, curs)
    print()
    no4(conn, curs)
    print()
    no5(conn, curs)

    curs.close()
    conn.close()
    print('Database 연결 종료')

main()