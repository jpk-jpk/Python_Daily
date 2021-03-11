def run_average():
    dr_time = []
    while True:
        try:
            dr_time.append(float(input('Enter the average running time for 10 km: ')))
        except ValueError as e:
            print(f"You didn't enter any number {e}")
            break
    if dr_time:
        print(f'The average running time is: {sum(dr_time) / (len(dr_time)):.2f}')


if __name__ == "__main__":
    run_average()
