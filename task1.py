def upper_and_lower(text):
    letter = 0
    lower_letter = 0
    upper_letter = 0
    for x in text:
        if x.isupper():
            upper_letter += 1
            letter += 1
        elif x.islower():
            lower_letter += 1
            letter += 1

    return letter, upper_letter, lower_letter

def percent_letter(letters):
    try:
        upper_letter = 100 / (letters[0] / letters[1])
    except:
        upper_letter = 0
    try:
        lower_letter = 100 / (letters[0] / letters[2])
    except:
        lower_letter = 0
    return round(upper_letter), round(lower_letter)

def main():
    text = input("Введите текст: ")
    letters = upper_and_lower(text)
    upper_letter, lower_letter = percent_letter(letters)
    print("Количество букв - ", letters[0])
    print(f"Буквы в вверхнем регистре - {upper_letter}%, в нижнем регистре - {lower_letter}%")

main()