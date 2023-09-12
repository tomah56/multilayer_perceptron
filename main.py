from load_csv import load
import matplotlib.pyplot as plt

def main():
    try:
        data_car = load("data.csv")
        # print(data_car[0])
        labels = data_car[1]
        values = data_car[7]
        
        # plt.scatter(values)
        count_of_M = 0
        number_of_data = len(values)
        plt.figure(figsize=(20, 6))
        plt.scatter(range(number_of_data), values, marker='o', color='black', s= 1, label='Data Points')
        for i, val in enumerate(labels):
            if val == 'M':
                count_of_M += 1
                plt.annotate(val, (i, values[i]), textcoords="offset points", xytext=(0,10), ha='center', color='red')
            else:
                plt.annotate(val, (i, values[i]), textcoords="offset points", xytext=(0,10), ha='center', color='blue')
        count_of_B = number_of_data - count_of_M
        print(f"all data: {number_of_data} M: {count_of_M} B: {count_of_B}")
        prasantage_of_M = round(count_of_M / number_of_data * 100)
        prasantage_of_B = round(count_of_B / number_of_data * 100)
        print(f"presentageof  M: {prasantage_of_M}% B: {prasantage_of_B}%")
        # plt.plot(values)
        # plt.bar(labels, values)
#         fig, ax = plt.subplots()
#         ax.plot(values)
# # Add labels and title
#         x_ticks = [1, 2, 3, 4, 5]
#         x_tick_labels = [labels]
#         ax.set_xticks(x_ticks)
#         ax.set_xticklabels(x_tick_labels)
        # plt.xlabel('bubu')
        plt.ylabel('Data')
        plt.title('Ploting one line only with diagnosys')

        # Show the plot
        plt.show()
        # trained_model = start(data_car)

    except (KeyError, Exception) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
