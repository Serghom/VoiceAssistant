import speech_recognition as sr
import patternCommand
import winsound
import directkeys
import hexDirKey
import time

frequency = 500  # Set Frequency To 2500 Hertz
duration = 400  # Set Duration To 1000 ms == 1 second

# функция прослушки микрофона и перевода в текст
#   flag - флаг внутри ты бота или нет
#   count - сколько иттераций ты внутри бота
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
            make_something(command(False))

    return word_command


# функция выполнения команды
def make_something(word_command):
    # обращение к боту
    for i in range(len(patternCommand.bot)):
        if word_command.find(patternCommand.bot[i]) > -1:
            print("Шо надо\n-=-=-=-=-=-=-=-=-=-")
            winsound.Beep(700, duration)
            word_command = command(True)

            # активация варп-двигателя
            for counter in range(len(patternCommand.warp_drive)):
                if word_command.find(patternCommand.warp_drive[counter]) > -1:
                    print(patternCommand.warp_drive[counter])
                    print('ГОТОВА ЕПТА\n-=-=-=-=-=-=-=-=-=-')
                    directkeys.PressKey(hexDirKey.C)
                    directkeys.ReleaseKey(hexDirKey.C)
                    winsound.Beep(frequency, duration)
                    return

            # убрать/выпустить шасси
            for counter in range(len(patternCommand.landing_gear)):
                if word_command.find(patternCommand.landing_gear[counter]) > -1:
                    print(patternCommand.landing_gear[counter])
                    print("шасси активированы\n-=-=-=-=-=-=-=-=-=-")
                    directkeys.PressKey(hexDirKey.G)
                    directkeys.ReleaseKey(hexDirKey.G)
                    winsound.Beep(frequency, duration)
                    return

            # запросить стыковку
            for counter in range(len(patternCommand.docking)):
                if word_command.find(patternCommand.docking[counter]) > -1:
                    print(patternCommand.docking[counter])
                    print("Запросил\n-=-=-=-=-=-=-=-=-=-")
                    directkeys.PressKey(hexDirKey.k1)
                    directkeys.ReleaseKey(hexDirKey.k1)
                    # time.sleep(0.1)
                    # directkeys.PressKey(hexDirKey.E)
                    # directkeys.ReleaseKey(hexDirKey.E)
                    # time.sleep(0.1)
                    # directkeys.PressKey(hexDirKey.E)
                    # directkeys.ReleaseKey(hexDirKey.E)
                    # time.sleep(0.1)
                    # directkeys.PressKey(hexDirKey.D)
                    # directkeys.ReleaseKey(hexDirKey.D)
                    # time.sleep(0.1)
                    # directkeys.PressKey(hexDirKey.SPACE)
                    # directkeys.ReleaseKey(hexDirKey.SPACE)
                    # time.sleep(0.1)
                    # directkeys.PressKey(hexDirKey.A)
                    # directkeys.ReleaseKey(hexDirKey.A)
                    # time.sleep(0.1)
                    # directkeys.PressKey(hexDirKey.Q)
                    # directkeys.ReleaseKey(hexDirKey.Q)
                    # time.sleep(0.1)
                    # directkeys.PressKey(hexDirKey.Q)
                    # directkeys.ReleaseKey(hexDirKey.Q)
                    # time.sleep(0.1)
                    # directkeys.PressKey(hexDirKey.k1)
                    # directkeys.ReleaseKey(hexDirKey.k1)
                    winsound.Beep(frequency, duration)
                    return

            # рассказать сказку
            for counter in range(len(patternCommand.story)):
                if word_command.find(patternCommand.story[counter]) > -1:
                    print(patternCommand.story[counter])
                    print("Как дед насрал в каляску\n-=-=-=-=-=-=-=-=-=-")

                    return


while True:
    make_something(command(False))
