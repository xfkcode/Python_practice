count = 0
with open("./word.txt","r",encoding="UTF-8") as f:
    for i,line in enumerate(f.readlines()):
        line = line.strip()
        word = line.split(" ")
        print(f"{word}")
        print(f"第{i+1}行内容>>>{line}")
        count += line.count("itheima")
print(f"word.txt文件'itheima'个数{count}")