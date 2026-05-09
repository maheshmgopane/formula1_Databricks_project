start=int(input("Enter the starting number: "))# Get user input for the starting number and convert it to an integer
end=int(input("Enter the ending number: "))# Get user input for the ending number and convert it to an integer
skip=int(input("Enter the number to skip: "))# Get user input for the number to skip and convert it to an integer
if skip < start and skip > end and skip != start and skip != end and skip != 0 and start < end and start > 0:# Check if the skip number is outside the range of start and end
    for i in range(start, end + 1):# Loop through numbers from start to end (inclusive)
        if i == skip:# If the current number is equal to the skip number, skip it
            print(i)
            continue
        print(i)
elif skip == 0:# If the skip number is zero, print an error message
    print("Skip number cannot be zero. Please enter a non-zero number to skip.")
elif skip == start or skip == end:# If the skip number is equal to start or end, print an error message
    print("Skip number cannot be equal to the starting or ending number. Please enter a number that is not equal to start or end.")
elif start >= end:# If the starting number is greater than or equal to the ending number, print an error message
    print("Starting number must be less than the ending number. Please enter valid start and end numbers.")
elif start <= 0:# If the starting number is less than or equal to zero, print an error message
    print("Starting number must be greater than zero. Please enter a positive starting number.")

        


