from chatterbot import ChatBot
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time
import pyttsx3

from appGenerator import startGenerator


class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        self.getVoiceAssistance = False
        self.getSpeachRecognizer = False

        tk.Tk.__init__(self, *args, **kwargs)

        self.bot= ChatBot('Bot')

        self.title("App Generator")

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 115)
        self.engine.setProperty('volume', 0.9)

        self.initialize()

    def initialize(self):
        
        self.grid()

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Bot-Integrated   App Generator')
        self.conversation_lbl.grid(column=0, row=0, sticky='w', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=1, columnspan=3, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=0, row=2, rowspan = 2, sticky='news', padx=3, pady=3)

        self.respond = tk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=1, row=2, columnspan=2, sticky='news', padx=3, pady=3)

        self.voiceAssistance = tk.Button(self, text='Voice Assistance', command=self.get_voiceAssistance)
        self.voiceAssistance.grid(column=1, row=3, sticky='news', padx=3, pady=3)

        self.speachRecognizer = tk.Button(self, text='Speach Recognizer', command=self.get_speachRecognizer)
        self.speachRecognizer.grid(column=2, row=3, sticky='news', padx=3, pady=3)

    def get_voiceAssistance(self):
        self.getVoiceAssistance = not self.getVoiceAssistance
        if self.getVoiceAssistance:
            self.voiceAssistance["bg"] = '#2A95BE'
            self.voiceAssistance["fg"] = 'white'
        else:
            self.voiceAssistance["bg"] = '#F0F0F0'
            self.voiceAssistance["fg"] = 'black'
    
    def get_speachRecognizer(self):
        self.getSpeachRecognizer = not self.getSpeachRecognizer
        if self.getSpeachRecognizer:
            self.speachRecognizer["bg"] = '#2A95BE'
            self.speachRecognizer["fg"] = 'white'
        else:
            self.speachRecognizer["bg"] = '#F0F0F0'
            self.speachRecognizer["fg"] = 'black'

    def get_response(self):

        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        response = self.bot.get_response(user_input)

        self.conversation['state'] = 'normal'

        if user_input.startswith( 'create' ):
            self.conversation.insert(
                tk.END, "You: " + user_input + "\n" 
            )
            startGenerator(user_input, self)
        elif user_input == 'bye':
            if self.getVoiceAssistance:
                self.engine.say("bye")
                self.engine.runAndWait()
            bot_root.quit()
        elif user_input == 'help':
            self.conversation.insert(
                tk.END, "You: " + user_input + "\n" + """ChatBot: use 'create' keyword to start creating app and also specify the language in which app should be developed."
            example: 'create addition of 2 numbers in vuejs'\n"""
            )
            
            if self.getVoiceAssistance:
                self.engine.say("""ChatBot: use 'create' keyword to start creating app and also specify the language in which app should be developed.
            example: 'create addition of 2 numbers in vuejs'""")
                self.engine.runAndWait()
        elif user_input == 'list':
            self.conversation.insert(
                tk.END, "You: " + user_input + "\n" + """use params to list:
        '-O' for listing operations    
        '-L' for listing the languages in which bot can build app\n"""
            )
            
            if self.getVoiceAssistance:
                self.engine.say("""use params to list:
        '-O' for listing operations    
        '-L' for listing the languages in which bot can build app""")
                self.engine.runAndWait()
        elif user_input == 'list -O':
            self.conversation.insert(
                tk.END, "You: " + user_input + "\n" + """List of operations:
        'add / addition / sum'
        'difference / subtract / subtraction'\n"""
            )
            
            if self.getVoiceAssistance:
                self.engine.say("""List of operations:
        'add / addition / sum'
        'difference / subtract / subtraction'""")
                self.engine.runAndWait()
        elif user_input == 'list -L':
            self.conversation.insert(
                tk.END, "You: " + user_input + "\n" + """ChatBot: List of languages in which bot can build apps:
        'javascript'
        'vuejs'
        'angular' \n"""
            )
            
            if self.getVoiceAssistance:
                self.engine.say("""List of languages in which bot can build apps:
        'javascript'
        'vuejs'
        'angular'""")
                self.engine.runAndWait()
        else:
            self.conversation.insert(
                tk.END, "You: " + user_input + "\n" + "ChatBot: " + str(response.text) + "\n"
            )
            
            if self.getVoiceAssistance:
                self.engine.say(str(response.text))
                self.engine.runAndWait()

        self.conversation['state'] = 'disabled'
        time.sleep(0.5)


bot_root = TkinterGUIExample()
bot_root.mainloop()