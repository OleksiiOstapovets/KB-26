import string

def is_only_digits(text): # Чи складається тільки з чисел
    return text.isdigit()

def is_too_short(text): # Чи не надто короткий
    return len(text) < 12

def is_only_lowercase_letters(text): # Чи не містить тільки малі букви
    for _ in text:
        if not ascii("a") <= ascii(_) <= ascii("z"):
            return False
    return True 

def from_weak_list(text): # Чи не є поширеним
    weak_passwords_list = ["password","admin","Password","Aa123456","Pass@123","P@ssw0rd","admin123","123456789","1234567890","12345678910","123456","12345678","qwerty","abc123","monkey","1q2w3e4r5t","dragon","111111","baseball","123123"]
    if text in weak_passwords_list:
        return True
    return False
    
def is_special_symbol(pw): # Чи містить спеціальний символ
    for _ in pw:
        if _ in string.punctuation:
            return True
    return False

def is_weak_password(pw): # Головна функція
    if from_weak_list(pw):
        return 'This password is too weak. It is too popular!'
    elif is_too_short(pw):
        return 'This password is too short!'
    elif is_only_digits(pw):
        return 'This password is too weak. It consist only of digits!'
    elif is_only_lowercase_letters(pw):
        return 'This password is too weak. It consist only of lowercase letters!'
    elif not is_special_symbol(pw):
        return 'This password is good, but you can make it more complicated by adding a special symbol!'
    else:
        return 'This password is good enough'
    
if __name__ == "__main__":
    word = str(input('Input your password\n'))
    print(is_weak_password(word))