
n = 5
------------------------------------------------------------------------------------------------------
"""" pattern 1
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * *
"""



# 1
for i in range(n) :
    for j in range(n) :
        print("* ", end="")
    print("")
# or
for i in range(1, n+1) :
    print("* "*n)


------------------------------------------------------------------------------------------------------
""" pattern 2
* 
* * 
* * * 
* * * * 
* * * * *
"""

for i in range(n) :
    for j in range(i+1) :
        print("* ", end="")
    print()

------------------------------------------------------------------------------------------------------
"""pattern 3 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

# 3
for i in range(n) :
    for j in range(n,i,-1) :
        print("* ",end="")
    print()


------------------------------------------------------------------------------------------------------
"""pattern 4
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
"""

# 4
for i in range(n) :
    print(" "*(n-i-1),end="")
    print("* "*(i+1),end="")
    print()

------------------------------------------------------------------------------------------------------
"""pattern 5 
* 
* * * 
* * * * * 
* * * * * * * 
* * * * * * * * *
"""

# 5
j = 1
for i in range(n) :
    print("* " * j, end="")
    j += 2
    print()

------------------------------------------------------------------------------------------------------
"""pattern 6
    *
   ***
  *****
 *******
*********
 """

# 6
j = 1
for i in range(n) :
    print((" "*(n-i-1)) + "*"*(j),end="")
    # print("*"*(j),end="")
    j +=2
    print()
   
   
------------------------------------------------------------------------------------------------------
"""pattern 7 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""


# 7
for i in range(n) :
    print(( (" ")* (i))  + "* "*(n-i) )

      
------------------------------------------------------------------------------------------------------
"""pattern 8
* 
 * * 
  * * * 
   * * * * 
    * * * * * 
     * * * * * * 
      * * * * * * * 
"""

# 8
for i in range(n, 0, -1) :
    print(( (" ")* (n-i))  + "* "*(n-i+1) )

      
------------------------------------------------------------------------------------------------------
"""pattern 9
       * * * * * * * 
      * * * * * * 
     * * * * * 
    * * * * 
   * * * 
  * * 
 * 
"""
# n = 7
for i in range(n) :
    print(( (" ")* (n-i))  + "* "*(n-i) )

------------------------------------------------------------------------------------------------------
"""pattern 10
* 
 * * 
  * * * 
   * * * * 
    * * * * * 
     * * * * * * 
    * * * * * 
   * * * * 
  * * * 
 * * 
* 
"""


# 10
for i in range(n, 0, -1) :
    print(( (" ")* (n-i))  + "* "*(n-i+1) )
for i in range(n+1) :
    print(( (" ")* (n-i))  + "* "*(n-i+1) )

------------------------------------------------------------------------------------------------------
"""pattern 11
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""

# 11
for i in range(n) :
    print(" "*(n-i-1) + "* "*(i+1))
for i in range(1,n) :
    print(" "*(i) + "* "*(n-i))

------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                               ALPHABETS
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
""" A
  * * *   
*       * 
*       * 
* * * * * 
*       * 
*       * 
*       * 
"""

# A 
for i in range(7) :
    for j in range(5) :
        # if ((j == 0 or j == 4) ) or (i == 0 and j != 0) or ( i == 3 ) :
        if ((j ==0 or j == 4 ) and i != 0) or ((i ==0 or i ==3) and (j > 0 and j < 4)) :
            print("* ", end=" ")
        else :
            print("  ", end=" ")
    print()

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

""" B
*  *  *  *     
*           *  
*           *  
*  *  *  *     
*           *  
*           *  
*  *  *  *  
"""
B
for i in range(7) :
    for j in range(5) :
        # if ((j == 0 or j == 4) ) or (i == 0 and j != 0) or ( i == 3 ) :
        if (i == 0 or i ==3 or i ==6) and (j != 4 )  or j ==0  or (j == 4 and (i != 0 and  i != 3 and i != 6)) :
            print("* ", end=" ")
        else :
            print("  ", end=" ")
            pass
    print()
   
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------


"""pattern C
  * * * * 
*     
*     
*     
*     
*     
 * * * * 
 """
# C
for row in range(7) :
    for col in range(5) :
        if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0)) :
            print("*", end =" ")
        else :
            print("",end=" ")
    print()
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

"""pattern D
*  *  *  *     
*           *  
*           *  
*           *  
*           *  
*           *  
*  *  *  *     
 """
# D
for i in range(7) :
    for j in range(5) :
        if (i == 0 or  i ==6) and (j != 4 )  or j ==0  or (j == 4 and (i != 0  and i != 6)) :
            print("* ", end=" ")
        else :
            print("  ", end=" ")
            pass
    print()
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

"""pattern E
#  #  #  #  #  
#              
#              
#  #  #  #  #  
#              
#              
#  #  #  #  #        
 """

# E
for i in range(7) :
    for j in range(5) :
        if (i == 0 or i == 3 or i ==6 ) or j ==0    :
            print("# ", end=" ")
        else :
            print("  ", end=" ")
            pass
    print()

   
   ------------------------------------------------------------------------------------------------------
   ------------------------------------------------------------------------------------------------------
"""pattern F
?  ?  ?  ?  ?  
?              
?              
?  ?  ?  ?  ?  
?              
?              
?         
"""

F
for i in range(7) :
    for j in range(5) :
        if i == 0 or i == 3   or j ==0     :
            print("? ", end=" ")
        else :
            print("  ", end=" ")
            pass
    print()
   ------------------------------------------------------------------------------------------------------
   ------------------------------------------------------------------------------------------------------
"""pattern H
()          () 
()          () 
()          () 
() () () () () 
()          () 
()          () 
()          ()         
 """

# H
for i in range(7) :
    for j in range(5) :
        if j == 0 or j == 4   or i == 3     :
            print("()", end=" ")
        else :
            print("  ", end=" ")
            pass
    print()

   
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
   
   
"""pattern G

@  @  @  @  @  
@              
@              
@     @  @  @  
@           @  
@           @  
@  @  @  @  @         

 """

# G
for i in range(7) :
    for j in range(5) :
        if j == 0 or i == 6 or i == 0 or (j==4 and i>3) or (i==3 and 1<j<5):
            print("@ ", end=" ")
        else :
            print("  ", end=" ")
            pass
    print()   
   
   
   
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

"""pattern I
:: :: :: :: :: 
      ::       
      ::       
      ::       
      ::       
      ::       
:: :: :: :: ::          
 """

# I
for i in range(7) :
    for j in range(5) :
        if i == 0 or i == 6   or j == 2     :
            print("::", end=" ")
        else :
            print("  ", end=" ")
            pass
    print()

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------



"""pattern J
'' '' '' '' '' 
      ''       
      ''       
      ''       
      ''       
      ''       
'' ''         
 """

# # J
# for i in range(7) :
#     for j in range(5) :
#         if (i == 0  or (j == 2 and i < 6)) or (i == 6 and j <=1  )   :
#             print("\''", end=" ")
#         else :
#             print("  ", end=" ")
#             pass
#     print()
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

"""pattern K
ð          ð  
ð       ð     
ð    ð        
ð ð           
ð    ð        
ð       ð     
ð          ð         
 """

# K
# p = 0
# for i in range(7) :
#     for j in range(5) :
#         if j == 0 or (i == j+2 and j >0)   :
#             print(chr(240), end=" ")
#         elif p+j == 4 and i < 3:
#             print(chr(240), end=" ")
#             p += 1
#         else :
#             print("  ", end=" ")
#             pass
#     print(" ")

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
"""pattern L
||             
||             
||             
||             
||             
||             
|| || || || ||        
 """

# L
# for i in range(7) :
#     for j in range(5) :
#         if j==0 or i == 6 :
#             print("||", end=" ")
#         else :
#             print("  ", end=" ")
#             pass
#     print()

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

"""pattern M
#           #   
#  #     #  #   
#     #     #   
#           #   
#           #   
#           #   
#           #         
 """

# M
# for i in range(7) :
#     for j in range(5) :
#         if (j==0 or j== 4)  :
#             print("# ", end=" ") # chr(196)
#         elif (i == j and i <3)  or (j-i == 2 and 0 < i <3):
#             print("# ", end=" ")
#         else :
#             print("  ", end=" ")
#             pass
#     print(" ")




------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
"""pattern N
%           %   
%           %   
%  %        %   
%     %     %   
%        %  %   
%           %   
%           %         
 """

# N
# for i in range(7) :
#     for j in range(5) :
#         if j==0 or j== 4 or i == j+1:
#             print("% ", end=" ") # chr(196)
#         else :
#             print("  ", end=" ")
#             pass
#     print(" ")

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
"""pattern O
   $$  $$  $$      
$$           $$   
$$           $$   
$$           $$   
$$           $$   
$$           $$   
   $$  $$  $$      
         
 """

# O
# for i in range(7) :
#     for j in range(5) :
#         if (i == 0 or j == 0 or i == 6 or j == 4) and (0 < i < 6 or 0 < j < 4):
#             print("$$ ", end=" ") # chr(196)
#         else :
#             print("  ", end=" ")
#             pass
#     print(" ")

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
"""pattern P
d  d  d  d      
d           d   
d           d   
d  d  d  d      
d               
d               
d     
 """

# P
# for i in range(7):
#     for j in range(5):
#         if j == 0 or (i == 0 and j <4) or (j == 4 and 0<i<3) or (i == 3 and j <4):
#             print(chr(100),"" , end=" ")  # chr(196)
#         else:
#             print("  ", end=" ")
#             pass
#     print(" ")


"""pattern R
**  **  **  **       
**              **   
**              **   
**  **  **  **       
**              **   
**              **   
**              **  
 """

# R
# for i in range(7):
#     for j in range(5):
#         if j == 0 or (i == 0 and j <4) or (j == 4 and 0<i<7 and i != 3) or (i == 3 and j <4):
#             print("** " , end=" ")  # chr(196)
#         else:
#             print("   ", end=" ")
#             pass
#     print(" ")

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------



""" S
   *  *  *     
*              
*              
   *  *  *     
            *  
            *  
   *  *  *    
"""

# S
# for i in range(7) :
#     for j in range(5) :
#         if ((i == 0 or i == 3 or i == 6 ) and (0 < j < 4)) or ((j ==0 and 0<i<3)) or ((j ==4 and 3<i<6))  :
#             print("* ", end=" ")
#         else :
#             print("  ", end=" ")
#     print()


------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------


""" T
[] [] [] [] [] 
      []       
      []       
      []       
      []       
      []       
      []       
"""

# T
for i in range(7) :
    for j in range(5) :
        if i ==0 or j == 2  :
            print("[]", end=" ")
        else :
            print("  ", end=" ")
    print()

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

""" U
{.}          {.} 
{.}          {.} 
{.}          {.} 
{.}          {.} 
{.}          {.} 
{.}          {.} 
   {.} {.} {.}         
"""

# U
# for i in range(7) :
#     for j in range(5) :
#         if ((j == 0 or j == 4) and i < 6) or (i ==6 and 0<j<4) :
#             print("{.}", end=" ")
#         else :
#             print("  ", end=" ")
#     print()

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

""" V
*           *  
*           *  
*           *  
*           *  
*           *  
   *     *     
      *         
"""

# V
for i in range(7) :
    for j in range(5) :
        if ((j ==0 or j == 4) and (i<5)) or (i == j+4) or (i-j == 2 and 4<i<6) :
            print("* ", end=" ")
        else :
            print("  ", end=" ")
    print()

   

   ------------------------------------------------------------------------------------------------------
   ------------------------------------------------------------------------------------------------------
   
     
      
   
   ------------------------------------------------------------------------------------------------------
   ------------------------------------------------------------------------------------------------------
   
   ------------------------------------------------------------------------------------------------------
   
   
   
   
   
   
   
   
   
   
   
     
      
      


# n = 10
# for i in range(n) :
#     print(" "*(n-i-1),end="")
#     print("* "*(i+1),end="")
#     print()
# n = 4
# p = 6
# for i in range(1, n+1) :
#     print(" "*p, end="")
#     print("* "*n)





