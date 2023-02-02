WIDTH = 600
HEIGTH = 765

class Get_Position:
    def get_postion(arr,max_position):
        new_arr = []
        one_x_pixel = int(WIDTH/max_position)
        one_y_pixel = int(HEIGTH/len(arr))-30
        new_arr.append((one_x_pixel*arr[0],20))
        for i in range(len(arr)-1):
            new_arr.append((one_x_pixel*arr[i+1],(one_y_pixel)*(i+1)))
        return new_arr

# a = [50, 82, 140, 170, 190, 16, 24, 43]
# Get_Position.get_postion(a,199)