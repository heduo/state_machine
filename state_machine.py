import socket
from graphviz import Digraph
import random

# connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# create a new graph
dot = Digraph()

# set the initial state to A
data = 'A'

# add the initial state to the graph
dot.node(data, shape='circle')

try:
    s.connect(('20.28.230.252', 65432))
    while True:
        # generate a random action
        action = str(random.randint(1, 3))
        print(f"Server：{data}")
        print(f"Client: {action}")
        # send the action to the server
        s.sendall(f"{action}\n".encode())
        prev_data = data
        # get the new state from the server
        data = s.recv(1024).decode().strip()[0]
        # add the current state and transition to the graph
        dot.node(data, shape='circle' if data == 'A' or data == 'Z' else 'circle')
        dot.edge(prev_data, data, label=action)
        # check if we have reached the terminal state
        if data == 'Z':
            print(f"Server：{data}")
            dot.node(data, shape='circle')
            dot.edge(data, 'A', label='')
            break

    # render the graph and save it as a PDF
    dot.render('state_machine', format='pdf')
except socket.error as e:
    print(f'Error connecting to server: {e}')
except Exception as e:
    print(f'Error: {e}')
finally:
    s.close()
