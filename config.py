# encoding:utf-8
DIALECT = 'MySQl'
DRIVER = 'MySQLdb'
USERNAME = 'root'
PASSWORD = ''
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo'
SQLALCHEMY_DATABASE_URL = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_ECHO = True
