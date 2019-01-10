import pymysql

from Plugins import Result


def parse_it(ip, port, user="root", password="root", timeout=5):
    try:
        conn = pymysql.Connect(host=ip, port=port, user=user, password=password, connect_timeout=timeout)
        cursor = conn.cursor()
        cursor.execute("show databases")
        result = [i[0] for i in cursor.fetchall()]
        info = {"databases": result}
        return Result(ip, port, info=info, success=True)
    except Exception as e:
        print(e)
        return Result(success=False, ip=ip, port=port, info={"failed"})


if __name__ == "__main__":
    print(parse_it("cdb-0u0zpsww.bj.tencentcdb.com", 10011, password="").__dict__)
