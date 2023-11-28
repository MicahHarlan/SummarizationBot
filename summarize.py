import os.path
import bot

#file_path = sum_bot.summarize(input())
file_path = input("Enter .txt file name (must be in the same directory and include extension): ")
# check if file exists
if os.path.isfile('./'+ file_path):
    print("File found. Please wait.")
    # open file
    f = open('./'+file_path, "r", encoding="utf8")
    lines = f.readlines()
    text = ""
    # build string from each line in file
    for line in lines:
        text += line
    # pass resulting text to bot
    summary = bot.hand_response(text)
    print('Summary:\n' + summary)
else:
    print("Invalid filename.")
    