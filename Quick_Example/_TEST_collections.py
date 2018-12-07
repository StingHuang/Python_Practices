import collections

# namedtuple
def _test_namedtuple():
    People_Data = collections.namedtuple("People", ["first_name", "last_name", "id", "mail"])

    raw_data = [
        ("Ellie", "Chen", 128, "abc123@fmail.com"),
        ("Jack", "Lin", 34, "frgdm@xmail.com"),
        ("Ray", "Yen", 610, "leoofd@fmail.com")
    ]

    p1 = People_Data._make(raw_data[0])
    print(p1)
    p2 = People_Data(raw_data[1][0], raw_data[1][1], raw_data[1][2], raw_data[1][3])
    print(type(p2))
    print(p2._asdict())


# OrderedDict
def _test_orderedDict():
    raw_dict = {
        '128': "Ellie Chen",
        '34': "Jack Lin",
        '610': "Abby Yen"
    }
    print(raw_dict)

    new_ordered_dict = collections.OrderedDict(raw_dict)
    print(new_ordered_dict)
    print("key set: {}".format(new_ordered_dict.keys()))
    new_ordered_dict.popitem(last=False)
    print(new_ordered_dict)



# _test_namedtuple()
# _test_orderedDict()


num_list = [5,9,3,4,7,6,1,8]

for i in reversed(num_list):
    print(i)

print(sorted(num_list))

deq_nums = collections.deque(num_list)
print(deq_nums.popleft())
print(deq_nums)