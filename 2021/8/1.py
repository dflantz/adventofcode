if __name__ == "__main__":
    unique_lengths = [2, 4, 3, 7]  # 1, 4, 7, 8
    sum = 0
    for line in open("2021/8/input.txt", "r"):
        signal_patterns, output_values = line.split("|")
        signal_patterns = signal_patterns.split()
        output_values = output_values.split()

        sum += len([v for v in output_values if len(v) in unique_lengths])

    print(sum)
