def intro():
    print('welcome to de game')
    print('you are a knight of the kingdom of potata')
    print('the evil potata mashes have invaded')
    print('your quest is mash the potata in kombat and save the beautiful queen from becoming potata fries')
def combat(enemy):
    pass

def command(prompt):
    if 'look' in prompt:
        print("you look around....")
        print('and see....')
    elif 'walk' in prompt:
        if 'north' in prompt:
            print('you walk north')
        elif 'south' in prompt:
            print('you walk south')
        elif 'east' in prompt:
            print('you walk east')
        elif 'west' in prompt:
            print('you walk west')
        else:
            print('which direction do you want to walk')
            direction = input('> ')
            prompt = prompt + '' + direction
            command(prompt)
        #TODO: look around.
    elif 'kill' in prompt:
        if 'boss' in prompt:
            print('the boss is too strong and u suck')
        else :
            print('who do you want to kill?')
            target  = input ('> ')
            if 'ryan' in prompt:
                input('how do you want to kill him?')
                if 'stab' in input:
                    print('ryan tong died of loosing too much blood')
                elif 'shoot' in prompt:
                    print('ryan tong died painfully in his own blood')
                else:
                    print('ryan tong was so scared that he peed his pants')
            else:
                print("idk who you want to kill")
                prompt = prompt+''+target
                command(prompt)




def game():
    intro()
    gameOver = False
    while not gameOver:
        print('wat u want to do?')
        ans = input("> ")
        command(ans)
game()
