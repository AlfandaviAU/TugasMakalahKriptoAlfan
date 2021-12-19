import os
import hashlib
import webbrowser

def deleteFile(path):
    os.remove(path)

def openFile(path):
    webbrowser.open_new(path)

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def convertPdfToBinInsideTxt(pathpdf,pathtxt):
    file = open(pathpdf, 'wb')
    for line in open(pathtxt, 'rb').readlines():
        file.write(line)
    file.close()

def convertBinToPdfInsideTxt(pathpdf,pathtxt):
    file = open(pathtxt, 'wb')
    for line in open(pathpdf, 'rb').readlines():
        file.write(line)
    file.close()

def corrupt(pathpdf):
    f = open("temporary.txt", "x")
    file = open(pathpdf, 'wb')
    for line in open("temporary.txt", 'rb').readlines():
        file.write(line)

    file = open("temporary.txt", 'wb')
    for line in open(pathpdf, 'rb').readlines():
        file.write(line)
    file.write(b"corruptingpayload")
    f.close()
    file.close()
    os.remove("temporary.txt")

def main_interface():
    print("=====================")
    print("DAVI INC FILE MANAGER")
    print("=====================")
    print("1. Open File")
    print("2. Sha256 Check")
    print("3. Close File Manager")
    options = int(input("input : "))
    return options

def main():
    option = main_interface()
    while(option != 3):
        if (option == 1):
            secret_password = "indo1234"
            attempt_flag = False
            filename = str(input("input filename : "))
            for i in range (1,4):
                passwordInput = str(input("input password : "))
                if (passwordInput == secret_password):
                    print("Correct password")
                    print("File hash : "+sha256sum(filename))
                    attempt_flag = True
                    openFile(filename)
                    inp = str(input("press enter to continue : "))
                    break
                else:
                    print("Wrong password pls try again")
            if (attempt_flag == False):
                print("attempt failed exceed 3")
                corrupt(filename)
            break
        if (option == 2):
            source = str(input("source filename : "))
            target = str(input("target filename : "))
            if (sha256sum(source) == sha256sum(target)):
                print("Source and Target are exactly same !")
            else:
                print("Source and Target seems different")
            inp = str(input("press enter to continue : "))
            break
    os.system('cls')
    main()

if __name__ == "__main__":
    main()
