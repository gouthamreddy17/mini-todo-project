data = {
    1: {
        "todo": "Reading a book",
        "markas": "Done"
    },
    2: {
        "todo": "Learn Python",
        "markas": "Pending"
    },
    3: {
        "todo": "Complete DSA Practice",
        "markas": "Done"
    },
    4: {
        "todo": "Watch AI Tutorial",
        "markas": "Pending"
    },
    5: {
        "todo": "Build To-Do App",
        "markas": "Done"
    },
    6: {
        "todo": "Update Resume",
        "markas": "Done"
    },
    7: {
        "todo": "Apply for Internship",
        "markas": "Pending"
    },
    8: {
        "todo": "Exercise for 30 Minutes",
        "markas": "Done"
    },
    9: {
        "todo": "Practice Aptitude Questions",
        "markas": "Pending"
    },
    10: {
        "todo": "Learn Git and GitHub",
        "markas": "Done"
    }
}

def showall(data):
    l=[]
    for i in data:
        l.append(data[i])
    for i in l:
        print(i)

def add(id,todo,markas):
    if id in data:
        return "Data already exists"
    data[id]={
        "todo":todo,
        "markas":markas
    }
    return "added sucessfully"

def delete(id):
    if id not in data:
        return "Task Not Found"
    else:
        del data[id]
    return "Deleted Sucessfully"
def update(id,todo,markas):
    if id not in data:
        return "Task not found"
    
    data[id]['todo']=todo
    data[id]['markas']=markas
    return list(data.items())
    
def markased():
    completed=[]
    for i in data:
        if data[i]['markas']=="Done":
            completed.append(data[i]['todo'])
    if len(completed)==0:
        return "There is no complted Tasks"
    else:
        for i in completed:
            print([i])
    
def unmarked():
    uncomplete=[]
    for i in data:
        if data[i]['markas']=="Pending":
            uncomplete.append(data[i]['todo'])
    if len(uncomplete)==0:
        return "There is no uncomplte tasks"
    else:
        for i in uncomplete:
            print([i])


if __name__=='__main__':
    print("welcome To small To-Do list")
    while True:
        print("Choose any operation")
        print("1.Show all tasks \n 2.Add tasks \n 3.Update tasks \n 4.Delete Tasks \n 5.Show Completed Tasks \n 6.Show Uncompleted Tasks \n 7.Exit")
        choose=int(input("Enter your choise: "))
        if choose==1:
            showall(data)
        elif choose==2:
            id=int(input("Enter the id: "))
            todo=input("Enter your Task: ")
            markas=input("Enter it is markas Done or not: ")
            res=add(id,todo,markas)
            print(res)
        elif choose==3:
            id=int(input("Enter id Here: "  ))
            todo=input("Enter the task to be updated: ")
            markas=input("Enter the markas option for update: ")
            res=update(id,todo,markas)
            print(res)
        elif choose==4:
            id=int(input('Enter the id to delete: '))
            res=delete(id)
            print(res)
        elif choose==5:
            markased()
        elif choose==6:
            unmarked()
        elif choose==7:
            print("!!!THANK YOU!!!   --VISIT AGAIN--")
            exit()
        else:
            print("Invalis Choice")