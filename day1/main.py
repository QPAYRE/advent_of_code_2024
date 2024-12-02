def calculate_total_distance(left_list, right_list):
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)
    total_distance = sum(abs(left - right) for left, right in zip(sorted_left_list, sorted_right_list))
    return total_distance

def main():
    left_list = []
    right_list = []
    try:
        with open("input.txt", "r") as file:
            for line in file:
                numbers = line.split()
                if len(numbers) == 2:
                    left_list.append(int(numbers[0]))
                    right_list.append(int(numbers[1]))
    except FileNotFoundError:
        print("Error: input.txt file not found!")
        return
    
    if not left_list or not right_list:
        print("Error: input.txt must contain pairs of numbers.")
        return

    distance = calculate_total_distance(left_list, right_list)
    print("The total distance is:", distance)

if __name__ == "__main__":
    main()
