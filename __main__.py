import main
import time
import sys
import pygame
pygame.mixer.init()
def parse(msg,param):
    if param=='i':
        msg=msg.strip()
        if msg.endswith(":") or msg.endswith(">"):
            return msg,'Q'

        else:
            return msg,'N'
    elif param=='c':
        
        
        if msg=='[STATIC]':
            return msg,'STRT_STATIC'
        elif msg=='[NEWLINE]':
            return msg,'NEWLINE'
        
        elif '[WAIT]' in msg:
            return msg,'WAIT'
        elif '[AUDIO]' in msg:
            return msg,'AUDIO'
        
        else:
            return msg,'N'
gen=main.strt()

sent=False
config='N'
while True:
    if sent==False:
        msg=next(gen)
    
    if isinstance(msg,str):
        msg_P,T=parse(msg,'i')
        if T=='Q':
            a=str(input(msg_P))
            msg=gen.send(a)
            sent=True

        else:
            print(msg_P)
            sent=False
    elif isinstance(msg,list):
        
        de=0
        for item in msg:
            msg_P,T=parse(item,'c')
            
            if T=='STRT_STATIC':
                config='S'
                
            elif T=='AUDIO':
                a,b=msg_P.split(']')
                
                pygame.mixer.music.load(b)
                pygame.mixer.music.play()
                
            elif T=='NEWLINE':
                config='N'
                print()
            elif T=='WAIT':
                a,b=msg_P.split(']')
                time.sleep(float(b))
            else:
                if config=='S':
                    sys.stdout.write(f"\r{msg_P:<50}")
                    sys.stdout.flush()
                    time.sleep(de)
                else:
                    print(msg_P)

        sent=False
    else:
        msg=next(gen)
