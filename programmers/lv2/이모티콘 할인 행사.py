# 1
rates = [10, 20, 30, 40]
emti_discount = []


def get_emti_discount(discount, n, r, emoticons):
    if n == r:
        emti_discount.append(discount)
        return
    
    for rate in rates:
        price = emoticons[n] * (100 - rate) * 0.01
        discount[n] = (rate, price)
        get_emti_discount(discount, n + 1, r, emoticons)
        discount = discount.copy()
    

def solution(users, emoticons):    
    m = len(emoticons)
    get_emti_discount([None] * m, 0, m, emoticons)
    
    answer = [0, 0]
    for emti in emti_discount:
        emti_plus, emti_sell = 0, 0
        for user_rate, user_price in users:
            user_buy = 0
            for rate, price in emti:
                if rate >= user_rate:
                    user_buy += price

            if user_buy >= user_price:
                emti_plus += 1
            else:
                emti_sell += user_buy
                
        answer = max(answer, [emti_plus, emti_sell])
                
    return answer


# 2
from itertools import product


def solution(users, emoticons):
    m = len(emoticons)
    rates = [10, 20, 30, 40]

    answer = [0, 0]
    for rate in product(rates, repeat=m):
        emti_plus, emti_sell = 0, 0
        for user_rate, user_price in users:
            user_buy = 0
            for r, emoticon in zip(rate, emoticons):
                if r >= user_rate:
                    user_buy += emoticon * (100 - r) * 0.01
            if user_buy >= user_price:
                emti_plus += 1
            else:
                emti_sell += user_buy

        answer = max(answer, [emti_plus, emti_sell])

    return answer
