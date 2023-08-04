stories_dict = {}

while True:
    command = input()
    if command == "End":
        break

    input_data = command.split(" ->")
    pre_story = input_data[0]
    post_story = input_data[1].split() if input_data[1] else []

    stories_dict[pre_story] = post_story

result = []

def find_story_line(pre_story, stories_dict, result):
    if not stories_dict[pre_story]:
        if pre_story not in result:
            result.append(pre_story)
        return

    for post_story in stories_dict[pre_story]:
        find_story_line(post_story, stories_dict, result)

    stories_dict[pre_story] = []
    result.append(pre_story)


for pre_story in stories_dict:
    find_story_line(pre_story, stories_dict, result)

print(*reversed(result), sep=" ")
