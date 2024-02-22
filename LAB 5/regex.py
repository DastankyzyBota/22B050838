#task1
import re
def t_m(x):
    p = '^a(b*)$'
    if re.search(p, x):
        return 'Match'
    else:
        return 'not match'
print(t_m("ac"))
print(t_m("abc"))
print((t_m("a")))
print(t_m("ab"))
print(t_m("abb"))
#not match
# not match
# Match
# Match
# Match

#task2
import re
def t_m(x):
    pat = 'ab{2,3}'
    if re.search(pat, x):
        return 'matches'
    else:
        return 'not matches'
print(t_m("ab"))
print(t_m("aabbbbc"))
#not matches
# matches

#task3
import re
def t_m(x):
        pat = '^[a-z]+_[a-z]+$'
        if re.search(pat,  x):
                return 'match'
        else:
                return'Not matched'

print(t_m("aab_cbbbc"))
print(t_m("aab_Abbbc"))
print(t_m("Aaab_abbbc"))
#match
# Not matched
# Not matched

#task 4
import re
def t_m(x):
        pat = '[A-Z]+[a-z]+$'
        if re.search(pat, x):
                return 'match'
        else:
                return 'not matched'
print(t_m("AaBbGg"))
print(t_m("Python"))
print(t_m("python"))
print(t_m("PYTHON"))
print(t_m("aA"))
print(t_m("Aa"))

#match
# match
# not matched
# not matched
# not matched
# match

#task5
import re
def t_m(x):
        pat = 'a.*?b$'
        if re.search(pat,  x):
                return 'match'
        else:
                return 'not match'

print(t_m("aabbbbd"))
print(t_m("aabAbbbc"))
print(t_m("accddbbjjjb"))

#not match
# not match
# match

#task 6
import re
a = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", a))

#Python:Exercises::PHP:exercises:

#task 7
def snake_to_camel(x):
        import re
        return ''.join(x.capitalize() or '_' for x in x.split('_'))

print(snake_to_camel('python_exs'))

#Python_exs

#task8
import re
a = "PythonExs"
print(re.findall('[A-Z][^A-Z]*', a))

#['Python', 'Exs']

#task 9
import re
def c_w_s(x):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", x)

print(c_w_s("Pyth"))
print(c_w_s("PythonLabs"))
print(c_w_s("PythonLabsSolution"))

#Pyth
# Python Labs
# Python Labs Solution

#task 10
def c_to_s(x):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', x)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(c_to_s('PythonLabsSolve'))

#python_labs_solve