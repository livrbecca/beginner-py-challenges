# parameter weekday is True if its a weekday, and vacation is True if on vacation
# sleep in if its NOT a weekday or youre on vacation
# return True if you're sleeping in

# if weekday == True or vacation == True:
# return True
# else:
# retutn false

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
