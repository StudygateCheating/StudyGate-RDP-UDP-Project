
UDP Communicatio system setup
-----------------------------
The system constitutes of 4 main algorithm 
control codes:
	
-> cnnctnResolv.py
	- This is an algorithm dedicated to monitor and control
	  rising issues within the signal pkts transmission 
	  channel i.e error detection, retransmission nad 
	  timeouts

-> receiver.py
	- Handles transmitted signal pkts at receiver end
	  through the defined ports of communication
	- Received signals pkts processing and utilizaton

-> transmtnVldt.py
	- This is dedicated for transmission validation checks
	  against pkts redundancy in the transmission channel.
	- If any, they're flagged

-> sender.py
	- This is responsible for signal pkts transmission across
	  the connection channel through the various dedicated ports.

The UDP communication protocol is achieved through the RDT(Reliable Data Transfer) 3.0 by executing the above algorithm codes in the following defined
order.

		transmtnVldt.py -> receiverHndlr.py -> senderHndlr.py

Run the files as follows:

		python2 transmtnVldt.py 1600 1601 1602 1603
			#sets validation check on the defined ports


		python receiver.py 127.0.0.1 1602 127.0.0.1 1601
			#initiate receiver over the local server at the 
			#defined ports "1602" and "1601"


		python sender.py 127.0.0.1 1600 127.0.0.1 1603 file.txt
			#initiate sender over the local server at the 
			#defined ports "1600" and "1603"
