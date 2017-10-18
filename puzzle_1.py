def purify(a_list):
  temp=[]
  for i in a_list:
    if i%2!=0:
      i=[]
      temp.extend(i)
    else:
      i=i
      temp.append(i)
  return temp

[temp for i in a_list ]

#If the list contains sublist
def purify(a_list):
  temp=[]
  for i in a_list:
      if type(i) is list:
          for item in i:
              if item%2!=0:
                  item=[]
                  temp.extend(item)
              else:
                  item=item
                  temp.append(item)
      else:
        if i%2!=0:
          i=[]
          temp.extend(i)
        else: 
          i=i
          temp.append(i)
  return temp