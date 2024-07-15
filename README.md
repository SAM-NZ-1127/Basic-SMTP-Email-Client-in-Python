# Basic SMTP Email Client in Python

This project implements a basic SMTP email client in Python using standard I/O and socket programming. The client can send emails by reading from files formatted as raw emails and contacting the recipient's email server.

## Features

- Reads email details (sender, recipient, subject, body) from text files.
- Resolves recipient's mail server using DNS MX records.
- Connects to mail servers using sockets and SSL for secure communication.
- Sends emails following the SMTP protocol.

## Installation

To run the project, ensure you have Python installed. No additional libraries are required beyond the Python standard library.

## Usage

### Running the Client

You can run the client by executing the `basic_smtp_client.py` script from the command line with the email files as arguments.

```sh
python3 basic_smtp_client.py email1.txt email2.txt
