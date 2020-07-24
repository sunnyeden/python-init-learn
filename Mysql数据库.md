#### 安装pymysql模块

`
pip install pymysql
`

#### 查询

```python
from pymysql import connect

def main():
    conn = connect(host='127.0.0.1',port=3306,user='root',password='',database='db_www',charset='utf8')

    print(conn)

    # 获取游标
    cursor = conn.cursor()

    # 返回查到的条数
    cursor.execute("select * from hd_config where 1")

    # 取出所有
    print(cursor.fetchall())

    # 取一条
    print(cursor.fetchone())

    # 取多条
    print(cursor.fetchmany(3))

    # 关闭链接
    cursor.close()
    conn.close()

if  __name__ == "__main__":
    main()
```
