def get_weight(courier_type):
    DATA = {"foot": 10, "bike": 15, "car": 50}
    weight_max = DATA[str(courier_type)]
    return weight_max
