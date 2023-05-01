
define p = Character("[p]") #This represents the player
define l = Character("Librarian", color ='#FCE697')
define b = Character("Bartender" , color = '#64353C')

default l_friendship = 0 #This counts up the affection point that the player has for Char A
default b_friendship = 0
default journal_pieces = 7 
default page_size = (694,551)
default correct_locations = [(406,382),(448,297),(376,433),(303,507,),(415,272),(403,448),(583,636)] 
default random_starting_locations = []
default correctly_placed = 0


init python:  
    def drag_placed(drags, drop): #The drag_placed function is referenced from https://github.com/VimislikArt/dragdropcode/blob/main/dragdrop.rpy#L6
        if not drop:
            renpy.jump('checkout_process')
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        return True

    def puzzle_maker(): #randomizes puzzle peices
        for piece in range(journal_pieces):#1300 1500 300 600
            peice_locations = (renpy.random.randint(1500,1600),renpy.random.randint(500,600))#100 300
            random_starting_locations.append(peice_locations)

    def piece_drop(dropped_piece,dragged_piece): #referenced from https://www.youtube.com/watch?v=IKLBSJMv50Q&t=635s
        finished_pieces = 0

        if dragged_piece[0].drag_name == dropped_piece.drag_name: #Checks if object drag name is equal to the location dropped name
            dragged_piece[0].snap(dropped_piece.x,dropped_piece.y)
            draggged_piece[0].draggable = False 
            finished_pieces +=1
            if finished_pieces == journal_pieces:
                renpy.jump('solved_puzzle')

# The game code starts here.

label start:
    play music 'audio/ambience.mp3' volume 0.3
    scene black bg
    scene black bg with vpunch
    'Alarm' 'BEEP BEEP BEEP'
    'Ughhhhhh. Time to wake up'
    scene bedroom day
    'That was such a weird dream, my head hurts so much'
    '...'
    'Why do my hands feel so funny???'
    scene bedroom day with vpunch
    show paw hands
    '...'
    'HUH?!?!?'
    'ARE THOSE PAWS'
    'WHATS GOING ON'
    'OK wait calm down, im probably just dreaming still'
    'I\'ve never had such a lucid dream before'
    'These claws are pretty cool'
    show paw hands with vpunch
    'YOUCH! They\'re sharp too'
    '...'
    'Wait if this is a dream why did that hurt'
    '...'
    'There is no way...'
    hide paw hands
    'WAIT EVEN THE POSTERS ARE ANIMALS'
    'THIS CAN\'T JUST BE HAPPENING TO ME I GOTTA GO ONLINE'
    scene laptop 
    'WHAT'
    'THERE IS ONLY ONE RESULT'
    scene laptop two 
    'ALTERNATE REALITY?'
    'THIS CANT BE HAPPENING'
    'I have no clue what any of this means'
    'Wait maybe I should try and read this book'
    'But where could I find it'
    scene black bg
    'I should check the the library'
    'Where is that anyway'
    'Oh nice theres a map!'
    call screen map_buttons


screen map_buttons: #referenced from https://www.youtube.com/watch?v=BJ3pqhQf2Rw&t=968s
    add 'bg_map'
    modal True
    imagebutton auto 'library_%s':
        xanchor .5
        yanchor .5
        xpos .5
        ypos .5
        action Jump('library_scene')

    if b_friendship < 2:
        imagebutton auto 'bar_%s':
            xanchor .5
            yanchor .5
            xpos .5
            ypos .5
            hovered  Show('locked_locations', message= 'This location has not been unlocked')
            unhovered Hide('locked_locations')
    else:
        imagebutton auto 'bar_%s':
            xanchor .5
            yanchor .5
            xpos .5
            ypos .5
            action [Hide('locked_locations'),Jump('bar_scene')]
   
    imagebutton:
        xanchor .5
        yanchor .5
        xpos .5
        ypos .5
        idle 'secret_idle.png'
        hover 'secret_hover.png'
        hovered  Show('locked_locations', message= 'This location has not been unlocked')
        unhovered Hide('locked_locations')

    imagebutton:
        xanchor .5
        yanchor .5
        xpos .5
        ypos .5
        idle 'apartment button.png'
        action Jump('library_scene')
    

screen locked_locations:
    default message = ''
    vbox:
        xalign .5
        yalign .5
        frame:
            text message

label library_scene:
    scene black bg
    scene library bg
    show librarian
    show friendship_0

    l 'Hi welcome to the library is there anything I can help you with'
    'ummmm yes do you have any books on alternate realities'
    show librarian happy
    show friendship_1
    $ l_friendship += 1
    l 'Ive never met someone also interested in quantum mechanics'
    '...Yeah totally I love this stuff...'
    l 'Your just in luck! Someone just returned our best book on Multiversal Theory'
    l 'Just drag it to the checkout box and we can loan it to you'
    show librarian at left with move
    l 'Here you go!'
    show checkout bg


label book_selection:
    call screen book_select
    show screen drop_option

    if droppable == 'Checkout':
        $ xpos_var = 500
    else:
        $xpos_var = 300
    if draggable == 'Book one':
        hide book one
        jump checkout_process
    elif draggable == 'Book two':
        hide book two with vpunch
    elif draggable == 'Book three':
        hide book three with vpunch

    #'I dont think thats it'
    #'Why dont you try again'
    #jump book_selection
    jump checkout_process

label checkout_process:
    hide checkout bg
    hide screen drop_option
    show librarian
    l 'Great now you just need to add your name to the checkout log'
    $ p = renpy.input('Enter you name here: ', length = 10) #Input player name with max 10 characters
    $ p = p.strip() #This strips away any accidental spaces before or after
    l 'Well its nice to meet you [p]'
    l 'Feel free to come back if you want discuss any ideas'
    hide librarian
    menu :
        'Totally!':
            show tester at left
            hide friendship_1 at left
            show  friendship_2 at left
            $ l_friendship += 1
            l 'Have a nice day!'
        'I\'d rather not':
            show librarian sad at left
            l 'Well never mind'
            hide friendship_1 at left
            show friendship_0 at left
    hide screen drop_option
    
            
screen book_select:
    draggroup:
        drag:
            drag_name 'Book one'
            child 'book one.png'
            draggable True
            droppable False
            drag_raise True
            dragged drag_placed 
        drag:
            drag_name 'Book two'
            child 'book two.png'
            draggable True
            droppable False
            drag_raise True
            dragged drag_placed
        drag:
            drag_name 'Book three'
            child 'book three.png'
            draggable True
            droppable False
            drag_raise True
            dragged drag_placed
        drag:
            drag_name 'Checkout'
            child 'checkout button.png'
            draggable False
            droppable True
            
screen drop_option:
    drag:
        drag_name 'Checkout'
        child 'checkout button.png'
        draggable False
        droppable False

label leaving_library:
    scene black bg
    p 'I can beleive I found someone who knows about quantem mechanics'
    p 'Maybe my luck is turning up!'
    p 'I wonder if I should talk to her about my... situation'
    p 'eghhh this really sucks I could really use a drink'
    
    
label bar_scene:
    scene bar_bg with None
    show friendship_0
    p 'Well this place doesnt look too bad'
    show bartender
    b 'Hey there what can I getcha!'
    p 'Woah is she a rabit??' 
    p '.... All drinks are all so weird I have no clue what to get' #Internal monolauge
    p 'Honestly anything will do'
    p 'Suprise me!'
    show bartender happy
    $ b_friendship += 1
    show friendship_1
    b 'You got it!'
    hide bartender happy 
    show bartender
    b 'Here is one of my favorites!'
    menu :
        'Woah this is so good!':
            show bartender happy
            $ b_friendship += 1
            b 'I KNOW RIGHT'
            hide friendship_1
            show friendship_2

        'YUCK! Is this just carrot juice':
            show bartender mad
            $ b_friendship -= 1
            b 'You have a problem with carrots'
            hide friendship_1
            show friendship_0

    show bartender
    b 'Oh hey whats that you got there?'
    p 'This?'
    p 'It\'s a book about alternate dimensions'
    p 'Don\t tell me you know about quantum mechanics too'
    b 'HAHAHA what no'
    b 'But there was a guy here not so long ago reading the same book'
    show bartender with vpunch
    p 'REALLY'
    b 'Yeah, the guy was a real lunatic spouting on and on about how the world isn\'t real and that he was actually a \'human\' whatever that\'s supposed to be'
    p 'HAHaha yeah that sounds crazy...'
    p 'You wouldnt have happened to have seen that guy lately would you? '
    b 'Oddly enough no... he used to come in everyday but last week he just stopped showing up'
    b 'I sure hope nothing bad happened to the guy he was pretty entertaining'
    b 'He did leave this journal last time he was here '
    b 'I dont think hes coming arround anytime soon but I can give you his notbook if you\'d like'
    p 'THAT WOULD BE GREAT'
    b 'Well here you go'
    b 'Well if you figure anything out come back and give me an update'
    p 'Yeah i\'ll be sure to do that!'

label walking_home:
    scene walk home
    p 'Wow today went a lot better than expected'
    p 'Now I just gotta get to my room and read this journal'
    scene walk home with vpunch
    p 'WOAH'
    p 'HUH'
    scene walk home with vpunch
    p 'NO'
    p 'ARE YOU KIDDING'

label puzzle:
    scene bedroom night
    p '*HUFF HUFF*'
    p 'THE JOURNAL'
    p 'NOOO ITS GONE'
    p 'All thats left is this one page.... and of course its torn to shreds'
    $ puzzle_maker()
    call screen puzzle_game

label solved_puzzle:
    scene bedroom night
    p 'GOOD AS NEW!'
    p 'Wait what does it say'
    p 'This guy really was crazy huh'
    p 'Who is they supposed to be?'
    p '...dont go to the ...'
    p 'WAIT IT JUST CUTS OFF'
    p 'I HAVE TO FIND THE REST OF THIS JOURNAL'
    p 'ughhh this seems like a tomorrow problem'

screen puzzle_game():
    image 'bedroom night.png'
    frame:
        background 'page_frame.png'
        xysize page_size
        anchor (.7 ,.7)
        pos (270, 380) #250,435
    draggroup:
        for i in range(journal_pieces): #This loop creates each piece and places it randomly
            drag:
                drag_name i
                pos random_starting_locations[i]
                anchor(.5,.5)
                draggable True
                focus_mask True
                drag_raise True
                image 'piece_%s.png' %(i+1)   #image goes on to next one with same name start and incread number
        for i in range(journal_pieces): #This sets up the correct locatins for each torn piece
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos correct_locations[i]
                anchor (.5,.5)
                focus_mask True
                image 'piece_%s.png' % (i+1) alpha 0.0 #alpha will make it invisible

label end:
    scene black bg
    'DAY ONE COMPLETE'
    'To be continued...'
    return
