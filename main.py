'''
1. Learn How to calculate Words per Minute
2. Make Basic Tkinter Body 
3. Build on Top of it.
'''
import random
import time
import tkinter as tk



WHITE = "#FFFFFF"
running=False
 

def get_sentence():
    with open('quotes.txt',mode="r") as file:
        quotes=list(file.readlines())
    # Sentence Editing.
    fresh_sentence="".join([x for x in random.choice(quotes) if x!='"'])
    fresh_sentence=fresh_sentence.split(".")[0]
    fresh_sentence="".join([fresh_sentence,"."])
  
    return fresh_sentence

sentence="..."



x=1
t0=0

def stop():
    global x,sentence,t0
    if x==1:
        x*=-1
        sentence=get_sentence()
        instructions_label.config(text=f"TYPE THE TEXT:\n{sentence}")
        t0=time.time()
        start_button.config(text='STOP')
        review_label.config(text=f"{0} WPM\n{0}% Accuracy\nTimeTaken:{(0):.02f} Mins")
        enter_the_text_entry.delete(0,tk.END)
    elif x==-1:
        x*=-1
        t1=time.time()
        accuracy=len(set(enter_the_text_entry.get().split(" ")))&len(set(sentence.split(" ")))
        wordcount=len(set(sentence.split(" ")))
        accuracy/=wordcount
        timetaken=t1-t0
        wpm=float(wordcount)/(timetaken/60)
        instructions_label.config(text=f"TYPE THE TEXT:\n{'...'}")
        review_label.config(text=f"{wpm:.2f} WPM\n{accuracy*100:.2f}% Accuracy\nTimeTaken:{(timetaken/60):.02f} Mins")
        enter_the_text_entry.delete(0,tk.END)
        start_button.config(text='START')



window=tk.Tk()
window.title('Speed Test App')
window.config(padx=40,pady=40,background=WHITE)
canvas=tk.Canvas(width=200,height=200,highlightthickness=0)
image_file=tk.PhotoImage(file='SpeedTestApp.png')
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=0,padx=5,columnspan=3)


instructions_label=tk.Label(text=f"TYPE THE TEXT:\n{sentence}",background=WHITE,font=("Cascadia Code",20),wraplength=800)
instructions_label.grid(row=1,column=0,padx=5,pady=15,columnspan=3)
start_typing_label=tk.Label(text="START TYPING: ",background=WHITE,font=("Cascadia Code",20))
start_typing_label.grid(row=2,column=1,padx=5)
review_label=tk.Label(text="",font=("Cascadia Code",20),background=WHITE)
review_label.grid(row=4,column=1,padx=5)

enter_the_text_entry=tk.Entry(width=50,font=("Cascadia Code",20,))
enter_the_text_entry.grid(row=3,column=0,padx=5,pady=2,columnspan=3)

enter_the_text_entry.focus()
print(enter_the_text_entry.get())

start_button=tk.Button(text='START',command=stop,font=("Cascadia Code",20))
start_button.grid(row=5,column=1,padx=5,pady=15)



window.mainloop()