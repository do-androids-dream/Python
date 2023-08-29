"""
As input data, you have a list of strings.

Write a method double_string() for counting the number of strings from the list, represented in the form of the concatenation of two strings from this arguments  list
"""
def double_string(data):
    counter = 0
    st = set()
    for i in data:
        for j in data:
            st.add(i + j)
    for i in st:
        for j in data:
            if i == j: counter += 1
    return counter

data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data))
data = ['aa', 'abc', 'qwerqwer']
print(double_string(data))
data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
print(double_string(data))
data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data))