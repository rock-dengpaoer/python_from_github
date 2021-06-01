import pymysql


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
                'update tb_dept set dname=%s, dloc=%s where dno=%s', (name, loc, no)
            )
        if result == 1:
            print('更新成功！')
        else:
            print('更新失败')
    finally:
        con.close()


def main():
    update_tables()


if __name__ == '__main__':
    main()