import os
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

class Gfg:
    def ouvir_microfone(self):
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            print("Diga sim ou não")
            microfone.adjust_for_ambient_noise(source)
            microfone.pause_threshold = 0.7
            audio = microfone.listen(source)
            
        try:
            print("Reconhecendo voz") 
            frase = microfone.recognize_google(audio,language='pt-BR')
            print("Você disse: " + frase)
            
        except sr.UnkownValueError:
            print("Não entendi")
            
        return frase

    def falar(self, audio):
        motor = pyttsx3.init('espeak')
        voz = motor.getProperty('voices')
        motor.setProperty('voice', voz[1].id) 
        motor.say(audio) 
        motor.runAndWait()

    def desligar(self):
        self.falar("Deseja desligar o computador senhor")
        levar = self.ouvir_microfone()
        escolha = levar

        if escolha == 'sim':
            print("Desligando o computador")
            self.falar("Desligando o computador")
            os.system('systemctl poweroff')

        if escolha == 'nao':
            print("Obrigado senhor") 
            self.falar("Obrigado senhor")

if __name__ == '__main__':
    senhor = Gfg()
    senhor.desligar()
