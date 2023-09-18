from pytube import YouTube;


def showOptionsType(typeList):
    print('=================================');
    print('SELECIONE O FORMATO');
    print('---------------------');
    for typeValue in typeList:
        index = typeList.index(typeValue);
        print(f'{index} - {typeValue}');
    print('=================================');


def showConfigStream(mediaCollection, isAudio):
    for content in mediaCollection:
        print("**************************************");
        print("ID: ", content.itag);
        print("Formato: ", content.mime_type);
        print("Qualidade: ", content.abr if isAudio is True else content.resolution);
        print("**************************************");


def validateLink(link):
    try:
        testYt = YouTube(link).streams;
        isValid = 1;
    except:
        isValid = 0;
    return isValid;


def validateTypeMedia(typeValue, typeList):
    if len(typeList) >= typeValue >= 0:
        isValid = 1;
    else:
        isValid = 0;
    return isValid;


def validateStreamId(mediaCollection):
    if mediaCollection is None:
        isValid = 0;
    else:
        isValid = 1;
    return isValid;


def filterStreamCollection(streamCollection, audioOnly):
    global filteredStream;
    if not audioOnly:
        filteredStream = streamCollection.filter(adaptive=True, type="video").order_by('resolution').asc();
        print(filteredStream);
    else:
        filteredStream = streamCollection.filter(only_audio=True).order_by('abr').asc();
    return filteredStream;
