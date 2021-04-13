def mutate_string(string, position, character):
    m_str = list(string)
    m_str[position] = character
    m_str = ''.join(m_str)
    return m_str



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
