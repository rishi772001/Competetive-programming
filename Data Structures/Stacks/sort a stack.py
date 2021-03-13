'''
@Author: rishi
https://www.geeksforgeeks.org/sort-a-stack-using-recursion/
'''


# Inserts element in correct place
def stack_insert(st, element):
    if len(st) == 0 or st[-1] <= element:
        st.append(element)
    else:
        # pop top element until correct place and insert element
        temp = st.pop()
        stack_insert(st, element)
        # add popped elements back to the stack
        st.append(temp)


def sort_stack(st):
    if st:
        # Remove top element and insert it in sorted order
        temp = st.pop()
        sort_stack(st)
        stack_insert(st, temp)


stack = [1, 4, 3, 9, 2]
sort_stack(stack)
print(stack)
