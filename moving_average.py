def compute_moving_average(buffer, window_ms = 100, hz_rate = 50):
    # window size: 100ms / (1000ms / 50Hz) = 5 (100 ms = 1/10 of seconds, 50hz means 50 datas every second so I took 1/10 of 50)
    ms = 1000 / hz_rate
    window_size = int(window_ms / ms)
    moving_avg = []

    for i in range(len(buffer)):
        # going bacwards from current index (i)
        start = i - window_size + 1 # +1 for include the slicing
        
        # if we come to the start of list (if index < 0 ) start from 0
        if start < 0:
            start = 0
            
        # Slice the window
        window = buffer[start : i + 1]
        
        # calculate the average and add to list
        avg = sum(window) / len(window)
        moving_avg.append(avg)
        
    return moving_avg

# To try it I randomly select 100 numbers.
def main():
    import random
    cencor_data = [random.randint(10, 20) for _ in range(100)]
    res = compute_moving_average(cencor_data)
    print(res)

if __name__ == '__main__':
    main()

