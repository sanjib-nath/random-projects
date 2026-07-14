import datetime
import json
from tkinter import *
from settings import Settings

class Todolist():
    """A overall class to maintain the main programe"""

    def __init__(self):

        #window
        self.window = Tk()
        self.window.title("To Do List")

        #class
        self.settings = Settings()

        a = self.settings.window_width
        b = self.settings.window_height

        self.window.config(background= self.settings.light_green)
        self.window.geometry(f"{a}x{b}")
        self.window.resizable(False, False)

        #label
        self.main_lable = Label(self.window, text = "TO DO LIST",
                                font = ("bahnschrift condensed", 20),
                                image = self.settings.main_icon,
                                compound = 'right',
                                background = self.settings.light_green)
        
        #x and y postion
        x_pos = (self.settings.window_width - int(self.main_lable.winfo_reqwidth()) )/ 2
        self.main_lable.place(x= x_pos, y = 50)

        #frame
        width = self.settings.window_width - 50
        height = self.settings.window_height - 3* int(self.main_lable.winfo_reqheight()) - 25

        self.main_frame = Frame(self.window, width = width, height = height,
                                background = self.settings.light_green1)
        self.main_frame.pack_propagate(False)

        #x and y postion
        x_pos = (self.settings.window_width - int(self.main_frame.winfo_reqwidth())) / 2
        y_pos = 3 * int(self.main_lable.winfo_reqheight())
        self.main_frame.place(x = x_pos, y = y_pos)

        #list of task saved
        self.task_list = []

        #window protocol
        self.window.protocol("WM_DELETE_WINDOW", self._save_tasks)

        #method
        self._show_dt()
        self._user_input()
        self._new_task()
        self.saved_show()

 
    def _show_dt(self):
        """Show date and time"""

        #date
        date = datetime.date.today()
        date = date.strftime("%d-%b-%y")

        date_lb = Label(self.window, text= f"Date: {date}",
                        font= ("segoe ui black", 10),
                        background = self.settings.light_green)
        date_lb.place(x = 2, y = 2)

        #time
        time = datetime.datetime.now()
        time = time.strftime("%I:%M %p")

        time_lb = Label(self.window, text = f"Time: {time}",
                        font = ("segoe ui black", 10),
                        background= self.settings.light_green)
        
        #finding the x postion
        x_pos = (self.settings.window_width - int(time_lb.winfo_reqwidth())) - 2
        time_lb.place(x = x_pos, y = 2)
        self.window.after(1000, self._show_dt)


    def saved_show(self):
        """Show the task if there are saved task"""

        try:
            with open("saved_task.json", "r") as f:
                list = json.load(f)


                if list == []:
                    pass

                else:
                    for dic in list:
                        task = dic['task']

                        tasks_frame = Frame(self.main_frame, background= self.settings.white)
                        tasks_frame.pack(padx = 10, pady = 7)

                        tasks = Label(tasks_frame, text = task , width = 35,
                                    font = ("bahnschrift condensed", 20),
                                    background = self.settings.white)
                        tasks.pack(side= "left")

                        #delete button
                        del_button = Button(tasks_frame, image = self.settings.bin,
                                            relief= "flat", background = self.settings.white,
                                            activebackground = self.settings.white)
                        del_button.pack(side="right")

                        #done button
                        done_button = Button(tasks_frame, image = self.settings.done,
                                            relief= "flat", background = self.settings.white,
                                            activebackground = self.settings.white)
                        done_button.place(x= 1.5, y = 3)

                        #create a dic of each task
                        task_crate = {'task' : task,
                                    'done' : dic['done']}

                        self.task_list.append(task_crate)

                        #button command
                        del_button.config(command= lambda f= tasks_frame,
                                        s = task_crate
                                        : self._del_task(f,s))
                        
                        done_button.config(command= lambda f = tasks_frame,
                                            t = tasks,
                                            d = del_button,
                                            b = done_button,
                                            s = task_crate 
                                            : self._done_task(f,t,d, b, s))
                        
                        if dic['done'] == True:

                            tasks_frame.config(background = self.settings.green)
                            tasks.config(background = self.settings.green)
                            del_button.config(background = self.settings.green)
                            done_button.config(background = self.settings.green)

                        else:
                            pass

        except Exception as e:
            print(e)

    def _user_input(self):
        """input the user's data"""

        input_frame = Frame(self.main_frame, background= self.settings.white)
        input_frame.pack(padx= 10, pady= 10)
        
        #button
        add_button = Button(input_frame, text = "Add", font = ("bahnschrift condensed", 15),
                            width = 6, height= 1, background = self.settings.green,
                            relief = "flat",
                            activebackground = self.settings.green, 
                            fg = self.settings.dark_gray,
                            activeforeground = self.settings.dark_gray,
                            command= self._new_task)
        add_button.pack(side = "right")

        #new task
        self.new_task = Entry(input_frame, width = 48,
                         font = ("bahnschrift condensed", 15),
                         relief = "flat")
        self.new_task.pack(side = "left",)

    
    def _new_task(self):
        """Add a new task"""

        task = self.new_task.get()

        if task == "":
            pass

        else:
            tasks_frame = Frame(self.main_frame, background= self.settings.white)
            tasks_frame.pack(padx = 10, pady = 7)

            tasks = Label(tasks_frame, text = task , width = 35,
                          font = ("bahnschrift condensed", 20),
                        background = self.settings.white)
            tasks.pack(side= "left")

            #delete button
            del_button = Button(tasks_frame, image = self.settings.bin,
                                relief= "flat", background = self.settings.white,
                                activebackground = self.settings.white)
            del_button.pack(side="right")

            #done button
            done_button = Button(tasks_frame, image = self.settings.done,
                                relief= "flat", background = self.settings.white,
                                activebackground = self.settings.white)
            done_button.place(x= 1.5, y = 3)

            #create a dic of each task
            task_crate = {'task' : task,
                          'done' : False}

            self.task_list.append(task_crate)

            #button command
            del_button.config(command= lambda f= tasks_frame,
                              s = task_crate
                              : self._del_task(f,s))
            
            done_button.config(command= lambda f = tasks_frame,
                                t = tasks,
                                d = del_button,
                                b = done_button,
                                s = task_crate 
                                : self._done_task(f,t,d, b, s))

            self.new_task.delete(0, END)

    def _save_tasks(self):
        with open("saved_task.json", "w") as f:

            json.dump(self.task_list, f)
            self.window.destroy()

        
    def _del_task(self, frame, save):
        """destroy a task"""
        frame.destroy()
        self.task_list.remove(save)

    def _done_task(self, frame, label, button0, button1, save):
        """Mark a task as complete"""

        frame.config(background = self.settings.green)
        label.config(background = self.settings.green)
        button0.config(background = self.settings.green,
                       activebackground = self.settings.green)
        button1.config(background = self.settings.green,
                       activebackground = self.settings.green)

        save['done'] = True

    def _stop_programe(self):
        """unable to change the list when day over """
        """And let the user create a new list"""
        pass

    def run_programe(self):
        """Run the programe"""
        
        self.window.mainloop()

if __name__ == '__main__':
    to_do_list = Todolist()
    to_do_list.run_programe()