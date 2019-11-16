import os

c = 0
for i in range(935):
    try: 
        f = open(f"memes/{i}.jpg", "rb")
    except:
        print(f"The phoot number {i} doesn't exist") 
    byte = f.read(4)
    str_byte = str(byte)[2:-1]

    if 'PNG' in str_byte:
        print(f"The phoot number {i} is a PNG") 
        os.system(f"mv memes/{i}.jpg memes/{i}.png")
        c = c+1

print(f"{c}/942 = {c/942.1}")