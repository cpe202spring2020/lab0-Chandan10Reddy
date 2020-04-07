def weight_on_planets():
    e_raw_weight = input("What do you weigh on earth? ")
    e_weight = float(e_raw_weight)
    m_weight = e_weight*0.38
    j_weight = e_weight*2.34
    print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." % (m_weight, j_weight))


if __name__ == '__main__':
    weight_on_planets()