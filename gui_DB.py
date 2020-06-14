import tkinter as tk
from tkinter import ttk

from mysql.connector import DataError, DatabaseError

from db import my_db


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Employee')
        self.tab_cont = ttk.Notebook(self.root)  # Create Tab Control
        self.tab_cont.pack(expand=2, fill='both')
        self.tab1 = ttk.Frame(self.tab_cont)  # Create a tab
        self.tab_cont.add(self.tab1, text='Input Employee Data')  # Add the tab
        self.tab2 = ttk.Frame(self.tab_cont)  # Create a tab
        self.tab_cont.add(self.tab2, text='Search and Update Employee Data')  # Add the tab
        # create a cursor
        self.curs = my_db.cursor()
        self.curs.execute('use mydb')
        self.myDB = my_db

        # label widgets for input employee window
        f_name = ttk.Label(self.tab1, text="Employee First Name")
        f_name.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        l_name = ttk.Label(self.tab1, text="Employee Last Name")
        l_name.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        address = ttk.Label(self.tab1, text="Address")
        address.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        phone_num = ttk.Label(self.tab1, text="Phone Number")
        phone_num.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        comp_mail = ttk.Label(self.tab1, text="Company Email")
        comp_mail.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        start_date = ttk.Label(self.tab1, text="Start Date")
        start_date.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        sup_f_name = ttk.Label(self.tab1, text="Manager First Name")
        sup_f_name.grid(row=6, column=0, padx=5, pady=5, sticky='w')
        sup_l_name = ttk.Label(self.tab1, text="Manager Last Name")
        sup_l_name.grid(row=7, column=0, padx=5, pady=5, sticky='w')
        dep_name = ttk.Label(self.tab1, text="Department Name")
        dep_name.grid(row=8, column=0, padx=5, pady=5, sticky='w')
        job_t = ttk.Label(self.tab1, text="Job Title")
        job_t.grid(row=9, column=0, padx=5, pady=5, sticky='w')
        salary = ttk.Label(self.tab1, text="Salary")
        salary.grid(row=10, column=0, padx=5, pady=5, sticky='w')

        # entry widgets for input employee window

        self.f_name_box = ttk.Entry(self.tab1)
        self.f_name_box.grid(row=0, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.l_name_box = ttk.Entry(self.tab1)
        self.l_name_box.grid(row=1, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.address_box = ttk.Entry(self.tab1)
        self.address_box.grid(row=2, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.phone_num_box = ttk.Entry(self.tab1)
        self.phone_num_box.grid(row=3, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.comp_mail_box = ttk.Entry(self.tab1)
        self.comp_mail_box.grid(row=4, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.start_date_box = ttk.Entry(self.tab1)
        self.start_date_box.grid(row=5, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.start_date_box.insert(0, 'YYYY-MM-DD')
        self.sup_f_name_box = ttk.Entry(self.tab1)
        self.sup_f_name_box.grid(row=6, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.sup_l_name_box = ttk.Entry(self.tab1)
        self.sup_l_name_box.grid(row=7, column=1, padx=5, pady=5, sticky='w', ipadx=24)

        # combobox for input employee

        self.department_name_c_box = ttk.Combobox(self.tab1,
                                                  values=['Administration', 'Product Development', 'Marketing', 'Sales',
                                                          'Accounting'])
        self.department_name_c_box.grid(row=8, column=1, padx=5, pady=5, ipadx=15)
        self.department_name_c_box.current(0)

        self.job_t_box = ttk.Entry(self.tab1)
        self.job_t_box.grid(row=9, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.salary_box = ttk.Entry(self.tab1)
        self.salary_box.grid(row=10, column=1, padx=5, pady=5, sticky='w', ipadx=24)

        # button widgets for input employee window

        self.clear_button = ttk.Button(self.tab1, text="Clear Data", command=self.clear_entry)
        self.clear_button.grid(row=12, padx=5, pady=5, columnspan=2, ipadx=114)
        self.add_employee_button = ttk.Button(self.tab1, text="Add Employee to DataBase", command=self.add_employee)
        self.add_employee_button.grid(row=13, padx=5, pady=5, columnspan=2, ipadx=76)

        # create label for exception date error
        self.ex_er_1 = ttk.Label(self.tab1)
        self.ex_er_1.grid(row=14, columnspan=2)
        self.ex_er_2 = ttk.Label(self.tab1)
        self.ex_er_2.grid(row=15, columnspan=2)
        self.ex_er_3 = ttk.Label(self.tab2)
        self.ex_er_3.grid(row=20, columnspan=3)
        self.ex_er_4 = ttk.Label(self.tab2)
        self.ex_er_4.grid(row=21, columnspan=3)

        # search button widgets for update employee window

        self.search_employee_button = ttk.Button(self.tab2, text="Search Employee", command=self.search_result)
        self.search_employee_button.grid(row=2, column=3, padx=5, pady=5, sticky='w', ipadx=21)
        self.clear_update_button = ttk.Button(self.tab2, text="Clear Result", command=self.clear_update)
        self.clear_update_button.grid(row=3, column=3, padx=5, pady=5, sticky='w', ipadx=33)

        # create label widget for update employee window

        search_label = ttk.Label(self.tab2, text="Search by:")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        parameter_label = ttk.Label(self.tab2, text="and")
        parameter_label.grid(row=0, column=2, padx=5, pady=5, rowspan=2)
        enter_label = ttk.Label(self.tab2, text="input:")
        enter_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        # create entry box for update employee window

        self.parameter_1_box = ttk.Entry(self.tab2)
        self.parameter_1_box.grid(row=1, column=1, padx=5, pady=5, sticky='w', ipadx=8)
        self.parameter_2_box = ttk.Entry(self.tab2)
        self.parameter_2_box.grid(row=1, column=3, padx=5, pady=5, sticky='w', ipadx=8)

        # create combobox widget for update employee window

        self.parameter_1_c_box = ttk.Combobox(self.tab2,
                                              values=['First Name', 'Last Name', 'Employee_ID'])
        self.parameter_1_c_box.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.parameter_1_c_box.current(0)
        self.parameter_2_c_box = ttk.Combobox(self.tab2,
                                              values=['Company Email', 'Address', 'Phone Number', 'Department Name'])
        self.parameter_2_c_box.grid(row=0, column=3, padx=5, pady=5)
        self.parameter_2_c_box.current(0)

        # create update field

        self.id_box_u = ttk.Entry(self.tab2)
        self.id_box_u.grid(row=2, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.f_name_box_u = ttk.Entry(self.tab2)
        self.f_name_box_u.grid(row=3, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.l_name_box_u = ttk.Entry(self.tab2)
        self.l_name_box_u.grid(row=4, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.address_box_u = ttk.Entry(self.tab2)
        self.address_box_u.grid(row=5, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.phone_num_box_u = ttk.Entry(self.tab2)
        self.phone_num_box_u.grid(row=6, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.comp_mail_box_u = ttk.Entry(self.tab2)
        self.comp_mail_box_u.grid(row=7, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.start_date_box_u = ttk.Entry(self.tab2)
        self.start_date_box_u.grid(row=8, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.end_date_box_u = ttk.Entry(self.tab2)
        self.end_date_box_u.grid(row=9, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.sup_f_name_box_u = ttk.Entry(self.tab2)
        self.sup_f_name_box_u.grid(row=10, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.sup_l_name_box_u = ttk.Entry(self.tab2)
        self.sup_l_name_box_u.grid(row=11, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.department_name_u = ttk.Entry(self.tab2)
        self.department_name_u.grid(row=12, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.job_t_box_u = ttk.Entry(self.tab2)
        self.job_t_box_u.grid(row=13, column=1, padx=5, pady=5, sticky='w', ipadx=24)
        self.salary_box_u = ttk.Entry(self.tab2)
        self.salary_box_u.grid(row=14, column=1, padx=5, pady=5, sticky='w', ipadx=24)

        # create update fields labels
        id_u = ttk.Label(self.tab2, text="Employee_ID")
        id_u.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        f_name_u = ttk.Label(self.tab2, text="Employee First Name")
        f_name_u.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        l_name_u = ttk.Label(self.tab2, text="Employee Last Name")
        l_name_u.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        address_u = ttk.Label(self.tab2, text="Address")
        address_u.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        phone_num_u = ttk.Label(self.tab2, text="Phone Number")
        phone_num_u.grid(row=6, column=0, padx=5, pady=5, sticky='w')
        comp_mail_u = ttk.Label(self.tab2, text="Company Email")
        comp_mail_u.grid(row=7, column=0, padx=5, pady=5, sticky='w')
        start_date_u = ttk.Label(self.tab2, text="Start Date")
        start_date_u.grid(row=8, column=0, padx=5, pady=5, sticky='w')
        end_date_u = ttk.Label(self.tab2, text="End Date")
        end_date_u.grid(row=9, column=0, padx=5, pady=5, sticky='w')
        sup_f_name = ttk.Label(self.tab2, text="Manager First Name")
        sup_f_name.grid(row=10, column=0, padx=5, pady=5, sticky='w')
        sup_l_name = ttk.Label(self.tab2, text="Manager Last Name")
        sup_l_name.grid(row=11, column=0, padx=5, pady=5, sticky='w')
        dep_name = ttk.Label(self.tab2, text="Department Name")
        dep_name.grid(row=12, column=0, padx=5, pady=5, sticky='w')
        job_t = ttk.Label(self.tab2, text="Job Title")
        job_t.grid(row=13, column=0, padx=5, pady=5, sticky='w')
        salary = ttk.Label(self.tab2, text="Salary")
        salary.grid(row=14, column=0, padx=5, pady=5, sticky='w')

        # record not found label
        self.rec_not_found = ttk.Label(self.tab2)
        self.rec_not_found.grid(row=20, padx=5, pady=5, columnspan=3)

        # commit update button
        commit_button = ttk.Button(self.tab2, text='Update Employee Record', command=self.update_result)
        commit_button.grid(row=18, column=0, padx=5, pady=5, sticky='w')

        # create delete button

        delete_button = ttk.Button(self.tab2, text='Delete Employee', command=self.clear_employee)
        delete_button.grid(row=19, column=0, sticky='w', padx=5, pady=5)

    def clear_entry(self):
        self.f_name_box.delete(0, tk.END)
        self.l_name_box.delete(0, tk.END)
        self.address_box.delete(0, tk.END)
        self.phone_num_box.delete(0, tk.END)
        self.comp_mail_box.delete(0, tk.END)
        self.start_date_box.delete(0, tk.END)
        self.sup_f_name_box.delete(0, tk.END)
        self.sup_l_name_box.delete(0, tk.END)
        self.department_name_c_box.delete(0, tk.END)
        self.job_t_box.delete(0, tk.END)
        self.salary_box.delete(0, tk.END)
        self.ex_er_1.destroy()
        self.ex_er_2.destroy()

    def search_result(self):
        sql_search = 'select e.emp_id, e.first_name, e.last_name, e.address, e.phone_number, e.company_email, ' \
                     'e.start_date, e.end_date, mgr.first_name, mgr.last_name, d.dep_name, e.job_title, e.salary from ' \
                     'employee e inner join department d on e.dept_id = d.dept_id left outer join employee mgr on ' \
                     'mgr.emp_id = e.superior_emp_id where (e.first_name = %s or e.last_name = %s or e.emp_id = %s ' \
                     ') and (e.company_email = %s or e.address = %s or e.phone_number = %s or d.dep_name = %s) '

        values_search = (self.parameter_1_box.get(),
                         self.parameter_1_box.get(),
                         self.parameter_1_box.get(),
                         self.parameter_2_box.get(),
                         self.parameter_2_box.get(),
                         self.parameter_2_box.get(),
                         self.parameter_2_box.get()
                         )

        self.curs.execute(sql_search, values_search)

        search_res = self.curs.fetchall()
        print(search_res)

        if not search_res:
            res = "Employee Not Exist"
            self.rec_not_found = ttk.Label(self.tab2, text=res)
            self.rec_not_found.grid(row=20, column=0, padx=5, pady=5, columnspan=3)

        else:
            self.id_box_u.insert(0, search_res[0][0])
            self.f_name_box_u.insert(0, search_res[0][1])
            self.l_name_box_u.insert(0, search_res[0][2])
            self.address_box_u.insert(0, search_res[0][3])
            self.phone_num_box_u.insert(0, search_res[0][4])
            self.comp_mail_box_u.insert(0, search_res[0][5])
            self.start_date_box_u.insert(0, search_res[0][6])
            if search_res[0][7] is None:
                self.end_date_box_u.insert(0, 'YYYY-MM-DD')
            else:
                self.end_date_box_u.insert(0, search_res[0][7])
            if search_res[0][8] is None:
                self.sup_f_name_box_u.insert(0, '-')
            else:
                self.sup_f_name_box_u.insert(0, search_res[0][8])
            if search_res[0][9] is None:
                self.sup_l_name_box_u.insert(0, '-')
            else:
                self.sup_l_name_box_u.insert(0, search_res[0][9])
            self.department_name_u.insert(0, search_res[0][10])
            self.job_t_box_u.insert(0, search_res[0][11])
            self.salary_box_u.insert(0, search_res[0][12])

            self.rec_not_found.destroy()

    def clear_update(self):
        self.id_box_u.delete(0, tk.END)
        self.f_name_box_u.delete(0, tk.END)
        self.l_name_box_u.delete(0, tk.END)
        self.address_box_u.delete(0, tk.END)
        self.phone_num_box_u.delete(0, tk.END)
        self.comp_mail_box_u.delete(0, tk.END)
        self.start_date_box_u.delete(0, tk.END)
        self.end_date_box_u.delete(0, tk.END)
        self.sup_f_name_box_u.delete(0, tk.END)
        self.sup_l_name_box_u.delete(0, tk.END)
        self.department_name_u.delete(0, tk.END)
        self.job_t_box_u.delete(0, tk.END)
        self.salary_box_u.delete(0, tk.END)
        self.ex_er_3.destroy()
        self.ex_er_4.destroy()
        self.rec_not_found.destroy()

    def update_result(self):
        sql_tm_res = 'create temporary table if not exists emp_tmp_up as select emp_id, first_name, last_name from employee'
        sql_up_res = 'update employee set first_name = %s, last_name = %s, address = %s, phone_number = %s, ' \
                     'company_email = %s, start_date = %s, end_date = %s, superior_emp_id = (select emp_id from ' \
                     'emp_tmp_up where first_name = %s and last_name = %s), dept_id = (select dept_id from department ' \
                     'where dep_name = %s), job_title = %s, salary = %s ' \
                     'where emp_id = %s'
        sql_drop = 'drop table emp_tmp_up'

        if self.end_date_box_u.get() == 'YYYY-MM-DD':
            value_update_res = (self.f_name_box_u.get(),
                                self.l_name_box_u.get(),
                                self.address_box_u.get(),
                                self.phone_num_box_u.get(),
                                self.comp_mail_box_u.get(),
                                self.start_date_box_u.get(),
                                None,
                                self.sup_f_name_box_u.get(),
                                self.sup_l_name_box_u.get(),
                                self.department_name_u.get(),
                                self.job_t_box_u.get(),
                                self.salary_box_u.get(),
                                self.id_box_u.get()
                                )
        else:
            value_update_res = (self.f_name_box_u.get(),
                                self.l_name_box_u.get(),
                                self.address_box_u.get(),
                                self.phone_num_box_u.get(),
                                self.comp_mail_box_u.get(),
                                self.start_date_box_u.get(),
                                self.end_date_box_u.get(),
                                self.sup_f_name_box_u.get(),
                                self.sup_l_name_box_u.get(),
                                self.department_name_u.get(),
                                self.job_t_box_u.get(),
                                self.salary_box_u.get(),
                                self.id_box_u.get()
                                )
        try:
            self.curs.execute(sql_tm_res)
            self.curs.execute(sql_up_res, value_update_res)
            self.curs.execute(sql_drop)
        except DataError:
            self.ex_er_3 = ttk.Label(self.tab2, text='Wrong Data Type, use YYYY-MM-DD')
            self.ex_er_3.grid(row=20, columnspan=2)
        except DatabaseError:
            self.ex_er_4 = ttk.Label(self.tab2, text='Wrong Data Type, use Decimal')
            self.ex_er_4.grid(row=21, columnspan=2)
        else:
            self.myDB.commit()
            self.clear_update()
            self.ex_er_3.destroy()
            self.ex_er_4.destroy()

    def clear_employee(self):
        sql_del = 'delete from employee where emp_id = %s and phone_number = %s'
        del_value = (self.id_box_u.get(),
                     self.phone_num_box_u.get())
        self.curs.execute(sql_del, del_value)
        self.myDB.commit()
        self.clear_update()

    def add_employee(self):
        sql_tm = "create temporary table if not exists emp_tmp as select emp_id, first_name, last_name from employee"
        sql_up = "update employee set superior_emp_id = (select emp_id from emp_tmp where first_name = %s and " \
                 "last_name = %s) where (first_name = %s and last_name = %s and phone_number = %s) "

        sql_drop_2 = 'drop table emp_tmp'
        value_update = (self.sup_f_name_box.get(),
                        self.sup_l_name_box.get(),
                        self.f_name_box.get(),
                        self.l_name_box.get(),
                        self.phone_num_box.get()
                        )

        sql_ins = "insert into employee (emp_id, first_name, last_name, address, phone_number, company_email, " \
                  "start_date, superior_emp_id, dept_id, job_title, salary) values (null, %s, %s, %s, %s, " \
                  "%s, %s, null, (select dept_id from department where dep_name = %s), %s, %s) "
        value = (self.f_name_box.get(),
                 self.l_name_box.get(),
                 self.address_box.get(),
                 self.phone_num_box.get(),
                 self.comp_mail_box.get(),
                 self.start_date_box.get(),
                 self.department_name_c_box.get(),
                 self.job_t_box.get(),
                 self.salary_box.get()
                 )

        self.curs.execute(sql_tm)
        try:
            self.curs.execute(sql_ins, value)
            self.curs.execute(sql_up, value_update)
            self.curs.execute(sql_drop_2)
        except DataError:
            self.ex_er_1 = ttk.Label(self.tab1, text='Wrong Data Type use YYYY-MM-DD')
            self.ex_er_1.grid(row=14, columnspan=2)
        except DatabaseError:
            self.ex_er_2 = ttk.Label(self.tab1, text='Wrong Data Type use Decimal')
            self.ex_er_2.grid(row=15, columnspan=2)
        else:
            self.myDB.commit()
            self.clear_entry()
            self.ex_er_1.destroy()
            self.ex_er_2.destroy()


my_gui = MainWindow()

my_gui.root.mainloop()
