from functools import reduce
from functools import partial
import operator
import random
import numpy as np
import math

def generate_fibonacci(series = 10000)-> 'list':
    i = 0
    j = 1
    fibonacci= [0, 1]
    for num in range(100):
        z = i + j
        #print(z)
        if z < series:
            fibonacci.append(z)
            i = j
            j = z
    return fibonacci

def check_fibonacci(num):
    fibonacci = generate_fibonacci()
    if list(filter(lambda x: x in fibonacci , num)):
        return "Number is a Fibonacci"
    else:
        return "Number is not a Fibonacci"

def check_profanity(paragraph="Hello"):
    prolist = ['4r5e','5h1t','5hit','a55','anal','anus','ar5e','arrse','arse','ass','ass-fucker','asses','assfucker','assfukka','asshole','assholes','asswhole','a_s_s','b!tch','b00bs','b17ch','b1tch','ballbag','balls','ballsack','bastard','beastial','beastiality','bellend','bestial','bestiality','bi+ch','biatch','bitch','bitcher','bitchers','bitches','bitchin','bitching','bloody','blow job','blowjob','blowjobs','boiolas','bollock','bollok','boner','boob','boobs','booobs','boooobs','booooobs','booooooobs','breasts','buceta','bugger','bum','bunny fucker','butt','butthole','buttmunch','buttplug','c0ck','c0cksucker','carpet muncher','cawk','chink','cipa','cl1t','clit','clitoris','clits','cnut','cock','cock-sucker','cockface','cockhead','cockmunch','cockmuncher','cocks','cocksuck ','cocksucked ','cocksucker','cocksucking','cocksucks ','cocksuka','cocksukka','cok','cokmuncher','coksucka','coon','cox','crap','cum','cummer','cumming','cums','cumshot','cunilingus','cunillingus','cunnilingus','cunt','cuntlick ','cuntlicker ','cuntlicking ','cunts','cyalis','cyberfuc','cyberfuck ','cyberfucked ','cyberfucker','cyberfuckers','cyberfucking ','d1ck','damn','dick','dickhead','dildo','dildos','dink','dinks','dirsa','dlck','dog-fucker','doggin','dogging','donkeyribber','doosh','duche','dyke','ejaculate','ejaculated','ejaculates ','ejaculating ','ejaculatings','ejaculation','ejakulate','f u c k','f u c k e r','f4nny','fag','fagging','faggitt','faggot','faggs','fagot','fagots','fags','fanny','fannyflaps','fannyfucker','fanyy','fatass','fcuk','fcuker','fcuking','feck','fecker','felching','fellate','fellatio','fingerfuck ','fingerfucked ','fingerfucker ','fingerfuckers','fingerfucking ','fingerfucks ','fistfuck','fistfucked ','fistfucker ','fistfuckers ','fistfucking ','fistfuckings ','fistfucks ','flange','fook','fooker','fuck','fucka','fucked','fucker','fuckers','fuckhead','fuckheads','fuckin','fucking','fuckings','fuckingshitmotherfucker','fuckme ','fucks','fuckwhit','fuckwit','fudge packer','fudgepacker','fuk','fuker','fukker','fukkin','fuks','fukwhit','fukwit','fux','fux0r','f_u_c_k','gangbang','gangbanged ','gangbangs ','gaylord','gaysex','goatse','God','god-dam','god-damned','goddamn','goddamned','hardcoresex ','hell','heshe','hoar','hoare','hoer','homo','hore','horniest','horny','hotsex','jack-off ','jackoff','jap','jerk-off ','jism','jiz ','jizm ','jizz','kawk','knob','knobead','knobed','knobend','knobhead','knobjocky','knobjokey','kock','kondum','kondums','kum','kummer','kumming','kums','kunilingus','l3i+ch','l3itch','labia','lmfao','lust','lusting','m0f0','m0fo','m45terbate','ma5terb8','ma5terbate','masochist','master-bate','masterb8','masterbat*','masterbat3','masterbate','masterbation','masterbations','masturbate','mo-fo','mof0','mofo','mothafuck','mothafucka','mothafuckas','mothafuckaz','mothafucked ','mothafucker','mothafuckers','mothafuckin','mothafucking ','mothafuckings','mothafucks','mother fucker','motherfuck','motherfucked','motherfucker','motherfuckers','motherfuckin','motherfucking','motherfuckings','motherfuckka','motherfucks','muff','mutha','muthafecker','muthafuckker','muther','mutherfucker','n1gga','n1gger','nazi','nigg3r','nigg4h','nigga','niggah','niggas','niggaz','nigger','niggers ','nob','nob jokey','nobhead','nobjocky','nobjokey','numbnuts','nutsack','orgasim ','orgasims ','orgasm','orgasms ','p0rn','pawn','pecker','penis','penisfucker','phonesex','phuck','phuk','phuked','phuking','phukked','phukking','phuks','phuq','pigfucker','pimpis','piss','pissed','pisser','pissers','pisses ','pissflaps','pissin ','pissing','pissoff ','poop','porn','porno','pornography','pornos','prick','pricks ','pron','pube','pusse','pussi','pussies','pussy','pussys ','rectum','retard','rimjaw','rimming','s hit','s.o.b.','sadist','schlong','screwing','scroat','scrote','scrotum','semen','sex','sh!+','sh!t','sh1t','shag','shagger','shaggin','shagging','shemale','shi+','shit','shitdick','shite','shited','shitey','shitfuck','shitfull','shithead','shiting','shitings','shits','shitted','shitter','shitters ','shitting','shittings','shitty ','skank','slut','sluts','smegma','smut','snatch','son-of-a-bitch','spac','spunk','s_h_i_t','t1tt1e5','t1tties','teets','teez','testical','testicle','tit','titfuck','tits','titt','tittie5','tittiefucker','titties','tittyfuck','tittywank','titwank','tosser','turd','tw4t','twat','twathead','twatty','twunt','twunter','v14gra','v1gra','vagina','viagra','vulva','w00se','wang','wank','wanker','wanky','whoar','whore','willies','willy','xrated','xxx']
    #prolist = ['apples', 'oranges']
    res = [ele for ele in prolist if(ele in paragraph)]
    if res:
        return "not a parlimentary text"
    else:
        return "parlimentary text"


def addevennumber(list):
    return reduce(lambda a, b: a + b, filter(lambda a:a%2==0,list))
    #return reduce(lambda a, b: a + b if a%2==0 and b%2==0 else b, list)

def findbigbyascii(inputstring = ""):
    return reduce(lambda a, b: a if ord(a) > ord(b) else b, inputstring)

def addthirdnumberinalist(listnum):
    return reduce(operator.add, filter(lambda a: listnum.index(a)%3==2,listnum))
    
def numberplategen(twodigitstart,twodigitend,fourdigitstart,fourdigitend,statecode):
    aplhalist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #print("KA" + random.randint(10,99) + 2*random.choice(aplhalist) + random.randint(1000,9900))
    numberplatelist = [statecode + str(random.randint(twodigitstart,twodigitend)) + str(random.choice(aplhalist)) + str(random.choice(aplhalist)) + str(random.randint(fourdigitstart,fourdigitend)) for i in range(15)]
    #print(numberplatelist)
    return numberplatelist

def removevowel(inputstr):
    str = ""
    #outputlist = [str.join(i) for i in list(filter(lambda a:a.lower() not in ['a','e','i','o','u'],inputstr))]
    #outputlist = [lambda a:a if a.lower() not in ['a','e','i','o','u'] else "" for a in inputstr]
    outputlist = list(filter(lambda a:a.lower() not in ['a','e','i','o','u'],inputstr))
    return str.join(outputlist)

def cycliccharacter(inputstr):
    outputlist =  [chr(ord(a.lower()) + 5) if (ord(a.lower()) + 5) < 123 else chr(ord(a.lower()) - 21) for a in inputstr]
    return "".join(outputlist)

def addtwoiterables(list1, list2):
    #return [a+b if (a%2==0 and b%2==1) else 0 for a in list1  for b in list2]
    return [a+b if (a%2==0 and b%2==1) else 0 for a, b in zip(list1,list2)]

def sigmoidfunction(list1):
    #return [a+b if (a%2==0 and b%2==1) else 0 for a in list1  for b in list2]
    return [1/(1 + np.exp(-a)) for a in list1]

if __name__ == '__main__':
    print(check_fibonacci([987]))
    print(check_profanity(paragraph="There are 2 apples for 4 persons"))
    print(addevennumber([1, 3, 6, 7, 2,4,6,8,9, 25]))
    print(findbigbyascii("hexllo dei vaad#a PODA mamaa"))
    print(addthirdnumberinalist([1, 3, 6, 7, 2,105,100,101,103,400,300,209]))
    print(numberplategen(10,99,1000,9999,'KA'))
    f = partial(numberplategen,10,99,1000,9999)
    print(f('DL'))
    print(f('KA'))
    print(removevowel('hello my India'))
    print(cycliccharacter("tsaiz"))
    print(addtwoiterables([1,2,3,4,5],[6,7,8,9,10]))
    print(sigmoidfunction([1,2,3,5]))