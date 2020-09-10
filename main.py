import speech_recognition as sr
import patternCommand


def command(flag):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите " + flag)
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        word_command = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + word_command)

    except:
        print("Я вас не поняла")
        word_command = command(flag)

    return word_command


def makeSomething(word_command):
    #обращение к боту
    if word_command.find("стасян") > -1:
        print("Шо надо")
        word_command = command("внутри")
        #активация варп-двигателя
        for i in range(len(patternCommand.warp_drive)):
            # print(patternCommand.warp_drive[i])
            if word_command.find(patternCommand.warp_drive[i]) > -1:
                print(patternCommand.warp_drive[i])
                print('ГОТОВА ЕПТА')

        #выпустить шасси
        if word_command.find('выпустить шасси') > -1:
            print("выпускаю")


while True:
    makeSomething(command("снаружи"))
# wordCommand = "активируй work"
# print(patternCommand.warp_drive)
# for i in range(len(patternCommand.warp_drive)):
#     # print(patternCommand.warp_drive[i])
#     if wordCommand.find(patternCommand.warp_drive[i]) > -1:
#         print(patternCommand.warp_drive[i])
#         print('ГОТОВА ЕПТА')
