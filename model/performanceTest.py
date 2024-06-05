from model.mongodb_connection import Mongodb
from model.products import GerateProduct
import threading
import time


gerateproduct = GerateProduct()

def execute_insert_18():
    for i in range(40):
        lista1 = [gerateproduct.create_product_entry_json() for i in range(200000)]

        route18 = Mongodb('SuperMercadoDasCoisas').mongodbroute18()
        route18_con = route18['Products']
        
        # removendo a crianção coleção para não enviesar o tempo dos insert 
        dt1 = time.time()
        route18_con.insert_many(lista1)
        dt2 = time.time()

        route18_con = route18['logs_teste']
        log = {'log_teste': i, 'rota':18, 'qtde_lin': 200000, 'tempo': dt2-dt1}
        route18_con.insert_one(log)




def execute_insert_19():   
    for i in range(40):
        lista1 = [gerateproduct.create_product_entry_json() for i in range(200000)]

        route19 = Mongodb('SuperMercadoDasCoisas').mongodbroute19()
        route19_con = route19['Products']
        
        # removendo a crianção coleção para não enviesar o tempo dos insert 
        dt1 = time.time()
        route19_con.insert_many(lista1)
        dt2 = time.time()

        route19_con = route19['logs_teste']
        log = {'log_teste': i, 'rota':18, 'qtde_lin': 200000 ,'tempo': dt2-dt1}
        route19_con.insert_one(log)




def execute_insert_20():    
    for i in range(40):
        lista1 = [gerateproduct.create_product_entry_json() for i in range(200000)]

        route20 = Mongodb('SuperMercadoDasCoisas').mongodbroute20()
        route20_con = route20['Products']
        
        # removendo a crianção coleção para não enviesar o tempo dos insert 
        dt1 = time.time()
        route20_con.insert_many(lista1)
        dt2 = time.time()

        route20_con = route20['logs_teste']
        log = {'log_teste': i, 'rota':18, 'qtde_lin': 200000, 'tempo': dt2-dt1}
        route20_con.insert_one(log)
