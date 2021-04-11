#hw8pr4.py
#
#Name: Ashkon Aghassi 

#
# Example user-interaction looping program
#  (a variant of the one done in class)
#

def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Input a new list")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the minimum and its day")
    print("(5) Find the maximum and its day")
    print("(6) Your TT investment plan")
    print("(9) Break! (quit)")
    print()

def predict(L):
    """Predict ignores its argument and returns
       what the next element should have been.
    """
    return 42

def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:
            result = x
    return result

def find_min(L):
    """find max uses a loop to return the maxiumum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x > result:
            result = x
    return result

def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    minval = L[0]
    minloc = 0

    for i in list(range(len(L))):
        if L[i] < minval:  # a smaller one was found!
            minval = L[i]
            minloc = i

    return minval, minloc

def find_max_loc(L):
    """find max loc uses a loop to return the maximum of L
            and the location (index or day) of that maximum.
        Argument L: a nonempty list of numbers.
        Results:  the largest value in L, its location (index)
    """
    maxval = L[0]
    maxloc = 0

    for i in list(range(len(L))):
        if L[i] > maxval:  # a larger one was found!
            maxval = L[i]
            maxloc = i

    return maxval, maxloc

def main():
    """The main user-interaction loop"""
    secret_value = 4.2

    L = [30, 10, 20]  # an initial list

    while True:     # the user-interaction loop
        print("\n\nThe list is", L)
        menu()
        choice = input("Enter your choice: ")
        print("")

        #
        # "Clean and check" the user's input
        # 
        try:
            choice = int(choice)   # make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        # run the appropriate menu option
        #
        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 1:  # We want to continue...

            for i in range(len(L)):
                print("Day:",i, " Price:",L[i])
            continue       # Goes back to the top of the while loop

        elif choice == 0:  # We want to enter a new list
            newL = input("Enter a new list: ")    # enter _something_
            
            #
            # "Clean and check" the user's input
            #
            try: 
                newL = eval(newL)   # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]): 
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL  # Here, things were OK, so let's set our list, L
            except:
                print("I didn't understand your input. Not changing L.")

        elif choice == 2: 
            print("Average price is: ", ave(L))
            continue

        elif choice == 3:  
            print("Standard deviation is: ", std(L))
            continue

        elif choice == 4:  # Another unannounced menu option (even more interesting...)
            minval, minloc = find_min_loc(L)
            print("The minimum value in L is", minval, "at day #", minloc)
            continue
        
        elif choice == 5:  
            maxval, maxloc = find_max_loc(L)
            print("The maxiumum value in L is", maxval, "at day #", maxloc)
            continue
        
        elif choice == 6:  
            buy, sell = IP(L)
            print("You should: \n Buy on Day:", buy, "at price: ", L[buy], "\n Sell on Day:", sell, "at price: ", L[sell])
            print("Profit of", L[sell]-L[buy])
            continue
        
        else:
            print(choice, "?    Sorry, that's not on the menu! Try again!")

    print()
    print("See you yesterday!")

def ave(L):
    """
    Arguments: List L
    Returns: Average of elements in L
    """
    sum = 0 
    for x in L:
        sum += x
    return  sum/(len(L))

def std(L):
    """
    Arguments: List L
    Returns: Standard Deviation of elements in L
    """

    sum = 0
    avg = ave(L)
    for x in L:
        sum += (x - avg)**2

    return (sum/len(L))**.5
    
def IP(L):
    """
    Argument: List L
    Returns:  the best day on which to buy and sell the stock in 
    question in order to maximize the profit earned. the sell 
    day must be greater than or equal to the buy day. 
    """

    max = L[1] - L[0]

    buy = 0
    sell = 0

    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] - L[i] > max:
                max = L[j] - L[i]
                sell = j
                buy = i
    
    return buy, sell

