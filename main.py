import hashlib
import time

def crack_passwords(hash_path, wordlist_path):
    type("\033[33m------------------- CRACKING HASHES -------------------\033[0m", True)
    return_string = ""
    target = []
    with open(hash_path, "r") as file:
        for line in file:
            target.append(line.strip())

    solved = []
    with open(wordlist_path, "r") as file:
        for line in file:
            word = line.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            if hashed_word in target:
                solved.append(hashed_word)
                return_string += f"{hashed_word} = \033[32m[{word}]\033[0m\n"

    for option in target:
        if option not in solved:
            return_string += f"\033[0m{option} \033[31m[Failed]\033[0m\n"

    return_string += "\033[33m------------------ CRACKING COMPLETE ------------------"
    return return_string

def type(phrase, newline):
    for char in phrase:
        print(char, end = "", flush = True)
        time.sleep(0.02)
    if newline == True:
        print("")
    time.sleep(0.2)
    return None

def path_handling(path):
    while True:
        try:
            with open(path, "r"):
                return path
        except FileNotFoundError:    
            type("File not found", True)
        type("Please retype: ", False); path = input()
    

def main():
    type("What is the path to the hash file? ", False); hash_path = path_handling(input())
    type("What is the path to the wordlist file? ", False); wordlist_path = path_handling(input())

    return print(crack_passwords(hash_path, wordlist_path))

main()