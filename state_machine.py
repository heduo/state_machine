import socket
from graphviz import Digraph
import random

# settings
HOST = "20.28.230.252"
PORT = 65432
MAX_LOOPS = 100

try:
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    s.connect((HOST, PORT))

    error_code = s.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
    if error_code != 0:
        print("Socket failed to connect to the server.")
        exit(1)

    print("<Connection established>")

    # create a new graph
    dot = Digraph()
    # set the initial state to A
    data = "A"
    # add the initial state to the graph
    dot.node(data, shape="circle")

    count = 0
    while True and count < MAX_LOOPS:
        # generate a random action ranging from 1 to 3
        action = str(random.randint(1, 3))
        print(f"Server：{data}")
        print(f"Client: {action}")
        # send the action to the server
        s.sendall(f"{action}\n".encode())
        prev_data = data
        # get the new state from the server
        data = s.recv(1024).decode().strip()[0]
        # add the current state and transition to the graph
        dot.node(data, shape="circle")
        dot.edge(prev_data, data, label=action)
        # check if we have reached the terminal state
        count += 1
        if data == "Z":
            print(f"Server：{data}")
            dot.node(data, shape="circle")
            dot.edge(data, "A", label="")
            # ask the user if they want to continue or exit
            choice = input("Reached Z. Do you want to continue? (y/n): ")
            if choice.lower() == "n":
                break
            else:
                data = "A"
    # render the graph and save it as a PDF
    print(f"<Transition count: {count}. Creating graph 'state_machine.pdf'>")
    dot.render("state_machine", format="pdf")
    print('<state_machine.pdf created. Ending connection.>')
except socket.error as e:
    print(f"Error connecting to server: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    s.close()
