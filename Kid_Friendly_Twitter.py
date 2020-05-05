import tweepy

consumer_key =
consumer_secret =
access_token =
access_token_secret =

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def filter(word):
    a_file = open("translated_words.txt", "r")

    bad_word = {}
    for line in a_file:
        stripped_line = line.strip()
        x, y = stripped_line.split(" = ")
        bad_word[x] = y
    a_file.close()

    wordcheck = 0
    for i in bad_word:
        if(i in word.lower()):
            word.lower().replace(i, bad_word[i])
            #print(word.lower().replace(i, bad_word[i]), end=" ")
            return(word.lower().replace(i, bad_word[i]))
            wordcheck += 1
            break
    if(wordcheck == 0):
        #print(word, end=" ")
        return(word)

def main():
    while(True):
        action = input("\nWhat would you like to do?\n\t1) Search User\n\t2) Search Twitter\n\t3) Post Update\n\t4) Quit\n> ")
        if(action.isdigit() and int(action) < 7 and int(action) > 0):
            action = int(action)
            if(action == 1):
                handle = input("Which user would you like to look up?: ")
                choice = input("What would you like to do?\n\t1) Print Timeline\n\t2) Print Friends list\n> ")
                while(True):
                    if(choice.isdigit() and int(choice) < 3 and int(action) > 0):
                        choice = int(choice)
                        if(choice == 1):
                            statuses = api.user_timeline(handle)
                            # statuses = api.GetUserTimeline(screen_name = handle, count = 20, include_rts = False)
                            i = 1
                            for status in statuses:
                                print(str(i) + ") ", end="")
                                split_text = status.text.split()
                                for j in split_text:
                                    print(filter(j), end =" ")
                                print()
                                i+=1
                            #break
                        if(choice == 2):
                            friends = api.friends(screen_name=handle, count=20)
                            #friends = api.friends(handle)
                            i = 1
                            for friend in friends:
                                #print(str(i) + ") " + friend.name)
                                print(str(i) + ") ", end="")
                                split_text = friend.name.split()
                                for j in split_text:
                                    print(filter(j), end = " ")
                                print()
                                i += 1
                        break
                    else:
                        print("Not a Valid Choice")
                        break

            if(action == 2):
                handle = input("What would you like to look up on twitter?: ")
                choice = input("What would you like to see?\n\t1) Popular\n\t2) Latest\n> ")
                while(True):
                    if(choice.isdigit() and int(choice) < 3 and int(action) > 0):
                        choice = int(choice)
                        if(choice == 1):
                            results = api.search(q=handle, result_type="popular")
                            i = 1
                            for result in results:
                                #print(result.text.encode('utf-8'))
                                print(str(i) + ") ", end="")
                                #split_text = result.text.encode('utf-8').split()
                                split_text = result.text.split()
                                for j in split_text:
                                    print(filter(j), end = " ")
                                print()
                                i += 1
                        else:
                            results = api.search(q=handle, result_type="recent")
                            i = 1
                            for result in results:
                                # print(result.text.encode('utf-8'))
                                print(str(i) + ") ", end="")
                                # split_text = result.text.encode('utf-8').split()
                                split_text = result.text.split()
                                for j in split_text:
                                    print(filter(j), end = " ")
                                print()
                                i += 1
                        break
                    else:
                        print("Not a Valid Choice")
                        break

            if(action == 3):
                tweet = input("What would you like your update to say?: ")
                split_text = tweet.split()
                message = ""
                for j in split_text:
                    message += filter(j)
                    message += " "
                print(message)
            if(action == 4):
                print("Have a good day!")
                break
        else:
            print("Not a Valid Option")
main()
