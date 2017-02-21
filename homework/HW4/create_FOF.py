def create_FOF(friends):
    #Your codes here


    return friends_of_friends


if __name__ == '__main__':
    friends = {}
    friends["Caro"] = set(["Ben", "Yanlin", "Sahil"])
    friends["Sahil"] = set(["Caro", "James", "Shreyas"])
    friends["Vidya"] = set(["Caro", "Yanlin", "Sahil", "Shreyas"])
    friends["Ben"] = set(["Yanlin", "Caro", "Vidya"])

    fof = {}
    fof["Caro"] = set(["Vidya","James","Shreyas"])
    fof["Sahil"] = set(["Ben", "Yanlin"])
    fof["Vidya"] = set(["Ben", "James"])
    fof["Ben"] = set(["Sahil", "Shreyas"])

    print("Friends Input:", friends)
    print("Your output:", create_FOF(friends))
    print("Expected output:", fof)
