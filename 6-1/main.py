import pymysql
from pymysql.cursors import DictCursor


def insert_table():
    print('正在连接')
    print('...')
    con = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='nilv', password='5514')
    print('连接成功')
    no = int(input('编号：'))
    name = input('名字：')
    loc = input('所在地：')
    try:
        with con.cursor() as cursor:
            result = cursor.execute('insert into tb_dept values (%s, %s, %s)', (no, name, loc))
        if result == 1:
            print('添加成功！')
        con.commit()
    finally:
        con.close()


def delete_tables():
    print('正在连接')
    print('...')
    con = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='nilv', password='5514',
                          autocommit=True)
    print('连接成功')
    no = int(input('编号：'))
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'delete from tb_dept where dno=%s', (no,)
            )
        if result == 1:
            print('删除成功')
    finally:
        con.close()


def update_tables():
    print('正在连接')
    print('...')
    con = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='nilv', password='5514',
                          autocommit=True)
    print('连接成功')
    no = int(input('编号：'))
    name = input('名字：')
    loc = input('所在地：')
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'update tb_dept set dname=(%s),dloc=(%s) where dno=%s', (name, loc, no)
                # 输入中文数据，则需要加上括号，对应到sql语句里边是加单引号
            )
        if result == 1:
            print('更新成功！')
        else:
            print('更新失败')
            print(result)
    finally:
        con.close()


def test_1():
    name = str(input())
    print('%s', (name))


def select_all_table():
    print('正在连接')
    print('...')
    con = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='nilv', password='5514',)
    print('连接成功')
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('\编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])
    finally:
        con.close()


class Emp(object):
    def __init__(self, no, name, job, sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'


def select_table_limit():
    print('正在连接')
    print('...')
    con = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='nilv', password='5514', )
    print('连接成功')
    page = int(input('页码：'))
    size = int(input('大小：'))
    try:
        with con.cursor() as cursor:
            cursor.execute(
                'select eno as no, enmae as name, job, sal from tb_emp limit %s,%s', ((page - 1) * size, size)
            )
        for emp_tuple in cursor.fetchall():
            emp = Emp(*emp_tuple)
            print(emp)
    finally:
        con.close()


def main():
    # update_tables()
    # test_1()
    # insert_table()
     select_all_table()
    # select_table_limit()


if __name__ == '__main__':
    main()