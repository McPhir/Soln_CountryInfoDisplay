def openfile():
  f = open('countries.csv')
  return f

def displayinfo_1():
  global infofile
  lines = infofile.readlines()
  print(lines)

def getregions():
  """this reads the csv file and generates a list of the regions - with no duplicates"""
  regions = []
  #lines = infofile.readlines()
  for line in lines:
    list_lines = line.split(',')
    region = list_lines[1]
    if region in regions:
      #do nothing
      pass
    else:
      regions.append(region)
  for r in regions:
    print(r)
  return regions



def displayinfo_2():
  global infofile
  #lines = infofile.readlines()
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

def displayinfo(region):
  global infofile
  #lines = infofile.readlines()
  #print heading first as they are strings
  list_line = lines[0].split(',')
  """Country,Region,Population,Area (sq. mi.),Pop. Density (per sq. mi.),Phones (per 1000)"""
  print(list_line[0].strip().ljust(20,' '),
  list_line[1].strip().ljust(20,' '),
  list_line[2].strip().ljust(15,' '),
  str(list_line[3]).strip().ljust(15,' '),
  str(list_line[10]).strip().ljust(10,' ') )

  for i in range(1,len(lines)):
    list_line = lines[i].split(',')
    """Country,Region,Population,Area (sq. mi.),Pop. Density (per sq. mi.),Phones (per 1000)"""
    if region.strip().lower() == list_line[1].strip().lower() :
      print(list_line[0].strip().ljust(20,' '),
      list_line[1].strip().ljust(20,' '),
      "{:,}".format(int(list_line[2])).strip().ljust(15),
      "{:,}".format(int(list_line[3])).strip().ljust(15),
      list_line[10].strip().ljust(10) )
    #print(i,': ',lines[i],)

infofile = openfile()
lines = infofile.readlines()
regions = getregions()
#displayinfo()
int_region = 0
while int_region != -1:
  print('Select region. Use its number')
  for i in range(1,len(regions)):
    print(i,regions[i])
  int_region = int(input('Region number: '))
  if 0 < int_region < len(regions):
    user_region = regions[int_region]
    displayinfo(user_region)
  else:
    if int_region != -1:
      print('invalid number')







"""user_region = input("Enter the region\n")
while user_region != "quit" :
  displayinfo(user_region)
  user_region = input("Enter the region\n")"""
