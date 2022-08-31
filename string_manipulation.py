def string_manipulate(str):
    originalString = str
    replacedString = originalString.replace('/', '\\')
    reversedString = replacedString[::-1]
    slashpos = reversedString.find('\\')
    appendString = reversedString[slashpos+1:]
    finalString = appendString [::-1]
    # #Setting main folder and image pattern
    src_folder = finalString + '\\'
    return(src_folder)