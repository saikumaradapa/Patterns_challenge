

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







