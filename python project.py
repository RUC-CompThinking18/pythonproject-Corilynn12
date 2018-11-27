import schedule
import time
#Import schedule and time in order to run the current time and schedule API
text ='Do not look for healing at the feet of those who broke you.'
text2 = 'You are the light that most people will never deserve'
#Wrote out the quote to be printed to the terminal at a certain time
#function that will hold the text
def quote():
    print(text)
def quote2():
    print(text2)
#schedule API to run the quote every  certain amount of seconds
#Each action I want to the scheduler to do has to be wrote out
#The quote will print to the terminal every couple seconds or couple minutes
schedule.every(30).seconds.do(quote)
schedule.every(01).minutes.do(quote2)
#As long as the above text is true, the API will run at the assigned days and time
while True:
    schedule.run_pending()
    time.sleep(60)
