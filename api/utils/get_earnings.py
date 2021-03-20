def get_salary(courier_type, completed_orders):
    DATA = {"foot": 2, "bike": 5, "car": 9}
    salary = 500 * DATA[str(courier_type)] * completed_orders
    return salary
