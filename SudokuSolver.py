def main():
  GenerateVariables()
  initInputSudo()
  SudoSolver()
def initInputSudo():
  sudo=[[0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 3,  0, 8, 5],
        [0, 0, 1,  0, 2, 0,  0, 0, 0],

        [0, 0, 0,  5, 0, 7,  0, 0, 0],
        [0, 0, 4,  0, 0, 0,  1, 0, 0],
        [0, 9, 0,  0, 0, 0,  0, 0, 0],

        [5, 0, 0,  0, 0, 0,  0, 7, 3],
        [0, 0, 2,  0, 1, 0,  0, 0, 0],
        [0, 0, 0,  0, 4, 0,  0, 0, 9]]
  for row in range(1, 10):
    for col in range(1, 10):
      if sudo[row-1][col-1] is not 0:
        print( "ASSERT(V" + str(row)+str(col)+str(sudo[row-1][col-1]) + ");")
def GenerateVariables():
  allVars = []
  for i in range(1, 10):
    for j in range(1, 10):
      possibleVariables = ["V"+str(i)+str(j)+str(d) for d in range(1, 10)]
      allVars += possibleVariables
  print(",".join(map(str, allVars)), end=" : BOOLEAN;\n")
def SudoSolver():
  for i in range(1, 10):
    validVerti([(i, j) for j in range(1, 10)])
    validHori([(j, i) for j in range(1, 10)])
    if (i+2)%3 == 0:
      for j in range(1, 10):
        if (j+2)%3 == 0:
          validBox(i, j)
  onePerCell()
def valid9cells(cells):
  for cell in cells:
    for var in cell:
      return
def validVerti(cells):
  for i, j in cells:
    for h in range (1, 10):
      for k in range(1, 10):
        if j is not k:
          print("ASSERT((V"+str(j)+str(i)+str(h)+" XOR V"+\
	          	str(k)+str(i)+str(h)+") OR " + \
	            "(NOT(V" + str(j)+str(i)+str(h) + \
            	") AND NOT(V" + str(k)+str(i)+str(h)+")));")
def validHori(cells):
  for i, j in cells:
    for h in range(1, 10):
      for k in range(1, 10):
        if j is not k:
          print("ASSERT((V"+str(i)+str(j)+str(h)+" XOR V"+\
          	str(i)+str(k)+str(h)+") OR " + "(NOT(V" + \
            str(i)+str(j)+str(h) + ") AND NOT(V" + \
            str(i)+str(k)+str(h)+")));")

def validBox(i, j):
  for d in range (1, 10):
    for a in range(3):
      for b in range(3):
        for c in range(3):
          for e in range(3):
            if not(a is c and b is e):
              print( "ASSERT((V"+str(i+a)+str(j+b)+str(d)+\
	              	" XOR "+"V"+str(i+c)+str(j+e)+str(d)+") OR "+\
	                "(NOT(V" + str(i+a)+str(j+b)+str(d) + \
                	") AND NOT(V" + str(i+c)+str(j+e)+str(d)+")));")
def onePerCell():
  for i in range(1, 10):
    for j in range(1, 10):
      total =""
      for k in range(1, 10):
        total += "V"+str(i)+str(j)+str(k)
        if k < 9:
          total+=" OR "
        for h in range(1, 10):
          if k is not h:
            print("ASSERT(V"+str(i)+str(j)+str(k)+" => NOT(V"+\
             str(i)+str(j)+str(h)+"));");
      print("ASSERT("+ total +");")
if __name__ == "__main__":
    main()