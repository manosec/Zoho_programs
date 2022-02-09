
def compare(str1, str2):
    if str1[1] != str1[2] and str2[1] != str2[2]:
        if (str1[0] == str1[1] or str1[0] == str1[2]) and (str2[0] != str2[1] or str2[0] != str2[2]):
            return False
        return True
    elif str1[1] == str1[2] and str2[1] == str2[2]:
        return True
    elif (str1[0] != str1[1] or str1[0] != str1[2]) and (str2[0] != str2[1] or str2[0] != str2[2]):
        return False
    elif (str1[0] == str1[1] or str1[0] == str1[2]) and (str2[0] != str2[1] or str2[0] != str2[2]):
        return False
    else:
        return False
        
                
print(compare("ofo","get"))

