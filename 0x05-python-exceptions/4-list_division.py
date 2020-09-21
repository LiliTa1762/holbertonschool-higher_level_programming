#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_length_2 = []
    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            list_length_2.append(r)
    return list_length_2
