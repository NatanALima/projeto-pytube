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

    def createNewFolder(self, path, folder):
        wasCreated = 0;
        if self.verifyCreateFolder(path, folder):
            wasCreated = 1;
        else:
            wasCreated = 0;
        return wasCreated;

    def setPath(self, path):
        dirFind = 0;
        if os.path.isdir(path):
            self.path = path;
            dirFind = 1;
        else:
            dirFind = 0;
        return dirFind
        # isCreateNewFolder = questionMessage('Deseja Criar uma Nova Pasta? (y/n)', f'Seu caminho atual é {path}');
        # if isCreateNewFolder:
        #     self.folder = str(input('Informe o nome da pasta que deseja criar: '));
        #     self.createNewFolder(path, self.folder);
