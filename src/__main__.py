from log import LogUtils as log
from db_connection import Connect
from email_service import EmailService as email

def main():
    log("é o frit")
    c = Connect().execute_sql("SELECT count(*) FROM baz_data_locker.DL202302 WHERE reatribucion = 1 AND event_date = '2023-02-01'")
    email("oi teste", f"Eu to criando do zero aqui.\nPode ignorar, rlx.\n{c}").send()
    log("cabou")


if __name__ == '__main__':
    main()
