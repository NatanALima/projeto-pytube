import errno
import os


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

