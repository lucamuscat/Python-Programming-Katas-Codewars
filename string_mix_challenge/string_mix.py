from collections import Counter, defaultdict


def mix(s1=None, s2=None):
    s1 = str(s1)
    s2 = str(s2)
    tallied_s1 =  sanitize_chars(Counter(s1).most_common())
    
    tallied_s2 = sanitize_chars(Counter(s2).most_common())

    # Easier to get data from a dict rather than a list of tuples.
    tallied_s1_dict = {k: v for k, v in tallied_s1}
    tallied_s2_dict = {k: v for k, v in tallied_s2}

    max_values = max(tallied_s1_dict, tallied_s2_dict)

    # Swap key with value
    transposed_max_values = transpose_dict(max_values)
    return display_result(sort(transposed_max_values))


def sanitize_chars(tallied_strings):
    return [i for i in tallied_strings if i[0].islower() and i[1] > 1]

def max(s1_dict={}, s2_dict={}):
    s1_key_set = {k for k in s1_dict.keys()}
    s2_key_set = {k for k in s2_dict.keys()}

    set_intersect = s1_key_set.intersection(s2_key_set)
    set_difference = s1_key_set.symmetric_difference(s2_key_set)

    set_result = {}
    for k in set_intersect:
        if s1_dict.get(k) > s2_dict.get(k): 
            set_result['1:'+k] = s1_dict.get(k)
        elif s1_dict.get(k) < s2_dict.get(k): 
            set_result['2:'+k] = s2_dict.get(k)
        else:
            set_result['=:'+k] = s1_dict.get(k)

    for k in set_difference:
        if s1_dict.get(k):
            set_result['1:'+k] = s1_dict.get(k)
        else:
            set_result['2:'+k] = s2_dict.get(k)

    return set_result


def transpose_dict(transposee):
    visited_values = defaultdict()
    for k, v in transposee.items():
        if not visited_values.get(v):
            visited_values[v] = []
        visited_values[v].append(k)
    return visited_values


def sort(transposed_sortee):
    items = sorted(transposed_sortee.items(),key=lambda x: x[0],reverse=True)
    
    result = {}
    for k, v in items:
        v = sorted(v, key=lambda x: x[2])
        v = sorted(v, key=lambda x: x[0])
        result[k] = v
    
    return result


def display_result(sorted_result):
    ret_value = ''
    for k, v in sorted_result.items():
        for j in v:
            ret_value += j[:2]+j[-1]*k+'/'
    return ret_value[:-1]


