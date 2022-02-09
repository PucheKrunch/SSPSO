import csv

input_file = csv.DictReader(open("data.csv", encoding='utf-8'))

vowels_list = ['a', 'e', 'i', 'o', 'u']

data = []

vowels = open("vowels.txt", "w", encoding='utf-8')
consonants = open("consonants.txt", "w", encoding='utf-8')
numbers = open("numbers.txt", "w", encoding='utf-8')

for row in input_file:
    word = row['id'] + row['name'] + row['car_year'] + row['country_code']
    for char in word:
        if char.lower() in vowels_list:
            vowels.write(char + " ")
        elif char.isalpha() == False:
            numbers.write(char + " ")
        else:
            consonants.write(char + " ")

vowels.close()
consonants.close()
numbers.close()