import notify2
#I need to define a function to send notifications to a user's phone from the app
#notify2 was installed with pip and imported into Atom
#Once notify2 was installed, I have to use an init statement to make sure the function
#finds the notifications within the data_url I provide later
#I set notify equal to the notification from the data_url, the actual content from the data_url
#and the qupte that will appear on the phone when the notification is sent
#Finally I printed the Nofication
def send(content):
    notify2.init('https://www.brainyquote.com/topics/inspirational')
    notify = notify2.Notification('https://www.brainyquote.com/topics/inspirational', Inspirational, 'Today I chose life.')
    notify.show()
    print(Notification)
