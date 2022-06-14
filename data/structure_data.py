import json

group_data, entity_data = None, None

with open("structured raw/grouped_files.json", "r") as f:
    group_data = json.load(f)

with open("structured raw/entities.json", "r") as f:
    entity_data = json.load(f)


labels = {}
type2inc = {}
proj2inc = {"pilot": []}
inc2lang2doc = {}
inc2str = {}

for inc_type in group_data:
    labels[inc_type] = f"Vesting {inc_type}"
    type2inc[inc_type] = list(group_data[inc_type].keys())

    for inc in group_data[inc_type]:
        labels[inc] = f"Jaar {inc}"
        proj2inc["pilot"].append(inc)
        inc2lang2doc[inc] = {"nl": []}
        inc2lang2doc[inc]["nl"] = group_data[inc_type][inc]

        inc2str[inc] = {"sem:hasTimeStamp": [f"{inc} | {inc}"],
                        "sem:hasActor": [], "sem:hasPlace": []}

        ent_inc = inc.split(",")[0]
        for item in entity_data[inc_type].get(ent_inc, []):
            str_item = f"{item['id']} | {item['text']}"
            if item["type"] in ["PER", "ORG", "SHP", "LOCderiv"]:
                inc2str[inc]["sem:hasActor"].append(str_item)
            elif item["type"] in ["LOC"]:
                inc2str[inc]["sem:hasPlace"].append(str_item)

with open("structured/labels.json", "w+") as f:
    json.dump(labels, f)

with open("structured/type2inc_index.json", "w+") as f:
    json.dump(type2inc, f)

with open("structured/proj2inc_index.json", "w+") as f:
    json.dump(proj2inc, f)

with open("structured/inc2str_index.json", "w+") as f:
    json.dump(inc2str, f)

with open("structured/inc2lang2doc_index.json", "w+") as f:
    json.dump(inc2lang2doc, f)

default_typicality = None
with open("lexical_data/typicality/typicality_scores/default.json", "r") as f:
    default_typicality = json.load(f)

for inc_type in group_data:
    with open(f"lexical_data/typicality/typicality_scores/{inc_type}.json", "w+") as f:
        json.dump(default_typicality, f)

default_ll = None
with open("lexical_data/typicality/lexical_lookup/nl/default.json", "r") as f:
    default_ll = json.load(f)

for inc_type in group_data:
    with open(f"lexical_data/typicality/lexical_lookup/nl/{inc_type}.json", "w+") as f:
        json.dump(default_ll, f)