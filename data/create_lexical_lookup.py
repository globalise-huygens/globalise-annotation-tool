import json

with open("lexical_data/lexicons/event_to_info.json", "r") as f:
    event_to_info = json.load(f)

result = {"lexical_lookup": {}, "ordered_frames": []}

for event, event_info in event_to_info.items():
    result["ordered_frames"].append([0, f"{event.split('-')[1]} (0)", event])

with open("lexical_data/typicality/lexical_lookup/nl/default.json", "w+") as f:
    json.dump(result, f)

result = {}

for event, _ in event_to_info.items():
    result[event.split("-")[1]] = 0

with open("lexical_data/typicality/typicality_scores/default.json", "w+") as f:
    json.dump(result, f)