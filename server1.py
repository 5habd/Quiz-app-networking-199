import socket
import random
from threading import Thread
server = socket.socket(socket.AF_INET, socket,socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

print("server has staarted... ")

questions=[
    " What is the italian word for PIE?? \n a.Mozerella \n b.Pasty \n c.Patty \n d.Pizza ",
    " Water boils at 212 at which scale?? \n a.fahrenheit \n b.Kelvin \n c.Celcius \n d.Rankine ",
    " Which sea creature has three hearts?? \n a.walrus \n b.seahorse \n c.lionfish \n d.octopus ",
    " How many bones does an adult human have?? \n a.206 \n b.208 \n c.201 \n d.196 "
]

answers=[
'c','a','d','d'
]

def get_random_question_answer(conn):
    random_index=random.randint(0,len(questions)-1)
    random_question=questions[random_index]
    random_answer=answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer



while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print (addr[0] + " connected")