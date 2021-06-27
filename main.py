def openfile():
  f = open('countries.csv')
  return f

def displayinfo_1():
  global infofile
  lines = infofile.readlines()
  print(lines)

def displayinfo():
  global infofile
  lines = infofile.readlines()
  for i in range(0,len(lines),7):
    list_line = lines[i].split(',')
    """Country,Region,Population,Area (sq. mi.),Pop. Density (per sq. mi.),Phones (per 1000)"""
    print(list_line[0],list_line[1].strip(),list_line[2] ,list_line[3],list_line[10]),
    #print(i,': ',lines[i])

infofile = openfile()
displayinfo()

