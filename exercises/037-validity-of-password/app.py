def valid_password(password):
    if len(password) > 12 or len(password)<6:
        return "Invalid password. Please try again"
    conditions = {"lower":False,"numbers":False,"upper":False,"spChar":False}
    for l in password:
        if l.islower() : conditions["lower"] =True
        elif l.isupper() : conditions["upper"] = True
        elif l.isdigit() : conditions["numbers"] = True
        elif l in ['$','#','@'] : conditions["spChar"] = True
    if all(conditions.values()):
        return "Valid password"
    return "Invalid password. Please try again"