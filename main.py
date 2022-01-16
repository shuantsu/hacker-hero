# -*- encoding: iso8859-1 -*-
import Cerealizer, ConfigParser, tkFileDialog, tkColorChooser, tkMessageBox, hashlib, sys
from Tkinter import *

IMAGE = \
'''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'''

def decodify(data):

  try:
    return Cerealizer.loads(data.decode('hex'))
  except:
    return None

class TextFunction:

  def text(self, text):

    if text == None:
      text = ''

    self.delete(0, len(self.get()))
    self.insert(0, text)

class MyEntry(Entry, TextFunction):

  pass

class MySpinbox(Spinbox, TextFunction):

  pass

class Window:

  def __init__(self, toplevel):

    self.fileName = None
    self.saveFileName = None
    self.filetypes = [('Configuration files', '*.ini'), ('All', '*.*')]
    self.changed = False
    self.last = None

    #image
    photo = PhotoImage(data = IMAGE)
    self.label = Label(image = photo)
    self.label.image = photo
    self.label.pack()

    #Frames
    self.topframe = Frame(toplevel)
    self.middleframe = Frame(toplevel)
    self.bottomframe = Frame(toplevel)

    #LabelFrames
    self.entriesframe = LabelFrame(self.topframe, text = 'Song Configurations')
    self.difficultiesframe = LabelFrame(self.middleframe, text = 'Difficulties')
    self.listboxframe = LabelFrame(self.middleframe, text = 'Scores')
    self.individual = LabelFrame(self.bottomframe, text = 'Edit Score')

    #song
    self.artistlabel = Label(self.entriesframe, text = 'artist')
    self.cassettecolorlabel = Label(self.entriesframe, text = 'cassettecolor')
    self.countlabel = Label(self.entriesframe, text = 'count')
    self.namelabel = Label(self.entriesframe, text = 'name')

    self.artist = MyEntry(self.entriesframe)
    self.cassettecolor = MyEntry(self.entriesframe)
    self.count = MySpinbox(self.entriesframe, from_ = 0, to = sys.maxint, width = 18)
    self.name = MyEntry(self.entriesframe)

    #scores
    self.playernamelabel = Label(self.individual, text = 'Name')
    self.starslabel = Label(self.individual, text = 'Stars')
    self.scorelabel = Label(self.individual, text = 'Score')

    self.playername = MyEntry(self.individual)
    self.stars = MySpinbox(self.individual, from_ = 0, to = 5, width = 18, command = self.changeStats)
    self.score = MyEntry(self.individual)

    self.radiovar = IntVar()
    self.radiovar.set(3)
    self.supaeasy = Radiobutton(self.difficultiesframe, text = 'Supaeasy',
                                variable = self.radiovar, value = 3, command = self.showStats)
    self.easy = Radiobutton(self.difficultiesframe, text = 'Easy',
                            variable = self.radiovar, value = 2, command = self.showStats)
    self.medium = Radiobutton(self.difficultiesframe, text = 'Medium',
                              variable = self.radiovar, value = 1, command = self.showStats)
    self.amazing = Radiobutton(self.difficultiesframe, text = 'Amazing',
                               variable = self.radiovar, value = 0, command = self.showStats)

    self.listbox = Listbox(self.listboxframe, height = 6)

    #grids and packs

    self.topframe.pack()
    self.middleframe.pack()
    self.bottomframe.pack()

    self.entriesframe.pack(side = TOP)

    self.artistlabel.grid(column = 0, row = 0)
    self.cassettecolorlabel.grid(column = 0, row = 1)
    self.countlabel.grid(column = 0, row = 2)
    self.namelabel.grid(column = 0, row = 3)

    self.artist.grid(column = 1, row = 0)
    self.cassettecolor.grid(column = 1, row = 1)
    self.count.grid(column = 1, row = 2)
    self.name.grid(column = 1, row = 3)

    self.difficultiesframe.pack(side = LEFT)

    self.supaeasy.grid(column = 0, row = 0)
    self.easy.grid(column = 0, row = 1)
    self.medium.grid(column = 0, row = 2)
    self.amazing.grid(column = 0, row = 3)

    self.listboxframe.pack(side = LEFT)

    self.listbox.grid(column = 0, row = 0)

    self.individual.pack()

    self.playernamelabel.grid(column = 0, row = 0)
    self.starslabel.grid(column = 0, row = 1)
    self.scorelabel.grid(column = 0, row = 2)
    self.playername.grid(column = 1, row = 0)
    self.stars.grid(column = 1, row = 1)
    self.score.grid(column = 1, row = 2)

    #menu
    self.menu = Menu(toplevel)
    self.filemenu = Menu(self.menu, tearoff = 0)
    self.filemenu.add_command(label = "Open", command = self.openFile, accelerator = 'Ctrl + O')
    self.filemenu.add_command(label = "Save", command = self.saveFile, accelerator = 'Ctrl + S')
    self.filemenu.add_command(label = "Save As...", command = self.saveAs)
    self.filemenu.add_separator()
    self.filemenu.add_command(label = "Exit", command = self.onQuit)
    self.menu.add_cascade(label = "File", menu = self.filemenu)
    toplevel.config(menu = self.menu)

    self.helpmenu = Menu(self.menu, tearoff = 0)
    self.helpmenu.add_command(label = "About", command = self.about)
    self.menu.add_cascade(label = "Help", menu = self.helpmenu)

    #binds
    self.cassettecolor.bind('<FocusIn>', self.color)
    toplevel.bind_all('<Control-o>', self.openFile)
    toplevel.bind_all('<Control-s>', self.saveFile)
    self.listbox.bind('<<ListboxSelect>>', self.showEntry)
    self.playername.bind('<KeyRelease>', self.changeStats)
    self.stars.bind('<KeyRelease>', self.changeStats)
    self.score.bind('<KeyRelease>', self.changeStats)
    self.count.bind('<FocusIn>', self.changeLastCount)
    self.artist.bind('<FocusIn>', self.changeLastArtist)

    self.artist.bind('<KeyRelease>', self.changedControls)
    self.name.bind('<KeyRelease>', self.changedControls)
    self.count.bind('<KeyRelease>', self.changedControls)
    self.count['command'] = self.changedControls

    self.toggleAllControls(DISABLED)

    #Validates
    self.countstringvar = StringVar()
    self.countstringvar.trace("w", lambda name, index, mode,
                              sv = self.countstringvar: self.noLettersValidate(sv, self.count))

    self.starsstringvar = StringVar()
    self.starsstringvar.trace("w", lambda name, index, mode,
                              sv = self.starsstringvar: self.noLettersValidate(sv, self.stars))

    self.scorestringvar = StringVar()
    self.scorestringvar.trace("w", lambda name, index, mode,
                              sv = self.scorestringvar: self.noLettersValidate(sv, self.score))

    self.count['textvariable'] = self.countstringvar
    self.stars['textvariable'] = self.starsstringvar
    self.score['textvariable'] = self.scorestringvar

  def changedControls(self, event = None):

    if event.keycode == 13:
      return
    self.changed = True

  def removeLetters(self, s):

    a = []
    for i in s:
      if i.isdigit():
        a.append(i)
    return ''.join(a)

  def noLettersValidate(self, sv, w):

    w.text(self.removeLetters(sv.get()))

  def colorTuple(self, color):
    if color == '':
      return ((255,255,255), '')
    c = lambda x, y, z: ord(x[y:z].decode('hex'))
    return ((c(color, 1, 3), c(color, 3, 5), c(color, 5, 7)), color)

  def changeLastCount(self, event):

    self.last = 'count'

  def changeLastArtist(self, event):

    self.last = 'artist'

  def color(self, event = None):

    if event != None:
      if self.last == 'count':
        self.artist.focus_set()
      else:
        self.count.focus_set()
    bg = ''
    fg = ''
    oldcolor = self.cassettecolor.get()
    if event != None:
      newcolor = tkColorChooser.askcolor(oldcolor)
    else:
      newcolor = self.colorTuple(oldcolor)
    if newcolor == (None, None):
      return
    fg = 'black' if (sum(map(int, newcolor[0])) / 3) > (255 / 2) else 'white'
    bg = newcolor[1]
    self.cassettecolor.text(bg)
    self.cassettecolor['bg'] = bg or 'white'
    self.cassettecolor['fg'] = fg or 'black'

  def saveFile(self, event = None, dontask = False):

    if self.fileName == None:
      tkMessageBox.showwarning('Warning', 'Please open a file')
      return
    if self.saveFileName or dontask:
      tosave = 'yes'
    else:
      tosave = tkMessageBox.askquestion('Save', 'Are you sure you want to rewrite this file?')
    if tosave == 'yes':
      f = file(self.saveFileName or self.fileName, 'w')
      artist = self.artist.get()
      cassette = self.cassettecolor.get()
      count = self.count.get()
      name = self.name.get()
      if artist:
        self.cp.set('song', 'artist', artist)
      if count:
        self.cp.set('song', 'count', count)
      if cassette:
        self.cp.set('song', 'cassettecolor', cassette)
      if name:
        self.cp.set('song', 'name', name)
      if self.scores:
        self.cp.set('song', 'scores', Cerealizer.dumps(self.scores).encode('hex'))
      self.cp.write(f)
      f.close()
      self.changed = False
    else:
      pass

  def saveAs(self):

    if self.fileName == None:
      tkMessageBox.showwarning('Warning', 'Please open a file')
      return

    fn = tkFileDialog.asksaveasfilename(filetypes = self.filetypes, defaultextension = '.ini')
    if fn:
      self.saveFileName = fn
      self.saveFile()

  def toggleControls(self, toggle):

    for i in [self.artist, self.cassettecolor, self.count, self.name,
              self.listbox, self.supaeasy, self.easy, self.medium, self.amazing]:
      i['state'] = toggle

  def toggleIndividual(self, toggle):
    self.playername['state'] = toggle
    self.stars['state'] = toggle
    self.score['state'] = toggle

  def toggleAllControls(self, toggle):

    self.toggleControls(toggle)
    self.toggleIndividual(toggle)

  def refreshValues(self, data):

    self.toggleControls(NORMAL)

    self.artist.text(self.data.get('song').get('artist'))
    self.cassettecolor.text(self.data.get('song').get('cassettecolor'))
    self.count.text(self.data.get('song').get('count'))
    self.name.text(self.data.get('song').get('name'))
    self.color()

  def openFile(self, event = None):

    self.toggleIndividual(DISABLED)

    if self.fileName != None and self.changed:
      do_open = self.askToSave()
      if not do_open:
        return

    self.fileName = tkFileDialog.askopenfilename(filetypes = self.filetypes)
    if self.fileName == '': return
    self.saveFileName = None
    self.data = self.readScores(self.fileName)
    try:
      self.scores = decodify(self.data['song']['scores'])
    except:
      self.scores = None
    self.refreshValues(self.data)

    self.changed = False

    self.loadScores()
    self.showStats()
    self.score.text('')
    self.stars.text('')
    self.playername.text('')

  def showEntry(self, event = None):

    i = self.radiovar.get()
    try:
      self.listbox.curselection()[0]
    except:
      return
    self.toggleIndividual(NORMAL)
    self.curselection = self.listbox.curselection()[0]
    self.score.text(self.scores[i][self.curselection][0])
    self.stars.text(self.scores[i][self.curselection][1])
    self.playername.text(self.scores[i][self.curselection][2])

  def showStats(self):

    i = self.radiovar.get()
    self.listbox.delete(0, self.listbox.size())
    for item in self.scores[i]:
      self.listbox.insert(END, item[2])

  def changeStats(self, event = None):

    if event.keycode == 13:
      return
    self.changed = True
    if event == None:
      widget = self.stars
    else:
      widget = event.widget
    i = int(self.radiovar.get())
    w = self.curselection
    s = widget.get()
    score = int(self.score.get()) if self.score.get() else 0
    stars = int(self.stars.get()) if self.stars.get() else 0
    name = self.playername.get().encode('iso8859-1')
    if widget == self.playername:
      self.listbox.delete(w)
      self.listbox.insert(w, s)
    hash = hashlib.sha1("%d%d%d%s" % (i, score, stars, name)).hexdigest()
    self.scores[i][w] = (score, stars, name, hash)
    print self.scores[i][w]

  def readScores(self, fileName):

    self.cp = ConfigParser.ConfigParser()
    self.cp.read(fileName)

    return dict([[s, dict(self.cp.items(s))] for s in self.cp.sections()])

  def loadScores(self):

    self.supaeasy['state'] = DISABLED
    self.easy['state'] = DISABLED
    self.medium['state'] = DISABLED
    self.amazing['state'] = DISABLED

    try:
      difficulties = [self.amazing, self.medium, self.easy, self.supaeasy]
      for k in self.scores.keys():
        difficulties[k]['state'] = NORMAL
        self.radiovar.set(k)
    except:
      pass

  def about(self):

    tkMessageBox.showinfo('About', 'This program was made with Python 2.7.8\n' + \
                                   'Author: Filipe Teixeira\n' + \
                                   'E-mail: shuantsu@gmail.com\n')

  def askToSave(self):

    if self.fileName == None:
      sys.exit()

    if self.changed == False:
      return True

    answer = tkMessageBox.askquestion('::Hacker Hero::',
                            'Save file "%s"?' % self.fileName,
                            type = 'yesnocancel')
    if answer == 'cancel':
      return False
    if answer == 'yes':
      self.saveFile(dontask = True)
    return True

  def onQuit(self):

    print self.changed

    if self.changed == False:
      sys.exit()

    quit = self.askToSave()
    if quit:
      sys.exit()

root = Tk()
w = Window(root)
root.resizable(0, 0)
root.config(padx = 10, pady = 10)
root.title('::Hacker Hero::')
root.protocol('WM_DELETE_WINDOW', w.onQuit)
root.mainloop()