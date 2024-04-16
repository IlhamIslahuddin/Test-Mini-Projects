def LinearSearch():  
  Item = int(input("pick a number from 1-10 "))
  Itemlist = [4,1,2,3,8,5,6,9,10,7]
  Found = False
  loop = 0
  for i in range (len(Itemlist)):
      if (Itemlist[int(i)]) == (int(Item)):
        print ("found it")
        print ("item number",i + 1,"in the array")
        Found = True
        break
      else:
        loop = loop + 1        
  if Found == False:
    print ("not found")
  print ("number of items in the list:",len(Itemlist))
  print ("number of loops: ",loop)

if __name__ == "__main__":
  LinearSearch()
