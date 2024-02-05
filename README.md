# Basic-SMTP-email-client

use standard I/O and socket programming (in any language of your choice), to implement a basic SMTP email client.

Create a program, hw2.c or hw2.py, and a matching Makefile to build the hw2 binary if you are writing code in c or c++.

The program takes a variable number of file names as command line arguments, thus:

./hw2.py hamed.txt tirth.txt test.txt

Each file contains an email to be sent, formatted like a simplified raw email (try ‘view source’ on any email of yours).

From: Busy Beaver <beaver@busy.com>
To: Hamed Rezaei <rezaeih@uwm.edu>
Subject: Give me an A

My program sends email. Thus, I deserve an A.
The parts above the blank line are headers that are interpreted differently for display by an email client, the part below is the email text body.

Your program should deliver the email in each file to its intended recipient, by contacting the recipient’s incoming email server. Which email server to contact depends on the destination address of the email. You may assume there is only one destination address in each email file.

Resolving MX DNS records
You remember that I used some Linux terminal commands to retrieve mail server's name from DNS server when sent an email to myself during the lecture. There are several ways to find the incoming mail server for a given domain, but they all come back to the domain’s MX record in the DNS. There is a function available in most programming languages that allows you to run a command in Linux termianl INSIDE your code (e.g., Python). the function is called: “popen()”. Once you call this function in your code, you can pass your query to it and save the output. For your case, this function runs the command “ host -t MX "domain_name". Please note that you need this step because your program is supposed to read domains from input (i.e., ./hw2.py hamed.txt mrinal.txt test.txt) and therefore, you need to call this function for each input file. This will be the only part of this assignment that you need to consult terminal. 

NOTE: if you are using a Windows machine, you can still call popen() function but you should run a different command: nslookup -q=MX example.com

 

Sending the email
To send the email, your program connects to the receiving server using a network socket. See “man socket” and “man connect” for API specifics. The exchange proceeds by SMTP (https://tools.ietf.org/html/rfc821) (anno 1982). Note that modern email servers generally require addresses to be on the form “Full Name <user@domain>” rather than simply “user@domain”.

Important notes:
1- We use https://getnada.comhttps://getnada.comLinks to an external site. and https://www.zoho.com/mail/https://www.zoho.com/mail/Links to an external site. as our main mail servers for this assignment. Please take a look at their website. You can use any other mail servers of your choice such as UWM's mail server. Since I have an active account at UIC right now (I am teaching Internet Management there), you can try sending me email through UIC's mail server. My email is hrezae2@uic.edu. 

2- I will give you some input files soon. The input files contain a working email address, an email address that doesn't exist, and email address that is wrongly formatted, etc. If you are able to finish your homework early, you can play with your own files until I release the actual input files that will be used for grading your homework. 

3- Some ISPs block raw SMTP requests. Also, some SMTP servers block your requests due to security reasons. If your ISP blocks your request, find a machine on UWM domain or some other domain and connect to that machine and run your code there instead of running your code on your own laptop. There were only 1 or 2 ISPs that did this last semester so I don't anticipate it to become an issue. If the SMTP server blocks your connection due to security issues, simply use a different mail server that doesn't do that. Please note that this homework is only for learning purposes not commercial use.  

Turn-in
If using C, your turn-in consists of two files: hw2.c and Makefile. If you coded in Python, just hw2.py will suffice. We will grade your program by running it with several example email files. If the program does not compile or encounters run-time error, we will not grade it. 
