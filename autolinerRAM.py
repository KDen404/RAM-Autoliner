# RAM Autoliner
#
# Copyright (c) 2022-2026 KDen404
# https://github.com/KDen404
#
# SPDX-License-Identifier: MIT
#
# This software is provided "as is", without warranty of any kind,
# express or implied. The author shall not be liable for any claim,
# damages, data loss, or other liability arising from the use,
# modification, or distribution of this software.
#
# See the LICENSE file for the full license terms.


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
        z.write("// This file was rewritten by KDen404's RAM Autoliner\n")
        z.write("// https://github.com/KDen404\n")
        for line in outf:
            z.write(str(line) + "\n")

        z.close()
