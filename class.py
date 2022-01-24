def countWordsFromFile():
    FileName = input("Enter the file name.")
    NUmberOfWord=0
    File = open(FileName,'r')
    for line in File:
        words = line.split()
        NUmberOfWord=NUmberOfWord+len(words)
    print("NUmberOfWord")
    print(NUmberOfWord)


countWordsFromFile()