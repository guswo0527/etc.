cas =1
wchk='s'

def think(hands, history, old_games):
    global cas
    global wchk
    if len(old_games)==0:
        return cas1(history)
    elif len(history)==0:
        wchk=chk(old_games)
    if len(old_games)!=0 and len(hands) != 6:
        return ret(cas,history)
    if wchk=='w':
        return ret(cas,history)
    elif wchk=='s':
        cas=2
        return cas2(history)
    elif wchk=='l':
        if old_games[len(old_games)-1][0][1]=='1':
            if ((len(old_games)+2))%7 ==0:
                cas=1
                return cas1(history)
            if ((len(old_games)+2))%7 ==1:
                cas=2
                return cas2(history)
            if ((len(old_games)+2))%7 ==2:
                cas=3
                return cas3(history)
            if ((len(old_games)+2))%7 ==3:
                cas=4
                return cas4(history)
            if ((len(old_games)+2))%7 ==4:
                cas=5
                return cas5(history)
            if ((len(old_games)+2))%7 ==5:
                cas=6
                return cas6(history)
            if ((len(old_games)+2))%7 ==6:
                cas=7
                return cas7(history)
        if old_games[len(old_games)-1][0][1]=='2':
            if ((len(old_games)+2))%8 ==0:
                cas=1
                return cas1(history)
            if ((len(old_games)+2))%8 ==1:
                cas=2
                return cas2(history)
            if ((len(old_games)+2))%8 ==2:
                cas=3
                return cas3(history)
            if ((len(old_games)+2))%8 ==3:
                cas=4
                return cas4(history)
            if ((len(old_games)+2))%8 ==4:
                cas=5
                return cas5(history)
            if ((len(old_games)+2))%8 ==5:
                cas=6
                return cas6(history)
            if ((len(old_games)+2))%8 ==6:
                cas=7
                return cas7(history)
            if ((len(old_games)+2))%8 ==7:
                cas=8
                return cas8(history)
        if old_games[len(old_games)-1][0][1]=='3':
            if ((len(old_games)+2))%6 ==0:
                cas=1
                return cas1(history)
            if ((len(old_games)+2))%6 ==1:
                cas=3
                return cas3(history)
            if ((len(old_games)+2))%6 ==2:
                cas=4
                return cas4(history)
            if ((len(old_games)+2))%6 ==3:
                cas=5
                return cas5(history)
            if ((len(old_games)+2))%6 ==4:
                cas=7
                return cas7(history)
            if ((len(old_games)+2))%6 ==5:
                cas=8
                return cas8(history)
        if old_games[len(old_games)-1][0][1]=='4':
            if ((len(old_games)+2))%5 ==0:
                cas=1
                return cas1(history)
            if ((len(old_games)+2))%5 ==1:
                cas=2
                return cas2(history)
            if ((len(old_games)+2))%5 ==2:
                cas=6
                return cas6(history)
            if ((len(old_games)+2))%5 ==3:
                cas=7
                return cas7(history)
            if ((len(old_games)+2))%5 ==4:
                cas=8
                return cas8(history)
        if old_games[len(old_games)-1][0][1]=='5':
            if ((len(old_games)+2))%8 ==0:
                cas=1
                return cas1(history)
            if ((len(old_games)+2))%8 ==1:
                cas=2
                return cas2(history)
            if ((len(old_games)+2))%8 ==2:
                cas=3
                return cas3(history)
            if ((len(old_games)+2))%8 ==3:
                cas=4
                return cas4(history)
            if ((len(old_games)+2))%8 ==4:
                cas=5
                return cas5(history)
            if ((len(old_games)+2))%8 ==5:
                cas=6
                return cas6(history)
            if ((len(old_games)+2))%8 ==6:
                cas=7
                return cas7(history)
            if ((len(old_games)+2))%8 ==7:
                cas=8
                return cas8(history)
        if old_games[len(old_games)-1][0][1]=='!':
            if ((len(old_games)+2))%8 ==0:
                cas=1
                return cas1(history)
            if ((len(old_games)+2))%8 ==1:
                cas=2
                return cas2(history)
            if ((len(old_games)+2))%8 ==2:
                cas=3
                return cas3(history)
            if ((len(old_games)+2))%8 ==3:
                cas=4
                return cas4(history)
            if ((len(old_games)+2))%8 ==4:
                cas=5
                return cas5(history)
            if ((len(old_games)+2))%8 ==5:
                cas=6
                return cas6(history)
            if ((len(old_games)+2))%8 ==6:
                cas=7
                return cas7(history)
            if ((len(old_games)+2))%8 ==7:
                cas=8
                return cas8(history)
def chk(old):
    count=0
    w_count=0
    while count<6:
        if w_count<=-3:
            return 'l'
        elif w_count>=3:
            return 'w'
        if old[len(old)-1][count][0]==old[len(old)-1][count][1]:
            count+=1
            continue
        if old[len(old)-1][count][0]=='1' and (old[len(old)-1][count][1]=='5' or old[len(old)-1][count][1]=='!'):
            w_count+=1
        elif old[len(old)-1][count][0]=='1':
            w_count-=1
        if old[len(old)-1][count][0]=='2' and old[len(old)-1][count][1]=='1':
            w_count+=1
        elif old[len(old)-1][count][0]=='2':
            w_count-=1
        if old[len(old)-1][count][0]=='3' and (old[len(old)-1][count][1]=='1' or old[len(old)-1][count][1]=='2' or old[len(old)-1][count][1]=='!'):
            w_count+=1
        elif old[len(old)-1][count][0]=='3':
            w_count-=1
        if old[len(old)-1][count][0]=='4' and (old[len(old)-1][count][1]=='1' or old[len(old)-1][count][1]=='2' or old[len(old)-1][count][1]=='3'):
            w_count+=1
        elif old[len(old)-1][count][0]=='4':
            w_count-=1
        if old[len(old)-1][count][0]=='5' and old[len(old)-1][count][1]!='1':
            w_count+=1
        elif old[len(old)-1][count][0]=='5':
            w_count-=1
        if old[len(old)-1][count][0]=='!' and (old[len(old)-1][count][1]=='2' or old[len(old)-1][count][1]=='4'):
            w_count+=1
        elif old[len(old)-1][count][0]=='!':
            w_count-=1
        count+=1
        if count>=6 and w_count<0:
            return 'l'
        elif count>=6 and w_count==0:
            return 's'
        elif count>=6 and w_count>0:
            return 'w'
            
def ret(inp,real):
    if inp==1:
        return cas1(real)
    if inp==2:
        return cas2(real)   
    if inp==3:
        return cas3(real)
    if inp==4:
        return cas4(real)         
    if inp==5:
        return cas5(real)
    if inp==6:
        return cas6(real)
    if inp==7:
        return cas7(real)
    if inp==8:
        return cas8(real)   
def cas1(history):
    if len(history) == 0:
        return '4'
    if len(history) == 1:
        return '1'
    if len(history) == 2:
        return '5'
    if len(history) == 3:
        return '!'
    if len(history) == 4:
        return '3'
    if len(history) == 5:
        return '2'
def cas2(history):
    if len(history) == 0:
        return '1'
    if len(history) == 1:
        return '3'
    if len(history) == 2:
        return '5'
    if len(history) == 3:
        return '!'
    if len(history) == 4:
        return '4'
    if len(history) == 5:
        return '2'   
def cas3(history):
    if len(history) == 0:
        return '1'
    if len(history) == 1:
        return '3'
    if len(history) == 2:
        return '!'
    if len(history) == 3:
        return '5'
    if len(history) == 4:
        return '4'
    if len(history) == 5:
        return '2'
def cas4(history):
    if len(history) == 0:
        return '3'
    if len(history) == 1:
        return '1'
    if len(history) == 2:
        return '5'
    if len(history) == 3:
        return '!'
    if len(history) == 4:
        return '4'
    if len(history) == 5:
        return '2'
def cas5(history):
    if len(history) == 0:
        return '3'
    if len(history) == 1:
        return '5'
    if len(history) == 2:
        return '1'
    if len(history) == 3:
        return '!'
    if len(history) == 4:
        return '4'
    if len(history) == 5:
        return '2'
def cas6(history):
    if len(history) == 0:
        return '3'
    if len(history) == 1:
        return '!'
    if len(history) == 2:
        return '1'
    if len(history) == 3:
        return '5'
    if len(history) == 4:
        return '4'
    if len(history) == 5:
        return '2'
def cas7(history):
    if len(history) == 0:
        return '3'
    if len(history) == 1:
        return '!'
    if len(history) == 2:
        return '5'
    if len(history) == 3:
        return '1'
    if len(history) == 4:
        return '4'
    if len(history) == 5:
        return '2'
def cas8(history):
    if len(history) == 0:
        return '!'
    if len(history) == 1:
        return '3'
    if len(history) == 2:
        return '5'
    if len(history) == 3:
        return '4'
    if len(history) == 4:
        return '1'
    if len(history) == 5:
        return '2'