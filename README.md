
                     NodeHopper
         Multi-Hop Messaging System in Python
==========================================================

📌 Description:
NodeHopper is a lightweight, cross-platform Python program that allows you
to send messages through a chain of nodes from a sender to a receiver. 
You can use it via a **Command-Line Interface (CLI)** or a **Graphical Interface (GUI)**.

Messages "hop" from node to node, making it ideal for testing network routing, 
simulations, or simple local messaging between computers.

----------------------------------------------------------
✨ Features:
----------------------------------------------------------
- CLI Mode: sender, node, receiver
- GUI Mode with Tkinter
- Multi-hop message relay through intermediate nodes
- Detects your local IP automatically for receiver mode
- Cross-platform: Windows, Linux, MacOS
- Minimal dependencies, easy to set up
- Auto-launch GUI when no arguments are provided

----------------------------------------------------------
💻 Installation:
----------------------------------------------------------
1. Clone the repository:

   git clone https://github.com/yourusername/NodeHopper.git
   cd NodeHopper

2. Make sure you have **Python 3** installed.

3. (Optional) Install Tkinter if not included:

   # Debian/Ubuntu
   sudo apt install python3-tk

----------------------------------------------------------
🚀 Usage:
----------------------------------------------------------

GUI Mode (Recommended for beginners):
------------------------------------
- Windows:
  1. Run the GUI directly:
     python nodehopper.py
  2. Or use the included `.bat` script:
     nodehopper.bat
  3. To make it runnable from anywhere:
     - Place `nodehopper.bat` in a folder, e.g., `C:\Users\YourUser\Scripts`
     - Add that folder to the **PATH** environment variable:
       1. Press **Win + R**, type `sysdm.cpl` → Enter  
       2. Go to **Advanced → Environment Variables**  
       3. Under **User variables**, select **Path** → Edit → New  
       4. Add the folder path (e.g., `C:\Users\YourUser\Scripts`)  
       5. Click OK and open a **new CMD** or PowerShell  
     - Now you can run NodeHopper GUI from anywhere:
       nodehopper

- Linux:
  1. Make the script executable:
     chmod +x nodehopper.sh
  2. Move or copy the script to a folder in your PATH, e.g.:
     sudo mv nodehopper.sh /usr/local/bin/nodehopper
  3. Ensure it is executable:
     sudo chmod +x /usr/local/bin/nodehopper
  4. Now you can run it from any folder:
     nodehopper

CLI Mode:
---------
1️⃣ Receiver:
   python nodehopper.py receiver 5003

2️⃣ Node:
   python nodehopper.py node 5001 127.0.0.1 5002

3️⃣ Sender:
   python nodehopper.py sender 127.0.0.1 5001 "Hello from NodeHopper!"

💡 Tip: Use ports between **5000–5999** to avoid conflicts with system services.

----------------------------------------------------------
🌐 How it works:
----------------------------------------------------------
1. Sender sends a message to the first node.
2. Nodes forward the message to the next node in the chain.
3. Receiver gets the final message and displays it.
4. GUI mode shows messages in real time and displays your local IP automatically.

----------------------------------------------------------
📌 Notes:
----------------------------------------------------------
- GUI is simple, lightweight, and shows logs in real-time.
- The receiver automatically detects your local IP so other devices can connect.
- CLI mode is useful for automation, scripting, or headless systems.
- Adding `.bat` or `.sh` to PATH allows launching NodeHopper from any folder.

----------------------------------------------------------
📄 License:
----------------------------------------------------------
This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0).  
You are free to use, modify, and distribute it, as long as proper credit is given.

==========================================================

