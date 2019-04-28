#old program idk how it works.................

import vlc, pafy, threading, os
from tkinter import Button, Label, PhotoImage, Tk, Toplevel, Text
song=1

position = '/home/praense/python/radio/files/' 

urllofifile = open(f"{position}.urllofi", 'r')
next_song=1

def next_song(next = True):
    global song
    if next == False:
        global number_song
        with open(f"{position}.songnumber", 'r') as _tempsong:
            number_song = int(_tempsong.read().strip())
            for num in range(0, number_song):
                song = urllofifile.readline()
    if next == True:
        with open(f'{position}.time', 'w') as _temptime:
            _temptime.write("0")
        with open(f"{position}.save", 'w') as _tempsave:
            _tempsave.write('0.0')
        with open(f"{position}.songnumber", 'w') as _tempsong:
            _tempsong.write(str(number_song))
        song = urllofifile.readline()
    number_song += 1
    main(song)
    if next == False:
        timethread = threading.Thread(target=time, args=(song,))
        timethread.start()
def list(event):
    global root_list
    root_list = Toplevel(root)

    x = (root_list.winfo_screenwidth() - root_list.winfo_reqwidth()) / 2
    y = (root_list.winfo_screenheight() - root_list.winfo_reqheight()) / 2
    root_list.wm_geometry("+%d+%d" % (x, y))

    root_list.geometry("356x476")
    root_list.title("Link list")
    text = Text(root_list,width=50, height=30)
    text.place(y=30)
    #[
    buttonsave = Button(root_list, text='Save',width=22)
    buttonsave.place(x=1,y=1)
    buttonexit = Button(root_list, text='Exit',width=21)
    buttonexit.place(x=180,y=1)
    buttonsave.bind("<Button-1>", save_link)
    buttonexit.bind("<Button-1>", exit_link)
    with open(f'{position}.urllofi', 'r') as _templofiurl:
        text.insert("1.0", _templofiurl.read())
    #root_list.protocol("WM_DELETE_WINDOW", ON_close_for_change)
    root_list.mainloop()
def save_link(event):
    with open(f'{position}.urllofi', 'w') as _tempurllofi:
        _tempurllofi.write(text.get('0.1', END))
    urllofifile = open(f'{position}.urllofi', 'r')
    next_song()
    roo_tlist.destroy()
def exit_link(event): root_list.destroy()
def gui():
    global songname,buttonpause, root, songtime
    root = Tk()
    root.title("♥ Lo-fi ♥")
    root.geometry("500x300")
    #icon{
    icon = PhotoImage(file=f"{position}icon.gif")
    root.tk.call('wm', 'iconphoto', root._w, icon)
    #icon}
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    #{
    frame2 = PhotoImage(file=f'{position}gif.gif', format="gif -index 2")
    label = Label(image=frame2)
    label.place(x=-1, y=-2)
    #}
    #[
    #pause
    root.bind('<space>', lambda event: pause(event, buttonpause["text"]))
    buttonpause = Button(root, text='Pause', width=12)
    buttonpause.place(x=380, y=260)
    buttonpause.bind('<Button-1>', lambda event: pause(event, buttonpause["text"]))
    #change urllife
    buttonlist = Button(root, text='List')
    buttonlist.place(x=330, y=260)
    buttonlist.bind('<Button-1>', list)
    #]
    #{
    songname = Label(root, text='Starting...')
    songname.pack()
    songtime = Label(root, text='Time', width="23")
    songtime.place(x=330, y=230)
    #}
    root.protocol("WM_DELETE_WINDOW", close_program)
    root.mainloop()

def time(url, first = True):
    import time
    seconds_length = pafy.new(song).length
    while True:
        time.sleep(1)
        now_length = player.get_position()
        second_now_length = str((now_length * seconds_length)).split('.')[0]
        songtime['text'] = str(second_now_length)+"/"+str(seconds_length)
        if str(second_now_length) == str(seconds_length-1):
            time.sleep(2)
            seconds_length = pafy.new(song).length
def close_program():
    try:
        player.get_position()
        with open (f'{position}.save', 'w') as tempsave:
            tempsave.write(str(player.get_position()))
        with open(f'{position}.time', 'w') as temptime:
            seconds_length = pafy.new(song).length
            now_length = player.get_position()
            second_now_length = (now_length * seconds_length)
            temptime.write(str(second_now_length))
    except NameError:
        False
    os.abort()
def pause(event, text):
    if text == 'Pause':
        buttonpause['text'] = 'Play'
    else:
        buttonpause['text'] = 'Pause'
    player.pause()
def main(url):
    global player
    try:
        lofi_url = pafy.new(url)
    except ValueError:
        sys.exit()
    vlcsession = vlc.Instance()
    player = vlcsession.media_player_new()

    player.set_mrl(lofi_url.getbestaudio().url)
    with open (f"{position}.save", 'r') as _tempsave:
        getposition = float(_tempsave.read())
    with open(f"{position}.time", 'r') as _temotime:
        gettime = _temotime.read().strip()
    player.play()
    player.set_position(getposition)
    songname['text'] = lofi_url.title
    try:
        threadingnewsong.cancel()
    except:
        False
    threadingnewsong = threading.Timer(pafy.new(url).length - int(gettime.split(".")[0]), next_song)
    threadingnewsong.start()
guithread = threading.Thread(target=gui)
guithread.start()
next_song(False)
