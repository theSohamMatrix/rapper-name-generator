password = input("enter your password: ")
if password == "Soham@123":
    print("welcome back soham, good to see you again on projecct")
else:
    print("Access denied, Try correct password")
    exit()



print("="*50)
print("🎤 Rapper Name Generator 🎤".center(50))
print("="*50)

# inputs
name = input("enter your real name: ").casefold()
mood = input("how was your mood today (ex. cool,savage,happy): ").lower()
thing = input("best thing you liked: ").upper()

# formatting styles 
format = name.replace("s","$").replace("a","@")

# rapper names
rap1 = (format + mood)
rap2 = (thing + format)
rap3 = (mood + thing)

# display output
print("\nhere are yours 3 rapper name 🤩")
print(f"1: {rap1}")
print(f"2: {rap2}")
print(f"3: {rap3}")
print("keep hustling and keep rapping")