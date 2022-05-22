from Model.getInfoFilePC import getInfoFilePC

class Menu:
    def __init__(self):
        self.nameFilePC = getInfoFilePC().infoFile()

    def menuForStart(self):
        while True:
            print('\nВерсия ПО 2.4\n'
                  '\nДля завершения ПО введите 777')

            for i in range(len(self.nameFilePC)):
                print('{} - {}'.format(i, self.nameFilePC[i]))

            seal = input('\nВыберите устройство для просмотра: ')

            if seal == '777':
                break

            try:
                with open(f'/home/vlalin/PycharmProjects/pc_os_sniffle/InfoPC/{self.nameFilePC[int(seal)]}', 'r') as file:
                    print(f'\n{file.read()}')
            except Exception as missing:
                print(missing)