import math
ID = 0
STARTTIME = 1
ENDTIME = 2
DURATION = 3
DISTANCE = 4
COST = 5
PAYMENT = 6
pickupLONG = 7
pickupLAT = 8
dropoffLONG = 9
dropoffLAT = 10

def read_file(filename):
    data = []
    try:
        count = 0
        file = open(filename, 'r')
        for line in file:
            try:
                count+= 1
                lineData = line.split(",")
                lineData[ID] = (lineData[ID])
                lineData[STARTTIME] = str(lineData[STARTTIME])
                lineData[ENDTIME] = str(lineData[ENDTIME])
                lineData[DURATION] = (lineData[DURATION])
                lineData[DISTANCE] = (lineData[DISTANCE])
                lineData[COST] = (lineData[COST])
                lineData[PAYMENT] = lineData[PAYMENT].strip()
                lineData[pickupLONG] = (lineData[pickupLONG])
                lineData[pickupLAT] = (lineData[pickupLAT])
                lineData[dropoffLONG] = (lineData[dropoffLONG])
                lineData[dropoffLAT] = (lineData[dropoffLAT])

                data.append(lineData)
            except ValueError:
                print("Error has occurred, line ", count, "has been skipped")
        file.close()
    except FileNotFoundError:
        print("File ", filename, "not found")
    return data

def average_cost_cash(data):
    cost = 0
    average = 0
    amount_of_payments_in_cash = 0
    for i in range(len(data)):
        if data[i][PAYMENT] == "Cash":
            cost += float(data[i][COST])
            amount_of_payments_in_cash +=1
            average = cost / amount_of_payments_in_cash
    return average

def average_cost_card(data):
    cost = 0
    average = 0
    amount_of_payments_in_card = 0
    #if payment in data[payment] = "cash"
    for i in range(len(data)):
        if data[i][PAYMENT] != "cash":
            cost += float(data[i][COST])
            amount_of_payments_in_card +=1
            average = cost / amount_of_payments_in_card
    return average

def trips_on_specific_date(file, data, date):
    trips_with_same_stateDate = 0
    trips_with_same_endDate = 0
    startDate = date.split("/")
    endDate = date.split("/")
    date = date.split("/")
    trip_info = []
    for row in data:
        if date in row[STARTTIME]:
            trips_with_same_stateDate += 1
        if date in row[ENDTIME]:
            trips_with_same_endDate += 1
        for line in trip_info:
            trip_info[line] = trip_info[line]
            file.append(trip_info)
            file.append(trips_with_same_stateDate, trips_with_same_endDate)

    return trip_info

def location_nearby(data, miles, longitude, latitude):
    #if the distance between on location is longer than the others?
    distanceFromPickUp = 0
    distanceFromDropOff = 0
    for row in data:
       #Calculates the distance from the pickup coordinates
       distanceFromPickUp =  math.acos(math.sin(math.sin(data[pickupLAT])) * math.sin(latitude) + math.cos(data[pickupLAT]) * math.cos(latitude) * math.cos(data[pickupLONG] - longitude)) * miles
       distanceFromDropOff = math.acos(math.sin(data[dropoffLAT]) * math.sin(latitude) + math.cos(data[dropoffLAT]) * math.cos(latitude) * math.cos(data[dropoffLONG] - longitude)) * miles
    return distanceFromPickUp, distanceFromDropOff

def main():
    trip_data = read_file("2016_09.csv")
    print("The average cost for cash is", average_cost_cash(trip_data))
    print("The average cost for card is", average_cost_card(trip_data))
    userDate = input("Enter a date:")
    same_dateFile = open("Trips_with_same_date", 'w')
    #print(trips_on_specific_date(same_dateFile, trip_data, userDate))


main()
