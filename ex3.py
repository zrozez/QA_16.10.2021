#Написать функцию, которая принимает на вход текст и вычисляет какое слово сколько раз повторялось
import re
str1 = 'Осень, осень, осень золотая, Наша гостья , гостья дорогая! Хорошо, что ты пришла, Что нам, осень, принесла?'
txt = 'Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless. But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'


def count_word(txt):
    txt = re.sub(r'[^\w\s]','',txt)
    txt = txt.lower()
    lst_of_txt = txt.split()
    pp = {}
    for i in lst_of_txt:
        if i in pp.keys():
            pp[i]= pp[i] + 1
        else:
            pp[i] = 1
    return pp

print(count_word(txt))
print(count_word(str1))
