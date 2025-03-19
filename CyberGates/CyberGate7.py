from time import time

def timekeeper(func):
    def wrapper(*args, **kwargs):
        print("### TIME TRAVEL EXPERIMENT ###")
        result = func(*args, **kwargs)
        return result
    return wrapper

def create_time_machine():
    def time_travel_executor():
        departure = time()
        input("READY TO TIME TRAVEL? [PRESS ENTER]")
        arrival = time()
        delta = arrival - departure
        if delta > 120:
            # ......
            ...
        elif delta < 0:
            raise Exception("GOING BACK IN TIME!!")
        else:
            print(f"GOING FORWARD! Time elapsed: {delta:.2f} seconds")
    return time_travel_executor

@timekeeper
def gate7():
    traveler = create_time_machine()
    traveler()
