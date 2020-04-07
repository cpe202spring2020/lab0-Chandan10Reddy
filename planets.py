def weight_on_planets():
    e_raw_weight = input("What do you weigh on earth? ")
    e_weight = float(e_raw_weight)
    m_weight = e_weight*0.38
    j_weight = e_weight*2.34
    print("\nOn Mars you would weigh "+str(m_weight)+" pounds.\nOn Jupiter you would weigh "+str(j_weight)+" pounds.")


if __name__ == '__main__':
    weight_on_planets()