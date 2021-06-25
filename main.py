def openfile():
  f = open('countries.csv')
  return f

def displayinfo():
  global infofile
  lines = infofile.readlines()
  print(lines)

infofile = openfile()
displayinfo()

