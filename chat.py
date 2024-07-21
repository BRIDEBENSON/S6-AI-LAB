qap={
    "a":"b",
    "c":"d"
}
def getr(ui):
    for key,val in qap.items():
        if ui.lower()==key.lower():
            return val

while True:
    ui=input("you: ")   
    resp=getr(ui)
    print("chat: ",resp) 
    if ui.lower()=="c":
        break
