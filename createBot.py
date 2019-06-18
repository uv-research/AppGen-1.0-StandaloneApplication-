from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = 'D:/r&d/personal research/chatterbot-corpus-master/chatterbot_corpus/data/english/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

