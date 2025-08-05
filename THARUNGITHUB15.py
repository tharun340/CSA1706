def decide(weather, humidity):
    if weather == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"
    elif weather == "Overcast":
        return "Yes"
    elif weather == "Rain":
        return "Yes"
    else:
        return "Unknown"

# Example usage
print("Play?" , decide("Sunny", "High"))      
print("Play?" , decide("Rain", "Normal"))     
print("Play?" , decide("Overcast", "High"))   
