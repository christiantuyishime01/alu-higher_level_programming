#!/usr/bin/python3
def list_division(mylist1, mylist2, list_length):
    results = []
    try:
        for i in range(list_length):
            try:
                results.append(mylist1[i] / mylist2[i])
            except TypeError:
                print("wrong type")
                results.append(0)
            except ZeroDivisionError:
                print("division by 0")
                results.append(0)
            except IndexError:
                print("out of range")
                results.append(0)
    finally:
        return results
