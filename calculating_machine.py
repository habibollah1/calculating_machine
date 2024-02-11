import tkinter as tk

window= tk.Tk()

lbl_input = tk.Label(
    window,
    text='0',
    width=30,
    height=3,
)

lbl_input.grid(row=0 , column=0 , columnspan=4)

last_op_index = -1
last_dot_index = -1    

def insert_number_in_calc_result(btn_text):
    
    global last_op_index , last_dot_index
    
    current = lbl_input['text']
    
        
    if btn_text in ['+', '-', '*']:
        last_op_index = len(current)
        
    # elif btn_text == '.':
    #     last_dot_index = len(current)
        
    if current == '0':
        lbl_input['text'] = btn_text
        
    elif btn_text == 'C':
        lbl_input['text'] = '0'
        last_dot_index , last_op_index = 0,0
        
    elif btn_text == '=':
        result = eval(str(current))
        lbl_input['text'] = result
        last_op_index = 0
        
        if '.' in result:
            last_dot_index = result.index('.')
        else:
            last_dot_index = 0
            
    elif btn_text in ['+', '-', '*'] and current[-1] in ['+', '-', '*']:
        lbl_input['text'] = current[:-1] + btn_text
    
    else:
        if btn_text == '.':
            if last_dot_index > last_op_index:
                pass
                print(1)
            elif current[-1] == '.':
                print(2)
                pass
            else:
                print(3)
                lbl_input['text'] += btn_text
                last_dot_index = len(current)
                # اینجا میاد دات را اپدیت میکنه
        # lbl_input['text'] +=  btn_text

        
        
        else:
            lbl_input['text'] += btn_text
        


buttons = (
    {
        'text':'1',
        'command': lambda: insert_number_in_calc_result('1'),
    },
    {
        'text':'2',
        'command': lambda: insert_number_in_calc_result('2'),
    },
    {
        'text':'3',
        'command': lambda: insert_number_in_calc_result('3'),
    },
    {
        'text':'+',
        'command': lambda: insert_number_in_calc_result('+'),
    },
    {
        'text':'4',
        'command': lambda: insert_number_in_calc_result('4'),
    },
    {
        'text':'5',
        'command': lambda: insert_number_in_calc_result('5'),
    },
    {
        'text':'6',
        'command': lambda: insert_number_in_calc_result('6'),
    },
    {
        'text':'-',
        'command': lambda: insert_number_in_calc_result('-'),
    },
    {
        'text':'7',
        'command': lambda: insert_number_in_calc_result('7'),
    },
    {
        'text':'8',
        'command': lambda: insert_number_in_calc_result('8'),
    },
    {
        'text':'9',
        'command': lambda: insert_number_in_calc_result('9'),
    },
    {
        'text':'*',
        'command': lambda: insert_number_in_calc_result('*'),
    },
    {
        'text':'.',
        'command': lambda: insert_number_in_calc_result('.'),
    },
    {
        'text':'0',
        'command': lambda: insert_number_in_calc_result('0'),
    },
    {
        'text':'C',
        'command': lambda: insert_number_in_calc_result('C'),
    },
    {
        'text':'=',
        'command': lambda: insert_number_in_calc_result('='),
    },
    
    
)

calc_key_objects  = []

for calc_key_data in buttons:
    btn = tk.Button(
        window,
        height=3,
        text=calc_key_data['text'],
        command=calc_key_data['command'],
    )
    calc_key_objects.append(btn)

for i , calc_key_obj in enumerate(calc_key_objects):
    calc_key_obj.grid(row=(i // 4)+1 , column =( i % 4), sticky = 'news' )
    
    

window.mainloop()