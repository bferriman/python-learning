import json

input1 = open("experiments/stories1.json")
stories_data_1 = json.load(input1)
input1.close()

input2 = open("experiments/stories2.json")
stories_data_2 = json.load(input2)
input2.close()

id_list_1 = [x["storyId"] for x in stories_data_1]
id_list_2 = [y["storyId"] for y in stories_data_2]

new_stories = [id for id in id_list_2 if id not in id_list_1]
dropped_stories = [id for id in id_list_1 if id not in id_list_2]

print("These are the new story ids:")
for id in new_stories:
    print(id)

print("These are the dropped story ids:")
for id in dropped_stories:
    print(id)