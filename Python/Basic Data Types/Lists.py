N = int(input())

lista = []

for _ in range(N):
    full_command = input()
    list_command = full_command.split(' ')
    main_com,*arg = list_command

    if main_com =='print':
        print(lista)
        
    else:
        method = getattr(lista,main_com)
        if len(arg) == 0:
            method()
    
        elif len(arg) == 1:
            method(int(arg[0]))
        
        if len(arg) > 1:
            method(int(arg[0]), int(arg[1]))