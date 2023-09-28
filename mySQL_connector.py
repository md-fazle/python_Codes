import mySQL_connector
from mySQL_connector import Error

def Create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection=mySQL_connector.connect(
            host=host_name
            user=user_name
            passwrd= user_password
        )
        print("Connection to mySQL DB sucesfull")
    except Error as e:
        print(f"the error '{e}' occurred ")
        return connection
connection = Create_connection("localhost","root"," ")