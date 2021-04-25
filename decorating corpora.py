ncorp = open("new_corp.txt", 'w', encoding="utf-8")
corp = open("corp.txt", 'r', encoding="utf-8")
for line in corp:
    dark = line.replace("This page has been proofread, but needs to be validated. ", "\n")
    dark1 = dark.replace("This page needs to be proofread. ", "\n")
    dark2 = dark1.replace("This page does not need to be proofread. ", "\n")
    if dark2 != "\n":
        ncorp.write(dark)
ncorp.close()
