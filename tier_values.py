def tier_values_LoLalytics (tier):
    if tier == "S+":
        return 15
    elif tier == "S":
        return 14
    elif tier == "S-":
        return 13
    elif tier == "A+":
        return 12
    elif tier == "A":
        return 11
    elif tier == "A-":
        return 10
    elif tier == "B+":
        return 9
    elif tier == "B":
        return 8
    elif tier == "B-":
        return 7
    elif tier == "C+":
        return 6
    elif tier == "C":
        return 5
    elif tier == "C-":
        return 4
    elif tier == "D+":
        return 3
    elif tier == "D":
        return 2
    elif tier == "D-":
        return 1
    else:
        return 0
    
def tier_values_Metasrc (tier):
    if tier == "S+":
        return 15
    elif tier == "S":
        return 13
    elif tier == "A":
        return 11
    elif tier == "B":
        return 8
    elif tier == "C":
        return 5
    elif tier == "D":
        return 2
    else:
        return 0
    

def tier_values_mobalytics (tier):
    if tier == "S":
        return 12
    elif tier == "A":
        return 8
    elif tier == "B":
        return 4
    else:
        return 0