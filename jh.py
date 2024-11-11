import requests


def get_exchange_rate():
    # Получаем актуальный курс валют
    url = "https://api.exchangerate-api.com/v4/latest/RUB"  # API для получения курсов
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['rates']['USD']  # Возвращаем курс доллара к рублю
    else:
        print("Ошибка при получении курса валют.")
        return None


def convert_rub_to_usd(rub_amount, exchange_rate):
    return rub_amount * exchange_rate


def main():
    print("Добро пожаловать в конвертер валют!")

    while True:
        exchange_rate = get_exchange_rate()

        if exchange_rate is None:
            break

        print(f"Актуальный курс: 1 RUB = {exchange_rate:.2f} USD")

        try:
            rub_amount = float(input("Введите сумму в рублях для конвертации в доллары (или 'exit' для выхода): "))
            usd_amount = convert_rub_to_usd(rub_amount, exchange_rate)
            print(f"{rub_amount:.2f} RUB = {usd_amount:.2f} USD")
        except ValueError:
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()
