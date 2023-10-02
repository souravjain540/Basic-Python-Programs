import re

def password_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("[!] Password is too short. Consider using a longer password for better security.")
    
    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("[!] Password should have at least one lowercase letter. Lowercase letters increase the complexity of your password.")
    
    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("[!] Password should have at least one uppercase letter. Uppercase letters make your password harder to guess.")
    
    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("[!] Password should have at least one numeral. Numerals can greatly enhance the strength of your password.")
    
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if special_characters.search(password):
        score += 1
    else:
        feedback.append("[!] Password should have at least one of the special characters like @, #, etc. Special characters significantly improve password security.")

    if score == 5:
        feedback.insert(0, "[~] Very Strong Password.")
    elif score == 4:
        feedback.insert(0, "[~] Strong Password.")
    elif score == 3:
        feedback.insert(0, "[~] Average Password.")
    elif score == 2:
        feedback.insert(0, "[~] Weak Password.")
    else:
        feedback.insert(0, "[!] Very Weak Password.")
    
    return "\n".join(feedback)

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(password_strength(password))

