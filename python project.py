import schedule
import time
#Import schedule and time in order to run the current time and schedule API
text ='Do not look for healing at the feet of those who broke you.'
#Wrote out the quote to be printed to the terminal at a certain time
#function that will hold the text
def quote():
    print(text)
#schedule API to run the quote every 10 seconds
#Each action I want to the scheduler to do has to be wrote out
#The quote will print to the terminal every couple seconds or couple minutes
#I want the quote to print every tuesday and thursday as well
schedule.every(10).seconds.do(quote)
schedule.every().day.do(quote)
schedule.every().tuesday.do(quote)
schedule.every().thursday.do(quote)
#As long as the above text is true, the API will run at the assigned days and time
while True:
    schedule.run_pending()
    time.sleep(1)
