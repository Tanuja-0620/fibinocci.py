nterms = int(input("n sequence numbers"))
#first two terms
n1,n2 = 0,1
count = 0
#to check if the number of terms is valid 
if nterms <= 0:
  print("Please enter a positive interger")Fibinocci
  elif nterms == 1:
    print("Fibonacci sequence upto " ,nterms,":")
    print(n1)
    else:
      print("Fibinocci sequence:")
      while count < nterms:
        print(n1)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1
        
