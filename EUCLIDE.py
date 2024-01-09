import math

def main():
     m = 1260
     n = 340

     a,b = max(a,b), min(a,b)

     while(b != 0):
          a, b = b, a % b
          
          print (a)
    

    
          




if __name__ == '__main__':
    main()