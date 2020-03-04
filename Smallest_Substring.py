#Function to find number of distinct characters in a given string
def numberOfDistinct(string) :
    unique = []
    for char in string[::]:
        if char not in unique:
            unique.append(char)
    return(len(unique))

#Function to find length of smallest substring with maximum distinct characters
def small_sub( sub_str , present_num) :
    if present_num == 2 :
        return 2
    if len(sub_str) <=1 :
        return len(sub_str)
    
    left_best = len(sub_str) - 1
    left_num = numberOfDistinct(sub_str[0:len(sub_str)-1])
    if left_num == present_num :
        left_best = small_sub(sub_str[0:len(sub_str)-1], present_num)
    
    right_best = len(sub_str) - 1
    right_num = numberOfDistinct(sub_str[1:len(sub_str)])
    if right_num == present_num :
        right_best = small_sub(sub_str[1:len(sub_str)], present_num)
    
    if left_num == present_num :
        if right_num == present_num :
            if left_best <= right_best :
                return left_best
    if right_num == present_num :
        return right_best
    
    return len(sub_str)

string = input("Enter a string: ")
num = numberOfDistinct(string)
ans=small_sub( string , num)
print(ans)
