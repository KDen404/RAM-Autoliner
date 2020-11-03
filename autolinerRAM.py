#This script was written by Github User Cybr3
#   https://github.com/Cybr3
#By using this Program i agree not to publish it on a third party


import os

folders = [r"input", r"output"]
diri = "input"

for x in folders:
    if not os.path.exists(x):
        os.makedirs(x)


for filename in os.listdir(diri):
    if filename.endswith(".ram") or filename.endswith(".txt"):
        target = r"output/" + filename
        source = r"input/" + filename

        i = open(source, "r")

        inpf = i.read().split("\n")
        n = 0
        outf = []
        for f in inpf:

            if f.startswith(str(n)):
                outf.append(str(f))

            elif not f.startswith(r"/") and f != "":
                outf.append(str(n) + ' ' + f)
                n += 1

            else:
                outf.append(str(f))

        z = open(target,"a")
        z.write("// This file was rewritten by Defeated's RAM Autoliner\n")
        z.write("// https://github.com/Cybr3\n")
        for line in outf:
            z.write(str(line) + "\n")

        z.close()
