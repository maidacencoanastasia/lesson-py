'''https://www.webfx.com/tools/emoji-cheat-sheet/'''
import emoji
import pyjokes

print(emoji.emojize('Impact is :thumbsup:', use_aliases=True))
print(emoji.emojize('Students are :blush: ', use_aliases=True))
print(emoji.demojize('Students are 👍'))
print(pyjokes.get_joke())
