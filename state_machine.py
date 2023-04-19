import socket
from graphviz import Digraph
import random

# create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create a new graph
dot = Digraph()

# set the initial state to A
data = 'A'

# add the initial state to the graph
dot.node(data, shape='circle')

try:
    # connect to the server
    s.connect(('20.28.230.252', 65432))
    
    # loop until we reach the terminal state
    while data != 'Z':
        # generate a random action
        action = str(random.randint(1, 3))
        print(f"Server: {data}")
        print(f"Client: {action}")
        # send the action to the server
        s.sendall(f"{action}\n".encode())
        prev_data = data
        # get the new state from the server
        data = s.recv(1024).decode().strip()[0]
        # add the current state and transition to the graph
        dot.node(data, shape='circle')
        dot.edge(prev_data, data, label=action)
    
    # add the final state to the graph
    dot.node(data, shape='circle')
    dot.edge(data, 'A', label='')
    
    # render the graph and save it as a PDF
    dot.render('state_machine', format='pdf')
    print(f"Server: {data}")
    print(f"Back to Server: A")
    print(f"End!")
except socket.error as e:
    print(f'Error connecting to server: {e}')
except Exception as e:
    print(f'Error: {e}')
finally:
    # close the socket connection
    s.close()
