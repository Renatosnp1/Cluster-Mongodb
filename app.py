from model.mongodb_connection import Mongodb
from model.performanceTest import *
import threading
import time



route20 = Mongodb('SuperMercadoDasCoisas').mongodbroute20()

route20_con = route20['Products']
print(route20_con.delete_many({}).deleted_count)

for i in range(10):
    dt1 = time.time()
    thread1 = threading.Thread(target=execute_insert_18)
    thread2 = threading.Thread(target=execute_insert_19)
    thread3 = threading.Thread(target=execute_insert_20)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    dt2 = time.time()
    route20_con = route20['logs_teste']

    log = {'log_teste': 'Teste geral', 'rota': '19', 'qtde_lin': 8000000, 'tempo': dt2-dt1}
    route20_con.insert_one(log)
    print('Teste %s' % i)


route20 = Mongodb('SuperMercadoDasCoisas').mongodbroute20()
route20_con = route20['Products']
print(route20_con.delete_many({}).deleted_count)

