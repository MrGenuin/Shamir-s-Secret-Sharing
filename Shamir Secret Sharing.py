import sympy as sp
import random

def Random_Digit():
    random_digit=random.randint(10,99);
    return random_digit
def decode_first_Degree():
    fisrt_share=[]
    second_share=[]
    share1=input("Enter the First Share in the form [,]  :")
    for char in share1:
        fisrt_share.append(char)
    if fisrt_share[0] != '(' or fisrt_share[-1] != ')':
        print("Input should be enclosed in half-circle brackets (x, y)")
        main()
    share2=input("Enter the Second Share in the form [,] : ")
    for char in share2:
        second_share.append(char)
    if second_share[0] != '(' or second_share[-1] != ')':
        print("Input should be enclosed in half-circle brackets (x, y)")
        main()
    x0 = fisrt_share[1]
    y0 = ""  # Initialize y0 as an empty string
    for char in share1[3:]:
        if char == ']':
            break
        y0 += char  # Concatenate the character to y0
    y0 = int(y0)
    x1=second_share[1]
    y1 = ""  # Initialize y0 as an empty string
    for char in share2[3:]:
        if char == ']':
            break
        y1 += char  # Concatenate the character to y0
    y1 = int(y1)
    # Define the symbolic variable x
    x = sp.symbols('x')
    l00=x-int(x1)
    l01=int(x0)-int(x1)
    l0=l00/l01
    # print(l00)
    # print(l01)
    # print(l0)
    l10=(x-int(x0))
    l11=(int(x1)-int(x0))
    l1=l10/l11
    # print(l10)
    # print(l11)
    # print(l1)s
    fx=(y0*l0)+(y1*l1)
    print("f(x)= ", fx)
    #print("Secert is: ")
    main()
    
def decode_second_Degree():
    
    fisrt_share=[]
    second_share=[]
    third_share=[]
    share1=input("Enter the First Share in the form (,)  : ")
    for char in share1:
        fisrt_share.append(char)
    if fisrt_share[0] != '(' or fisrt_share[-1] != ')':
        print("Input should be enclosed in half-circle brackets (x, y)")
        main()
    share2=input("Enter the Second Share in the form (,) : ")
    for char in share2:
        second_share.append(char)
    if second_share[0] != '(' or second_share[-1] != ')':
        print("Input should be enclosed in half-circle brackets (x, y)")
        main()
    share3=input("Enter the Third Share in the form (,)  : ")
    for char in share3:
        third_share.append(char)
    if third_share[0] != '(' or third_share[-1] != ')':
        print("Input should be enclosed in half-circle brackets (x, y)")
        main()
    x0 = fisrt_share[1]
    x1=second_share[1]
    x2=third_share[1]

    y0 = ""  # Initialize y0 as an empty string
    for char in share1[3:]:
        if char == ')':
            break
        y0 += char  # Concatenate the character to y0
    y0 = int(y0)
    y1 = ""
    for char in share2[3:]:
        if char == ')':
            break
        y1 += char  
    y1 = int(y1)
    y2 = ""
    for char in share3[3:]:
        if char == ')':
            break
        y2 += char  
    y2 = int(y2)

    x = sp.symbols('x')  # Define the symbolic variable x
    l0=((x-int(x1))/(int(x0)-int(x1)))*(((x-int(x2))/(int(x0)-int(x2))))
    l1=((x-int(x0))/(int(x1)-int(x0)))*(((x-int(x2))/(int(x1)-int(x2))))
    l2=((x-int(x0))/(int(x2)-int(x0)))*(((x-int(x1))/(int(x2)-int(x1))))

    fx=(y0*l0)+(y1*l1)+(y2*l2)
    simplified_expression = sp.simplify(fx) #simplify the output
    constant_part = simplified_expression.as_coefficients_dict()[1] # extract only the constant value
    #print(constant_part)
    #print("f(x)= ",simplified_expression)
    print("Secert is: ",constant_part )

def first_degree(S,N,K):
    dict={}
    a=S 
    b=Random_Digit()
    for x in range(1,N+1):
        y=a+(b*x)
        dict[x]=y
    for key in dict:
        print("(",key,",",dict[key],")")
   
def second_degree(S,N,K):
    dict={}
    a=Random_Digit()
    b=Random_Digit()
    c=S
    for x in range(1,N+1):
        y=(a*(pow(x,2))+(b*x)+c)
        dict[x]=y
    for key in dict:
        print("(",key,",",dict[key],")")
    
def encode():
    S=int(input("Enter The Secret String    (S): "))
    N=int(input("Enter Number of Shares     (N): "))
    K=int(input("Enter Number of Threshold  (K): "))
    degree=K-1
    if(degree==1):
        first_degree(S,N,K)
        main()
    elif(degree==2):
        second_degree(S,N,K)
        main()
    else:
        print("Big K Number, only 2 or 3 are allowe. ")
        main()

def decode():
    K=int(input("Enter number of Threshold: "))
    if (K==2):
        decode_first_Degree()
        main()
    elif (K==3):
        decode_second_Degree()
        main
    else:
        print(f"{K} is NOT supported, only 2 or 3 is allowed")
        main()
     
def main():
    print("----------------")
    print("Selct Operation: ")
    print("1-  Encoding\n2-  Decoding\n3-  Exit")
    option=int(input("          :"))
    if option==1:
        encode()
    elif option==2:
        decode()
    elif option==3:
        exit()
    else:
        print("Invalid option")
        main()

if __name__=="__main__":
    main()