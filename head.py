def get_head(nums):
    """get_head supose treated one string where have eight numbers, one birthday.
    It's returned one list with five numbers represent the head's Afro numerology. For more information about this,
    go to Orixa's house or contact one Father or Mother's Saint. And no, you dont become Saint's father for knowing that
    this, and, yeah, i know, my code have much to grow up"""
    h1, f1, h2, f2,h3,f3, h4, f4= nums[0],nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7]
    more16 = lambda m: int(str(m)[0])+int(str(m)[1])
    adic= lambda *args: more16(sum(args)) if sum(args) > 16 else sum(args)
    head =adic(int(h1)+int(h2)+int(h3)+int(h4)) 
    foot= adic(int(f1)+int(f2)+int(f3)+int(f4)) 
    future = adic(head+foot) 
    past = adic(foot+future)
    center = adic(head+foot+future+past)
    return [head, foot, future, past, center]


if __name__=='__main__':
    import re
    def treat_str(string):
        """One intern function just for treat de input """
        data=re.compile(r'[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]')
        if len(string) !=10 or re.match(data,string) is None:
            return None
        else:
            string=string.split('/')
            if int(string[0]) >31 or int(string[1]) > 12 or int(string[2]) > 2021:
                return None
            else:
                return ''.join(string)

    while True:
        data=input('Digite sua data de nascimento:\n')
        if treat_str(data) is None:
            print('Digite corretamente sua data de nascimento, tipo dd/mm/aaaa')
        else:
            head,foot, future, past, center = get_head(treat_str(data))
            print("cabeça: {}\nPé: {}\nFuturo: {}\nPassado: {}\nCentro: {}".format(head,foot,future,past,center))
            break
            