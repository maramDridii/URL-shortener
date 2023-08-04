import tkinter
import pyshorteners


def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))


root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("300x150")
root.configure(bg="#8076a3")
root.resizable(0,0)

longurl_label = tkinter.Label(root, text="Enter Long URL",bg="#8076a3",fg="#FFFFFF",font=("Arial",10))
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root, text="Output shortened URL",bg="#8076a3",fg="#FFFFFF",font=("Arial",10))
shorturl_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root, text="Shorten URL", command=shorten,bg="#8076a3",fg="#FFFFFF",font=("Arial",10))

longurl_label.grid(row=0, column=0, columnspan=2, sticky='news',pady=10)
longurl_entry.grid(row=0,column=3,columnspan=2, sticky='news',pady=10)
shorturl_label.grid(row=2,column=0,columnspan=2, sticky='news',pady=10)
shorturl_entry.grid(row=2,column=3,columnspan=2, sticky='news',pady=10)
shorten_button.grid(row=4,column=2,columnspan=2, sticky='news',pady=10)

root.mainloop()