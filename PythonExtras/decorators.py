def func_1(callMe):
    print("Function_1 Called")
    return callMe

@func_1
def callMe():
    print("Call Me Called")


#func_1(callMe)
callMe()
