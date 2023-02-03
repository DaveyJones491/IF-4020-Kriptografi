import numpy as np
import re

def choose_cipher():
    print("\n1. Vigenere Cipher\n2. Auto-Key Vigenere Cipher\n3. Extended Vigenere Cipher (Doesn't work)\n4. Affine Cipher\n5. Playfair Cipher\n6. Hill Cipher (Kunci hanya bisa 2x2 atau 3x3)\n0. Exit""")
    cipher = int(input("Choose Cipher : "))
    while (cipher < 0 or cipher > 6) :
        cipher = int(input("Invalid input, Choose Cipher : "))
        print("\n")
    return cipher

def choose_action():
    print("1. Encrypt\n2. Decrypt\n0. Cancel")
    action = int(input("Choose Action : "))
    while (action < 0 or action > 2) :
        action = int(input("Invalid input, Choose Action : "))
        print("\n")
    return action

def vigenere(string, keyword, action):
    if (action == 1) :
        encrypted = [] 
        for i in range(len(string)): 
            x = (ord(string[i]) + ord(keyword[i]) - 194) % 26
            x += ord('a') 
            encrypted.append(chr(x))
        return("" . join(encrypted))
    else :
        decrypted = [] 
        for i in range(len(string)): 
            x = (ord(string[i]) -ord(keyword[i]) + 26) % 26
            x += ord('a') 
            decrypted.append(chr(x)) 
        return("" . join(decrypted))

def generateKeyVig(string, kkey): 
  kkey = list(kkey) 
  if len(string) == len(kkey): 
    return(kkey) 
  else: 
    for i in range(len(string) -len(kkey)): 
      kkey.append(kkey[i % len(kkey)]) 
  return("" . join(kkey)) 

def auto_vigenere(string, keyword, action):
    if (action == 1) :
        encrypted = [] 
        for i in range(len(string)): 
            x = (ord(string[i]) + ord(keyword[i]) - 194) % 26
            x += ord('a') 
            encrypted.append(chr(x))
        return("" . join(encrypted))
    else :
        decrypted = [] 
        for i in range(len(string)): 
            x = (ord(string[i]) -ord(keyword[i]) + 26) % 26
            x += ord('a') 
            decrypted.append(chr(x))
            keyword = keyword + (chr(x)).lower()
        return("" . join(decrypted))

def generateKeyAutoVig(string, kkey): 
  kkey = list(kkey) 
  if len(string) > len(kkey): 
    kkey.append(string)
    return("" . join(kkey))

def affine(string, action):
    prima = int(input("Masukkan bilangan prima : "))
    while ((prima % 2) == 0 or prima == 13 ) :
        prima = int(input("Masukkan bilangan prima : "))
    geser = int(input("Masukkan jumlah pergeseran : "))
    if (action == 1) :
        encrypted = [] 
        for i in range(len(string)): 
            x = (prima * (ord(string[i]) - 97) + geser) % 26
            x += ord('a') 
            encrypted.append(chr(x))
        return("" . join(encrypted))
    else :
        decrypted = [] 
        for i in range(len(string)): 
            x = ((pow(prima, -1, 26)) * ((ord(string[i]) - 97) - geser)) % 26
            x += ord('a') 
            decrypted.append(chr(x))
        return("" . join(decrypted))

def playfair(string, keyword, action):
    keymatrix = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
    alphabet = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    count = 0
    for i in range (len(keyword)):
        if (checkduplicate(keymatrix, keyword[i])):
            keymatrix[count//5][count % 5] = keyword[i]
            count += 1
            
    for i in range (len(alphabet)):
        if (checkduplicate(keymatrix, alphabet[i])):
            keymatrix[count//5][count % 5] = alphabet[i]
            count += 1
    print(keymatrix)
    print(string)
    
    if (action == 1):
        encrypted = [] 
        count = 0
        while (count < len(string)):
            if (len(string) - count == 1):
                temp = check(string[count], "x", keymatrix)
            else :
                temp = check(string[count], string[count+1], keymatrix)
            if (temp[0] == temp[2]):
                count += 2
                x = keymatrix[temp[0]][(temp[1]+1) % 5]
                y = keymatrix[temp[2]][(temp[3]+1) % 5]
                count -= temp[4]
            elif (temp[1] == temp[3]):
                count += 2
                x = keymatrix[temp[0]+1][(temp[1]) % 5]
                y = keymatrix[temp[2]+1][(temp[3]) % 5]
                count -= temp[4]
            else :
                count += 2
                x = keymatrix[temp[0]][(temp[3]) % 5]
                y = keymatrix[temp[2]][(temp[1]) % 5]
                count -= temp[4]
            encrypted.append(x)
            encrypted.append(y)
        return("" . join(encrypted))
    else:
        decrypted = [] 
        count = 0
        while (count < len(string)):
            if (len(string) - count == 1):
                temp = check(string[count], "x", keymatrix)
            else :
                temp = check(string[count], string[count+1], keymatrix)
            if (temp[0] == temp[2]):
                count += 2
                x = keymatrix[temp[0]][(temp[1]-1) % 5]
                y = keymatrix[temp[2]][(temp[3]-1) % 5]
                count -= temp[4]
            elif (temp[1] == temp[3]):
                count += 2
                x = keymatrix[temp[0]-1][(temp[1]) % 5]
                y = keymatrix[temp[2]-1][(temp[3]) % 5]
                count -= temp[4]
            else :
                count += 2
                x = keymatrix[temp[0]][(temp[3]) % 5]
                y = keymatrix[temp[2]][(temp[1]) % 5]
                count -= temp[4]
            decrypted.append(x)
            decrypted.append(y)
        return("" . join(decrypted))
        
            
def check(a,b,list):
    count = 0
    if (a == b):
        b = "x"
        count = 1
    for i in range(5):
        for j in range(5):
            if (a == list[i][j]):
                ra = i
                ca = j
            elif (b == list[i][j]):
                rb = i
                cb = j
    return (ra,ca,rb,cb,count)

def checkduplicate(list, char):
    for i in range(5):
        for j in range(5):
            if (char == list[i][j]):
                return False
    return True

def hill(string, action):
    size = int(input("Masukkan ukuran kunci : "))
    if (size == 2):
        key = [[0,0],[0,0]]
    elif (size == 3):
        key = [[0,0,0],[0,0,0],[0,0,0]]
    else :
        print("Invalid Size")
    for i in range(size):
        for j in range (size):
            key[i][j] = int(input("Masukkan kunci untuk matrix kunci baris " + str(i+1) + " kolom " + str(j+1) + " : "))
    print(key)
    
    number = []
    for i in range(len(string)):
        letter = (ord(string[i]) - 97) % 26
        number.append(letter)
    
    encrypted = [] 
    if (action == 1):
        for i in range(len(string)//size):
            temp = []
            for j in range (size):
                temp.append(number[(i*size)+j])
            result = (np.dot(key,temp)) % 26
            for k in range (size):
                x = result[k]
                x += ord('a')
                encrypted.append(chr(x))
        return("" . join(encrypted))
    else:
        inverse = np.linalg.inv(key)
        for i in range (size):
            for j in range(size):
                inverse[i][j] = inverse[i][j] % 26
        print(inverse)

def main():
    cipher = 1
    done = "NULL"
    while (cipher != 0):
        cipher = choose_cipher()
        if (cipher == 0):
            break
        action = choose_action()
        if (action != 0):
            
            read = int(input('1. Masukkan teks dari file \n2. Input teks manual \nPilih input : '))
            if (read == 1):
                name = input("Masukkan nama file : ")
                f = open(name, "r")
                text = f.read()
            elif (read == 2):
                text = input("Masukkan teks : ")
            etext = (text.lower()).replace(" ", "")
            etext = re.sub(r'[^A-Za-z]', '', etext)
            
            if (cipher == 1):
                key = (input("Insert Key : ")).lower()
                key = re.sub(r'[^A-Za-z]', '', key)
                key = generateKeyVig(etext, key)
                done = vigenere(etext, key, action)
            elif (cipher == 2):
                key = (input("Insert Key : ")).lower()
                key = re.sub(r'[^A-Za-z]', '', key)
                if (action == 1) : 
                    key = generateKeyAutoVig(etext, key)
                done = auto_vigenere(etext, key, action)
            elif (cipher == 4):
                done = affine(etext, action)
            elif (cipher == 5):
                key = (((input("Insert Key : ").replace(" ", "")).lower()).replace("j", ""))
                key = re.sub(r'[^A-Za-z]', '', key)
                print(key)
                done = playfair(etext, key, action)
            elif (cipher == 6):
                done = hill(etext, action)

            if (action == 1):
                print("")
                print("Plainteks : " + text)
                print("Cipherteks : " + done.upper())
                print("Cipherteks dengan spasi : " + (str(" ".join(done[i:i+5] for i in range(0, len(done), 5)))).upper())
                print("")
                with open("ciphertext.txt", "w") as text_file:
                    text_file.write(done.upper())
            else:
                print("")
                print("Cipherteks : " + text)
                print("Plainteks : " + done.upper())
                print("")
main()