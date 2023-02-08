def main():
    print(" Welcome to the mail slicer")
    print("")

    email= input("Enter your email address")

    (username,domain)= email.split("@")
    (domain,extension)= domain.split(".")
    print(f"Your username is: {username}")
    print(f'Your domain is: {domain}')
    print(f'Your extension is: {extension}')

main()