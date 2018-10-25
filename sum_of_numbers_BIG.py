#!python3

# sum_of_numbers_BIG.py

# date; python3.7 sum_of_numbers_BIG.py --max=10000000 -d=NONE; date

import datetime
import getopt
import sys

# DB Solution
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.cursor import MySQLCursorPrepared

#############

global g_cnx

#############
# Fibonacci Series using Dynamic Programming 
def fibonacci(n): 
      
    # Taking 1st two fibonacci nubers as 0 and 1 
    FibArray = [0, 1] 

    while len(FibArray) < n + 1:  
        FibArray.append(0)  
      
    if n <= 1: 
       return n 
    else: 
       if FibArray[n - 1] ==  0: 
           FibArray[n - 1] = fibonacci(n - 1) 
      
       if FibArray[n - 2] ==  0: 
           FibArray[n - 2] = fibonacci(n - 2) 
      
       FibArray[n] = FibArray[n - 2] + FibArray[n - 1] 
    return FibArray[n] 
      
#### print(fibonacci(9)) 


# Python 3 Program to find n'th fibonacci Number in 
# with O(Log n) arithmatic operations 
MAX = 1000
  
# Create an array for memoization 
f = [0] * MAX
  
# Returns n'th fuibonacci number using table f[] 
def fib(n) : 
    # Base cases 
    if (n == 0) : 
        return 0
    if (n == 1 or n == 2) : 
        f[n] = 1
        return (f[n]) 
  
    # If fib(n) is already computed 
    if (f[n]) : 
        return f[n] 
  
    if( n & 1) : 
        k = (n + 1) // 2
    else :  
        k = n // 2
  
    # Applyting above formula [Note value n&1 is 1 
    # if n is odd, else 0. 
    if((n & 1) ) : 
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) 
    else : 
        f[n] = (2*fib(k-1) + fib(k))*fib(k) 
  
    return f[n] 
  
  
# Driver code 
#n = 9
#print(fib(n)) 
  
  
# This code is contributed by Nikita Tiwari.
#############

####
def f_sum_of_num_as_num(p_num):
    sum_of_num = 0
    i=1

    while p_num%(10**i) != p_num:
      sum_of_num += ( p_num%(10**i)-p_num%(10**(i-1)) ) / 10**(i-1)

    return sum_of_num
####

####
####
# Internal Structure
####
def f_sum_of_num(p_num):
    sum_of_num = 0
    i = 0

    for x in str(p_num):
#        print(x)
        sum_of_num += int(x)
#        g_array_of_digits[i] = int(x)
        i+=1
    return sum_of_num
####

####
def f_keep_number_in_array(p_num):
    i = 0

    ## + ##
    g_array_of_digits.clear()
    ##
    for x in str(p_num):
        g_array_of_digits.append(int(x))
        i+=1
    return i
####

####
# by Algorithm, that works for numbers: 
# 1. N=2*k
# 2. N = a2a1a0, a2+a1+a0=2*k
# 2. N = 11*k
#

def f_lookup_number_digits(p_num):
    if ( g_mydb == "MYSQL" ):
        l_cnx = mysql.connector.connect(user='frick', password='frick',
                        host='127.0.0.1',database='numfrick')

    my_str = '0'
    tmp_out = []
    a1 = 0
    a2 = 0
    found_sum = False
    found_digit = True
    sum_of_num = g_array_of_sums[p_num]
    half_sum_of_num = sum_of_num//2

    if p_num%2 == 0:
        a1 = p_num//2
        a2 = a1
        found_sum = True
#        print(p_num, g_array_of_sums[p_num], a1, a2, True)
#        return
# numbers like 11*K
    elif p_num%11 == 0:
        a1 = p_num//11
        a2 = p_num - a1
        found_sum = True
    elif sum_of_num%2 == 1:
        return
    else:
        while half_sum_of_num >= 10:
            sum_of_num = half_sum_of_num

        f_keep_number_in_array(p_num)

        print('\n','TEST', 'p_num', 'half_sum_of_num', 'sum(g_array_of_digits)', 'my_str', 'tmp_out', 'sum(tmp_out)')
        for indx, dgt in enumerate(g_array_of_digits):
            if sum(tmp_out) == half_sum_of_num:
                tmp_out.append(0)
                my_str += '0'
                continue
 
#            if sum(g_array_of_digits[0:indx+1]) > half_sum_of_num:
#                my_str += '0'
#                my_str += str(half_sum_of_num - dgt)
#                tmp_out.append(half_sum_of_num - dgt)
#            if dgt > half_sum_of_num and sum(tmp_out)+dgt< half_sum_of_num:
#                my_str += str(half_sum_of_num)
#                tmp_out.append(half_sum_of_num)
#            else:
            if sum(tmp_out) + dgt <= half_sum_of_num:
                tmp_out.append(dgt)
                my_str += str(dgt)
            else:
                tmp_out.append(half_sum_of_num - sum(tmp_out))
                my_str += str(tmp_out[-1])

            print('TEST', p_num, half_sum_of_num, sum(g_array_of_digits[0:indx+1]), my_str, tmp_out, sum(tmp_out))

#        if len(my_str)>0 and my_str != '0':
#            a1 = int(my_str)
#            a2 = p_num - a1
#        for d in tmp_out:
#            my_str += str(d)

        if len(my_str)>0 and my_str != '0':
            a1 = int(my_str)
            a2 = p_num - a1


    if g_array_of_sums[a1] == g_array_of_sums[a2]:
        found_sum = True
    
    if found_sum:
        print('+', p_num, g_array_of_sums[p_num], a1, a2, found_sum)
    else:
        print('*--->', p_num, g_array_of_sums[p_num], a1, a2, found_sum)
        

        if ( g_mydb == "MYSQL" ):
            if ( not l_cnx.is_connected() ):
                l_cnx = mysql.connector.connect(user='frick', password='frick',
                                    host='127.0.0.1',
                                    database='numfrick')                        
            f_store_data_in_DB(p_num, a1, a2, l_cnx, 1)
            l_cnx.commit()

    return sum_of_num
####

####
# Dynamic Programming
####
def f_DP_sum_of_num(p_max_num):
    for i in range(0, p_max_num):
        g_array_of_sums[i] = f_sum_of_num(i)
    print(datetime.datetime.now(), "f_DP_sum_of_num:: ", "done")
####

####
def f_prepare_table_in_DB(p_DB):
    TABLES = {}
    TABLES['number_data_0'] = (
        """CREATE TABLE `number_data_0` (
            `num` int(11) NOT NULL,
            `a` int(11) NOT NULL,
            `b` int(11) NOT NULL,
            `sum_of_a` int(11) DEFAULT NULL,
            `sum_of_num` int(11) DEFAULT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
    )

    try:
        cursor = p_DB.cursor()
        cursor.execute(TABLES['number_data_0'])

    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
    else:
        print("OK")

####

####
def f_store_data_in_DB(p_num, p_a, p_b, p_DB, p_algo = 0):
    cursor = p_DB.cursor(cursor_class=MySQLCursorPrepared)

    add_number_data = ("INSERT INTO number_data "
                "(num, a, b, sum_of_a, sum_of_num, type_algorithm) "
                "VALUES (%s, %s, %s, %s, %s, %s)")
    data_of_number = (p_num, p_a, p_b, g_array_of_sums[p_a], g_array_of_sums[p_num], p_algo)

    # Insert new employee
    cursor.execute(add_number_data, data_of_number)

    # Make sure data is committed to the database
    #p_DB.commit()

    cursor.close()
####

####
def f_lookup_couple_num(rng):

    l_cnx = mysql.connector.connect(user='frick', password='frick',
                        host='127.0.0.1',
                        database='numfrick')
    f_prepare_table_in_DB(l_cnx)

    for i in rng:
        found_sum = False
        hash_good_num[i]=[]

        if verbose:
            if not i%1000:
                print(datetime.datetime.now(), "f_lookup_couple_num: ", i)
                l_cnx.commit()

        for j in range(1, i//2 + 1):
            if g_array_of_sums[j] == g_array_of_sums[i-j]:
                found_sum = True
                if ( g_mydb == "MYSQL" ):
                    if ( not l_cnx.is_connected() ):
                        l_cnx = mysql.connector.connect(user='frick', password='frick',
                                            host='127.0.0.1',
                                            database='numfrick')                        
                    f_store_data_in_DB(i, j, i-j, l_cnx)

                if not [i-j, j] in hash_good_num[i]:
                    hash_good_num[i].append([j, i-j])
                    hash_good_num[i].append(g_array_of_sums[j])
    #            print("%d:: %d %d:: %d" % (i, j, i-j, f_sum_of_num(j)) )
    #            fout.write(i + " " + j + "," + i-j + "" + f_sum_of_num(j))
    ##            arr_sum_of_num[f_sum_of_num(j)] += 1
    ##            arr_good_num[i] += 1
        
        if not found_sum:
            hash_bad_num.append(i)
            f_store_data_in_DB(i, 0, 0, l_cnx)

    l_cnx.commit()
    if ( l_cnx.is_connected() ):
        l_cnx.close()
    
    print(hash_bad_num)

# EOF f_lookup_couple_num
####

####
def f_lookup_alone_num(rng):
    global hash_good_num
    global hash_bad_num

    for i in rng:
        if not i%1000:
            print("f_lookup_alone_num: ",i)
    
        found_sum = False
        for j in range(1, i // 2 + 1):
#            print("f_lookup_alone_num: ",i, j)
#            if f_sum_of_num(j) == f_sum_of_num(i-j):
            if g_array_of_sums[j] == g_array_of_sums[i-j]:
                # DP
                found_sum = True
                break
    #            print("%d:: %d %d:: %d" % (i, j, i-j, f_sum_of_num(j)) )
    #            fout.write(i + " " + j + "," + i-j + "" + f_sum_of_num(j))
    ##            arr_sum_of_num[f_sum_of_num(j)] += 1
    ##            arr_good_num[i] += 1
        
        if not found_sum:
            hash_bad_num.append(i)

    print(hash_bad_num)
####

####
def main_calculate(p_max_number_of_couple):
    # 4: hash_good_num = [[a,b], c]
    #max_number_of_couple = 8
    hash_good_num.clear()
    hash_bad_num.clear()
    f_lookup_param_couple_num(range(1,max_num), p_max_number_of_couple)
    print("""***************
* NUMBER OF COUPLES: %s
***************""" % str(p_max_number_of_couple//2))

    for item in hash_good_num:
        if len(hash_good_num[item]) == p_max_number_of_couple:
            print(item,":", hash_good_num[item])

####

####
def f_lookup_param_couple_num(rng, p_max_number_of_couple = 2):
    global hash_good_num

    for i in rng:

        if verbose:
            if not i%100000:
                print(datetime.datetime.now(), "f_lookup_param_couple_num: ", i)

        found_sum = False
        hash_good_num[i]=[]
        for j in range(1, i // 2 + 1):
            if g_array_of_sums[j] == g_array_of_sums[i-j]:
                found_sum = True
                if not [i-j, j] in hash_good_num[i]:
                    hash_good_num[i].append([j, i-j])
                    hash_good_num[i].append(g_array_of_sums[j])

            if len(hash_good_num[i]) > p_max_number_of_couple:
                break
        
        if not found_sum:
            hash_bad_num.append(i)
#####

#####
# GLOBAL VAR
#####
lst = [1, 3, 5, 7, 9, 29, 49, 69, 89, 199, 399, 599, 799, 999, 2999, 4999, 6999, 8999]

# CONFIG VARS
verbose=False
max_num = 1000
#g_mydb = "MYSQL"
g_mydb = "NONE"

# DATA VARS
arr_good_num = [0]*max_num
hash_good_num = {}
hash_bad_num = []
hash_bad_sum = []
found_sum = False
# used to fill it max DP algorithm
g_array_of_sums = {}
g_array_of_digits = []
#####
# MAIN
#####

def main(argv):
    global max_num
    global g_mydb
    global verbose
   
    inputfile = ''
    outputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:m:d:v",["ifile=","ofile=", "max=", "db="])
    except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-v", "--verbose"):
         verbose = True
      elif opt in ("-d", "--db"):
         g_mydb = arg
      elif opt in ("-m", "--max"):
         max_num = int(arg)
      elif opt in ("-o", "--ofile"):
         outputfile = arg

    print("CONFIG:")
    print('Input file is "', inputfile) 
    print('Output file is "', outputfile)
    print('max= "', max_num)
    print('DB= "', g_mydb)
    print("config done.")

    # implementing DP
    f_DP_sum_of_num(max_num)
    #print(g_array_of_sums)
#    f_lookup_alone_num(range(1, max_num))
    f_lookup_number_digits(99)
    f_lookup_number_digits(13)
    f_lookup_number_digits(101)
    f_lookup_number_digits(123)
    f_lookup_number_digits(2033)
    f_lookup_number_digits(2035)
#    f_lookup_number_digits(99998)
#    f_lookup_number_digits(318925)
    return

    for i in range(1, max_num):
        f_lookup_number_digits(i)

    if ( g_mydb == "MYSQL"):
        g_cnx = mysql.connector.connect(user='frick', password='frick',
                                host='127.0.0.1',
                                database='numfrick')
        f_lookup_couple_num(range(1, max_num))
        g_cnx.close()

# EOF MAIN
##########################################
if __name__ == "__main__":
   main(sys.argv[1:])

# implementing DP
#f_DP_sum_of_num(max_num)
#print(g_array_of_sums)
#f_lookup_alone_num(range(1, max_num))

#main_calculate(1*2)
#main_calculate(2*2)
#main_calculate(3*2)
#main_calculate(4*2)
#main_calculate(5*2)
#main_calculate(6*2)
#main_calculate(7*2)
#main_calculate(8*2)
#main_calculate(9*2)
#main_calculate(10*2)
sys.exit(0)



print("""***************
* ALL DATA
***************""")

for item in hash_good_num:
    print(item,":", hash_good_num[item], "couples:",len(hash_good_num[item]) // 2)

exit()


#
# 800 - 
#

hash_good_num = {}
for i in range(10000, 100000, 10000):
    lst.append(i-1)
    print(i-1)

for i in range(100000, 1000001, 100000):
    lst.append(i-1)
    print(i-1)

for i in range(1000000, 10000001, 1000000):
    lst.append(i-1)
    print(i-1)

print(lst)

f_lookup_alone_num(lst)
exit(0)

for i in lst:
    found_sum = False
    hash_good_num[i]=[]
    for j in range(1, i):
        if f_sum_of_num(j) == f_sum_of_num(i-j):
            found_sum = True
            if not [i-j, j] in hash_good_num[i]:
                hash_good_num[i].append([j, i-j])
                hash_good_num[i].append(f_sum_of_num(j))
#            print("%d:: %d %d:: %d" % (i, j, i-j, f_sum_of_num(j)) )
#            fout.write(i + " " + j + "," + i-j + "" + f_sum_of_num(j))
##            arr_sum_of_num[f_sum_of_num(j)] += 1
##            arr_good_num[i] += 1
    
    if not found_sum:
        hash_bad_num.append(i)

print(hash_bad_num)
