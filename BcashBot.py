import praw
import keys
import time
import os
import random


Footer = "*\n\nFixed it for you.\n\n---\n^\(I ^am ^a ^bot.) ^[*Info*](https://reddit.com/user/BcashBot/comments/98wot8/what_is_this_bot/) ^/ ^[*Code*](https://github.com/Btc-Dev/BcashBot) ^/ ^[*Donate*](https://www.blockchain.com/btc/address/3KnT5RWFYqtAy4DsPGyjXvX3i4VkyU1LLx)"

    
def bot_login():
        print ("Logging in...")
        r = praw.Reddit(username = keys.username,
                                password = keys.password,
                                client_id = keys.client_id,
                                client_secret = keys.client_secret,
                                user_agent = "BcashBot")
        print ("Logged in!")

        return r


def run_bot(r, comments_replied_to):
        print ("Searching last 1,000 comments")
        
        for comment in r.subreddit('Bitcoin').comments(limit=1000):

                 if "BitcoinCash" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
                         print ("String with \"BitcoinCash\" found in comment " + comment.id)
                         
                         with open ("comment_text.txt", "a") as p:
                                p.write(comment.body)

                         with open("comment_text.txt", "r") as q: 
                                text = q.read() 
                                text = text.replace("BitcoinCash", "Bcash")
                                text = text.replace("Bitcoincash", "Bcash")
                                text = text.replace("Bitcoin Cash", "Bcash")
                                text = text.replace("Bitcoin cash", "Bcash")
                                text = text.replace("bitcoin cash", "Bcash")
                                text = text.replace("bitcoincash", "Bcash")
                                text = text.replace("bitcoin Cash", "Bcash")
                                text = text.replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')
                                
                         ans = "> " + text + Footer
                         comment.reply(ans)
                         print ("Replied to comment " + comment.id)
                         open("comment_text.txt", 'w').close()

                         comments_replied_to = [];
                         comments_replied_to.append(comment.id)

                         with open ("comments_replied_to.txt", "a") as f:
                                f.write(comment.id + "\n")
                        
                         print ("Search Completed.")

                         print (comments_replied_to)
                        
                         print ("Sleeping for 10 minutes...")
                                        
                         time.sleep(600)

                 else:
                         
                     if "Bitcoincash" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
                             print ("String with \"Bitcoincash\" found in comment " + comment.id)
                         
                             with open ("comment_text.txt", "a") as p:
                                    p.write(comment.body)

                             with open("comment_text.txt", "r") as q: 
                                    text = q.read() 
                                    text = text.replace("BitcoinCash", "Bcash")
                                    text = text.replace("Bitcoincash", "Bcash")
                                    text = text.replace("Bitcoin Cash", "Bcash")
                                    text = text.replace("Bitcoin cash", "Bcash")
                                    text = text.replace("bitcoin cash", "Bcash")
                                    text = text.replace("bitcoincash", "Bcash")
                                    text = text.replace("bitcoin Cash", "Bcash")
                                    text = text.replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')

                             ans = "> " + text + Footer
                             comment.reply(ans)
                             print ("Replied to comment " + comment.id)
                             open("comment_text.txt", 'w').close()

                             comments_replied_to = [];
                             comments_replied_to.append(comment.id)

                             with open ("comments_replied_to.txt", "a") as f:
                                    f.write(comment.id + "\n")
                        
                             print ("Search Completed.")

                             print (comments_replied_to)
                        
                             print ("Sleeping for 10 minutes...")
                                        
                             time.sleep(600)

                     else:

                         if "Bitcoin Cash" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
                                 print ("String with \"Bitcoin Cash\" found in comment " + comment.id)
                         
                                 with open ("comment_text.txt", "a") as p:
                                        p.write(comment.body)
        
                                 with open("comment_text.txt", "r") as q: 
                                        text = q.read() 
                                        text = text.replace("BitcoinCash", "Bcash")
                                        text = text.replace("Bitcoincash", "Bcash")
                                        text = text.replace("Bitcoin Cash", "Bcash")
                                        text = text.replace("Bitcoin cash", "Bcash")
                                        text = text.replace("bitcoin cash", "Bcash")
                                        text = text.replace("bitcoincash", "Bcash")
                                        text = text.replace("bitcoin Cash", "Bcash")
                                        text = text.replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')
       
                                 ans = "> " + text + Footer
                                 comment.reply(ans)
                                 print ("Replied to comment " + comment.id)
                                 open("comment_text.txt", 'w').close()

                                 comments_replied_to = [];
                                 comments_replied_to.append(comment.id)

                                 with open ("comments_replied_to.txt", "a") as f:
                                        f.write(comment.id + "\n")
                        
                                 print ("Search Completed.")

                                 print (comments_replied_to)
                        
                                 print ("Sleeping for 10 minutes...")
                                        
                                 time.sleep(600)

                         else:

                             if "Bitcoin cash" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
                                     print ("String with \"Bitcoin cash\" found in comment " + comment.id)
                         
                                     with open ("comment_text.txt", "a") as p:
                                            p.write(comment.body)

                                     with open("comment_text.txt", "r") as q: 
                                            text = q.read() 
                                            text = text.replace("BitcoinCash", "Bcash")
                                            text = text.replace("Bitcoincash", "Bcash")
                                            text = text.replace("Bitcoin Cash", "Bcash")
                                            text = text.replace("Bitcoin cash", "Bcash")
                                            text = text.replace("bitcoin cash", "Bcash")
                                            text = text.replace("bitcoincash", "Bcash")
                                            text = text.replace("bitcoin Cash", "Bcash")
                                            text = text.replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')
  
                                     ans = "> " + text + Footer
                                     comment.reply(ans)
                                     print ("Replied to comment " + comment.id)
                                     open("comment_text.txt", 'w').close()

                                     comments_replied_to = [];
                                     comments_replied_to.append(comment.id)

                                     with open ("comments_replied_to.txt", "a") as f:
                                            f.write(comment.id + "\n")
                        
                                     print ("Search Completed.")

                                     print (comments_replied_to)
                        
                                     print ("Sleeping for 10 minutes...")
                                        
                                     time.sleep(600)

                             else:

                                 if "bitcoin cash" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
                                         print ("String with \"bitcoin cash\" found in comment " + comment.id)
                         
                                         with open ("comment_text.txt", "a") as p:
                                                p.write(comment.body)

                                         with open("comment_text.txt", "r") as q: 
                                                text = q.read() 
                                                text = text.replace("BitcoinCash", "Bcash")
                                                text = text.replace("Bitcoincash", "Bcash")
                                                text = text.replace("Bitcoin Cash", "Bcash")
                                                text = text.replace("Bitcoin cash", "Bcash")
                                                text = text.replace("bitcoin cash", "Bcash")
                                                text = text.replace("bitcoincash", "Bcash")
                                                text = text.replace("bitcoin Cash", "Bcash")
                                                text = text.replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')
                                
                                         ans = "> " + text + Footer
                                         comment.reply(ans)
                                         print ("Replied to comment " + comment.id)
                                         open("comment_text.txt", 'w').close()

                                         comments_replied_to = [];
                                         comments_replied_to.append(comment.id)

                                         with open ("comments_replied_to.txt", "a") as f:
                                                f.write(comment.id + "\n")
                        
                                         print ("Search Completed.")
    
                                         print (comments_replied_to)
                        
                                         print ("Sleeping for 10 minutes...")
                                        
                                         time.sleep(600)

                                 else:

                                     if "bitcoincash" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
                                             print ("String with \"bitcoincash\" found in comment " + comment.id)
                         
                                             with open ("comment_text.txt", "a") as p:
                                                    p.write(comment.body)

                                             with open("comment_text.txt", "r") as q: 
                                                    text = q.read() 
                                                    text = text.replace("BitcoinCash", "Bcash")
                                                    text = text.replace("Bitcoincash", "Bcash")
                                                    text = text.replace("Bitcoin Cash", "Bcash")
                                                    text = text.replace("Bitcoin cash", "Bcash")
                                                    text = text.replace("bitcoin cash", "Bcash")
                                                    text = text.replace("bitcoincash", "Bcash")
                                                    text = text.replace("bitcoin Cash", "Bcash")
                                                    text = text.replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')

                                             ans = "> " + text + Footer
                                             comment.reply(ans)
                                             print ("Replied to comment " + comment.id)
                                             open("comment_text.txt", 'w').close()

                                             comments_replied_to = [];
                                             comments_replied_to.append(comment.id)

                                             with open ("comments_replied_to.txt", "a") as f:
                                                    f.write(comment.id + "\n")
                        
                                             print ("Search Completed.")

                                             print (comments_replied_to)
                                
                                             print ("Sleeping for 10 minutes...")
                                        
                                             time.sleep(600)

                                     else:

                                         if "bitcoin Cash" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
                                                 print ("String with \"Bitcoin Cash\" found in comment " + comment.id)
                         
                                                 with open ("comment_text.txt", "a") as p:
                                                        p.write(comment.body)

                                                 with open("comment_text.txt", "r") as q: 
                                                        text = q.read() 
                                                        text = text.replace("BitcoinCash", "Bcash")
                                                        text = text.replace("Bitcoincash", "Bcash")
                                                        text = text.replace("Bitcoin Cash", "Bcash")
                                                        text = text.replace("Bitcoin cash", "Bcash")
                                                        text = text.replace("bitcoin cash", "Bcash")
                                                        text = text.replace("bitcoincash", "Bcash")
                                                        text = text.replace("bitcoin Cash", "Bcash")
                                                        text = text.replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')

                                                 ans = "> " + text + Footer
                                                 comment.reply(ans)
                                                 print ("Replied to comment " + comment.id)
                                                 open("comment_text.txt", 'w').close()

                                                 comments_replied_to = [];
                                                 comments_replied_to.append(comment.id)
  
                                                 with open ("comments_replied_to.txt", "a") as f:
                                                        f.write(comment.id + "\n")
                        
                                                 print ("Search Completed.")

                                                 print (comments_replied_to)
                                    
                                                 print ("Sleeping for 10 minutes...")
                                        
                                                 time.sleep(600)

                                           
                                         

def get_saved_comments():
        if not os.path.isfile("comments_replied_to.txt"):
                comments_replied_to = []
        else:
                with open("comments_replied_to.txt", "r") as f: 
                        comments_replied_to = f.read()
                        comments_replied_to = comments_replied_to.split("\n") 

        return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()
print (comments_replied_to)

while True:
        print ("Sleeping for 5 seconds...")
        time.sleep(5)
        run_bot(r, comments_replied_to)

# END #
