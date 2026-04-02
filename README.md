# Hash Cracker (Python)

This is a small project I made to understand how hash cracking works in cybersecurity.

The program takes a hash as input and tries to find the original password. It basically compares hashes of different words until it finds a match.

## Features
- Auto detects hash type (md5, sha1, sha256, sha512)
- Dictionary attack using a wordlist
- Brute force attack (tries combinations)

## Working
First the program checks what type of hash it is based on length. Then depending on the mode selected, it either:
- reads words from a file and checks them, or
- generates combinations and compares hashes

If it finds the correct match, it prints the password.

## Example
Input hash: 5f4dcc3b5aa765d61d8327deb882cf99  
Output: password

## What I learned
- Basics of hashing
- How weak passwords can be cracked
- Difference between brute force and dictionary attack

This project is just for learning purpose.
