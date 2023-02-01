def replace():
    string= 'There are some words in this string need to be replaced. This is theword'
    word_need_replce=input('Enter the words need to replace')
    word_will_replace=input('Enter the words will replace')
    print(string.replace(word_need_replce,word_will_replace))

replace()