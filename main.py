from load_csv import load


def main():
    try:
        data_car = load("data.csv")
        # trained_model = start(data_car)

    except (KeyError, Exception) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
