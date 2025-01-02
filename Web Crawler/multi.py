import time
import threading

#Serve para fazer multi processo ao mesmo tempo, bastantew usado quando se tem um entrada e uma saida

def fazendo_requisicao_web_test():
    print("fazendo requisição...")
    time.sleep(3)
    print("requisição feita")
    
thread_1 = threading.Thread(target=fazendo_requisicao_web_test)
thread_1.start()

thread_2 = threading.Thread(target=fazendo_requisicao_web_test)
thread_2.start()

thread_3 = threading.Thread(target=fazendo_requisicao_web_test)
thread_3.start()