# Online Python compiler (interpreter) to run Python online.

def shift_char(ch):
    if ch.isalpha():
        if ch.islower():
            return chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))
        else:
            return chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))
    return ch

def main():
    input_str = input().strip()
    ans = ""

    i = 0
    while i < len(input_str):
        if i + 1 < len(input_str) and input_str[i] == input_str[i + 1]:
            count = 0
            ans += shift_char(input_str[i])
            while i + 1 < len(input_str) and input_str[i] == input_str[i + 1]:
                count += 1
                i += 1
            ans += str(count + 1)
        else:
            ans += shift_char(input_str[i])
        i += 1

    for char in ans:
        print(char, end=" ")

if __name__ == "__main__":
    main()
