import sys

if len(sys.argv) == 2:
    try:
        with open(sys.argv[1], "r") as file:
            readfile = file.read()
        print("============WELCOME TO BOOKBOT============")
        print("==========LETS ANALISE YOUR FILE==========")
        print("=================POGNALI==================")
        print()

        words = readfile.split()
        word_count = len(words)

        print(f"Words in file: {word_count}")
        print()

        char_count = {}
        for char in readfile:
            if char.isalnum() or char.isspace():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        for char, count in sorted(char_count.items()):
            if(char != ' ' and char != "\n"):
                print(f"'{char}' : {count}")

        print()
        print("=================DONE=====================")
        print("===========FOR YOUR SERVICE===============")
        print("===============BYE BYE^^==================")

    except Exception:
        print("Please provide arguments as ./main.py [file]")
        exit(1)

else:
    print("Please provide arguments as ./main.py [file]")