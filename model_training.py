def get_data_from_file():
    """Import des donnees d'apprentissage"""
    fd = open("data.csv", "r+")
    str_lst = []
    tmp_str = ""
    data = [[], []]
    for line in fd:
        if line == 'km,price\n':
            pass
        else:
            line = line.replace('\n', '')
            str_lst.append(str(line))
    for i in range(len(str_lst)):
        tmp_str = str_lst[i].split(',')
        if i % 2 == 0:
            data[0].append(tmp_str[0])
        else:
            data[1].append(tmp_str[1])
    return data
    #####
    # To remove
    #for i in range(len(data[0])):
    #    print(data[0][i], '\t', data[1][i])
    #
    #####

def cast_list_elems_to_float(data):
    new_data = [[], []]
    for i in range(len(data[0])):
        new_data[0].append(float(data[0][i]))
        new_data[1].append(float(data[1][i]))
    return new_data


def calculer_derivees_partielles(old_theta_0, old_theta_1):
    """Calcul des derivees partielles de theta_0 et theta_1 pour la fonction de cout"""
    derivee_theta_0 = float(0)
    derivee_theta_1 = float(0)
    for i in range(0, len(X)):
        derivee_theta_0 += float(((old_theta_0 + (old_theta_1 * X[i])) - float(Y[i])))
        derivee_theta_1 += (((old_theta_0 + (old_theta_1 * X[i]))) - float(Y[i])) * float(X[i])
    derivee_theta_0 = (1/M) * derivee_theta_0
    derivee_theta_1 = (1/M) * derivee_theta_1
    return [derivee_theta_0, derivee_theta_1]

def calculer_nouvelles_theta(old_theta_0, old_theta_1):
    """Mise a jour des valeurs de theta_0 et theta_1"""
    [derivee_theta_0, derivee_theta_1] = calculer_derivees_partielles(old_theta_0, old_theta_1)
    new_theta_0 = old_theta_0 - (learning_rate * derivee_theta_0)
    new_theta_1 = old_theta_1 - (learning_rate * derivee_theta_1)
    print(old_theta_0, old_theta_1, '\t', new_theta_0, new_theta_1)
    return [new_theta_0, new_theta_1]

def start_gradiant_descent():
    """Algorithme de Gradient descent"""
    tmp_theta_0 = initial_theta_0
    tmp_theta_1 = initial_theta_1
    for i in range(nb_loop):
        [new_theta_0, new_theta_1] = calculer_nouvelles_theta(tmp_theta_0, tmp_theta_1)
        tmp_theta_0 = new_theta_0
        tmp_theta_1 = new_theta_1
    return [tmp_theta_0, tmp_theta_1]

def return_thetas():
    [final_theta_0, final_theta_1] = start_gradiant_descent()
    print("After {} iterations, theta_0 = {}, theta_1 = {}".format(nb_loop, final_theta_0, final_theta_1))
    return final_theta_0, final_theta_1

data = get_data_from_file()
data = cast_list_elems_to_float(data)
X = data[0]
Y = data[1]
M = len(data[0])
learning_rate = float(0.0001)
initial_theta_0 = float(0)
initial_theta_1 = float(0)
nb_loop = 20
