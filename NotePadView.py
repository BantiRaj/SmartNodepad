import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, messagebox, filedialog
import NotePadController
import traceback


class Notepad:
    def __init__(self, root):
        self.root = root
        self.url = ''
        self.text_changed = False
        self.notepadController = NotePadController.Controller()
        self.root.geometry('1376x768')
        self.root.title('MyNotePad')
        self.root.wm_iconbitmap('icon.ico')
        self.set_icons()
        self.set_menu_bar()
        self.set_file_sub_menu()
        self.set_edit_sub_menu()
        self.set_tool_bar()
        self.set_canvas()
        self.set_status_bar()
        self.set_file_menu_event_bindings()
        self.root.protocol("WM_DELETE_WINDOW", self.exit_func)

    def set_icons(self):
        self.new_icon = tk.PhotoImage(file='icons/new.png')
        self.open_icon = tk.PhotoImage(file='icons/open.png')
        self.save_icon = tk.PhotoImage(file='icons/save.png')
        self.save_as_icon = tk.PhotoImage(file='icons/save_as.png')
        self.exit_icon = tk.PhotoImage(file='icons/exit.png')
        self.copy_icon = tk.PhotoImage(file='icons/copy.png')
        self.paste_icon = tk.PhotoImage(file='icons/paste.png')
        self.cut_icon = tk.PhotoImage(file='icons/cut.png')
        self.clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
        self.find_icon = tk.PhotoImage(file='icons/find.png')
        self.tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
        self.status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')
        self.light_default_icon = tk.PhotoImage(file='icons/light_default.png')
        self.light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
        self.dark_icon = tk.PhotoImage(file='icons/dark.png')
        self.red_icon = tk.PhotoImage(file='icons/red.png')
        self.monokai_icon = tk.PhotoImage(file='icons/monokai.png')
        self.night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

    def set_menu_bar(self):
        self.main_menu = tk.Menu()
        self.file = tk.Menu(self.main_menu, tearoff=False)
        self.edit = tk.Menu(self.main_menu, tearoff=False)
        self.view = tk.Menu(self.main_menu, tearoff=False)
        self.color_theme = tk.Menu(self.main_menu, tearoff=False)

        self.main_menu.add_cascade(label="File", menu=self.file)
        self.main_menu.add_cascade(label="Edit", menu=self.edit)
        self.main_menu.add_cascade(label="View", menu=self.view)
        self.main_menu.add_cascade(label="ColorTheme", menu=self.color_theme)
        self.root.config(menu=self.main_menu)

    def set_file_sub_menu(self):
        self.file.add_command(label='New', image=self.new_icon, compound=tk.LEFT,
                              accelerator='Ctrl+N', command=self.new_file)
        self.file.add_command(label='Open', image=self.open_icon, compound=tk.LEFT,
                              accelerator='Ctrl+O', command=self.open_file)
        self.file.add_command(label='Save', image=self.save_icon, compound=tk.LEFT,
                              accelerator='Ctrl+S', command=self.save_file)
        self.file.add_command(label='Save As', image=self.save_as_icon, compound=tk.LEFT,
                              accelerator='Alt+S', command=self.save_as)
        self.file.add_command(label='Exit', image=self.exit_icon, compound=tk.LEFT,
                              accelerator='Ctrl+Q', command=self.exit_func)

    def set_canvas(self):
        self.text_editor = tk.Text(self.root)
        self.text_editor.config(wrap='word', relief=tk.FLAT)
        self.text_editor.focus_set()
        self.scroll_bar = tk.Scrollbar(self.root)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        self.scroll_bar.config(command=self.text_editor.yview)
        self.text_editor.config(yscrollcommand=self.scroll_bar.set)

        self.text_changed = False
        self.text_editor.bind('<<Modified>>', self.changed)

    def set_status_bar(self):
        self.status_bar = ttk.Label(self.root, text='Status Bar')
        self.status_bar.pack(side=tk.BOTTOM)
        self.count = 0

    def set_file_menu_event_bindings(self):
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-N>", self.new_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-O>", self.open_file)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-S>", self.save_file)
        self.root.bind("<Alt-s>", self.save_as)
        self.root.bind("<Alt-S>", self.save_as)
        self.root.bind("<Control-q>", self.exit_func)
        self.root.bind("<Control-Q>", self.exit_func)

    def exit_func(self):
        pass

    def run(self):
        root.mainloop()

    def save_file(self, event=None):
        try:
            content = self.text_editor.get(1.0, "end-1c")
            if self.url == "":
                self.save_dialog()
                self.notepadController.save_file(content, self.url)
                self.text_changed = False
            else:
                self.notepadController.save_file(content, self.url)
                self.text_changed = False
        except Exception:
            messagebox.showerror("Error!", "Please Select A File to Save")
            print(traceback.format_exc())

    def save_dialog(self):
        self.url = filedialog.asksaveasfile(mode='w', defaultextension='.ntxt',filetypes=([("All Files", "*.*"),("Text Documents", "*.txt")]))

    def open_file(self, event=None):
        try:
            self.open_dialog()
            self.msg, self.base = self.notepadController.read_file(self.url)
            self.text_editor.delete(1.0, tk.END)
            self.text_editor.insert(1.0, self.msg)
            self.root.title(self.base)
            self.text_editor.edit_modified(False)
        except FileNotFoundError:
            messagebox.showerror("Error", "Please Select A File First!")
            print(traceback.format_exc())

    def open_dialog(self):
        self.url = filedialog.askopenfilename(title='Select File',filetypes=[("Text Documents", "*.*")])

    def save_as(self, event=None):
        try:
            content = self.text_editor.get(1.0, "end-1c")
            self.save_dialog()
            self.notepadController.save_as(content, self.url)
            self.text_changed = False
        except Exception:
            messagebox.showerror("Error!", "Please Select File to Save As")
            print(traceback.format_exc())

    def new_file(self, event=None):
        self.url = ""
        self.root.title("MyNotePad")
        self.text_editor.delete(1.0, tk.END)

    def changed(self,event=None):
        words = len(self.text_editor.get(1.0, 'end-1c').split())
        characters = len(self.text_editor.get(1.0,'end-1c'))
        self.status_bar.config(text=f'Characters : {characters} Word : {words}')
        if self.text_editor.edit_modified():
            self.text_changed = True
        self.text_editor.edit_modified(False)

    def exit_func(self):
        result = messagebox.askyesnocancel('Quiting','Do You want to Quit')
        if result == Falsez:
            return
        try:
            if self.url=='':
                if len(self.text_editor.get("1.0",'end-1c')) == 0:
                    self.text_changed = False
            if self.text_changed:
                mbox = messagebox.askyesno('Warning', 'Do you want to save the file ?')
                if mbox == True:
                    content = self.text_editor.get(1.0,"end-1c")
                    if self.url == "":
                        self.save_dialog()
                        self.notepadController.save_file(content,self.url)

                    else:
                        self.notepadController.save_file(content,self.url)
            messagebox.showinfo("Have a Good Day!", "Thank You For Using \"MyNotePad\"")
            self.root.destroy()

        except:
            messagebox.showerror("Error!", "Please Select File to Save")
            print(traceback.format_exc())

    def set_edit_sub_menu(self):
        self.file.add_command(label='Copy', image=self.copy_icon, compound=tk.LEFT,
                              accelerator='Ctrl+C', command=lambda: self.text_editor.event_generate("<<Copy>>"))
        self.file.add_command(label='Paste', image=self.paste_icon, compound=tk.LEFT,
                              accelerator='Ctrl+P', command=lambda: self.text_editor.event_generate("<<Paste>>"))
        self.file.add_command(label='Cut', image=self.cut_icon, compound=tk.LEFT,
                              accelerator='Ctrl+X', command=lambda : self.text_editor.event_generate("<<Cut>>"))
        self.file.add_command(label='Clear All', image=self.clear_all_icon, compound=tk.LEFT,
                              accelerator='Alt+X', command=lambda : self.text_editor.delete(1.0,tk.END))
        self.file.add_command(label='Find', image=self.find_icon, compound=tk.LEFT,
                              accelerator='Ctrl+F', command=self.find_func)
    def find_func(self):
        self.find_dialogue = tk.Toplevel()
        self.find_dialogue.geometry('450x250+500+200')
        self.find_dialogue.title('Find')
        self.find_dialogue.resizable(0,0)

        self.find_frame = ttk.LabelFrame(self.find_dialogue, text='Find/Replace')
        self.find_frame.pack(pady=20)

        self.text_find_label = ttk.Label(self.find_frame, text='Find :')
        self.text_replace_label = ttk.Label(self.find_frame, text='Replace')

        self.find_input = ttk.Entry(self.find_frame, width=30)
        self.replace_input = ttk.Entry(self.find_frame, width=30)

        self.find_button = ttk.Button(self.find_frame, text='Find',command=self.find)
        self.reolace_button = ttk.Button(self.find_frame,text='Replace',command=self.replace)

        self.text_find_label.grid(row=0, column=0, padx=4, pady=4)
        self.text_replace_label.grid(row=1, column=0, padx=4 ,pady=4)

        self.find_input.grid(row=0, column=1, padx=4, pady=4)
        self.replace_input.grid(row=1,column=1,padx=4,pady=4)

        self.find_button.grid(row=2, column=0, padx=8, pady=4)
        self.replace_button.grid(row=2, column=1, padx=8, pady=4)

        self.find_dialogue.mainloop()

    def find(self):
        word = self.find_input.get()
        self.text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = self.text_editor.search(word.start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                print(start_pos,end_pos)
                self.text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos = end_pos
                self.text_editor.tag_config('match',foreground='red',background='yellow')
            if matches:
                messagebox.showinfo("Word Found",f"{word} occurs {matches} times")

    def replace(self):
        word = self.find_input.get()
        self.replace_text = self.replace_input.get()
        self.content = self.text_editor.get(1.0,tk.END)
        self.new_content = self.content.replace(word,self.replace_text)
        self.text_editor.delete((1.0,tk.END))
        self.text_editor.insert(1.0,self.new_content)

    def set_tool_bar(self):
        self.tool_bar = ttk.Label(self.root)
        self.tool_bar.pack(side=tk.TOP, fill=tk.X)
        ## font box
        self.font_tuple = tk.font.families()
        self.font_family = tk.StringVar()
        self.font_box = ttk.Combobox(self.tool_bar, width=30, textvariable=self.font_family, state='readonly')
        self.font_box['values'] = self.font_tuple
        self.font_box.current(self.font_tuple.index('Arial'))
        self.font_box.grid(row=0, column=0, padx=5)

        ## size box
        self.size_var = tk.IntVar()
        self.font_size = ttk.Combobox(self.tool_bar, width=14, textvariable=self.size_var, state='readonly')
        self.font_size['values'] = tuple(range(8, 81))
        self.font_size.current(4)
        self.font_size.grid(row=0, column=1, padx=5)

        ## bold button
        self.bold_icon = tk.PhotoImage(file='icons/bold.png')
        self.bold_btn = ttk.Button(self.tool_bar, image=self.bold_icon)
        self.bold_btn.grid(row=0, column=2, padx=5)

        ## italic button
        self.italic_icon = tk.PhotoImage(file='icons/italic.png')
        self.italic_btn = ttk.Button(self.tool_bar, image=self.italic_icon)
        self.italic_btn.grid(row=0, column=3, padx=5)

        ## underline button
        self.underline_icon = tk.PhotoImage(file='icons/underline.png')
        self.underline_btn = ttk.Button(self.tool_bar, image=self.underline_icon)
        self.underline_btn.grid(row=0, column=4, padx=5)

        ## font color button
        self.font_color_icon = tk.PhotoImage(file='icons/font_color.png')
        self.font_color_btn = ttk.Button(self.tool_bar, image=self.font_color_icon)
        self.font_color_btn.grid(row=0, column=5, padx=5)

        ## align left
        self.align_left_icon = tk.PhotoImage(file='icons/align_left.png')
        self.align_left_btn = ttk.Button(self.tool_bar, image=self.align_left_icon)
        self.align_left_btn.grid(row=0, column=6, padx=5)

        ## align center
        self.align_center_icon = tk.PhotoImage(file='icons/align_center.png')
        self.align_center_btn = ttk.Button(self.tool_bar, image=self.align_center_icon)
        self.align_center_btn.grid(row=0, column=7, padx=5)

        ## align right
        self.align_right_icon = tk.PhotoImage(file='icons/align_right.png')
        self.align_right_btn = ttk.Button(self.tool_bar, image=self.align_right_icon)
        self.align_right_btn.grid(row=0, column=8, padx=5)
        ## mike
        self.mike_icon = tk.PhotoImage(file='microphone.png')
        self.mike_btn = ttk.Button(self.tool_bar, image=self.mike_icon)
        self.mike_btn.grid(row=0, column=9, padx=5)

    def set_tool_bar_event_bindings(self):
        self.current_font_family = 'Arial'
        self.current_font_size = 12
        self.font_box.bind("<<ComboboxSelected>>", self.change_font)
        self.font_size.bind("<<ComboboxSelected>>", self.change_fontsize)
        self.bold_btn.configure(command=self.change_bold)
        self.italic_btn.configure(command=self.change_italic)
        self.underline_btn.configure(command=self.change_underline)
        self.font_color_btn.configure(command=self.change_font_color)
        self.align_right_btn.configure(command=self.align_right)
        self.align_center_btn.configure(command=self.align_center)
        self.align_left_btn.configure(command=self.align_left)
        self.mike_btn.configure(command=self.saySomething)

    def set_tool_bar_event_bindings(self):
        self.current_font_family = 'Arial'
        self.current_font_size = 12
        self.font_box.bind("<<ComboboxSelected>>", self.change_font)
        self.font_size.bind("<<ComboboxSelected>>", self.change_fontsize)
        self.bold_btn.configure(command=self.change_bold)
        self.italic_btn.configure(command=self.change_italic)
        self.underline_btn.configure(command=self.change_underline)
        self.font_color_btn.configure(command=self.change_font_color)
        self.align_right_btn.configure(command=self.align_right)
        self.align_center_btn.configure(command=self.align_center)
        self.align_left_btn.configure(command=self.align_left)
        self.mike_btn.configure(command=self.saySomething)


root = tk.Tk()
obj = Notepad(root)
obj.run()