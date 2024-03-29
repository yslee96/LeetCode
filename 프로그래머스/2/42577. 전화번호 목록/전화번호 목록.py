def solution(phone_book):
    is_exist = {}
    for phone_number in sorted(phone_book):
        cur_digit = ""
        for digit in phone_number:
            cur_digit += digit
            if is_exist.get(cur_digit, 0):
                return False
        is_exist[phone_number] = 1
        
    return True