import socket
import sys
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# -------------------- CLI FUNCTIONS ------------------------
def run_sender(target_host, target_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (target_host, target_port))
    print(f"[NodeHopper • Sender] Message sent to {target_host}:{target_port}")

def run_node(my_port, next_host, next_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", my_port))
    print(f"[NodeHopper • Node] Listening on port {my_port}, hopping to {next_host}:{next_port}")
    while True:
        data, addr = sock.recvfrom(4096)
        print(f"[NodeHopper • Node] Hop received from {addr}: {data.decode()}")
        sock.sendto(data, (next_host, next_port))
        print("[NodeHopper • Node] Hop forwarded.")

def run_receiver(my_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", my_port))
    print(f"[NodeHopper • Receiver] Waiting for final hop on port {my_port}...")
    while True:
        data, addr = sock.recvfrom(4096)
        print(f"[NodeHopper • Receiver] Final hop received: {data.decode()}")

# -------------------- GUI FUNCTIONS ------------------------
def get_local_ip():
    try:
        temp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp.connect(("8.8.8.8", 80))
        ip = temp.getsockname()[0]
        temp.close()
        return ip
    except:
        return socket.gethostbyname(socket.gethostname())

class NodeHopperGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NodeHopper — GUI Mode")
        self.window.geometry("500x420")

        tk.Label(self.window, text="NodeHopper GUI", font=("Arial", 16, "bold")).pack(pady=10)

        # Mode selection
        tk.Label(self.window, text="Mode:").pack()
        self.mode_var = tk.StringVar(value="sender")
        tk.OptionMenu(self.window, self.mode_var, "sender", "node", "receiver").pack()

        # Inputs
        self.frame_inputs = tk.Frame(self.window)
        self.frame_inputs.pack(pady=10)

        tk.Label(self.frame_inputs, text="My port / Target port:").grid(row=0, column=0)
        self.port_entry = tk.Entry(self.frame_inputs)
        self.port_entry.grid(row=0, column=1)

        tk.Label(self.frame_inputs, text="Target host (optional):").grid(row=1, column=0)
        self.host_entry = tk.Entry(self.frame_inputs)
        self.host_entry.grid(row=1, column=1)

        tk.Label(self.frame_inputs, text="Message / Next port:").grid(row=2, column=0)
        self.msg_entry = tk.Entry(self.frame_inputs, width=30)
        self.msg_entry.grid(row=2, column=1)

        # Output
        self.output = scrolledtext.ScrolledText(self.window, height=10)
        self.output.pack(pady=10)

        # Start button
        tk.Button(self.window, text="Start", command=self.start_mode).pack()

    def log(self, text):
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)

    def start_mode(self):
        mode = self.mode_var.get()
        port = self.port_entry.get()
        host = self.host_entry.get()
        message = self.msg_entry.get()

        if not port or (mode == "sender" and not host):
            messagebox.showerror("Error", "Please fill required fields.")
            return

        port = int(port)

        if mode == "sender":
            run_sender(host, port, message)
            self.log(f"[GUI Sender] Sent to {host}:{port} → {message}")

        elif mode == "receiver":
            local_ip = get_local_ip()
            self.log(f"[Your Local IP] {local_ip}")
            thread = threading.Thread(target=self.gui_receiver, args=(port,), daemon=True)
            thread.start()
            self.log(f"[GUI Receiver] Listening on port {port}")

        elif mode == "node":
            if not host or not message:
                messagebox.showerror("Error", "Node mode requires host and next port.")
                return
            next_port = int(message)
            thread = threading.Thread(target=self.gui_node, args=(port, host, next_port), daemon=True)
            thread.start()
            self.log(f"[GUI Node] Forwarding from {port} to {host}:{next_port}")

    def gui_receiver(self, my_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", my_port))
        while True:
            data, addr = sock.recvfrom(4096)
            self.log(f"[Receiver] {data.decode()}")

    def gui_node(self, my_port, next_host, next_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", my_port))
        while True:
            data, addr = sock.recvfrom(4096)
            self.log(f"[Node] Hop from {addr}: {data.decode()}")
            sock.sendto(data, (next_host, next_port))

# -------------------- MAIN ------------------------
def print_usage():
    print("""
NodeHopper - Multi-hop message system (CLI + GUI)

Usage (CLI):

  Sender mode:
    python nodehopper.py sender <host> <port> <message>

  Node mode:
    python nodehopper.py node <my_port> <next_host> <next_port>

  Receiver mode:
    python nodehopper.py receiver <my_port>

GUI mode:
    python nodehopper.py gui
Or simply run without arguments to launch GUI.
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Launch GUI if no arguments
        app = NodeHopperGUI()
        app.window.mainloop()
    else:
        mode = sys.argv[1]
        if mode == "gui":
            app = NodeHopperGUI()
            app.window.mainloop()
        elif mode == "sender":
            if len(sys.argv) != 5:
                print_usage()
                sys.exit(1)
            run_sender(sys.argv[2], int(sys.argv[3]), sys.argv[4])
        elif mode == "node":
            if len(sys.argv) != 5:
                print_usage()
                sys.exit(1)
            run_node(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]))
        elif mode == "receiver":
            if len(sys.argv) != 3:
                print_usage()
                sys.exit(1)
            run_receiver(int(sys.argv[2]))
        else:
            print("Unknown mode.")
            print_usage()
