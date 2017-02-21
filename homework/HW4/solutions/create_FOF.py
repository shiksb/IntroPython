def create_FOF(friends):
    # person: friends_of_friends set
    friends_of_friends = {}
    # go through all the name keys
    for person in friends:
        # get the set of the current person's friends
        curr_friends = friends[person]
        # build up a set of friends of friends
        FOFset = set()
        # iterate through all of the friends of the current person
        for friend in curr_friends:
            # make sure that this friend is in the input dict
            if friend in friends:
                # get all of this friend's friends
                friends_of_friend = friends[friend]
                # iterate through all of the friends of this friend
                for FOF in friends_of_friend:
                    # ensure that this FOF is not the original person
                    # nor are they one of the original person's friends
                    if not FOF == person and FOF not in curr_friends:
                        FOFset.add(FOF)
        friends_of_friends[person] = FOFset
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
