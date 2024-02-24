import csv
import itertools

def generate_wordlist(username, passwords):
    wordlist = []
    for new in range(1,4):
        for combo in itertools.product(passwords, repeat=new):  # Change repeat value based on the desired combination length
            wordlist.append({'Username': username, 'Password': ''.join(combo)})
    return wordlist

def main():
    username = input("Enter the base username: ")
    passwords_input = input("Enter a list of passwords (comma-separated): ")
    passwords = passwords_input.split(',')

    wordlist = generate_wordlist(username, passwords)

    with open('wordlist.csv', 'w', newline='') as csvfile:
        fieldnames = ['Username', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in wordlist:
            writer.writerow(row)

    print(f'Wordlist generated successfully in wordlist.csv with {len(passwords)}^2 combinations.')

if __name__ == "__main__":
    main()
