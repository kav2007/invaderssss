import math
import cmath
import fractions

# Basic Arithmetic Functions

# Addition
def add(x,y):
    sum = x+y
    return (sum)

# Add multiple numbers
def add_multple(*args):
    list(args)
    sum = 0
    for x in list(args):
        sum += x
    return(sum)

# Subtraction
def subtract(x,y):
    difference = x-y
    return (difference)

# Multiplication
def multiply(x,y):
    product = x*y
    return (product)

# Multiply multiple numbers
def multiply_multiple(*args):
    list(args)  
    product = 1
    for x in list(args):
        product *= x  
    return (product)

# Division
def divide(x,y):
    value = x/y
    return (value)

# Finding remainder on division or Modulus
def remainder(x,y):
    remainder = x%y
    return (remainder)

# Square
def square(x):
    square = x**2
    return (square)

# Cube
def cube(x):
    cube = x**3
    return (cube)

# Exponential
def exponential(x,y):
    value = x**y
    return (value)

# Square Root
def sq_root(x):
    x = math.sqrt(x)
    return (x)

# Cube Root
def cb_root(x):
    cb_root = x**(1/3)
    return (cb_root)

# Any root
def root(x,y):
    root = (x**1/y)
    return (root)

# Percentage
def percentage(x,y):
    percentage = (x/100)*y
    return (percentage)

# Python program to calculate sum of fractions
def fraction_sum(*args):
    num_list =list(args)
    num_list= [fractions.Fraction(i) for i in num_list]
    sum = 0
    for j in num_list:
        sum += j
    return (sum)   

# Python program to calculate difference of fractions
def fraction_difference(*args):
    num_list =list(args)
    num_list= [fractions.Fraction(i) for i in num_list]
    num_list.sort()
    difference = num_list[1] - num_list[0]
    return (difference)

# Python program to calculate multiplication of fractions
def fraction_product(*args):
    num_list =list(args)
    num_list= [fractions.Fraction(i) for i in num_list]
    product = 1
    for j in num_list:
        product *= j
    return (product)      

# Python program to calculate division of fractions
def fraction_divide(*args):
    num_list = list(args)
    num_list= [fractions.Fraction(i) for i in num_list]
    division = num_list[0] / num_list[1]
    return (division)

# Finding the roman equivilant of a number
def number_to_roman(num):
    roman_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_symbol = ["M", "CM","D", "CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman = ""
    i = 0
    while num > 0:
        for _ in range(num // roman_num[i]):
            roman += roman_symbol[i]
            num = num - roman_num[i]
        i += 1
    return(roman)

# Finding the number equivilant of a roman number
def roman_to_number(roman_num):
    roman_symbol_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400,"C": 100, 
                         "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    num = 0
    for i in roman_num:
        for key in roman_symbol_dict:
            if i == key:
                num += roman_symbol_dict[key]
    return(num)

# Finding the value of x in a quadratic equation
def x_in_quadratic(a,b,c):
    x_add = (-(b)+cmath.sqrt((b**2)- (4*a*c)))/(2*a)
    x_minus = (-(b)-cmath.sqrt((b**2)- (4*a*c)))/(2*a)
    return(x_add,x_minus)

# End of basic arithmetic functions


# Area of 2D and 3D shapes, Perimeter of 2D shapes, Volume of 3D shapes

# Area of Square
def area_square(side):
    area_square = (side*side)
    return (area_square)

# Area of Rectangle
def area_rectangle(length,breadth):
    area_rectangle = (length*breadth)
    return (area_rectangle)

# Area of Triangle
def area_triangle(base,height):
    area_triangle = (base*height)/2
    return (area_triangle)

# Area of Equilateral Triangle
def area_equilateral_triangle(side):
    area_equilateral_triangle = (math.sqrt(3)/4)* side * side
    return (area_equilateral_triangle)

# Area of Triangle using Heron's Theorem
def area_heron_triangle(side1,side2,side3):
    s = (side1+side2+side3)/2
    area_heron_triangle = (math.sqrt(s*(s-side1)*(s-side2)*(s-side3)))
    return (area_heron_triangle)

# Area of Parallelogram
def area_parallelogram(base,height):
    area_parallelogram = (base*height)
    return (area_parallelogram)

# Area of Rhombus
def area_rhombus(diagonal1,diagonal2):
    area_rhombus = (diagonal1*diagonal2)/2
    return (area_rhombus)

# Area of Rhombus with parallelogram way
def area_rhombus_parallelogram_way(base,height):
    area_rhombus_parallelogram_way = (base*height)
    return (area_rhombus_parallelogram_way)

# Area of Circle
def area_circle(r):
    area_circle = math.pi * r * r
    return (area_circle)

# Area of Trapezium
def area_trapezium(base1,base2,height):
    area_trapezium = ((base1+base2)/2)*height
    return (area_trapezium)

# Area of Kite
def area_kite(diagonal1,diagonal2):
    area_kite = (diagonal1*diagonal2)/2
    return (area_kite)

# Area of Ellipse
def area_ellipse(axis1,axis2):
    area_ellipse = math.pi * axis1 * axis2
    return (area_ellipse)

# Surface area of Cube
def tsa_cube(edge):
    surface_area_cube = (6*(edge**2))
    return (surface_area_cube)

# Lateral Surface Area of Cube
def lsa_cube(edge):
    lateral_surface_area_cube = (4*(edge**2))
    return (lateral_surface_area_cube)

# Surface Area of Cuboid
def tsa_cuboid(length,breadth,height):
    surface_area_cuboid = 2*((length*breadth)+(length*height)+(breadth*height))
    return (surface_area_cuboid)

# Lateral Surface Area of Cuboid
def lsa_cuboid(length,breadth,height):
    lateral_surface_area_cuboid = 2 * height * (length+breadth)
    return (lateral_surface_area_cuboid)

# Total Surface Area of Cylinder
def tsa_cylinder(r,height):
    surface_area_cylinder = (2 * math.pi * r)*(r + height)
    return (surface_area_cylinder)

# Curved Surface Area of Cylinder
def lsa_cylinder(r,height):
    curved_surface_area_cylinder = (2 * math.pi * r * height)
    return (curved_surface_area_cylinder)

# Total Surface Area of Cone
def tsa_cone(slant_height,r):
    surface_area_cone = math.pi * r * (slant_height + r)
    return (surface_area_cone)

# Curved Surface Area of Cone
def lsa_cone(slant_height,r):
    curved_surface_area_cone = math.pi * r * slant_height
    return (curved_surface_area_cone)

# Surface Area of Sphere
def tsa_sphere(r):
    surface_area_sphere = 4 * math.pi * (r**2)
    return (surface_area_sphere)

# Total surface area of Hemisphere
def tsa_hemisphere(r):
    surface_area_hemisphere = 3 * math.pi * (r**2)
    return (surface_area_hemisphere)

# Curved Surface Area of Hemisphere
def lsa_hemisphere(r):
    curved_surface_area_hemisphere = 2 * math.pi * (r**2)
    return (curved_surface_area_hemisphere)

# Total Surface Area of triangular prism
def tsa_triangular_prism(a,b,c,h):
    tsa = (a*h) + (b*h) + (c*h) + 1/2*math.sqrt(-(a**4) + (2*(a*b)**2) + (2*(a*c)**2) - (b**4) + (2*(b*c)**2) - (c**4))
    return (tsa) 

# Total Surface Area of square prism
def tsa_square_prism(a,h):
    tsa = (2)*(a**2)+(4)*(a)*(h)    
    return (tsa)

# Total Surface Area of rectangular prism
def tsa_rectangular_prism(l,w,h):
    tsa = 2*((w*l)+(h*l)+(h*w)) 
    return (tsa)   

# Total Surface Area of pentagonal prism
def tsa_pentagonal_prism(a,h):
    tsa = 5*(a*h) + (1/2)*math.sqrt(((5*5)+(5*2)*math.sqrt(5)))*(a**2)
    return (tsa)

# Total Surface Area of hexagonal prism
def tsa_hexagonal_prism(a,h):
    tsa = (6*a*h)+((3*math.sqrt(3))*(a**2))
    return (tsa)

# Total Surface Area of octagonal prism
def tsa_ocatagonal_prism(a,h):
    tsa = (8)*(a)*(h)+(4)*((1)+math.sqrt(2))*(a**2)
    return (tsa)    

# Lateral Surface Area of triangular prism
def lsa_triangular_prism(a,b,c,h):
    lsa = (a+b+c)*(h)
    return (lsa)    

# Lateral Surface Area of pentagonal prism
def lsa_pentagonal_prism(a,h):
    lsa = 5*a*h
    return (lsa)    

# Lateral Surface Area of hexagonal prism
def lsa_hexagonal_prism(a,h):
    lsa = 6*a*h
    return (lsa)

# Lateral Surface area of octagonal prism
def lsa_octagonal_prism(a,h):
    lsa = 8*a*h
    return (lsa)    

# Total Surface Area of tetrahedron
def tsa_tetrahedron(a):
    tsa = (math.sqrt(3))*(a**2)
    return (tsa)

# Total Surface Area of square pyramid
def tsa_square_pyramid(a,h):
    tsa = (a**2)+(2)*(a)*math.sqrt((a**2/4)+(h**2))
    return (tsa)    

# Total Surface Area of rectangular pyramid
def tsa_rectangular_pyramid(l,w,h):
    tsa = (l*w)+(l*math.sqrt(((w/2)**2)+(h**2)))+(w*math.sqrt(((l/2)**2)+(h**2)))
    return (tsa)

# Total Surface Area of hexagonal pyramid
def tsa_hexagonal_pyramid(a,h):
    tsa = (3*(math.sqrt(3)/2))*(a**2)+(3)*(a)*(math.sqrt((h**2)+((3)*(a**2)/4)))        
    return (tsa)

# Lateral Surface Area of square pyramid
def lsa_square_pyramid(a,h):
    lsa = (a)*(math.sqrt((a**2)+(4)*(h**2)))
    return (lsa)    

# Lateral Surface Area of rectangular pyramid
def lsa_rectangular_pyramid(l,w,h):
    lsa = l*(math.sqrt(((w/2)**2)+(h**2)))+(w)*(math.sqrt(((l/2)**2)+(h**2)))
    return (lsa)

# Lateral Surface Area of hexagonal pyramid
def lsa_hexagonal_pyramid(a,h):
    lsa = (3)*(a)*(math.sqrt((h**2)+((3)*(a**2)/4)))        
    return (lsa)

# Area of Torus
def area_torus(R,r):
    area = (2*math.pi*R)*(2*math.pi*r)
    return (area)

# Perimeter of Square
def peri_square(side):
    peri_square = (side*4)
    return (peri_square)

# Perimeter of Rectangle
def peri_rectangle(length,breadth):
    peri_rectangle = (2*(length+breadth))
    return (peri_rectangle)

# Perimeter of Triangle
def peri_triangle(side1,side2,side3):
    peri_triangle = (side1+side2+side3)
    return (peri_triangle)

# Perimeter of Parallelogram
def peri_parallelogram(parallel1,parallel2):
    peri_parallelogram = (2*(parallel1+parallel2))
    return (peri_parallelogram)

# Perimeter of Rhombus
def peri_rhombus(side):
    peri_rhombus = (side*4)
    return (peri_rhombus)

# Circumference of Circle
def circum_circle(r):
    circum_circle = math. pi * 2 * r
    return (circum_circle)

# Perimeter of Trapezium
def peri_trapezium(side1,side2,side3,side4):
    peri_trapezium = (side1+side2+side3+side4)
    return (peri_trapezium)

# Perimeter of Kite
def peri_kite(side1,side2):
    peri_kite = 2*(side1+side2)
    return (peri_kite)

# Volume of Cube
def vol_cube(edge):
    volume_cube = edge**3
    return (volume_cube)

# Volume of Cuboid
def vol_cuboid(length,breadth,height):
    volume_cuboid = length*breadth*height
    return (volume_cuboid)

# Volume of Cylinder
def vol_cylinder(r,height):
    volume_cylinder = math.pi * (r**2) * height
    return (volume_cylinder)

# Volume of Cone
def vol_cone(r, height):
    volume_cone = (1/3)* math.pi * (r**2) * height
    return (volume_cone)

# Volume of Sphere
def vol_sphere(r):
    volume_sphere = (4/3)*math.pi*(r**3)
    return (volume_sphere)

# Volume of Hemisphere
def vol_hemishphere(r):
    volume_hemishphere = (2/3)*math.pi*(r**3)
    return (volume_hemishphere)

# Volme of triangular prism
def vol_triangular_prism (a,b,c,h):
    vol = 1/4*h*math.sqrt(-(a**4) + (2*(a*b)**2) + (2*(a*c)**2) - (b**4) + (2*(b*c)**2) - (c**4))
    return (vol)

# Volume of square prism
def vol_square_prism (a,h):
    vol = ((a**2)*h)
    return (vol)

# Volume of rectangular prism
def vol_rectangular_prism (l,w,h):
    vol = (w*h*l)
    return (vol)

# Volume of pentagonal prism
def vol_pentagonal_prism(a,h):
    vol = (1/4)*math.sqrt(((5*5)+(5*2)*math.sqrt(5)))*(a**2)*(h)
    return (vol)

# Volume of hexagonal prism
def vol_hexagonal_prism(a,h):
    vol = ((3*math.sqrt(3))/2)*(a**2)*(h)
    return (vol)

# Volume of octagonal prism 
def vol_octagonal_prism(a,h):
    vol = (2)*(1 + math.sqrt(2))*(a**2)*(h)
    return (vol)

# Volume of tetrahedron
def vol_tetrahedron(a):
    vol = ((a**3)/(6*math.sqrt(2)))
    return (vol)

# Volume of square pyramid
def vol_square_pyramid(a,h):
    vol = (a**2)*(h/3)
    return (vol)

# Volume of rectangular pyramid
def vol_rectangular_pyramid(l,w,h):
    vol = (l*w*h)/3
    return (vol)  

# Volume of hexagonal pyramid 
def vol_hexagonal_pyramid(a,h):
    vol = (math.sqrt(3)/2)*(a**2)*(h)          
    return (vol)

# Volume of Torus   
def vol_torus(R,r):
    vol = (math.pi*(r**2))*(2*math.pi*R)
    return (vol)

# End of Area of 2D and 3D shapes, Perimeter of 2D shapes, Volume of 3D shapes


# Playing with numbers

#LCM: Lowest Common Multiple
def lcm(*nums):
    lcm = math.lcm(nums)
    return (lcm)

# HCF: Highest Common Factor or GCD: Greatest Common Divisor
def hcf(*nums):
    hcf = math.gcd(nums)
    return (hcf)

# Fining if a number is prime or not
def prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print('The number',num,'is not a prime number')
            else:
                print('The number',num,'is a prime number')
    elif num == 1:
        print('The number is a 1 which is not a prime number or a composite number')
    else:
        print('The number',num,'is not a prime number')

# Finding if a number is an armstrong number or not
def armstrong(num):
    num_str = str(num)
    num_list = list()
    sq_list = list()
    for i in num_str:
        i = int(i)
        num_list.append(i)
    for i in num_list:
        sq_list.append(i**3)
    sum = add_multple(sq_list)
    if sum == num:
        print('The number',num,'is an armstrong number')
    else:
        print('The number',num,'is not an armstrong num')

# Reversing a number
def reverse(num):
    num_str = str(num)
    num_list = list()
    for i in num_str:
        num_list.append(i)
    return(num_list)

# Sum of the digits of the number
def sum_digits(num):
    num_str = str(num)
    num_list = list()
    sum = 0
    for i in num_str:
        i = int(i)
        num_list.append(i)
        sum += i
    return(sum)

# Finding if a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print('The number',num,'is an even number')
    else:
        print('The number',num,'is an odd number')

# Finding Prime Factors
def prime_factors(num):
    while num % 2 == 0:
        print(2)
        num /= 2
    for i in range(3,int(math.sqrt(num)+1),2):
        while num % i == 0:
            print(i)
            num /= i
    if num > 2:
        print(num)

# Finding the greatest number in a list
def greatest_number(*args):
    nums = list(args)
    greatest_number = None
    for num in nums:
        if greatest_number == None:
            greatest_number = num
        elif num > greatest_number:
            greatest_number = num
    if greatest_number is None:
        print('The Numbers provided were wrong. Please provide valid numbers')
        quit() 
    return(greatest_number)

# Finding the lowest number in a list
def lowest_number(*args):
    nums = list(args)
    lowest_number = None
    for num in nums:
        if lowest_number == None:
            lowest_number = num
        elif num < lowest_number:
            lowest_number = num
    if lowest_number is None:
        print('The Numbers provided were wrong. Please provide valid numbers')
        quit() 
    print('The lowest number is',lowest_number)

# Finding if a number is in a list or not
def find_number(num,*args):
    num_list = list(args)
    for i in num_list:
        if i == num:
            place = num_list.index(num)
            print('The number',num,'was found in the list at the',place+1,'index')
        elif num not in (num_list):
            print ('The number',num,'was not found in the list')

# Number of numbers in a list
def how_many_numbers(*args):
    num_list = list(args)
    count = 0
    for _ in num_list:
        count += 1
    return(count)

# Average of numbers
def average(*args):
    num_list = list(args)
    sum = add_multple(num_list)
    count = how_many_numbers(num_list)
    average = sum/count
    return (average)

# Factorial of number
def factorial(num):
    factorial = math.factorial(num)
    return (factorial)

# Finding the ASCII value of a character
def ascii(character):
    ascii = ord(character)
    return (ascii)

# Finding the character of a ascii value
def ascii_character(ascii_value):
    character = chr(ascii_value)
    return (character)

# Finding if a character is perfect or not
def perfect(num):
    factor_list = list()
    for i in range(1,num+1):
        if num % i == 0:
            factor_list.append(i)
    sum = add_multple(factor_list)
    if sum/2 == num:
        print('The number',num,'is a perfect number')
    else :
        print('The number',num,'is not a perfect number')

# Python program to find additive inverse of a number
def additive_inverse(num):
    if num == -num:
        return (num)
    else:
        return (-(num))

# Python program to find absolute value of a number
def absolute_value(num):
    if (num < 0):
        return (-(num))
    if (num > 0):
        return num                  

# Python program to calculate multiplicative inverse of a number
def multiplicative_inverse(num):
    num_fraction = fractions.Fraction(num)
    num_reciprocal = 1/num_fraction
    return (num_reciprocal)

# Python program to find if two numbers are coprime
def co_prime(*args):
    num_list = list(args)
    gcd = math.gcd(num_list) 
    if gcd == 1:
        print('They are coprime')
    else:
        print('They are not coprime')

# Python program to sort in ascending order
def ascending_order(*args):
    num_list = list(args)
    num_list.sort()
    return (num_list)

# Python program to sort in descending order
def descending_order(*args):
    num_list = list(args)
    num_list.sort(reverse=True)
    return (num_list)  

# Python program to sort out even numbers from a given list
def even_numbers(*args):
    evennum = []
    for n in args:
        if n % 2 == 0:
            evennum.append(n)
    return evennum

# Python program to print multiplication table of a number
def multiplication_table(num):
    print("Multiplication table of", num)
    for i in range(1, 11):
        print(num,"X",i,"=",num * i)

# Returning a unique list with the unique elements of the list entered by the user
def unique_list(*args):
    ununique_list = list(args)
    unique_list = list()
    for i in ununique_list:
        if i not in unique_list:
            unique_list.append(i)
    return(unique_list)

# Finding if a number is a twin prime or not
def twin_prime(num):
    num1 = num+2
    num2 = num-2
    if prime(num) is True :
        if prime(num1) is True or prime(num2) is True:
            print('The Number is a twin prime')
        else:
            print('The number is prime, but is not a prime number')
    else:
        print('The number is not a prime number')

# Python program to check if a year is leap year or not
def leap_year(year):
    if (year % 4) == 0:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")

# Finding Mean of a list
def mean(*args):
    num_list = list(args)
    sum = 0
    for i in num_list:
        sum += i
    num = len(num_list)
    mean = sum/num
    return(mean)

# Finding Mode of a list
def mode(*args):
    num_list = list(args)
    greatest_num = None
    for i in num_list:
        if greatest_num is None:
            greatest_num = i
        elif i > greatest_num:
            greatest_num = i
    return(greatest_num)

# Finding Median of a list
def median(*args):
    num_list = list(args)
    n = len(num_list)
    if n % 2 == 0:
        median = (n/2 + (n+1)/2)/2
    else: 
        median = (n+1)/2
    return(median)

# Finding if a given point is on the x-axis, y-axis, origin
def point_x_y_origin(x1, y1):
    if x1 == 0 and y1 == 0:
        print('The point is on the origin')
    elif x1 == 0:
        print('The point is on x axis')
    elif y1 == 0:
        print('The point is on y axis')
    else:
        print('The point is somewhere on the cartesian plane')

# Finding if three points lie on a straight line
def three_point_straight_line(x1,y1,x2,y2,x3,y3):
    if (y2 - y1)/(x2 - x1) == (y3 - y1)/(x3 - x1):
        print('The three points lie on a stright line')
    else : 
        print("The three points don't lie on a straight line")

# End of Playing with Numbers


# String related functions

# Most common letter in a string
def common_letter(text):
    letter_list = list(text)
    counts = dict()
    for letter in letter_list:
        counts[letter] = counts.get(letter, 0) + 1
    biggest_count = None
    common_letter = None
    for letter,count in counts.items():
        if biggest_count is None or count > biggest_count:
            biggest_count = count
            common_letter = letter
    print('The most common letter was',common_letter,'and its count was',biggest_count)

# Most common letter in file
def common_letter_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    letter_list = list(handle.read().strip("\n"))
    counts = dict()
    for letter in letter_list:
        counts[letter] = counts.get(letter, 0) + 1
    biggest_count = None
    common_letter = None
    for letter,count in counts.items():
        if biggest_count is None or count > biggest_count:
            biggest_count = count
            common_letter = letter
    print('The most common letter was',common_letter,'and its count was',biggest_count)

# Number of Letters in a string
def letter_count(text):
    letter_list = list(text)
    count = 0
    for _ in letter_list:
        count += 1
    print('The number of letters in the text were',count)

# Number of Letters in a file
def letter_count_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    letter_list = list(handle.read().strip("\n"))
    count = 0
    for _ in letter_list:
        count += 1
    print('The number of letters in the file were',count)

# Most common word in a string
def common_word(text):
    counts = dict()
    for line in text:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    biggest_count = None
    common_word = None
    for word,count in counts.items():
        if biggest_count is None or count > biggest_count:
            biggest_count = count
            common_word = word
    print('The most common word was',common_word,'and its count was',biggest_count)
    print(counts)

# Most common word in a file
def common_word_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    biggest_count = None
    common_word = None
    for word,count in counts.items():
        if biggest_count is None or count > biggest_count:
            biggest_count = count
            common_word = word
    print('The most common word was',common_word,'and its count was',biggest_count)

# Number of Words in a string
def word_count(text):
    count = len(text.split())
    print('The number of words in text were ' + str(count))

# Number of words in a file
def word_count_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    count = 0
    for line in handle:
        words = line.split()
        for _ in words:
                count += 1
    print('The number of words in the text were',count)

# Finding if a word is in a file or not
def find_word(word_to_be_found,file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    for line in handle:
        words = line.split()
        for word in words:
            if word == word_to_be_found:
                print("The word '",word_to_be_found,"' was found in the text file")

# Finding if a number is a lowercase, uppercase, number or a special character
def check(character):
    character_ascii = ord(character)
    if character_ascii >= 97 and character_ascii <= 122:
        print('The character',character,'is a lowercase letter')
    elif character_ascii >= 65 and character_ascii <= 90:
        print('The character',character,'is a uppercase letter')
    elif character_ascii >= 48 and character_ascii <= 57:
        print('The character',character,'is a number')
    else :
        print('The character',character,'is a special character')

# Finding the number of uppercase and lowercase characters in string
def find_uppercase_lowecase(text):
    character_list = list(text)
    lowercase_count = 0
    uppercase_count = 0
    number_count = 0
    special_count = 0
    for character in character_list:
        if ord(character) >= 97 and ord(character) <= 122:
            lowercase_count += 1
        elif ord(character) >= 65 and ord(character) <= 90:
            uppercase_count += 1
        elif ord(character) >= 48 and ord(character) <= 57:
            number_count += 1
        else :
            special_count += 1
    print('Uppercase Count:',uppercase_count,'\nLowercase Count:',lowercase_count,'\nNumber Count:',number_count,'\nSpecial Charcater Count:',special_count)

# Finding the number of uppercase and lowercase characters in a file
def find_uppercase_lowercase_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    lowercase_count = 0
    uppercase_count = 0
    number_count = 0
    special_count = 0
    letter_list = list(handle.read().strip("\n"))
    for character in letter_list:
        if ord(character) >= 97 and ord(character) <= 122:
            lowercase_count += 1
        elif ord(character) >= 65 and ord(character) <= 90:
            uppercase_count += 1
        elif ord(character) >= 48 and ord(character) <= 57:
            number_count += 1
        else :
            special_count += 1
    print('Uppercase Count:',uppercase_count,'\nLowercase Count:',lowercase_count,'\nNumber Count:',number_count,'\nSpecial Charcater Count:',special_count)
    
# Python program to check if a string is palindrome
def is_str_palindrome(string):
	left_side = 0
	right_side = len(string) - 1	

	while right_side >= left_side:
		if not string[left_side] == string[right_side]:
			print('The string is not a palindrome')
		left_side += 1
		right_side -= 1
	print('The string is a palindrome')

# Python program to check if a string is pangram or not
def is_str_pangram(string): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string:
            print('The string is not a pangram')
        else:
            print('The string is a pangram')

# End of String related functions


# Functions related to mathematics in daily life

# Python program to calculate Profit when CP and SP are given
def profit(cp,sp):
    profit = sp-cp
    return (profit)

# Python program to calculate Loss when CP and SP are given
def loss(cp,sp):
    loss = cp-sp
    return (loss)

# Python Program to calculate Gain%
def gain_percentage(profit,cp):
    gain = (profit/cp)*100
    return (gain)

# Python program to calculate Loss%
def loss_percentage(loss,cp):
    loss = (loss/cp)*100
    return (loss)

# Python program to calculate SP when Gain% and CP are given
def selling_price_when_gain_percentage_and_cp_are_given(gain_percentage,cp):
    sp = ((100+gain_percentage)/100)*cp
    return (sp)

# Python program to calculate SP when Loss% and CP are given
def selling_price_when_loss_percentage_and_cp_are_given(loss_percentage,cp):
    sp = ((100-loss_percentage)/100)*cp
    return (sp) 

# Python program to calculate CP when Gain% and SP are given
def cost_price_when_gain_percentage_and_sp_are_given(gain_percentage,sp):
    cp = (100/(100+gain_percentage))*sp 
    return (cp)

# Python program to calculate CP when Loss% and SP are given
def cost_price_when_loss_percentage_and_sp_are_given(loss_percentage,sp):
    cp = (100/(100-loss_percentage))*sp 
    return (cp)                         

# Python program to find Selling Price when Marked Price and Discount percent are given
def find_selling_price(mp,discpercent):
    sp = mp * (100 - discpercent)/100
    return (sp)

# Finding tax when selling price and tax percent is given
def tax(sp,tax_percent):
    bill_amount = sp * (tax_percent+100) / 100
    return(bill_amount)

# Finding tax when selling price and bill amount is given
def tax_when_sp_and_billamount(sp,bill_amount):
    tax = bill_amount - sp
    return(tax)

# Finding sp when tax% and bill amount is given
def sp_when_tax_and_billamount(tax_percent,bill_amount):
    sp = bill_amount * 100 / (100 + tax_percent)
    return(sp) 

# Python program to find Simple Interest
def find_simple_interest(p,r,t):
    si = (p * r * t)/100
    return (si)

# Python program to find compound interest annually 
def find_compund_interest(p,r,t):
    ci = p * (1 + r/100)**t
    return (ci)

# Python program to find compound interest half-yearly
def find_compund_interest_halfyearly(p,r,t):
    ci = p * ( 1 + ( (r / 2) / 100 ) )**(t*2)
    return (ci)

# Python program to find compound interest quarterly
def find_compund_interest_quartelry(p,r,t):
    ci = p * ( 1 + ( (r / 4) / 100 ) )**(t*4)
    return (ci)    

# End of functions related to mathematics in daily life 


# Some geometrical functions

# Python program to check if a triangle is valid
def triangle_is_valid(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a): 
        print("Triangle is invalid")
    else: 
        print("Triangle is valid")
       
# Python program to find one angle of a traingle when two angles are given using Angle Sum property
def angle_sum_property(a1,a2):
    a3 = 180 - (a1 + a2)
    return (a3)

# Python program to take out Hypotenuse of a right-angled triangle using Pythagoras theorem
def take_out_hypotenuse(a,b):
    Hypotenuse = math.sqrt((a**2) + (b**2))
    return (Hypotenuse)

# Python program to take out Perpendicular of a right-angled triangle using Pythagoras theorem
def take_out_perpendicular(c,b):
    Perpendicular = math.sqrt((c**2) - (b**2))
    return (Perpendicular)

# Python program to take out Base of a right-angled triangle using Pythagoras theorem
def take_out_base(c,a):
    Base = math.sqrt((c**2) - (a**2))
    return (Base)

# Finding if the triangle is equilateral, isosceles or scalene
def type_triangle(side1,side2,side3):
    if side1 == side2 == side3:
        print('The triangle is equilateral')
    elif side1 == side2 != side3 or side2 == side3 != side1 or side1 == side3 !=side2:
        print('The triangle is isosceles')
    else:
        print('The triangle is scalene')

# Finding what congruence the two triangles are or if they are not even congruent
def congruency(sides1,sides2,angles1,angles2):
    sides1 = [float(i) for i in sides1]
    sides2 = [float(i) for i in sides2]
    angles1 = [float(i) for i in angles1]
    angles2 = [float(i) for i in angles2]

    sides1.sort()
    sides2.sort()
    angles1.sort()
    angles2.sort()

    sss = sss_congruence(sides1,sides2,angles1,angles2)
    sas = sas_congruence(sides1,sides2,angles1,angles2)
    asa = asa_congruence(sides1,sides2,angles1,angles2)
    rhs = rhs_congruence(sides1,sides2,angles1,angles2)
    if sss or sas or asa or rhs:
        print('Triangles are congruent by: ')
        if sss: print('SSS')
        if sas: print('SAS')
        if asa: print('ASA')
        if rhs: print('RHS')
    else: 
        print('Triangles are not congruent')
# Check for SSS
def sss_congruence(sides1,sides2,angles1,angles2):
    sides1 = [float(i) for i in sides1]
    sides2 = [float(i) for i in sides2]
    angles1 = [float(i) for i in angles1]
    angles2 = [float(i) for i in angles2]

    sides1.sort()
    sides2.sort()
    angles1.sort()
    angles2.sort()

    if sides1[0] == sides2[0] and sides1[1] == sides2[1] and sides1[2] == sides2[2]:
        return True
    else:
        return False

# Check for SAS
def sas_congruence(sides1,sides2,angles1,angles2):
    sides1 = [float(i) for i in sides1]
    sides2 = [float(i) for i in sides2]
    angles1 = [float(i) for i in angles1]
    angles2 = [float(i) for i in angles2]

    sides1.sort()
    sides2.sort()
    angles1.sort()
    angles2.sort()
    
    if sides1[0] == sides2[0] and sides1[1] == sides2[1] and angles1[2] == angles2[2]:
        return True
    if sides1[1] == sides2[1] and sides1[2] == sides2[2] and angles1[0] == angles2[0]:
        return True
    if sides1[0] == sides2[0] and sides1[2] == sides2[2] and angles1[1] == angles2[1]:
        return True
    else: 
        return False

# Check for ASA
def asa_congruence(sides1,sides2,angles1,angles2):
    sides1 = [float(i) for i in sides1]
    sides2 = [float(i) for i in sides2]
    angles1 = [float(i) for i in angles1]
    angles2 = [float(i) for i in angles2]

    sides1.sort()
    sides2.sort()
    angles1.sort()
    angles2.sort()
    
    if sides1[0] == sides2[0] and angles1[1] == angles2[1] and angles1[2] == angles2[2]:
        return True
    if sides1[1] == sides2[1] and angles1[0] == angles2[0] and angles1[2] == angles2[2]:
        return True
    if sides1[2] == sides2[2] and angles1[0] == angles2[0] and angles1[1] == angles2[1]:
        return True
    else:
        return False

# Check for RHS
def rhs_congruence(sides1,sides2,angles1,angles2):
    sides1 = [float(i) for i in sides1]
    sides2 = [float(i) for i in sides2]
    angles1 = [float(i) for i in angles1]
    angles2 = [float(i) for i in angles2]

    sides1.sort()
    sides2.sort()
    angles1.sort()
    angles2.sort()
    
    if sides1[2] == sides2[2]:
        if sides1[0] == sides2[0] or sides1[1] == sides2[1]:
            return True
    else: 
        return False

# End of geometrical functions


# Conversions

# Python program to convert celsius to fahrenheit 
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return (fahrenheit)

# Python program to convert fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return (celsius)

# Unit Conversions
def unit_conversions(what_to_convert,value):
    if what_to_convert == 'm to km':
        m_to_km = value / 1000
        return m_to_km
    elif what_to_convert == 'm to cm':
        m_to_cm = value * 100
        return m_to_cm
    elif what_to_convert == 'cm to km':
        cm_to_km = value / (100 * 1000)
        return cm_to_km
    elif what_to_convert == 'cm to m':
        cm_to_m = value / 100
        return cm_to_m
    elif what_to_convert == 'km to cm':
        km_to_cm = value * 100 * 1000
        return km_to_cm
    elif what_to_convert == 'km to m':
        km_to_m = value * 1000
        return km_to_m
    elif what_to_convert == 'm^2 to km^2':
        msq_to_kmsq = value / (1000*1000)
        return msq_to_kmsq
    elif what_to_convert == 'm^2 to cm^2':
        msq_to_cmsq = value * (100*100)
        return msq_to_cmsq
    elif what_to_convert == 'cm^2 to km^2':
        cmsq_to_kmsq = value / (100*100*1000*1000)
        return cmsq_to_kmsq
    elif what_to_convert == 'cm^2 to m^2':
        cmsq_to_msq = value / (100*100)
        return cmsq_to_msq
    elif what_to_convert == 'km^2 to m^2':
        kmsq_to_msq = value * (1000*1000)
        return kmsq_to_msq
    elif what_to_convert == 'km^2 to cm^2':
        kmsq_to_cmsq = value * (100*100*1000*1000)
        return kmsq_to_cmsq
    elif what_to_convert == 'm^3 to km^3':
        mcb_to_kmcb = value / (1000*1000*1000)
        return mcb_to_kmcb
    elif what_to_convert == 'm^3 to cm^3':
        mcb_to_cmcb = value * (100*100*100)
        return mcb_to_cmcb
    elif what_to_convert == 'cm^3 to km^3':
        cmcb_to_kmcb = value / (100*100*100*1000*1000*1000)
        return cmcb_to_kmcb
    elif what_to_convert == 'cm^3 to m^3':
        cmcb_to_mcb = value / (100*100*100)
        return cmcb_to_mcb
    elif what_to_convert == 'km^3 to m^3':
        kmcb_to_mcb = value * (1000*1000*1000)
        return kmcb_to_mcb
    elif what_to_convert == 'km^3 to cm^3':
        kmcb_to_cmcb = value * (100*100*100*1000*1000*1000)
        return kmcb_to_cmcb
    elif what_to_convert == 'm/s to km/h':
        km_hour = value * 3600 / 1000
        return km_hour
    elif what_to_convert == 'km/h to m/s':
        m_second = value * 1000 / 3600
        return m_second

# Binary to Decimal Conversion
def binary_to_decimal(num):
    num_string = str(num)
    decimal_num = int(num_string,2)
    return(decimal_num)

# Binary to Octal Conversion
def binary_to_octal(num):
    num_decimal = binary_to_decimal(num)
    num_octal = decimal_to_octal(num_decimal)
    return(num_octal)

# Binary to Hexadecimal Conversion
def binary_to_hexadecimal(num):
    num_decimal = binary_to_decimal(num)
    num_hexadecimal = decimal_to_hexadecimal(num_decimal)
    return(num_hexadecimal)

# Decimal to Binary Conversion
def decimal_to_binary(num):
    num_binary = bin(num).replace("0b","")
    return(num_binary)

# Decimal to Octal Conversion
def decimal_to_octal(num):
    num_octal = oct(num).replace("0o","")
    return(num_octal)

# Decimal to Hexadecimal Conversion
def decimal_to_hexadecimal(num):
    num_hexadecimal = hex(num).replace("0x","")
    return(num_hexadecimal)

# Octal to Binary Conversion
def octal_to_binary(num):
    num_decimal = octal_to_decimal(num)
    num_binary = decimal_to_binary(num_decimal)
    return num_binary

# Octal to Decimal Conversion
def octal_to_decimal(num):
    num_string = str(num)
    num_decimal = int(num_string,8)
    return num_decimal

# Octal to Hexadecimal Conversion
def octal_to_hexadecimal(num):
    num_decimal = octal_to_decimal(num)
    num_hexadecimal = decimal_to_hexadecimal(num_decimal)
    return num_hexadecimal

# Hexadecimal to Binary Conversion
def hexadecimal_to_binary(num):
    num_decimal = hexadecimal_to_decimal(num)
    num_binary = decimal_to_binary(num_decimal)
    return num_binary

# Hexadecimal to Decimal Conversion
def hexadecimal_to_decimal(num):
    num_string = str(num)
    num_decimal = int(num_string,16)
    return num_decimal

# Hexadecimal to Octal Conversion
def hexadecimal_to_octal(num):
    num_decimal = hexadecimal_to_decimal(num)
    num_octal = decimal_to_octal(num_decimal)
    return num_octal

# End of conversions


# Science related functions

# Finding the number of images formed when there are multiple mirrors
def num_images_multiple_mirrors(num_of_mirrors):
    num_of_images = (360/num_of_mirrors) - 1
    return num_of_images

# Finding the speed when distance and time are given
def speed(distance, time):
    speed = distance / time
    return speed 

# Finding distance when speed and time are given
def distance(speed, time):
    distance = speed * time
    return distance

# Finding time when distance and speed are given
def time(distance, speed):
    time = distance/speed
    return time

# End of Science related functions