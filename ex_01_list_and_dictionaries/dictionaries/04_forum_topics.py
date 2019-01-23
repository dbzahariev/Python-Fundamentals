my_dict = {}

data = input()
while not data.lower() == 'filter':
    pair = data.split(' -> ')
    topic = pair[0]
    if topic not in forum_dict:
        forum_dict[topic] = []

    for hashtag in pair[1].split(', '):
        if hashtag not in forum_dict[topic]:
            forum_dict[topic].append(hashtag)

<<<<<<< HEAD
    data = input()

target_topic_set = set(input().split(', '))
for topic, hashtag in forum_dict.items():
    if target_topic_set.issubset(set(hashtag)):
        print(f"{topic} | {', '.join(list(map(lambda x: '#' + x, hashtag)))}")
=======
while True:
    internal = input()
    if internal.lower() == 'filter':
        target_topic = input().split(', ')
        for key, value in my_dict.items():
            if len(value) > 0 and is_contains(target_topic, value):
                value = add_prefix('#', value)
                print(f"{key} | {', '.join(value)}")
        break
    pair = internal.split(' -> ')
    key = pair[0]
    values = pair[1].split(', ')
    if key not in my_dict:
        my_dict[key] = []

    for value in values:
        if value not in my_dict[key]:
            my_dict[key].append(value)
>>>>>>> parent of b7388fb... Add new files
