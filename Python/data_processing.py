import pandas as pd
import datetime as dt

class CompanyIndicator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            df = pd.read_excel(self.file_path, header=0, index_col=0, parse_dates=True)
            df.columns = pd.to_datetime(df.columns, format='%d.%m.%Y')
            df = df.transpose()
            return df
        except Exception as e:
            raise ValueError("Ошибка загрузки данных из Excel файла") from e

    def get_average_indicator(self, company_name, date):
        try:
            date = pd.to_datetime(date, format='%d.%m.%Y')
        except ValueError:
            raise ValueError("Неверный формат даты. Пожалуйста, используйте дд.мм.гггг")
        
        if company_name not in self.data.columns:
            raise ValueError("Неверное название компании. Пожалуйста, введите A, B или C")

        one_year_ago = date - pd.DateOffset(years=1)
        company_data = self.data[company_name]

        if not (company_data.index.min() <= date <= company_data.index.max()):
            raise ValueError("Дата не найдена в наборе данных")

        past_year_data = company_data[(company_data.index >= one_year_ago) & (company_data.index <= date)]

        if past_year_data.empty:
            raise ValueError("Нет данных за указанный период")

        average_value = past_year_data.mean()
        return average_value, past_year_data

def print_bordered_table(df):
    headers = ["Дата", "Значение"]
    header_line = "+{:-^20}+{:-^20}+".format("", "")
    header_content = "|{:^20}|{:^20}|".format(headers[0], headers[1])

    rows = []
    for index, value in df.iteritems():
        rows.append("|{:^20}|{:^20.2f}|".format(index, value))
    
    print(header_line)
    print(header_content)
    print(header_line)
    for row in rows:
        print(row)
    print(header_line)

if __name__ == "__main__":
    file_path = 'indicators.xlsm'  
    
    while True:
        try:
            company_name = input("Введите название компании (A, B или C): ").strip()
            if company_name not in ['A', 'B', 'C']:
                raise ValueError("Неверное название компании. Пожалуйста, введите A, B или C")

            date = input("Введите дату (дд.мм.гггг): ").strip()
            date = pd.to_datetime(date, format='%d.%m.%Y')

            ci = CompanyIndicator(file_path)
            average_value, past_year_data = ci.get_average_indicator(company_name, date.strftime('%d.%m.%Y'))

            print(f"\nСреднее значение индикатора для компании {company_name} за год до {date.strftime('%d.%m.%Y')} составляет: {average_value:.2f}\n")
            print(f"Данные для компании {company_name} за год до {date.strftime('%d.%m.%Y')}:")

            display_data = past_year_data.tail(5)
            display_data.index = display_data.index.strftime('%d.%m.%Y')

            print_bordered_table(display_data)
            print(f"Среднее значение = ({' + '.join([str(value) for value in past_year_data])}) / {len(past_year_data)} = {average_value:.2f}")
            
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {type(e).__name__}")
