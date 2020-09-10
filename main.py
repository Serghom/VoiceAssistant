import speech_recognition as sr
import patternCommand

# функция прослушки микрофона и перевода в текст
"""
    flag - флаг внутри ты бота или нет
    count - сколько иттераций ты внутри бота
"""
def command(flag, count=0):
    r = sr.Recognizer()

    # слушает микрофон
    with sr.Microphone() as source:
        print("Говори " + str(flag) + " " + str(count))
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    # переводит в текст
    try:
        word_command = r.recognize_google(audio, language="ru-RU").lower()
        print("Ты сказал: " + word_command)

    # в случае ошибки отправляет на второй круг
    except:
        print("Говори внятнее")
        if flag and count <= 3:
            count += 1
            word_command = command(flag, count)
        else:
            makeSomething(command(False))

    return word_command


def makeSomething(word_command):
    # обращение к боту
    if word_command.find("стасян") > -1:
        print("Шо надо")
        word_command = command(True)
        # активация варп-двигателя
        for i in range(len(patternCommand.warp_drive)):
            # print(patternCommand.warp_drive[i])
            if word_command.find(patternCommand.warp_drive[i]) > -1:
                print(patternCommand.warp_drive[i])
                print('ГОТОВА ЕПТА')

        # выпустить шасси
        if word_command.find('выпустить шасси') > -1:
            print("выпускаю")


while True:
    makeSomething(command(False))
# wordCommand = "активируй work"
# print(patternCommand.warp_drive)
# for i in range(len(patternCommand.warp_drive)):
#     # print(patternCommand.warp_drive[i])
#     if wordCommand.find(patternCommand.warp_drive[i]) > -1:
#         print(patternCommand.warp_drive[i])
#         print('ГОТОВА ЕПТА')
