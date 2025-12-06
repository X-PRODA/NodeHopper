==========================================================
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
  3. To make it usable from anywhere:
     - Place `nodehopper.bat` in a folder, e.g., `C:\Users\YourUser\Scripts`
     - Add that folder to the **PATH** environment variable
     - Open a new CMD or PowerShell and type:
       nodehopper

- Linux:
  1. Make the script executable:
     chmod +x nodehopper.sh
  2. Run the script:
     ./nodehopper.sh
  3. Or run directly with Python:
     python3 nodehopper.py
  4. To make it usable from anywhere:
     - Move `nodehopper.sh` to a folder in your PATH, e.g. `/usr/local/bin/`
     - Make sure it’s executable: chmod +x /usr/local/bin/nodehopper
     - Now you can type:
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

Example chain:
---------------
- Node1 → 5001
- Node2 → 5002
- Receiver → 5003

----------------------------------------------------------
🛠 Scripts for Easy GUI Launch:
----------------------------------------------------------
**Windows (.bat):**
-------------------
1. Create a file named `nodehopper.bat` in the project folder (already included).  
2. Content:

   @echo off
   python "%~dp0\nodehopper.py" gui
   pause

3. Double-click or run from CMD:
   nodehopper.bat

**Linux (.sh):**
----------------
1. Create a file named `nodehopper.sh` (already included).  
2. Content:

   #!/bin/bash
   python3 "$(dirname "$0")/nodehopper.py" gui

3. Make it executable:
   chmod +x nodehopper.sh

4. Run:
   ./nodehopper.sh

💡 Tip: Add the script to a folder in PATH to run from anywhere:
   nodehopper

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
- The `.bat` and `.sh` scripts allow launching the GUI with a single command,
  and can be made global by adding them to your PATH.

----------------------------------------------------------
📄 License:
----------------------------------------------------------
This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0).  
You are free to use, modify, and distribute it, as long as proper credit is given.

==========================================================

