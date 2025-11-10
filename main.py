import hashlib
import time

def crack_passwords(hash_path, wordlist_path, hash_type = "md5"):
    return_dict = {}
    target = []
    with open(hash_path, "r") as file:
        for line in file:
            target.append(line.strip())

    with open(wordlist_path, "r") as file:
        match hash_type:
            case "md5":
                def crack(line):
                    return hashlib.md5(line.encode()).hexdigest()
            case "sha1":
                def crack(line):
                    return hashlib.sha1(line.encode()).hexdigest()
            case "sha256":
                def crack(line):
                    return hashlib.sha256(line.encode()).hexdigest()

        for line in file:
            hashed_word = crack(line.strip())
            
            if hashed_word in target:
                return_dict.update({hashed_word: line.strip()})

    for option in target:
        if option not in return_dict:
            return_dict.update({option: "Failed"})
    
    print(return_dict)
    return return_dict

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
    type("What is the path to the hash file? ", False)
    hash_path = path_handling(input())
    type("What is the path to the wordlist file? ", False)
    wordlist_path = path_handling(input())

    type("What type of hash are you cracking? [md5/sha1/sha256] ", False)
    hash_type = input().lower()
    while hash_type != "md5" and hash_type != "sha1" and hash_type != "sha256":
        type("That wasn't an option, please retype: ", False)
        hash_type = input().lower()

    type("\033[33m------------------- CRACKING HASHES -------------------\033[0m", True)
    cracked_dict = crack_passwords(hash_path, wordlist_path, hash_type)
    for word in cracked_dict:
        if cracked_dict[word] == "Failed":
            print(f"{word} \033[31m[Failed]\033[0m")
        else:
            print(f"{word} = \033[32m[{cracked_dict[word]}]\033[0m")
    type("\033[33m------------------ CRACKING COMPLETE ------------------\033[0m", True)
    return None

main()