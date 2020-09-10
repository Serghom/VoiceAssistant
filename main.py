import speech_recognition as sr
import patternCommand

# функция прослушки микрофона и перевода в текст
"""
    flag - флаг внутри ты бота или нет
    count - сколько иттераций ты внутри бота
"""
def command(flag, count=0):
    global word_command
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

# функция выполнения команды
def makeSomething(word_command):
    # обращение к боту
    for i in range(len(patternCommand.bot)):
        if word_command.find(patternCommand.bot[i]) > -1:
            print("Шо надо\n-=-=-=-=-=-=-=-=-=-")
            word_command = command(True)

            # активация варп-двигателя
            for counter in range(len(patternCommand.warp_drive)):
                if word_command.find(patternCommand.warp_drive[counter]) > -1:
                    print(patternCommand.warp_drive[counter])
                    print('ГОТОВА ЕПТА\n-=-=-=-=-=-=-=-=-=-')
                    return

            # убрать/выпустить шасси
            for counter in range(len(patternCommand.landing_gear)):
                if word_command.find(patternCommand.landing_gear[counter]) > -1:
                    print(patternCommand.landing_gear[counter])
                    print("шасси активированы\n-=-=-=-=-=-=-=-=-=-")
                    return

            # запросить стыковку
            for counter in range(len(patternCommand.docking)):
                if word_command.find(patternCommand.docking[counter]) > -1:
                    print(patternCommand.docking[counter])
                    print("Запросил\n-=-=-=-=-=-=-=-=-=-")
                    return

            # рассказать сказку
            for counter in range(len(patternCommand.story)):
                if word_command.find(patternCommand.story[counter]) > -1:
                    print(patternCommand.story[counter])
                    print("Как дед насрал в каляску\n-=-=-=-=-=-=-=-=-=-")
                    return


while True:
    makeSomething(command(False))
