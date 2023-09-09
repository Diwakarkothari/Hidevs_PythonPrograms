from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")  # pura html aa jayega
# print(soup)
table = soup.find_all('table')[1]  # apan ko jo table chahiye uske liye
# print(table)
world_titles = table.find_all('th')  # header ke th tags dhunde
# print(world_titles)
world_table_titles = [title.text.strip() for title in world_titles]  # strip ki help se \n remove hoga
# print(world_table_titles)  # table ke titles aa gye
# titles ko pandas ki help se dataset ke columns bana denge
df = pd.DataFrame(columns=world_table_titles)
# print(dataframe)
column_data = table.find_all('tr') # table se tr find kara
for row in column_data[1:]:  # first row empty hai isliye
    row_data = row.find_all('td')  # tr mein se td dhunda taaki columns ka data mil paye
    individual_row_data = [data.text.strip() for data in row_data]  # data ko filter kiya taaki actual list mil sake
    # print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data

# print(df)
df.to_csv(r'companies.csv', index=False)
