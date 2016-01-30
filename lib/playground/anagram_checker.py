def check_for_anagram(string_a, string_b):
    char_list_a = list(string_a)
    char_list_b = list(string_b)

    char_list_a.sort()
    char_list_b.sort()

    if char_list_a == char_list_b:
        print ("Anagram exists")
        return True
    else:
        print ("The words don't form an Anagram")
        return False

check_for_anagram("caoalba", "bacalao")