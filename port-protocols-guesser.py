import os
import random
import time

# List of protocols and ports
protocols_list = [
    ("File Transfer Protocol (FTP)", "20/21"),
    ("Secure Shell (SSH)", "22"),
    ("Secure File Transfer Protocol (SFTP)", "22"),
    ("Telnet", "23"),
    ("Simple Mail Transfer Protocol (SMTP)", "25"),
    ("Domain Name System (DNS)", "53"),
    ("Dynamic Host Configuration Protocol \n(DHCP)", "67/68"),
    ("Trivial File Transfer Protocol (TFTP)", "69"),
    ("Hypertext Transfer Protocol (HTTP)", "80"),
    ("Post Office Protocol v3 (POP3)", "110"),
    ("Network Time Protocol (NTP)", "123"),
    ("Internet Message Access Protocol (IMAP)", "143"),
    ("Simple Network Management Protocol \n(SNMP)", "161/162"),
    ("Lightweight Directory Access Protocol \n(LDAP)", "389"),
    ("Hypertext Transfer Protocol Secure \n(HTTPS) [Secure Sockets Layer (SSL)]", "443"),
    ("HTTPS [Transport Layer Security (TLS)]", "443"),
    ("Server Message Block (SMB)", "445"),
    ("Syslog", "514"),
    ("SMTP TLS", "587"),
    ("Lightweight Directory Access Protocol \n(over SSL) (LDAPS)", "636"),
    ("IMAP over SSL", "993"),
    ("POP3 over SSL", "995"),
    ("Structured Query Language (SQL) Server", "1433"),
    ("SQLnet", "1521"),
    ("MySQL", "3306"),
    ("Remote Desktop Protocol (RDP)", "3389"),
    ("Session Initiation Protocol (SIP)", "5060/5061")
]

def play_game():
    # Clear the screen
    os.system("clear")

    # Start the game
    print("Welcome to the Ports and Protocols game!\n")
    print("You will be presented with a protocol.\n")
    print("Your task is to enter the \ncorresponding port number.\n")
    input("Press Enter to start the game...")

    # Game variables
    correct_count = 0
    total_count = len(protocols_list)

    # Copy the protocols list to a new list to keep track of remaining protocols
    remaining_protocols = protocols_list.copy()

    # Iterate until all protocols are answered correctly or the user quits
    while len(remaining_protocols) > 0:
        # Clear the screen
        os.system("clear")

        # Randomly select a protocol from the remaining protocols
        protocol, port = random.choice(remaining_protocols)

        # Display the protocol
        print(f"Protocol: {protocol}\n")

        # Ask the user to enter the corresponding port number
        user_answer = input("Enter the port number (or 'q' to quit): ")
        if user_answer.lower() == "q":
            break

        if user_answer == port:
            # Correct answer
            print("\nCorrect!")
            correct_count += 1
            time.sleep(1)

            # Remove the protocol from the remaining protocols
            remaining_protocols.remove((protocol, port))
        else:
            # Incorrect answer
            print(f"\nIncorrect. The correct port number is {port}.")
            time.sleep(3)

    # Clear the screen
    os.system("clear")

    # Display the game results
    print(f"You scored {correct_count} out of {total_count}.\n")

# Start the game
play_game()

# Ask the user if they want to
while True:
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() == "y":
        play_game()
    elif play_again.lower() == "n":
        print("\nThanks for playing!")
        break
    else:
        print("Invalid input. Please enter Y or N.")
