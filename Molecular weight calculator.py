
molecular_weight = 0
number_element = int(input("Hello \n How many elements do you have in your molecular formula ? "))
molecule = input("What is you first Element ? ")
number_of_atoms = int(input("What is the number of atoms of first element ? "))
if molecule == "H":
     molecular_weight += 1
elif molecule == "He":
        molecular_weight += 4
elif molecule == "Li":
    molecular_weight += 7
elif molecule == "Be":
    molecular_weight += 9
elif molecule == "B":
    molecular_weight += 11
elif molecule == "C":
    molecular_weight += 12
elif molecule == "N":
    molecular_weight += 14
elif molecule == "O":
    molecular_weight += 16
elif molecule == "F":
    molecular_weight += 19
elif molecule == "Ne":
    molecular_weight += 20
elif molecule == "Na":
    molecular_weight += 23
elif molecule == "Mg":
    molecular_weight += 24
elif molecule == "Al":
    molecular_weight += 27
elif molecule == "Si":
    molecular_weight += 28
elif molecule == "P":
    molecular_weight += 31
elif molecule == "S":
    molecular_weight += 32
elif molecule == "Cl":
    molecular_weight += 35
elif molecule == "K":
    molecular_weight += 39
elif molecule == "Ar":
    molecular_weight += 40
elif molecule == "Ca":
    molecular_weight += 40
elif molecule == "Sc":
    molecular_weight += 45
elif molecule == "Ti":
    molecular_weight += 48
elif molecule == "V":
    molecular_weight += 51
elif molecule == "Cr":
    molecular_weight += 52
elif molecule == "Mn":
    molecular_weight += 55
elif molecule == "Fe":
    molecular_weight += 56
elif molecule == "Co":
    molecular_weight += 59 
elif molecule == "Ni":
    molecular_weight += 59
elif molecule == "Cu":
    molecular_weight += 64
elif molecule == "Zn":
    molecular_weight += 65 
elif molecule == "Ga":
    molecular_weight += 70
elif molecule == "Ge":
    molecular_weight += 73
elif molecule == "As":
    molecular_weight += 75
elif molecule == "Se":
    molecular_weight += 79
elif molecule == "Br":
    molecular_weight += 80
elif molecule == "Kr":
    molecular_weight += 84
elif molecule == "Rb":
    molecular_weight += 85
elif molecule == "Sr":
    molecular_weight += 88
elif molecule == "Y":
    molecular_weight += 89
elif molecule == "Zr":
    molecular_weight += 91
elif molecule == "Nb":
    molecular_weight += 93
elif molecule == "Mo":
    molecular_weight += 96
elif molecule == "Tc":
    molecular_weight += 97
elif molecule == "Ru":
    molecular_weight += 101
elif molecule == "Rh":
    molecular_weight += 103
elif molecule == "Pd":
    molecular_weight += 106
elif molecule =="Ag":
    molecular_weight += 108
elif molecule == "Cd":
    molecular_weight += 112
elif molecule == "In":
    molecular_weight += 115
elif molecule == "Sn":
    molecular_weight += 119
elif molecule == "Sb":
    molecular_weight += 122
elif molecule == "Te":
    molecular_weight += 128
elif molecule == "I":
    molecular_weight += 127
elif molecule == "Xe":
    molecular_weight += 131
elif molecule == "Cs":
    molecular_weight += 133
elif molecule == "Ba":
    molecular_weight += 137
elif molecule == "La":
    molecular_weight += 139
elif molecule == "Ce":
    molecular_weight += 140
elif molecule == "Pr":
    molecular_weight += 141
elif molecule == "Nd":
    molecular_weight += 144
elif molecule == "Pm":
    molecular_weight += 145
elif molecule == "Sm":
    molecular_weight += 150
elif molecule == "Eu":
    molecular_weight += 152
elif molecule == "Gd":
    molecular_weight += 157
elif molecule == "Tb":
    molecular_weight += 159
elif molecule == "Dy":
    molecular_weight += 163
elif molecule == "Ho":
    molecular_weight += 165
elif molecule == "Er":
    molecular_weight += 167
elif molecule == "Tm":
    molecular_weight += 169
elif molecule == "Yb":
    molecular_weight += 173
elif molecule == "Lu":
    molecular_weight += 175
elif molecule == "Hf":
    molecular_weight += 178
elif molecule == "Ta":
    molecular_weight += 181
elif molecule == "W":
    molecular_weight += 184
elif molecule == "Re":
    molecular_weight += 186
elif molecule == "Os":
    molecular_weight += 186
elif molecule == "Ir":
    molecular_weight += 192
elif molecule == "Pt":
    molecular_weight += 195
elif molecule == "Au":
    molecular_weight += 197
elif molecule == "Hg":
    molecular_weight += 201
elif molecule == "Tl":
    molecular_weight += 204
elif molecule == "Pb":
    molecular_weight += 207
elif molecule == "Bi":
    molecular_weight += 209
elif molecule == "Po":
    molecular_weight += 209
elif molecule == "At":
    molecular_weight += 210
elif molecule == "Rn":
    molecular_weight += 222
elif molecule == "Fr":
    molecular_weight += 223
elif molecule == "Ra":
    molecular_weight += 226
elif molecule == "Ac":
    molecular_weight += 227
elif molecule == "Th":
    molecular_weight += 232
elif molecule == "Pa":
    molecular_weight += 231
elif molecule == "U":
    molecular_weight += 238
elif molecule == "Np":
    molecular_weight += 237
elif molecule == "Pu":
    molecular_weight += 244
elif molecule == "Am":
    molecular_weight += 243
elif molecule == "Cm":
    molecular_weight += 247
elif molecule == "Bk":
    molecular_weight += 247
elif molecule == "Cf":
    molecular_weight += 251
elif molecule == "Es":
    molecular_weight += 252
elif molecule == "Fm":
    molecular_weight += 257
elif molecule == "Md":
    molecular_weight += 258
elif molecule == "No":
    molecular_weight += 259
elif molecule == "Lr":
    molecular_weight += 262
elif molecule == "Rf":
    molecular_weight += 267
elif molecule == "Db":
    molecular_weight += 270
elif molecule == "Sg":
    molecular_weight += 269
elif molecule == "Bh":
    molecular_weight += 270
elif molecule == "Hs":
    molecular_weight += 270
elif molecule == "Mt":
    molecular_weight += 278
elif molecule == "Ds":
    molecular_weight += 281
elif molecule == "Rg":
    molecular_weight += 281
elif molecule == "Cn":
    molecular_weight += 285
elif molecule == "Nh":
    molecular_weight += 286
elif molecule == "Fl":
    molecular_weight += 289
elif molecule == "Mc":
    molecular_weight += 289
elif molecule == "Lv":
    molecular_weight += 293
elif molecule == "Ts":
    molecular_weight += 293
elif molecule == "Og":
    molecular_weight += 294
molecular_weight *= number_of_atoms
number_element -= 1
print(f"{molecular_weight}")
while number_element != 0:
    molecule_more = input("What is the other element ? ")
    molecular_weigh = 0
    number_of = int(input("What is the number of atoms of element ? "))
    if molecule_more == "H":
        molecular_weigh += 1
    elif molecule_more == "He":
        molecular_weigh += 4
    elif molecule_more == "Li":
        molecular_weigh += 7
    elif molecule_more == "Be":
        molecular_weigh += 9
    elif molecule_more == "B":
        molecular_weigh += 11
    elif molecule_more == "C":
        molecular_weigh += 12
    elif molecule_more == "N":
        molecular_weigh += 14
    elif molecule_more == "O":
        molecular_weigh += 16
    elif molecule_more == "F":
        molecular_weigh += 19
    elif molecule_more == "Ne":
        molecular_weigh += 20
    elif molecule_more == "Na":
        molecular_weigh += 23
    elif molecule_more == "Mg":
        molecular_weigh += 24
    elif molecule_more == "Al":
        molecular_weigh += 27
    elif molecule_more == "Si":
        molecular_weigh += 28
    elif molecule_more == "P":
        molecular_weigh += 31
    elif molecule_more == "S":
        molecular_weigh += 32
    elif molecule_more == "Cl":
        molecular_weigh += 35
    elif molecule_more == "K":
        molecular_weigh += 39
    elif molecule_more == "Ar":
        molecular_weigh += 40
    elif molecule_more == "Ca":
        molecular_weigh += 40
    elif molecule_more == "Sc":
        molecular_weigh += 45
    elif molecule_more == "Ti":
        molecular_weigh += 48
    elif molecule_more == "V":
        molecular_weigh += 51
    elif molecule_more == "Cr":
        molecular_weigh += 52
    elif molecule_more == "Mn":
        molecular_weigh += 55
    elif molecule_more == "Fe":
        molecular_weigh += 56
    elif molecule_more == "Co":
        molecular_weigh += 59 
    elif molecule_more == "Ni":
        molecular_weigh += 59
    elif molecule_more == "Cu":
        molecular_weigh += 64
    elif molecule_more == "Zn":
        molecular_weigh += 65 
    elif molecule_more == "Ga":
        molecular_weigh += 70
    elif molecule_more == "Ge":
        molecular_weigh += 73
    elif molecule_more == "As":
        molecular_weigh += 75
    elif molecule_more == "Se":
        molecular_weigh += 79
    elif molecule_more == "Br":
        molecular_weigh += 80
    elif molecule_more == "Kr":
        molecular_weigh += 84
    elif molecule_more == "Rb":
        molecular_weigh += 85
    elif molecule_more == "Sr":
        molecular_weigh += 88
    elif molecule_more == "Y":
        molecular_weigh += 89
    elif molecule_more == "Zr":
        molecular_weigh += 91
    elif molecule_more == "Nb":
        molecular_weigh += 93
    elif molecule_more == "Mo":
        molecular_weigh += 96
    elif molecule_more == "Tc":
        molecular_weigh += 97
    elif molecule_more == "Ru":
        molecular_weigh += 101
    elif molecule_more == "Rh":
        molecular_weigh += 103
    elif molecule_more == "Pd":
        molecular_weigh += 106
    elif molecule_more =="Ag":
        molecular_weigh += 108
    elif molecule_more == "Cd":
        molecular_weigh += 112
    elif molecule_more == "In":
        molecular_weigh += 115
    elif molecule_more == "Sn":
        molecular_weigh += 119
    elif molecule_more == "Sb":
        molecular_weigh += 122
    elif molecule_more == "Te":
        molecular_weigh += 128
    elif molecule_more == "I":
        molecular_weigh += 127
    elif molecule_more == "Xe":
        molecular_weigh += 131
    elif molecule_more == "Cs":
        molecular_weigh += 133
    elif molecule_more == "Ba":
        molecular_weigh += 137
    elif molecule_more == "La":
        molecular_weigh += 139
    elif molecule_more == "Ce":
        molecular_weigh += 140
    elif molecule_more == "Pr":
        molecular_weigh += 141
    elif molecule_more == "Nd":
        molecular_weigh += 144
    elif molecule_more == "Pm":
        molecular_weigh += 145
    elif molecule_more == "Sm":
        molecular_weigh += 150
    elif molecule_more == "Eu":
        molecular_weigh += 152
    elif molecule_more == "Gd":
        molecular_weigh += 157
    elif molecule_more == "Tb":
        molecular_weigh += 159
    elif molecule_more == "Dy":
        molecular_weigh += 163
    elif molecule_more == "Ho":
        molecular_weigh += 165
    elif molecule_more == "Er":
        molecular_weigh += 167
    elif molecule_more == "Tm":
        molecular_weigh += 169
    elif molecule_more == "Yb":
        molecular_weigh += 173
    elif molecule_more == "Lu":
        molecular_weigh += 175
    elif molecule_more == "Hf":
        molecular_weigh += 178
    elif molecule_more == "Ta":
        molecular_weigh += 181
    elif molecule_more == "W":
        molecular_weigh += 184
    elif molecule_more == "Re":
        molecular_weigh += 186
    elif molecule_more == "Os":
        molecular_weigh += 186
    elif molecule_more == "Ir":
        molecular_weigh += 192
    elif molecule_more == "Pt":
        molecular_weigh += 195
    elif molecule_more == "Au":
        molecular_weigh += 197
    elif molecule_more == "Hg":
        molecular_weigh += 201
    elif molecule_more == "Tl":
        molecular_weigh += 204
    elif molecule_more == "Pb":
        molecular_weigh += 207
    elif molecule_more == "Bi":
        molecular_weigh += 209
    elif molecule_more == "Po":
        molecular_weigh += 209
    elif molecule_more == "At":
        molecular_weigh += 210
    elif molecule_more == "Rn":
        molecular_weigh += 222
    elif molecule_more == "Fr":
        molecular_weigh += 223
    elif molecule_more == "Ra":
        molecular_weigh += 226
    elif molecule_more == "Ac":
        molecular_weigh += 227
    elif molecule_more == "Th":
        molecular_weigh += 232
    elif molecule_more == "Pa":
        molecular_weigh += 231
    elif molecule_more == "U":
        molecular_weigh += 238
    elif molecule_more == "Np":
        molecular_weigh += 237
    elif molecule_more == "Pu":
        molecular_weigh += 244
    elif molecule_more == "Am":
        molecular_weigh += 243
    elif molecule_more == "Cm":
        molecular_weigh += 247
    elif molecule_more == "Bk":
        molecular_weigh += 247
    elif molecule_more == "Cf":
        molecular_weigh += 251
    elif molecule_more == "Es":
        molecular_weigh += 252
    elif molecule_more == "Fm":
        molecular_weigh += 257
    elif molecule_more == "Md":
        molecular_weigh += 258
    elif molecule_more == "No":
        molecular_weigh += 259
    elif molecule_more == "Lr":
        molecular_weigh += 262
    elif molecule_more == "Rf":
        molecular_weigh += 267
    elif molecule_more == "Db":
        molecular_weigh += 270
    elif molecule_more == "Sg":
        molecular_weigh += 269
    elif molecule_more == "Bh":
        molecular_weigh += 270
    elif molecule_more == "Hs":
        molecular_weigh += 270
    elif molecule_more == "Mt":
        molecular_weigh += 278
    elif molecule_more == "Ds":
        molecular_weigh += 281
    elif molecule_more == "Rg":
        molecular_weigh += 281
    elif molecule_more == "Cn":
        molecular_weigh += 285
    elif molecule_more == "Nh":
        molecular_weigh += 286
    elif molecule_more == "Fl":
        molecular_weigh += 289
    elif molecule_more == "Mc":
        molecular_weigh += 289
    elif molecule_more == "Lv":
        molecular_weigh += 293
    elif molecule_more == "Ts":
        molecular_weigh += 293
    elif molecule_more == "Og":
        molecular_weigh += 294
    molecular_weigh *= number_of
    molecular_weight += molecular_weigh
    number_element -= 1
    print(f"{molecular_weight}")
