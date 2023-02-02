#(82,170,43,140,24,16,190)

class Set_sequnce:

    def FCFS(arr,starting_point):
        input_array = []
        input_array = arr
        input_array.insert(0,starting_point)
        return input_array

    def SSTF(arr,starting_point):
        input_array = []
        input_array = arr
        temp_array = []
        final_array = []
        current = starting_point
        while(len(input_array)!=0):
            for i in range(len(input_array)):
                temp_array.append(abs(current-input_array[i]))
            final_array.append(input_array[temp_array.index(min(temp_array))])
            current = input_array[temp_array.index(min(temp_array))]
            input_array.remove(input_array[temp_array.index(min(temp_array))])
            temp_array = []
        final_array.insert(0,starting_point)
        return final_array

    def SCAN(arr,starting_point,ending_value):
        input_array = []
        temp_array = []
        temp_array_1 = []
        final_array = []
        input_array = arr
        for i in range(len(input_array)):
            if(starting_point<input_array[i]):
                temp_array.append(input_array[i])
        temp_array.sort()
        temp_array.append(ending_value)
        for i in range(len(input_array)):
            if(starting_point>=input_array[i]):
                temp_array_1.append(input_array[i])
        temp_array_1.sort()
        temp_array_1.reverse()
        final_array = temp_array+temp_array_1
        final_array.insert(0,starting_point)
        return final_array

    def CSCAN(arr,starting_point,ending_value,starting_value):
        input_array = []
        temp_array = []
        temp_array_1 = []
        final_array = []
        input_array = arr
        for i in range(len(input_array)):
            if(starting_point<input_array[i]):
                temp_array.append(input_array[i])
        temp_array.sort()
        temp_array.append(ending_value)
        temp_array.append(starting_value)
        for i in range(len(input_array)):
            if(starting_point>=input_array[i]):
                temp_array_1.append(input_array[i])
        temp_array_1.sort()
        final_array = temp_array+temp_array_1
        final_array.insert(0,starting_point)
        return final_array

    def LOOK(arr,starting_point):
        input_array = []
        temp_array = []
        temp_array_1 = []
        final_array = []
        input_array = arr
        for i in range(len(input_array)):
            if(starting_point<input_array[i]):
                temp_array.append(input_array[i])
        temp_array.sort()
        for i in range(len(input_array)):
            if(starting_point>=input_array[i]):
                temp_array_1.append(input_array[i])
        temp_array_1.sort()
        temp_array_1.reverse()
        final_array = temp_array+temp_array_1
        final_array.insert(0,starting_point)
        return final_array

    def CLOOK(arr,starting_point):
        input_array = []
        temp_array = []
        temp_array_1 = []
        final_array = []
        input_array = arr
        for i in range(len(input_array)):
            if(starting_point<input_array[i]):
                temp_array.append(input_array[i])
        temp_array.sort()
        for i in range(len(input_array)):
            if(starting_point>=input_array[i]):
                temp_array_1.append(input_array[i])
        temp_array_1.sort()
        final_array = temp_array+temp_array_1
        final_array.insert(0,starting_point)
        return final_array

class Time_calculation:
    def SEEK_TIME(arr):
        seek_time = 0
        for i in range(len(arr)-1):
            seek_time = seek_time + abs(arr[i]-arr[i+1])
        return seek_time

# a = [82]
# b = Time_calculation.SEEK_TIME(a)
# print(b)