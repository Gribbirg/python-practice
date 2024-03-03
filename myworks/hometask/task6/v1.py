from math import prod, floor


def main(delta_set: set):
    e_set = {b % 3 - abs(b)
             for b in delta_set
             if bool(b < 23) != bool(b > -76)}
    gamma_set = delta_set | e_set
    m_set = {e % 2 + 3 * o for e in e_set for o in gamma_set if e > o}
    p_set = {o % 2 + 6 * m for o in gamma_set for m in m_set if o >= m}
    return sum(floor(m / 3) for m in m_set) - prod(p % 3 for p in p_set)
