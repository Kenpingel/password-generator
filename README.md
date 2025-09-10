# Password Generator

## Short description of the project.
the Password Generator is a command line program that when ran, will return a password based off of a few parameters given. 
It will be able to return to you a secure password that you can use for any external programs. 

## Installation / Setup
no external dependencies currently

## How to Run
```bash
python main.py
```

## Features / Roadmap
- [x] basic password generation
    - [ ] length parameter
    - [ ] option to include numbers
    - [ ] option to include symbols
- [ ] option for password to be more memorable
- [ ] option for saving to file
- [ ] update to use Curses library to have a nicer format in the CLI
- [ ] potentially make a web based version

## Lessons Learned
When generating random things that require security such as passwords, using the secrets library is superior to using the random library.
This is because secrets number generation is based on OS-provided sources of randomness such as hardware level noise or other unpredicable events.
Whereas random uses a seed that could be replicated through brute force or other methods.
