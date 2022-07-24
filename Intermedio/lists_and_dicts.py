def run():
    my_list=[1, "Hello", True, 4.5]
    my_dict={"fisrtname":"Esteban", "lastname":"Usma"}

    super_list=[
        {"fisrtname":"Esteban", "lastname":"Usma"},
        {"fisrtname":"Miguel", "lastname":"Torres"},
        {"fisrtname":"Pepe", "lastname":"Sierra"},
        {"fisrtname":"jose", "lastname":"Garcia"},
        {"fisrtname":"Susana", "lastname":"Perez"},
    ]

    super_dict={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,1.5,6.43],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i)

if __name__ == "__main__":
    run()

