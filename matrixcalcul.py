#matrix input lena and display


def display_menu_matrix():
   
   print("*****************MATRIX CALCULATOR******************\n1. Single Matrix Operations\n2. Multiple Matrix Operations\n3. Exit\n")

def input_matrix():
   rows=int(input("Enter number of rows:"))
   column=int(input("Enter number of columns:"))
   matrix=[]
   for i in range(0,rows):
      row=[]
      for j in range(0,column):
         element=int(input(f"Enter element [{i}][{j}]:"))
         row.append(element)  #current row me elements add karega
      matrix.append(row)      #complete row ko matrix me add karega like=> [[1,2],[3,4]]
   return matrix

def display_single_matrix_types_menu():
    
    print("\n ----------------------Check MATRIX TYPE---------------------------\n")
    print("1. Symmetric\n 2. Skew-Symmetric\n3. Diagonal\n4. Unit/Identity\n5. Check all types\n6. Back to Main Menu")


def transpose_matrix():
   pass

def determinant_matrix():
   pass

def is_symmetric():
   pass


def is_skew_symmetric():
   pass


def is_diagonal():
   pass

def is_unit():
   pass



def check_all_types():

   print("Symmetric:",is_symmetric())
   print("Skew-Symmetric:",is_skew_symmetric())
   print("Diagonal:",is_diagonal())
   print("Unit:",is_unit())


   pass
 

  
def check_matrix_type():

   while True:
      display_single_matrix_types_menu()
      choice=int(input("CHOOSE UR OPTION:"))
      match choice:              #in python match works same as c++ switchcase
         case "1":
            print(is_symmetric())
         case "2":
            print(is_skew_symmetric())
         case "3":
            print(is_diagonal())
         case "4":
            print(is_identity())
         case "5":
            print(check_all_types())
         case "6":
            break
         case _:                       # case _ where "_" is a wildcard pattern , iska mtlab h koi bhi value jo pehle ke cases se match nhi hui just like default in c++
            print("Invalid option!!!!! Try again:")

def single_matrix_menu():
   matrix=input_matrix() 
   if matrix is None:
      return

   while True:
      display_single_matrix_types_menu()
      choice=input("choose your option:")

      match choice:
         case "1":
            result=transpose_matrix()
         case "2":
            print(determinant_matrix())
         case "3":
            check_matrix_type()
         case "4":
            break;
         case _:
            print("Invalid option!!!!!!! Try Again........")





def single_matrix():
   print("\n _________single_matrix Operation__________")
   print("1. Transpose\n2. Determinant\n3. Matrix Type Check\n4. Back to Main Menu")



   
def display_multiple_matrix_menu():
   print("\n---------------------------------MULTIPLE MATRIX OPERATIONS------------------------------------------\n")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Both matrix are equal or not")
   print("5. Back to Main Menu")


def add_matrix():
   pass


def subtract_matrix():
   pass


def multiply_matrix():
   pass


def are_equal():
   pass


def multiple_matrix_menu():
   while True:
      display_multiple_matrix_menu()
      choice = input("choose your option")

      match choice:
         case "1":
            pass
         case "2":
            pass
         case "3":
            pass
         case "4":
            pass
         case "5":
            break
         case _:
            print("Invalid option!!!! TRY AGAIN.........")



def main():

   while True:
      display_menu_matrix()
      choice=input("Choose your option:")

      match choice:
         case "1":
            single_matrix_menu()
         case "2":
            multiple_matrix_menu()
         case "3":
            exit()
         case _:
            print("INVALID OPTION !!! TRY AGAIN")
        