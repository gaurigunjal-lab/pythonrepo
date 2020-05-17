#Assignment : 4
#Author : Gauri Gunjal

# Problem statement:1

def orangecap(dict1):
    dict2 = {}
    for k1 in dict1:
        for k2 in dict1[k1]:
            dict2[k2] = dict2.get(k2, 0) + dict1[k1][k2]
    player = max(dict2, key=dict2.get)
    return player, dict2[player]


  
  #Assignment : 4
#Author : Gauri Gunjal

# Problem statement:2

def isZeroPoly(lst):
    if lst == []:
        return True
    else:
        return False


def addpoly(p1, p2):

    if isZeroPoly(p1):
    	if isZeroPoly(p2):
        	return []
          
  
    for i in range(len(p1)):
        for item in p2:
            if p1[i][1] == item[1]:
                p1[i] = ((p1[i][0] + item[0]), p1[i][1])
                p2.remove(item)
    p3 = p1 + p2
    for item in (p3):
        if item[0] == 0:
            p3.remove(item)
    return sorted(p3)


def multpoly(p1, p2):
  
  if isZeroPoly(p1):
    return []

  if isZeroPoly(p2):
    return []


  for i in range(len(p1)-1):
    for item in p2:
      p1[i] = ((p1[i][0] * item[0]), (p1[i][1] + item[1]))
      p2.remove(item)
      return p1

