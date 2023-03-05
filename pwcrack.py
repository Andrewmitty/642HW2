import hashlib



def passwordGuess(username, password, salt):
    return hashlib.sha256(f"{username},{password},{salt}".encode()).hexdigest()


# create a nested for loop which interates through all ascii strings consisting of only numeric digits up to 8 digits
def crackPassword(username, hash, salt):
    # create a nested for loop which interates through all ascii strings consisting of only numeric digits up to 8 digits
    count = 0
    for one in range(-1, 10):
        for two in range(-1, 10):
            for three in range(-1, 10):
                for four in range(-1, 10):
                    for five in range(-1, 10):
                        for six in range(-1, 10):
                            for seven in range(-1, 10):
                                for eight in range(-1, 10):
                                    # if -1 is the current number, then replace it with a blank space
                                    if one == -1:
                                        one = ""
                                    if two == -1:
                                        two = ""
                                    if three == -1:
                                        three = ""
                                    if four == -1:
                                        four = ""
                                    if five == -1:
                                        five = ""
                                    if six == -1:
                                        six = ""
                                    if seven == -1:
                                        seven = ""
                                    if eight == -1:
                                        eight = ""
                                    # create a string of the current combination of digits
                                    password = str(one) + str(two) + str(three) + str(four) + str(five) + str(
                                        six) + str(seven) + str(eight)
                                    # if the password guess matches the hash, print the password
                                    if passwordGuess(username, password, salt) == hash:
                                        print(password + " is the password for username " + username + " Iteration # ",
                                              count)
                                        return password
                                    if count % 100 == 0:
                                        print("Iteration count: " + str(count) + " for username: " + username +
                                              "current password: " + password)
                                    count += 1

# Verify that the passwordGuess function works given the example in HW2 Writeup

assert(hashlib.sha256("user,12345,999999".encode()).hexdigest() ==
      "c50603be4fedef7a260ef9181a605c27d44fe0f37b3a8c7e8dbe63b9515b8e96")

assert(passwordGuess("user", "12345", "999999") == "c50603be4fedef7a260ef9181a605c27d44fe0f37b3a8c7e8dbe63b9515b8e96")

# Set the hash and salt for each username and run the crackPassword function

bjacobsenHash = "ffa2dcdd84a45582b17d4f535cda63887273f34a679eded10428b480999c3a8b"
bjacobsenSalt = "980166"
crackPassword("bjacobsen", bjacobsenHash, bjacobsenSalt)


# ceccioHash = "41db4f70c8ce1c866462b4c0636aef38c1ea5ef36809bf099165c826bc3a8881"
# ceccioSalt = "547750"
# crackPassword("ceccio", ceccioHash, ceccioSalt)
#
#verifying that the crackPassword function works given my own
# mittyHash = passwordGuess("mitty", "09876543", "123499")
# assert(crackPassword("mitty", mittyHash, "123499") == "09876543")