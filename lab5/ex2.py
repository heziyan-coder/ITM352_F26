
trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

trip = {
    "miles": trip_durations,
        "fares": trip_fares
}


print(trip)

print("The duration of the 3rd trip is:", trip["miles"][2], "miles")
print("the fare of the 3rd trip is", trip["fares"][2], "fares")