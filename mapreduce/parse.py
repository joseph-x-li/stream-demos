with open("hold.txt", "r") as f:
    with open("out.txt", "w") as fw:
        fw.write("{\n")
        for row in f:
            idx, *name = row[:-1].split(" ")
            fw.write(f"    {idx}: ")
            hold = " ".join(name)
            fw.write("\"" + hold + "\",")
            fw.write("\n")
        fw.write("}")