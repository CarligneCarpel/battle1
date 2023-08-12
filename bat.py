non = input("tanpri, antre nonw : ")
majiskil = ""

premye_let = True
for let in non:
    if premye_let and let.isalpha():
        majiskil += let.upper()
        premye_let = False
    else:
      majiskil += let.lower()

    if let.isspace():
        premye_let = True

print( majiskil )
