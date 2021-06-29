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
  #print heading first as they are strings
  list_line = lines[0].split(',')
  """Country,Region,Population,Area (sq. mi.),Pop. Density (per sq. mi.),Phones (per 1000)"""
  print(list_line[0].strip().ljust(20,' '),
  list_line[1].strip().ljust(20,' '),
  list_line[2].strip().ljust(15,' '),
  str(list_line[3]).strip().ljust(15,' '),
  str(list_line[10]).strip().ljust(10,' ') )

  for i in range(1,len(lines),7):
    list_line = lines[i].split(',')
    """Country,Region,Population,Area (sq. mi.),Pop. Density (per sq. mi.),Phones (per 1000)"""
    print(list_line[0].strip().ljust(20,' '),
    list_line[1].strip().ljust(20,' '),
    "{:,}".format(int(list_line[2])).strip().ljust(15),
    "{:,}".format(int(list_line[3])).strip().ljust(15),
    list_line[10].strip().ljust(10) )
    #print(i,': ',lines[i],)

infofile = openfile()
displayinfo()