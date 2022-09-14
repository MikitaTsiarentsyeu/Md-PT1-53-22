while True:
    length = input('Enter the length (must be >35): ')
    if length.isdigit() and int(length) > 35:
        length = int(length)
        break
    else:
        print("Incorerect lenght!")

with open ("text.txt", "r") as f:
    x = 0
    res = ""
    while True:
        f.seek(x)
        s = f.read(length)        
        end1 = s.find("\n")

        if not len(s) == length:
            string = s[0:]
            res = res + "\n" + string
            res = res.replace("\n", "", 1)
            break

        if end1 == -1:

            end = s.rfind(" ")
            string = s[0:end+1]
            y = len(string)

            while True:
                if len(string) < len(s):
                    count = len(s)-len(string)
                    string = string.replace(" ", "  ", count)

                    continue
    
                if len(string) == len(s):
                    break
        
            x = x + y
            res = res + "\n" + string
            
        if not end1 == -1:            
            string = s[0:end1]
            x = x + end1 + 1
            res = res + "\n" + string
           

        
        if s == "":
            break

with open("f_text.txt", 'w') as f:
    f.write(res)

