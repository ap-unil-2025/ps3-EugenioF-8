"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""


def get_numbers_from_user():
    numbers = []

    while True:
        user_list = input("Please provide a list of numbers and type 'done' at the end of your list ")
        if user_list == "done":
            print(numbers)
            break

        elif user_list.isnumeric() == True:
            numbers.append(float(user_list))

        else:
            print("Please only provide a list of numbers or type 'done' once your list is complete")
            
    return numbers



def analyze_numbers(numbers):

    analysis = {}
    analysis["count"] = len(numbers)
    analysis["sum"] = sum(numbers)
    analysis["average"] = analysis["sum"]/analysis["count"]
    analysis["minimum"] = min(numbers)
    analysis["maximum"] = max(numbers)

    even_count = 0
    odd_count = 0
    
    for i in numbers:
        if i.is_integer():
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
   
    return analysis


def display_analysis(analysis):
    print("\nAnalysis Results:")
    print("-" * 20)

    if not analysis:
        return
    
    for key in analysis.keys():
        print(f"{key}: {analysis[key]}")

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.



def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()