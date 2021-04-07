
import math
def countRectangles():
    print("Introduce 2 coordinates per line until introducing -99 ")
    
    i=0
    t=0
    while(True):
      
        arr=[]
        #read data until introducting value -99 for the first coordinate
        while(True):
           
            # x-contains the coordinates, x[0]-first coordinate, x[1]-second coordinate
            x = input().split()
            if(int(x[0])==-99):
                break
               
            arr.append(x)
            #t-number of pairs of coordinates
            t=t+1
        #1, 2 or 3 points cannot form a rectangle
        if t<4:
            print(0)
        else:
            #sort the array because we want to have the x[0]s equals coordinate to be consecutive
            arr.sort(key = lambda x : (x[0],x[1]))
            
            dictionary1 = {}

            i = 0
            while i < len(arr):
                #if we have equals x[0]s consecutives, we have to verify if  the pair of x[1]s as a key is in dictionary dictionary1
                if(i+1 < len(arr) and arr[i][0] == arr[i+1][0]):
                    x = (arr[i][1],arr[i+1][1])
                    if(x in dictionary1):
                      
                        #using a dictionary, the key is the pair of x[1]s (ys) for the equals x[0]s consecutives
                        dictionary1[x] += 1
                    else:
                        dictionary1[x] = 1
                    i += 2
                else:
                    i += 1
            result = 0
      
            #elements -  list that contains the values of the keys
            #for example if we have the points A(2,4) B(2,3) D(3,4)E(3,3) =>   dictionary1[4,3]=2, so there can be one rectangle
            elements = list(dictionary1.values())
            for i in range(len(elements)):
                val = ((elements[i]-1)*elements[i])//2
                result += val
            #result - represents the number of rectangles
            return(result)


print("The result is: "+ str(countRectangles()))

#example:
# 1 1
# 1 3
# 2 1
# 2 3
# 3 1
# 3 3
# -99
# 3   (result)