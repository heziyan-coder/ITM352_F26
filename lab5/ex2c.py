
trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

trip = dict(zip(trip_durations, trip_fares))
print(trip)

trip_num = int(input("what trip do you want?"))

print("the duration of the trip is:", trip_durations[trip_num-1],"miles")
print("the fare of the trip is:", trip_fares[trip_num-1])
