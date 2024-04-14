string = "ahmet ankara'ya gidecek bunu ingilizceye çevirir misin"
substring = string[string.find("bunu")+5:string.find("bunu")+16]

print(substring)

if substring.lower() == 'ingilizceye':
    print("Substring 'ingilizceye' ile eşleşiyor.")
else:
    print("Substring 'ingilizceye' ile eşleşmiyor.")
