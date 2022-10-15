""" -----------------------------------------------------------------------------------------------------

Complete the following code (without using the replace function)-

def replace_comma_with_space(text):
    …
    …

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)


-------------------------------------------------------------------------------------------------------"""

def replace_comma_with_space(text):
    i = 0
    out = ""
    for i in text:
        if i == ',':
            out += ' '
        else:
            out += i

    return out


s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
