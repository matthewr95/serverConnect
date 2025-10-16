import os
import sys
import time

serverQuestion = """
Enter the number for the kind of connection you want to establish:
1. Automation Server
2. Cloud Connect Server
3. Forwarder 3
4. Forwarder 4
0. Exit

Option: """

actionQuestion = """
Enter the number for the kind of connection you want to establish:
1. SSH to the server
2. Upload a file to the server
3. Download a file from the server
0. Exit

Option: """


serverChoice = input(serverQuestion)
print("You chose option:",serverChoice)

if serverChoice == "1" or serverChoice == 1:
  server = HOSTNAME1
elif serverChoice == "2" or serverChoice == 2:
  server = HOSTNAME2


actionChoice = input(actionQuestion)
print("You chose option:",actionChoice)

if actionChoice == "1" or actionChoice == 1:
  print("Connecting to "+server)
  cmd = "ssh USERNAME@"+server
  os.system(cmd)
