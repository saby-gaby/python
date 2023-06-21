class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'

emails = []

while True:
    message = input()
    if message == 'Stop':
        break
    sender, receiver, content = message.split()
    emails.append(Email(sender, receiver, content))



indexes = [int(index) for index in input().split(', ')]
for i in indexes:
    emails[i].send()

for mail in emails:
    print(mail.get_info())