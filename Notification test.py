#I need to define a function to send notifications to a user's phone from the app
#notify2 was installed with pip and imported into Atom
#Once notify2 was installed, I have to use an init statement to make sure the function
finds the notifications within the data_url I provide later
#I set notify equal to the notification from the data_url, the actual content from the data_url
and the qupte that will appear on the phone when the notification is sent
#Finally I printed the Nofication 
def send(content)
    import notify2
    notify2.init('data_url')
    notify = notify2.Notification('data_url', content, 'quote')
    notify.show()
        print(Notification)
