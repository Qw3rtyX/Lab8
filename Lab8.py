from tkinter import *
from tkinter import ttk
import Pokeapi

def main():

    # Create the main window and icon displayed on the window and Windows taskbar
    root = Tk()
    root.title("Pokemon Info")
    root.resizable(False, False)
    root.iconbitmap('poke-ball.ico')

    # User input
    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=0, columnspan=2, pady=(20,10))

    lbl_name = ttk.Label(frm_input, text='Pokemon Name:')
    lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1)

    #Create the 'Get Info' button
    def handle_btn_get_info():
        poke_name = ent_name.get()
        poke_info = Pokeapi.get_pokemon_info(poke_name)
        if poke_info:
            lbl_height_val['text'] = str(poke_info['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_info['weight']) + ' hg'
            types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
            lbl_type_val['text'] = ', '.join(types_list)
            bar_hp['value'] = poke_info['stats'][0]['base_stat']
            bar_attack['value'] = poke_info['stats'][1]['base_stat']
            bar_defence['value'] = poke_info['stats'][2]['base_stat']
            bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
            bar_special_defence['value'] = poke_info['stats'][4]['base_stat']
            bar_speed['value'] = poke_info['stats'][5]['base_stat']

    btn_get_info = ttk.Button(frm_input, text='Get Info', command=handle_btn_get_info)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10, sticky=W)

    #Info
    lblfrm_info = ttk.LabelFrame(root, text="Info")
    lblfrm_info.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

    lbl_height = ttk.Label(lblfrm_info, text="Height:")
    lbl_height.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=W)
    lbl_height_val = ttk.Label(lblfrm_info, width=20)
    lbl_height_val.grid(row=0, column=1, padx=(0,10), pady=(10,5), sticky=W)

    lbl_weight = ttk.Label(lblfrm_info, text="Weight:")
    lbl_weight.grid(row=1, column=0, padx=(10,5), pady=5, sticky=E)
    lbl_weight_val = ttk.Label(lblfrm_info)
    lbl_weight_val.grid(row=1, column=1, padx=(0,10), pady=5, sticky=W)

    lbl_type = ttk.Label(lblfrm_info, text="Type:")
    lbl_type.grid(row=2, column=0, padx=(10,5),pady=(5,10), sticky=E)
    lbl_type_val = ttk.Label(lblfrm_info)
    lbl_type_val.grid(row=2, column=1, padx=(0,10), pady=(5,10), sticky=W)

    #Stats
    lblfrm_stats = ttk.LabelFrame(root, text="Stats")
    lblfrm_stats.grid(row=1, column=1, padx=(0,10), pady=(10,20), sticky=N)

    lbl_hp = ttk.Label(lblfrm_stats, text="HP:")
    lbl_hp.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
    bar_hp = ttk.Progressbar(lblfrm_stats)
    bar_hp.grid(row=0, column=1, padx=(0,10), pady=(10,5))


    lbl_attack = ttk.Label(lblfrm_stats, text="Attack:")
    lbl_attack.grid(row=1, column=0, padx=(10,5), pady=(5), sticky=E)
    bar_attack = ttk.Progressbar(lblfrm_stats)
    bar_attack.grid(row=1, column=1, padx=(0,10), pady=(5))


    lbl_defence = ttk.Label(lblfrm_stats, text="Defence:")
    lbl_defence.grid(row=2, column=0, padx=(10,5), pady=(5), sticky=E)
    bar_defence = ttk.Progressbar(lblfrm_stats)
    bar_defence.grid(row=2, column=1, padx=(0,10), pady=(5))


    lbl_special_attack = ttk.Label(lblfrm_stats, text="Special Attack:")
    lbl_special_attack.grid(row=3, column=0, padx=(10,5), pady=(5), sticky=E)
    bar_special_attack = ttk.Progressbar(lblfrm_stats)
    bar_special_attack.grid(row=3, column=1, padx=(0,10), pady=(5))


    lbl_special_defence = ttk.Label(lblfrm_stats, text="Special Defence:")
    lbl_special_defence.grid(row=4, column=0, padx=(10,5), pady=(5), sticky=E)
    bar_special_defence = ttk.Progressbar(lblfrm_stats)
    bar_special_defence.grid(row=4, column=1, padx=(0,10), pady=(5))


    lbl_speed = ttk.Label(lblfrm_stats, text="Speed:")
    lbl_speed.grid(row=5, column=0, padx=(10,5), pady=(5), sticky=E)
    bar_speed = ttk.Progressbar(lblfrm_stats)
    bar_speed.grid(row=5, column=1, padx=(0,10), pady=(5))

    root.mainloop()

main()