#length and width of top platform
mat_top_l = 1265
mat_top_w = 100
#length and width of bottom platform
mat_bot_l = 1265
mat_bot_w = 100
#I structure, height and length
I_height = 226
I_l = 1265
#Area of matboard given
T_area = 1016*813

def remaining_area():
    '''Calculates the remaining amount of area that we are able to use after structures

    Args:
        None

    Returns:
        integer: (remaining area of matboard (mm^2))
    '''
    area = T_area

    #subtracts area 
    area -= mat_top_l*mat_top_w
    area -= mat_bot_l*mat_bot_w
    #double I, mult 2
    area -= 2*(I_height*I_l)

    return area

if __name__ == "__main__":
    print(remaining_area())