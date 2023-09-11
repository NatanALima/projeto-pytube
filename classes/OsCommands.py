import errno
import os
import time


def questionMessage(question, msg=None):
    if msg is not None:
        print(msg);
    answer = input(question).upper();
    return 1 if answer == "Y" else 0;


class OsCommands:
    def __init__(self, path=None, folder=None, archive=None):
        self.path = path;
        self.folder = folder;
        self.archive = archive;

    def verifyCreateFolder(self, dirLocale, folder):
        isCreated = 0;
        try:
            self.path = os.path.join(dirLocale, folder);
            os.mkdir(self.path);
            isCreated = 1;
        except OSError:
            if OSError.errno == errno.EEXIST:
                isCreated = 0;

        return isCreated;

    def createNewFolder(self, path):
        while True:
            self.folder = str(input('Informe o nome da pasta que deseja criar: '));
            if self.verifyCreateFolder(path, self.folder):
                print('Pasta Criada com Sucesso!');
                break;
            else:
                print('Não foi possível Criar a pasta. Ela já existe!')
                time.sleep(1);
                print('--------------');
                question = questionMessage('Deseja Continuar? (y/n)');
                if not question == "Y":
                    print('Criação de nova pasta Cancelada');

    def setPath(self, path):
        self.path = path;
        isCreateNewFolder = questionMessage('Deseja Criar uma Nova Pasta? (y/n)', f'Seu caminho atual é {path}');
        if isCreateNewFolder:
            self.createNewFolder(path);
        return self.path;
