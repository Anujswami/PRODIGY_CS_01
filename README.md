**Caesar Cipher Encryption and Decryption**


This repository contains a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. It allows users to input a message and a shift value to perform encryption and decryption.

The Caesar Cipher is one of the simplest and most widely known encryption techniques. Named after Julius Caesar, who reportedly used it to protect his private correspondence, this method is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

How It Works


Alphabet Shift:


Each letter in the plaintext is shifted a fixed number of places down the alphabet.


For example, with a shift of 3:


'A' becomes 'D'


'B' becomes 'E'


'C' becomes 'F'


This process continues for all letters in the alphabet.


Modular Arithmetic:



When the shift reaches the end of the alphabet, it wraps around to the beginning.


This is handled using modular arithmetic. For example, with a shift of 3:


'X' becomes 'A'


'Y' becomes 'B'


'Z' becomes 'C'


Encryption:


To encrypt a message, each letter in the plaintext is replaced by the letter that is a fixed number of places down the alphabet.


Non-alphabetic characters (such as spaces, punctuation, and numbers) are not changed.


Decryption:


To decrypt the message, the process is reversed by shifting the letters in the ciphertext back by the same number of places.


For example, if the original shift was 3, the decryption shift will be -3.


Example


Plaintext: HELLO


Shift: 3


Ciphertext: KHOOR


In the example above, each letter in "HELLO" is shifted three places to the right:


'H' -> 'K'


'E' -> 'H'


'L' -> 'O'


'L' -> 'O'


'O' -> 'R'


Applications and Limitations


Applications: Historically used for simple encryption purposes, now more of an educational tool.


Limitations: It is easy to break using frequency analysis since it does not significantly alter the distribution of letters in the ciphertext. Also, with only 25 possible shifts, a brute force attack is trivial.



**Table of Contents**


Features
Getting Started
Usage
Examples

**Features**


Encrypts plaintext using the Caesar Cipher method.
Decrypts ciphertext back to plaintext.
Handles both uppercase and lowercase letters.
Leaves non-alphabetic characters unchanged.


**Getting Started**


Prerequisites
Python 3.x


**Installation**


Clone the repository to your local machine:


git clone https://github.com/Anujswami/PRODIGY_CS_01.git

Navigate to the project directory:


cd PRODIGY_CS_01


**Usage**


The main script is Caesar_Cipher_Encryption_Decryption.py, which contains functions for encryption and decryption.

**Running the Script**


To run the script, use the following command:


python Caesar_Cipher_Encryption_Decryption.py

You will be prompted to choose between encryption and decryption, and then to enter the text you want to process.

**Examples**


Here are some examples of using the Caesar Cipher script:

Example 1: Encrypting

Press 1 for Encryption


Press 2 for Decryption:


1


Enter the text for Encryption: HELLO WORLD


The cipher text is:


:- KHOOR ZRUOG


Example 2: Decrypting


Press 1 for Encryption


Press 2 for Decryption:


2


Enter the text for Decryption: KHOOR ZRUOG


The Plain text is


:- HELLO WORLD
