class User:
    def __init__(self, Username, ReceivedMessages):
        self.Username = Username
        self.ReceivedMessages = ReceivedMessages


class Message:
    def __init__(self, Content, Sender):
        self.Content = Content
        self.Sender = Sender


users_list = []
message_all = []

while True:
    data = input()
    if data == 'exit':
        data = input().split(' ')
        count_message = 0
        from_user = data[0]
        to_user = data[1]

        for i in range(0, 1000):
            for_user = [from_user, to_user][i % 2]
            print(for_user)
        # for user in users_list:
        #     for message in user.ReceivedMessages:
        #         print(user)

        # for user in users_list:
        #     if user.Username == from_user or user.Username == to_user:
        #         for message in user.ReceivedMessages:
        #             if message.Sender == to_user or message.Sender == from_user:
        #                 count_message += 1
        #                 kk = [from_user, to_user, message.Content]
        # message_all.append(kk)
        break
    data = data.split()
    if data[0] == 'register':
        one_user = User(data[1], [])
        if one_user not in users_list:
            users_list.append(one_user)
    else:
        one_massage = Message(data[3], data[0])
        for user in users_list:
            if user.Username == data[2]:
                user.ReceivedMessages.append(one_massage)

print(message_all)
