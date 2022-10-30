import os
import json

frames = ["Bringing", "Travel", "Submitting_documents", "Quarreling", "Execution", "Quitting_a_place", "Emptying", "Motion", "Suasion", "Change_tool", "Surrendering_possession", "Rotting", "Fluidic_motion", "Transfer", "Lose_possession", "Besieging", "Hindering", "Respond_to_proposal", "Reporting", "Traversing", "Intentional_traversing", "Be_in_agreement_on_action", "Delivery", "Be_in_agreement_on_assessment", "Warning", "Cotheme", "Origin", "Contacting", "Fear", "Discussion", "Preventing_or_letting", "Arrest", "Rewards_and_punishments", "Detaining", "Try_defendant", "Friendly_or_hostile", "Agree_or_refuse_to_act", "Giving", "Becoming_aware ", "Compliance", "Supply", "Extradition", "Leadership", "Arriving", "Military_operation", "Operating_a_system", "Filling", "Departing", "Attempt_suasion", "Imprisonment", "Sending", "Abandonment ", "Deciding", "Receiving", "Telling", "Sign_agreement", "Hostile_encounter", "Downing", "Having_commercial_agreement", "Prohibiting_or_licensing", "Destroy", "Giving_in", "Reparation", "Sacrificing_for", "Deny_or_grant_permission", "Change_of_leadership", "Control ", "Jury_deliberation", "Fugitive", "Ride_vehicle", "Process_continue", "Expressing_publicly", "Statement", "Request", "Make_compromise", "Disembarking", "Successfully_communicate_message", "Activity_resume", "Use_firearm", "Make_agreement_on_action", "Releasing_from_custody", "Forgiveness", "Verdict", "Motion_directional", "Setting_out", "Destroy ", "Speak_on_topic", "Killing", "Imposing_obligation", "Operate_vehicle", "Sentencing", "Defending", "Board_vehicle", "Abandonment", "Surrendering", "Want_suspect", "Claim_ownership"]

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
