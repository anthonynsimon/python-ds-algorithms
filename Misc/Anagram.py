def checkForAnagram(stringA, stringB):
    charListA = list(stringA)
    charlistB = list(stringB)

    charListA.sort()
    charlistB.sort()

    if charListA == charlistB:
        print ("Anagram exists")
        return True
    else:
        print ("The words don't form an Anagram")
        return False

checkForAnagram("caoalba", "bacalao")