# Jane The Ripper

This project is a simple hash-cracker that cracks md5, sha1, or sha256 hashes based off of a wordlist.


## Requirements

* python3


## Installation

Download as a zip file or clone from github
* git clone **_https://github.com/WTCSC/jane-the-ripper-DexterityB.git_**

(_Unzip if neccessary_) and open **jane-the-ripper-DexterityB** in the terminal
* cd **jane-the-ripper-DexterityB**

Run **main.py**, using python3, in the terminal
* python3 **main.py**


## Examples

Basic usage:

```python
def crack(line):
    return hashlib.sha256(line.encode()).hexdigest()
```


Advanced usage:

```python
for line in file:
    hashed_word = crack(line.strip())
            
    if hashed_word in target:
        return_dict.update({hashed_word: line.strip()})
```


Intended flow of the program:
1. The program asks for the path to the hashes file and then the wordlist file
2. The program asks for the what hash you're cracking
3. The program outputs the list of hashes in the hash file followed by what word the hash is or **[Failed]** if it couldn't find one


## Contributing

* Add more hash types
* Use pull requests


## Testing

* Use pytest -s in the directory in the terminal in order to test that the hash cracking function works
* After going through the program once the terminal should show what tests it was able to pass
* You can also run the code using python3, and go through the program to make sure it works properly, meaning:
 * The calculator asks for the file paths, with error handling
 * The calculator asks what hash you're doing, with error handling
 * The calculator properly cracks whichever hashes correspond to words in the wordlist
* Don't push if there are errors


## License

This project is not licensed


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d_w3ds2H)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21385848)
