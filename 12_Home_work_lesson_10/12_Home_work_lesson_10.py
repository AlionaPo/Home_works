#File-o-Scope: Context Managers & The Great Python Paperwork

#1. Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
#To each file append a random number between 1 and 100. 
#Create a summary file (summary.txt) that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98

import string, os, random
FOLDER_NAME = "letters"

if not os.path.exists(FOLDER_NAME):
   os.makedirs(FOLDER_NAME)

for letter in string.ascii_uppercase:
    with open(f'{FOLDER_NAME}/{letter}.txt', "w") as files:
       random_number = random.randint(1,100)
       files.write(str(random_number))


files_all = os.listdir(FOLDER_NAME)

with open (os.path.join(FOLDER_NAME, "summary.txt"), "w") as summary_file:
   for file_name in files_all:
      if file_name.endswith(".txt") and file_name != "summary.txt":
        with open (os.path.join(FOLDER_NAME, file_name), "r") as file:
            number = file.read().strip()
            summary_file.write(f'{file_name}:{number}\n')


#2. Create a file with some content. As example, you can take this one:
# “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
#Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
#Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum”.
# Create a second file and copy the content of the first file to the second file in upper case.

file1 = open ("New_file1.txt","w")
file1.write("Some day I will be a Python expert")
file1.close()

with open ('New_file1.txt','r') as file1, open ("New_file2.txt","w") as file2:
    data = file1.read()
    file2.write(data)
 

#3 Write a program that will simulate user scores in a game. Create a list with 5 players’ names after that simulate 100 rounds for each player. 
#  As a result of the game create a list with the player's name and score (0-1000 range). And save it to a CSV file.

# The file should look like this:

# Player name, Score
# Josh, 56
# Luke, 784
# Kate, 90
# Mark, 125
# Mary, 877
# Josh, 345
# ...

import csv

# Simulating scores for 5 players over 100 rounds
players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
num_rounds = 100
# scores = [[round(score * 10) for _ in range(num_rounds)] for score in range(len(players))]

# Writing scores to a CSV file
with open('scores.csv', 'w', newline='') as file3:
    writer = csv.writer(file3)
    header = ["Player_name", "Score"]
    writer.writerow(header) # Header row
    for round in range(num_rounds):
        for player in players:
            random_number = random.randint(0,1000)
            writer.writerow([player, random_number ])  # Values by rows



#4 Write a script that reads the data from the previous CSV file 
#and creates a new file called high_scores.csv where each row contains the player name and their highest score.
# The final score should be sorted by descending to the highest score.

# The output CSV file should look like this:
# Player name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345
            
players_dict = {}

with open('scores.csv', 'r') as file4:
    reader = csv.reader(file4)
    next(reader)
    #reader = csv.reader(file4, delimiter=";") in case if there other delimiter, comma by default
    for player, score in reader:
        #print(player, score)
        if player in players_dict.keys():
            if players_dict[player] < int(score):
                players_dict[player] = int(score)

        else:
            players_dict[player] = int(score)
        print(players_dict)

with open('high_scores.csv','w', newline="") as file5:
    writer2 = csv.writer(file5)
    header2 = ["Player_name", "Score"]
    writer2.writerow(header2) # Header row
    #print(sorted(players_dict.items(),key=lambda x: x[1], reverse=True))
    sorted_list = sorted(players_dict.items(),key=lambda x: x[1], reverse=True)
    for item in sorted_list:
        writer2.writerow(item)
    #print(item)