from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pylab import plot, show, xlabel, ylabel
from tkinter import messagebox
from tkinter import *
from bankaccount import BankAccount
import tkinter as my_tk
from matplotlib.figure import Figure

my_win = my_tk.Tk();
my_win.geometry("440x640") # window size '440x640' pixels
my_win.title('FedUni Banking')# window title 'FedUni Banking'

# account-number-entry & associated-variable
account_number_var = my_tk.StringVar();account_number_entry = my_tk.Entry(my_win, textvariable=account_number_var,width=8)
account_number_entry.focus_set()

#pin-number-entry & associated-variable.
pin_number_var = my_tk.StringVar()
account_pin_entry = my_tk.Entry(my_win, text='PIN Number', textvariable=pin_number_var,width=8,show="*")

#balance-label & associated-variable
balance_var = my_tk.StringVar();balance_var.set('Balance: $0.000');balance_label = my_tk.Label(my_win, textvariable=balance_var)

#Entry widget to accept a numerical value to deposit or withdraw
amount_entry = my_tk.Entry(my_win)

#transaction text-widget holds text of the accounts transactions
transaction_text_widget = my_tk.Text(my_win, height=10, width=48)

# The bank account object we will work with
account = BankAccount()
# ---------- Button Handlers for Login Screen ----------

# '''Function to clear the PIN number entry when the Clear / Cancel button is clicked.'''
def clear_pin_entry():
	global account_pin_entry
	account_pin_entry.delete(0,END);
	account_number_entry.delete(0,END)

def button_handler(id):
	global account_pin_entry,account_number_entry
	global pin_number_var;global account_number_var;
	if account_number_entry == account_number_entry.focus_get():
		cur_value = account_number_entry.get()
		account_number_var.set(cur_value+str(id))
	elif account_pin_entry==account_pin_entry.focus_get():
		cur_value = account_pin_entry.get()		
		pin_number_var.set(cur_value+str(id))

def log_in():
    '''Function to log in to the banking system using a known account number and PIN.'''
    global account,pin_number_var;
    global account_number_var,account_number_entry,account_pin_entry;
    acc_no = (account_number_entry.get());acc_pin = (account_pin_entry.get());
    # Create the filename from the entered account number with '.txt' on the end
    filename = str(acc_no) + ".txt";
    try:
    	f = open(filename);
    	original_acc_no = f.readline().strip();original_acc_pin = f.readline().strip();
    	balance = float(f.readline().strip());interest_rate = float(f.readline().strip());
    	if(original_acc_no == acc_no and original_acc_pin == acc_pin):
    		account.account_number = acc_no;account.pin_number = acc_pin;
    		account.balance = balance;account.interest_rate = interest_rate
    		while(True):    			
    			l1 = f.readline().strip()
    			if(l1 == ''):
    				break
    			else:
	    			l2 = f.readline().strip()
	    			if(l1 == "Deposit"):
	    				account.transaction_list.append(float(l2))
    				else:
	    				account.transaction_list.append(-(float(l2)))    					
    		create_account_screen()
    	else:
    		account_number_entry.delete(0,END);account_pin_entry.delete(0,END);
    		account_number_entry.focus_set();
    		messagebox.showinfo('Wrong Credentials!', 'Please enter valid UserID and Password');	
    except:
    		account_number_entry.delete(0,7);
    		account_pin_entry.delete(0,END);
    		account_number_entry.focus_set()
    		messagebox.showinfo('Wrong Credentials!', 'Wrong Account Number!')


def save_and_log_out():
	global account,account_number_entry;global account_pin_entry
	account_number_entry.delete(0,END);clear_pin_entry()	
	account.save_to_file();create_login_screen()	

def perform_deposit():
    '''Function to add a deposit for the amount in the amount entry to the
       account's transaction list.'''
    global account,amount_entry
    global balance_label,balance_var
    if(account.deposit_funds(amount_entry.get())):
    	dep_amt = float(amount_entry.get());
    	account.balance = account.balance + dep_amt;
    	account.transaction_list.append(dep_amt);
    	amount_entry.delete(0,END);create_account_screen();
    else:
    	amount_entry.delete(0,END)
    	messagebox.showinfo('Transaction Error','Enter a valid Input ammount!');
        
def perform_withdrawal():
    '''Function to withdraw the amount in the amount entry from the account balance and add an entry to the transaction list.'''
    global account,amount_entry
    global balance_label,balance_var
    if(account.withdraw_funds(amount_entry.get())):
    	w_amt = float(amount_entry.get());account.balance = account.balance - w_amt;
    	account.transaction_list.append(-w_amt);amount_entry.delete(0,END);
    	create_account_screen();
    else:
    	amount_entry.delete(0,END)
    	messagebox.showinfo('Transaction Error','Enter a valid Input ammount');        

# ---------- Utility functions ----------

def remove_all_widgets():
    '''Function to remove all the widgets from the window.'''
    global my_win
    for widget in my_win.winfo_children():
        widget.grid_remove()

def plot_interest_graph():
	global account
	i_rate = account.interest_rate
	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	tmp_balance = account.balance
	y = [tmp_balance]
	mlt = 1+ (i_rate/12);m = 1;
	while(m<12):
		tmp_balance = tmp_balance*mlt;
		y.append(tmp_balance);m = m + 1;
	figure = Figure(figsize=(3,2), dpi=100);figure.suptitle('Cumulative Interest 12 Months')
	a = figure.add_subplot(111);a.plot(x, y, marker='o');a.grid()
	canvas = FigureCanvasTkAgg(figure, master=my_win);canvas.draw();graph_widget = canvas.get_tk_widget()
	graph_widget.grid(row=5, column=0, columnspan=5, sticky='nsew')


# ---------- UI Screen Drawing Functions ----------
def create_login_screen():
	global my_win,account_number_entry
	global account_pin_entry
	remove_all_widgets()
	lbl = Label(my_win,text="FedUni Banking",font=("Arial Bold", 32));
	lbl.grid(column=1,row=0);

	tmp_lbl = Label(my_win,text="Acc_no/Pin");
	tmp_lbl.grid(column=0,row=1);account_number_entry.grid(column=1,row = 1);
	account_pin_entry.grid(column=2,row=1)

	btn1 = Button(my_win, text="1",height=4,width=4,command= lambda: button_handler(1));btn1.grid(column=0, row=2)	
	btn2 = Button(my_win, text="2",height=4,width=4,command= lambda: button_handler(2));btn2.grid(column=1, row=2)	
	btn3 = Button(my_win, text="3",height=4,width=4,command= lambda: button_handler(3));btn3.grid(column=2, row=2)	

	btn4 = Button(my_win, text="4",height=4,width=4,command= lambda: button_handler(4));btn4.grid(column=0, row=3)	
	btn5 = Button(my_win, text="5",height=4,width=4,command= lambda: button_handler(5));btn5.grid(column=1, row=3)	
	btn6 = Button(my_win, text="6",height=4,width=4,command= lambda: button_handler(6));btn6.grid(column=2, row=3)	

	btn7 = Button(my_win, text="7",height=4,width=4,command= lambda: button_handler(7));btn7.grid(column=0, row=4)	
	btn8 = Button(my_win, text="8",height=4,width=4,command= lambda: button_handler(8));btn8.grid(column=1, row=4)	
	btn9 = Button(my_win, text="9",height=4,width=4,command= lambda: button_handler(9));btn9.grid(column=2, row=4)	

	btn_clear = Button(my_win, text="Clear",height=4,width=4,bg='red',command=clear_pin_entry);btn_clear.grid(column=0, row=5)	
	btn0 = Button(my_win, text="0",height=4,width=4,command= lambda: button_handler(0));btn0.grid(column=1, row=5)	
	btn_login = Button(my_win, text="Login",height=4,width=4,bg='green',command=log_in);btn_login.grid(column=2, row=5)	

def create_account_screen():
    '''Function to create the account screen.'''
    global amount_text,amount_label,transaction_text_widget
    global balance_var,my_win,account
    remove_all_widgets()    
    # ----- Row 0 -----
    lbl = Label(my_win,text="FedUni Banking",font=("Arial Bold", 24));
    lbl.grid(column=1,row=0);
    tmp_lbl = Label(my_win,text="Account number: " + str(account_number_entry.get()));
    tmp_lbl.grid(column=0,row=1);
    tmp_lbl2 = Label(my_win,text="Balance:$" + str(account.balance));
    tmp_lbl2.grid(column=1,row=1);
    btn_logout = Button(my_win, text="Logout",height=1,width=6,command=save_and_log_out);btn_logout.grid(column=2, row=1);

    tmp_lbl = Label(my_win,text="Amount($) " );
    tmp_lbl.grid(column=0,row=2);
    amount_entry.grid(column=1,row = 2);
    btn_dep = Button(my_win, text="Deposit",height=1,width=7,command=perform_deposit);btn_dep.grid(column=1, row=3)
    btn_wid = Button(my_win, text="Withdraw",height=1,width=7,command=perform_withdrawal);btn_wid.grid(column=2, row=3)
    T = Text(my_win,height = 10,width =30);
    T.insert(INSERT, account.get_transaction_string())
    T.grid(row=4, column=1);
    plot_interest_graph()
create_login_screen()
my_win.mainloop()
