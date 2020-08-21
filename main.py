print("#"*10)
articel = ""
print("Please enter Articel:")
while True:
    line = input()
    if line:
        articel += line + '/n'
    else:
        break
print("{\"content\": \""+articel.replace("\\", "\\\\")+"\"}")
print("#"*10)