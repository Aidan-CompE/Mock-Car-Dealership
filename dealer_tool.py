

'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''

def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")


#### To complete (all functions below)

def initialize():
    vehicle1 = ["Toyota","Camry","2018","45000","20000"]
    vehicle2 = ["Ford","Escape","2019","30000","23500"]
    vehicle3 = ["Honda","Accord","2017","60000","16200"]
    vehicle4 = ["Chevorlet","Silverado","2020","25000","41000"]
    vehicle5 = ["BMW","3 Series","2016","60000","20500"]
    vehicle6 = ["Nissan","Rogue","2019","40000","17800"]
    vehicle7 = ["Hyundai","Sonata","2018","42000","16500"]
    vehicle8 = ["Jeep","Wrangler","2021","15000","32000"]
    vehicle9 = ["Ford","Mustang","2015","50000","22000"]
    vehicle10 = ["Volkswagen","Golf","2017","38000","17800"]
    
    vehicleList = [vehicle1,vehicle2,vehicle3,vehicle4,vehicle5,vehicle6,vehicle7,vehicle8,vehicle9,vehicle10]
    return vehicleList

def display(vehicleList):
    print("\tMake\t\tModel\t\tYear\tMileage\tPrice ($)")
    print("-----------------------------------------------------------------")
 
    for i in range(0,len(vehicleList)):
        
        print(i+1,end="\t")
        for i2 in range(0,2):
            print(vehicleList[i][i2],end="\t\t" if len(vehicleList[i][i2]) < 8 else "\t")
        for i2 in range(2,5):
            print(vehicleList[i][i2],end="\t")
        print("")

        
def info(vehicleList):
    print("#Vehicles",len(vehicleList))

    totalPrice = 0

    lessThan10k = 0
    tens = 0
    twenties = 0
    thirties = 0
    fortiesPlus = 0

    for i in range(len(vehicleList)):
        price = int(vehicleList[i][4])
        totalPrice += price
        if price < 10000:
            lessThan10k += 1
        elif price >=10000 and price < 20000:
            tens += 1
        elif price >= 20000 and price < 30000:
            twenties += 1
        elif price >= 30000 and price < 40000:
            thirties += 1
        elif price >= 40000:
            fortiesPlus += 1

    print("<10,000 :",str(float((lessThan10k/len(vehicleList)*100)))+"%")
    print("10,000s :",str(float((tens/len(vehicleList)*100)))+"%")
    print("20,000s :",str(float((twenties/len(vehicleList)*100)))+"%")
    print("30,000s :",str(float((thirties/len(vehicleList)*100)))+"%")
    print(">=40,000 :",str(float((fortiesPlus/len(vehicleList)*100)))+"%")
    print("\nMean Price:",(totalPrice/len(vehicleList)))

def remove(vehicleList):
    carID = int(input("Which vehicle do you want to remove (enter number): ")) - 1
    if carID < 0 or carID >= len(vehicleList):
        print("Vehicle not found!")
        return
    elif carID >= 0 and carID < len(vehicleList):
        del(vehicleList[carID])
    
def add_new_vehicle(vehicleList):
    newVehicle = ([[input("Enter Make: "),input("Enter Model: "),input("Enter Year: "),input("Enter Mileage: "),input("Enter Price: ")]])
    vehicleList += newVehicle

def compare(vehicle1,vehicle2):
    print("")
    print(vehicle1[0],vehicle1[1],"vs",vehicle2[0],vehicle2[1])

    if vehicle1[0] == vehicle2[0]:
        print("The two vehicles are the same make.")
    else:
        print("The two vehicles are different makes.")
        
    if vehicle1[2] == vehicle2[2]:
        print("The vehicles were made the same year.")
    elif int(vehicle1[2]) > int(vehicle2[2]):
        print("The first vehicle is newer.")
    elif int(vehicle2[2]) > int(vehicle1[2]):
        print("The second vehicle is newer.")

    if int(vehicle1[4]) == int(vehicle2[4]):
        print("The vehicles cost the same.")
    elif int(vehicle1[4]) > int(vehicle2[4]):
        print("The first vehicle costs more.")
    elif int(vehicle2[4]) > int(vehicle1[4]):
        print("The second vehicle costs more.")
    
def search(vehicleList,minimumPrice,maximumPrice):
    print("")
    totalVehicles = 0
    print("Vehicles that cost between:",minimumPrice,"and",maximumPrice)
    for a in vehicleList:
        if int(a[4]) in range(minimumPrice,maximumPrice+1):
            totalVehicles += 1
            print(a[0],a[1],a[4])
    print("")
    print("Total number of vehicles:",totalVehicles)

def discount(car,percentDiscount):
    price = int(car[4])
    discount = (int(car[4])/100)*percentDiscount
    newPrice = price - discount
    print("Price:",price)
    print("Discount:",discount)
    print("New Price:", newPrice)
