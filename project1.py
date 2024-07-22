
'''----------------Import Modules----------------'''
import dealer_tool as dealer

'''----------------Main program starts here----------------'''
print("\n==================================")
print("Dealership Vehicle Management Tool")
print("==================================")
print("")

vehicleList = dealer.initialize()

#This While loop will keep asking for user inputs until the they simply press enter.
while True:
    dealer.display_menu()  
    option=input("Command (Enter to exit): ")
    
    if option=="":
        break
    elif option=="1":
        dealer.display(vehicleList)
    elif option=="2":
        dealer.info(vehicleList)
    elif option=="3":
        dealer.remove(vehicleList)
    elif option=="4":
        dealer.add_new_vehicle(vehicleList)
    elif option=="5":
        ID1 = int(input("First vehicle (enter number): ")) - 1
        ID2 = int(input("Second vehicle (enter number): ")) - 1
        if ID1 in range(len(vehicleList)) and ID2 in range(len(vehicleList)+1):
            vehicle1 = vehicleList[ID1]
            vehicle2 = vehicleList[ID2]
            dealer.compare(vehicle1,vehicle2)
    elif option=="6":
        minimumPrice = int(input("Please select a minimum price: "))
        maximumPrice = int(input("Please select a maximum price: "))
        dealer.search(vehicleList,minimumPrice,maximumPrice)
    elif option=="7":
        carID = int(input("Which vehicle do you want to discount? (enter number): ")) - 1
        if carID in range(len(vehicleList)):
            percentDiscount = int(input("What percent would you like to disount the vehicle? (0-100): "))
            if percentDiscount in range(0,101):
                dealer.discount(vehicleList[carID],percentDiscount)
            else:
                print("Invalid discount!")
        else:
            print("Vehicle not found!")




# Code reaches here after the loop ends
print("\nThanks for using this tool!"+"\nCome back soon!\n")