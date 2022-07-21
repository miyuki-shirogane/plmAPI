import os
import psycopg2.pool
import configparser


# ================读取db_config.ini文件设置=================
class ReadDB:
    root_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_path, "db_config.ini")
    cf = configparser.ConfigParser()
    cf.read(config_path, encoding='UTF-8')
    host = cf.get("plm", "host")
    port = cf.get("plm", "port")
    db = cf.get("plm", "db")
    user = cf.get("plm", "user")
    password = cf.get("plm", "password")
    conn = psycopg2.connect(
        host=host, port=port, user=user, password=password, dbname=db)
    cur = conn.cursor()

    def select_count_of_bom_is_released_or_not(self, company_id: int, is_released: bool):
        sql = "select count(*) from bom " \
              "where is_deleted is False " \
              "and company_id = " + str(company_id) + \
              "and is_released is " + str(is_released)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def select(self):
        sql = "select * from tenant_company_id where tenant_id = 'b3f71a21-14c5-4146-95a4-0c6f7fbe0e16'"
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return res


if __name__ == '__main__':
    r = ReadDB()
    print(r.select())
    # print(r.select_count_of_bom_is_released_or_not(company_id=11, is_released=True)[0])
