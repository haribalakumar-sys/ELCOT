def per(n):
    sum=0
    

    for i in range(1,n):
         if(n%i==0):
             sum=sum+i
# Check AFTER loop ends
    if sum == n:
         print("perfect")
    else:
         print("Not ")

    
n = int(input("Enter the number = "))    
per(n)
    
