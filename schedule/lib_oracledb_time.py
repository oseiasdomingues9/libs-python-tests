import oracledb
import time

def connect_to_oracle():
    oracledb.init_oracle_client(lib_dir="C:/oraclexe/instantclient")
    connection = oracledb.connect(user="MVINTEGRA", password="DBAMV", dsn="179.131.8.25:1521/sml")
    return connection

def check_table(connection):
    cursor = connection.cursor()
    
    query = "SELECT * FROM imv_evento_esocial WHERE tp_status = :valor"
    
    cursor.execute(query, valor="E")
    result = cursor.fetchall()
    
    if result:
        print("Registros encontrados:", result)
    else:
        print("Nenhum registro encontrado.")
    
    cursor.close()

def main():
    connection = connect_to_oracle()
    
    try:
        while True:
            check_table(connection)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Processo interrompido.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()
