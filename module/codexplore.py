
def emailProcess(email):
    email_username = email[0:email.index('@')]
    #print(f"{email_username}")
    email_domain = email[email.index('@') + 1:]
    return [email_username, email_domain]

def main():
    email = input("Please enter your email: ").strip()
    email_username, email_domain = emailProcess(email)
    print_message(email_username, email_domain)

def print_message(username, domain):
    print(f"Username: {username}, Domain: {domain}")

if __name__ == '__main__':
    main()