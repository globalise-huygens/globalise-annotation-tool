import os
import json

frames = ["Successfully_communicate_message", "Expressing_publicly", "Talking_into", "Having_commercial_agreement", "Setting_out", "Rewards_and_punishments", "Military_operation", "Reveal_secret", "Motion_directional", "Attempt_suasion", "Filling", "Downing", "Request", "Detaining", "Verdict", "Agree_or_refuse_to_act", "Change_tool", "Arriving", "Contacting", "Deny_or_grant_permission", "Change_of_leadership", "Friendly_or_hostile", "Sacrificing_for", "Be_in_agreement_on_action", "Releasing_from_custody", "Preventing_or_letting", "Intentional_traversing", "Sentencing", "Giving", "Operate_vehicle", "Emptying", "Execution", "Forgiveness", "Speak_on_topic", "Killing", "Respond_to_proposal", "Suasion", "Travel", "Fugitive", "Quarreling",
          "Transfer", "Sending", "Make_compromise", "Quitting_a_place", "Surrendering_possession", "Warning", "Bringing", "Execute_plan", "Defending", "Leadership", "Compliance", "Discussion", "Hostile_encounter", "Telling", "Operating_a_system", "Departing", "Traversing", "Make_agreement_on_action", "Jury_deliberation", "Disembarking", "Extradition", "Surrendering", "Statement", "Use_firearm", "Fluidic_motion", "Besieging", "Want_suspect", "Firing", "Claim_ownership", "Be_in_agreement_on_assessment", "Submitting_documents", "Sign_agreement", "Prohibiting_or_licensing", "Motion", "Imprisonment", "Arrest", "Supply", "Reporting", "Try_defendant", "Get_a_job", "Deciding", "Ride_vehicle", "Delivery", "Board_vehicle", "Imposing_obligation"]

for file in os.listdir("lexical_data/typicality/lexical_lookup/nl"):
    if file == "default.json":
        continue
    
    result = {"lexical_lookup": {}, "ordered_frames": []}
    with open(f"lexical_data/typicality/lexical_lookup/nl/{file}") as f:
        data = json.load(f)

    for lemma in data["lexical_lookup"]:
        for pos in data["lexical_lookup"][lemma]:
            for frame_info in data["lexical_lookup"][lemma][pos]:
                frame = frame_info[1].split(" (")[0]
                if frame in frames:
                    if lemma not in result["lexical_lookup"]:
                        result["lexical_lookup"][lemma] = {}

                    if pos not in result["lexical_lookup"][lemma]:
                        result["lexical_lookup"][lemma][pos] = []
                    result["lexical_lookup"][lemma][pos].append(frame_info)

    for frame_info in data["ordered_frames"]:
        frame = frame_info[1].split(" (")[0]
        if frame in frames:
            result["ordered_frames"].append(frame_info)
    
    with open(f"lexical_data/typicality/lexical_lookup/nl/{file}", "w+") as f:
        json.dump(result, f)