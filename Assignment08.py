# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Brooke Biscoe,March 6, 2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    def __init__(self,product_name,product_price):
        self.__product_name = product_name
        self.__product_price = product_price
    @property
    def product_name(self):
        return str(self.__product_name).title()
    @product_name.setter
    def product_name(self,value):
        self.__product_name = value
    @property
    def product_price(self):
        return str(self.__product_price)
    @product_price.setter
    def product_price(self,value):
        self.__product_name = value
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Brooke Biscoe,March 6, 2022,Modified code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        objFile = open(file_name,'w')
        for row in list_of_product_objects:
            objFile.write(row['Product Name']+','+row['Product Price']+'\n')
        objFile.close()
        return list_of_product_objects
    @staticmethod
    def read_data_from_file(file_name):
        lstOfProductObjects.clear()  # clear current data
        try:
            file = open(file_name, "r")
            for line in file:
                product_name, product_price = line.split(",")
                row = {"Product Name": product_name.strip(), "Product Price": product_price.strip()}
                lstOfProductObjects.append(row)
            file.close()
        except FileNotFoundError:
            file = open(file_name,'w')
            file.close()
        except Exception as e:
            print('There was a non-specific error')
            print('Below is the python documentation')
            print(e,e.__doc__,type(e),sep='\n')
        return lstOfProductObjects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    '''
    This Class handles all user input and output.

    methods:
    output_menu_tasks -> prints a string of menu options

    input_menu_choice -> returns user input

    output_current_products_in_list(lstOfProductObjects) -> prints the current items in the list

    input_new_name_and_price() -> returns the product name and product price

    changelog: (When,Who,What)
        Brooke Biscoe,March 6, 2022,Modified code to complete assignment 8
    '''
    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Save Data to File        
        3) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_products_in_list(lstOfProductObjects):
        """ Shows the current Tasks in the list of dictionaries rows

        :param lstOfProductObjects: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for row in lstOfProductObjects:
            print(row["Product Name"] + " " + row["Product Price"])
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_name_and_price():
        """  Gets a product name and price to be added to the list

        :return: (string, string) with product name and price
        """
        while True:
            strProdName = input("Please enter the product name: ")
            if strProdName.isnumeric() == False:
                break
            else:
                print('Product name cannot contain numbers')
        while True:
            strProdPrice = input("Please enter the product price: ")
            try:
                strProdPrice = float(strProdPrice) # This line of code is to force an error if the user does not enter a floating point
                strProdPrice = "${:,.2f}".format(strProdPrice) # Formats the code to look like a currency
                break
            except ValueError:
                print('Product price must contain numbers')
        return strProdName, strProdPrice
# Presentation (Input/Output)  -------------------------------------------- #
print('Hello! Welcome to the product database!')
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
while True:
    IO.output_current_products_in_list(lstOfProductObjects)
    IO.output_menu_tasks()
    choice = IO.input_menu_choice()
    if choice == '1':
        name, price = IO.input_new_name_and_price()
        myproduct = Product(name,price)
        row = {"Product Name": str(myproduct.product_name).strip(), "Product Price": str(myproduct.product_price).strip()}
        lstOfProductObjects.append(row)
    elif choice == '2':
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        print('Data Saved!\n')
    elif choice =='3':
        print('You have exited the program!')
        break
    else:
        print('That is not a valid choice.\n')
# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

