# import os
# from pytube import YouTube;
#
# link = input('Informe o Link do Youtube: ');
# yt = YouTube(link);
# print(yt.streams.filter(adaptive=True).first());
#
# typesList = [1, 2];
# print("====================");
# print("Opções de Download:");
# print('--------------------');
# print("1: Arquivo de Vídeo + Áudio (.mp4)");
# print("2: Arquivo de Áudio (.mp3)");
# print("====================");
#
#
# # Validação dos tipos de formato selecionado
# def verifyTypeInList(typeValue):
#     try:
#         typesList.index(typeValue);
#         find = 1;
#     except ValueError:
#         find = 0;
#     return find;
#
#
# def existsFolder(folder):
#     return os.path.exists(folder);
#
#
# # Função que adiciona uma nova pasta/diretório para o diretório "pai"
# def addFolder(parentDir):
#     while True:
#         folderName = str(input('Informe o nome da Nova Pasta: '));
#         path = os.path.join(parentDir, folderName);
#         try:
#             os.mkdir(path);
#             break;
#         except OSError:
#             retry = str(input("Pasta já existe! Deseja tentar outro Nome?(s/n): ")).upper();
#             if not retry == "S":
#                 path = parentDir;
#                 break;
#
#     return path;
#
#
# # Seleciona o diretório que será utilizado para armazenar o download
# def dirSelect():
#     dir = str(input("Informe o Diretório: "));
#     while True:
#         isCreate = input("Criar uma Nova Pasta? (s/n): ").upper();
#         if isCreate == "S":
#             dir = addFolder(dir);
#             break;
#         elif isCreate == "N":
#             break;
#         else:
#             print("Insira um Valor válido!");
#     return dir;
#
#
# # Verifica quando o tipo de download for selecionado corretamente
# while True:
#     typeFile = int(input("Tipo: "));
#     if not verifyTypeInList(typeFile):
#         print(typeFile);
#         print('É necessário informar o formato de Arquivo para prosseguir');
#     else:
#         break;
#
#
# dirInfo = dirSelect();
#
# # Mostrando as opções de Download
# def showConfigStream(streamInfo, isAudioOnly):
#     for content in streamInfo:
#         print("**************************************");
#         print("ID: ", content.itag);
#         print("Formato: ", content.mime_type);
#         print("Qualidade: ", content.abr if isAudioOnly is True else content.resolution);
#         print("**************************************");
#
#
# # Selecionando o formato e qualidade do vídeo
# def selectConfigStream():
#     if typeFile == 1:
#         streamValues = yt.streams.filter(adaptive=True, type="video");
#         showConfigStream(streamValues, False);
#     else:
#         streamValues = yt.streams.filter(only_audio=True);
#         showConfigStream(streamValues, True);
#
#     while True:
#         getId = str(input("Informe o Id da Stream que deseja baixar: "));
#         filteredStream = streamValues.get_by_itag(getId);
#         if filteredStream is None:
#             print("Id Inválido. Digite novamente!");
#         else:
#             break;
#     return filteredStream;
#
# stream = selectConfigStream();
# stream.download(output_path=dirInfo);
#

from classes.OsCommands import OsCommands


def questionMessage(question, msg=None):
    if msg is not None:
        print(msg);
    answer = input(question).upper();
    return 1 if answer == "Y" else 0;


# Criar um looping para ocorrer enquanto (while) o diretório for incorreto!


# Adicionar verificação para a criação de pasta + looping em caso de erro

osCmd = OsCommands();


def pathSelect():
    while True:
        pathLocal = str(input('Informe o diretório:'));
        if osCmd.setPath(pathLocal):
            pathLocal = osCmd.path;
            break;
        else:
            print('Diretório não existe. Tente Novamente!');
    return pathLocal;


def createFolderAndSelect():
    while True:
        pathParent = str(input('Informe o diretório Pai: '));
        folderName = str(input('Informe o nome da pasta: '));
        if osCmd.createNewFolder(pathParent, folderName):
            print('Pasta Criada e Selecionada com Sucesso!');
            pathLocal = osCmd.path;
            break;
        else:
            answer = questionMessage('Tentar novamente? (y/n): ', 'Pasta já Existe!')
            if not answer:
                print('Criação de Pasta cancelada... ')
                print('Ainda é necessário selecionar o caminho...');
                pathLocal = pathSelect();
                break;
    return pathLocal;


path = createFolderAndSelect();

print(path);
