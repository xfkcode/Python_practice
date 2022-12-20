with open("./bill.txt","r",encoding="UTF-8") as f1:
    lines = f1.readlines()
with open("./bill.txt.bak","w",encoding="UTF-8") as f2:
    for line in lines:
        line = line.strip()
        if line.split("，")[3]=="正式":
            f2.write(line)
            f2.write("\n")


