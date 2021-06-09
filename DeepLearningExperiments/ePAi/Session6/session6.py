vals = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['S', 'C', 'H', 'D']

def deck_function()-> 'list':
    '''This is a Zip function for creating a deck of 52 cards '''
    deck = sorted(list(map(lambda t: (t[0]+t[1]), zip(vals*len(vals), suits*len(vals)))))
    return deck

def merge()-> 'list':
    '''This is a normal function for creating a deck of 52 cards '''
    deck= []
    for j in range(0,len(suits)):
        for i in range(0,len(vals)):
            deck.append(vals[i]+suits[j])
    return deck



def straight(ranks:'list of the rank of cards')->'bool':
    '''Straight is consecutive 5 different cards.
    So, set(ranks) will see all cards should be different and its length will check they are 5
    And their max difference == 4 will check for consecutive'''
    if ranks[0]==14 and ranks[4]==2:
        ranks[0]=1
    if len(set(ranks))== 5 and (max(ranks) - min(ranks)== 4):
        return True
    return False

def straight_3cards(ranks:'list of the rank of cards')->'bool':
    '''Straight is consecutive 3 different cards.
    So, set(ranks) will see all cards should be different and its length will check they are 5
    And their max difference == 2 will check for consecutive'''
    if ranks[0]==14 and ranks[2]==2:
        ranks[0]=1
    if len(set(ranks))== 3 and (max(ranks) - min(ranks)== 2):
        return True
    return False

def straight_4cards(ranks:'list of the rank of cards')->'bool':
    '''Straight is consecutive 3 different cards.
    So, set(ranks) will see all cards should be different and its length will check they are 5
    And their max difference == 3 will check for consecutive'''
    if ranks[0]==14 and ranks[3]==2:
        ranks[0]=1
    if len(set(ranks))== 4 and (max(ranks) - min(ranks)== 3):
        return True
    return False

def flush(suits:'list of the suits of cards')->'bool':
    ''' All of same deck
    So set will make all 5 to 1 and we will check that by its length'''
    if len(set(suits)) == 1:
        return True
    return False

def kind(n:'This variable tells the type of kind',ranks:'list of the rank of cards')->'list':
    '''We are getting n which type of kind
    Now take each type of number from ranks and count its presence
    if it matches n then return true else false'''
    '''for r in set(ranks):
        if ranks.count(r) == n:
            return True
    return False'''
    '''Another implementation
    As we are assuming we are getting ranks in desc order
    eg - [11, 2, 2, 1, 1]'''
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks:'list of the rank of cards')->'bool':

    '''
    flag = 0
    for r in set(ranks):
        if ranks.count(r) > 1:
            flag = flag + 1
    if flag == 2:
        return True
    return False
    '''
    hicard = kind(2,ranks)
    locard = kind(2, tuple(reversed(ranks)))

    if hicard != locard:
        return (hicard, locard)
    return False


def card_ranks(hand:'It is a list of values in one hand')->'list':
    '''This fucntion is used to find the rank of the hands shared by the 2 players
    It uses the standard ordering for the deck of cards
    '''
    ranks=["--23456789TJQKA".index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

def card_suits(hand:'It is a list of values in one hand')->'list':
    '''This fucntion is used to know the suits of cards, it acts as
    a helper function hand_rank fucntion.
    '''
    return [s for r,s in hand]

def poker(hands:'It is a tuple conatining both the values of hands from the two players')->'list':
    '''Given two hands find out which one is the winner'''

    if(len(hands[0])==5 and len(hands[1])==5):
        
        l=[]
        for i in range(len(hands)):
            l.append(list(hand_rank(hands[i])))
    elif (len(hands[0])==3 and len(hands[1])==3):
        l=[]
        for i in range(len(hands)):
            l.append(list(hand_rank_v1(hands[i])))
    elif (len(hands[0])==4 and len(hands[1])==4):
        l=[]
        
        for i in range(len(hands)):
            l.append(list(hand_rank_v2(hands[i])))
    else:
        raise ValueError ('Both Hands should be of same size')

    a= l.index(max(l))
    m=max(l)
    k=['Straight Flush','Four of a Kind','Full House','Flush','Straight','Three of a Kind','Two Pair','One Of a Kind','HighestCard']
    k=list(reversed(k))

    if(m==[8,14]) or (m==[7,14]) or (m==[5,14]) :
        if (l[0]!=l[1]):
            ww=a+1
            return str(a+1)
        else:
            return ("HARD LUCK")

    else:
        if (l[0][0]!=l[1][0]):
            ww=a+1
            return str(a+1)
        else:
            return ("HARD LUCK")

def hand_rank_v1(hand:'It is a list of values in one hand')->'tuple':
    '''
    Get the highest rank for a hand except High Card
    Rules vary depending upon the number of cards in a hand as follows:
    For 5-card poker ranks in order (highest to lowest)
    Royal flush
    Straight flush
    Four of a kind
    Full house
    Flush
    Straight
    Three of a kind
    Two pair
    Pair
    High Card'''
    ranks = card_ranks(hand)
    suits = card_suits(hand)
    if straight_3cards(ranks) and flush(suits):
        return (5, max(ranks))
    elif flush(suits):
        return (4,)+tuple(ranks)
    elif straight_3cards(ranks):
        return (3, max(ranks))
    elif kind(3,ranks):
        same=kind(3,ranks)
        return (2,same)+tuple([i for i in ranks if i!=same])
    elif kind(2,ranks):
        same=kind(2,ranks)
        return (1,same)+tuple([i for i in ranks if i!=same])
    else:
        return (0,)+tuple(ranks)

def hand_rank(hand:'It is a list of values in one hand')->'tuple':
    '''For 3-card poker ranks in order (highest to lowest)
    Straight flush
    Three of a kind
    Straight
    Flush
    Pair
    High card
    '''
    ranks = card_ranks(hand)
    suits = card_suits(hand)

    if straight(ranks) and flush(suits):
        return (8, max(ranks))
    elif kind(4,ranks):
        return (7, kind(4,ranks),kind(1,ranks))
    elif kind(3,ranks) and kind(2,ranks):
        return (6, kind(3,ranks),kind(2,ranks))
    elif flush(suits):
        return (5,)+tuple(ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3,ranks):
        same=kind(3,ranks)
        return (3,same)+tuple([i for i in ranks if i!=same])
    elif two_pair(ranks):
        return (2,)+two_pair(ranks)+((kind(1,ranks)),)
    elif kind(2,ranks):
        same=kind(2,ranks)
        return (1,same)+tuple([i for i in ranks if i!=same])
    else:
        return (0,)+tuple(ranks)

def hand_rank_v2(hand:'It is a list of values in one hand')->'tuple':
    '''For 4-card poker ranks in order (highest to lowest)
    Four of a kind
    Straight flush
    Three of a kind
    Flush
    Straight
    Two pair
    One pair
    High card'''
    ranks = card_ranks(hand)
    suits = card_suits(hand)
    if straight_4cards(ranks) and flush(suits):
        return (7, max(ranks))
    elif kind(4,ranks):
        return (6, kind(4,ranks),kind(1,ranks))
    elif flush(suits):
        return (5,)+tuple(ranks)
    elif straight_4cards(ranks):
        return (4, max(ranks))
    elif kind(3,ranks):
        same=kind(3,ranks)
        return (3,same)+tuple([i for i in ranks if i!=same])
    elif two_pair(ranks):
        return (2,)+two_pair(ranks)+((kind(1,ranks)),)
    elif kind(2,ranks):
        same=kind(2,ranks)
        return (1,same)+tuple([i for i in ranks if i!=same])
    else:
        return (0,)+tuple(ranks)