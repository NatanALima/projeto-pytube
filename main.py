import os
from classes.OsCommands import OsCommands
from MediaYT import *;

osCmd = OsCommands();

typeList = ['Arquivo de Vídeo + Áudio', 'Arquivo de Áudio'];


def questionMessage(question, msg=None):
    if msg is not None:
        print(msg);
    answer = input(question).upper();
    return 1 if answer == "Y" else 0;


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


# Processo de verificação e inserção do link;
while True:
    link = str(input('Informe o Link do youtube que deseja baixar: '));
    if validateLink(link):
        break;
    else:
        print('Link Inválido! Por favor insira um link válido.');

# Seleciona o formato que será utilizado para o download + filtra a coleção para o formato selecionado;
while True:
    showOptionsType(typeList);
    mediaFormatValue = int(input('Informe o formato: '));
    if validateTypeMedia(mediaFormatValue, typeList):
        print(f'Formato {typeList[mediaFormatValue].upper()} selecionado!');
        break;
    else:
        print('Valor informado é inválido. Tente novamente.');

# Mostrando e selecionando as opções de download;
isAudioOnly = False if mediaFormatValue == 0 else True;
allStreams = YouTube(link).streams;
mediaFiltered = filterStreamCollection(allStreams, isAudioOnly);
showConfigStream(mediaFiltered, isAudioOnly);

while True:
    idMedia = int(input('Informe o ID: '));
    media = mediaFiltered.get_by_itag(idMedia);
    if validateStreamId(media):
        print(media);
        break;
    else:
        print('ID Inválido. Tente novamente!');

# Selecionando o local de Download;
path = pathSelect();

media.download(output_path=path);
