def validateCreditCardNumber(card_number):
    digit_counter = 0
    group_counter = 0
    last_digit = ""
    last_digit_counter = 1

    #  It must start with a 4, 5 or 6.
    first_digit = int(card_number[0])
    if first_digit != 4 and first_digit != 5 and first_digit != 6:
        return "Invalid"

    for x in card_number:
        # It must only consist of digits (0-9).
        if x.isdigit():
            digit_counter += 1
            group_counter += 1

            # It must contain exactly 16 digits.
            if digit_counter > 16:
                return "Invalid"

            # It must NOT have 4 or more consecutive repeated digits.
            if last_digit == x:
                last_digit_counter += 1
            elif last_digit_counter >= 4:
                return "Invalid"
            else:
                last_digit = x
                last_digit_counter = 1

        # It must NOT use any other separator like ' ' , '_', etc.
        elif x != "-":
            return "Invalid"

        # It may have digits in groups of 4, separated by one hyphen "-".
        elif group_counter == 4:
            group_counter = 0
        else:
            return "Invalid"

    if digit_counter != 16:
        return "Invalid"
    else:
        return "Valid"
    
def main():
    n = int(input())
    cards_numbers = []
    
    for _ in range(n):
        card_number = input()
        print(validateCreditCardNumber(card_number))
    
    
main()