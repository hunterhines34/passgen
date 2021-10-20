###################################
# DRH Health - Password generator #
#   Created by Hunter Hines - IT  #
###################################

# Imports
import random, array, webbrowser
import PySimpleGUI as sg

# PySimpleGUI theme
#sg.theme('DarkGrey12')

# Create password pattern
def create_password(pass_length):
    MAX_LEN = pass_length

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOWCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

    # Combine all character arrays into a single array
    combined_list = DIGITS + UPCASE_CHARACTERS + LOWCASE_CHARACTERS + SYMBOLS
    
    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOWCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # Generate a temporary set of character strings
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # Randomly combine and shuffle the temp pass
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(combined_list)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # Instantiate an empty password variable
    password = ''

    # Generate the new password pattern by looping through each random character in temp_pass
    for x in temp_pass_list:
        password = password + x    

    # Retrun instance of password
    return password

# Main entry point 
def main():
    # Frame layout
    frame_layout = [
        [sg.Text('Choose the amount of characters to generate (16 is the default recommended size):')],
        [sg.Slider(range=(10,200), default_value=16, size=(55,10), orientation='horizontal', key='-SLIDER-')]
    ]

    # Layout
    layout = [
        [sg.Text('This tool can generate secure passwords starting from 10 to 200 characters in length.')],
        [sg.Frame('Password options', frame_layout)],
        [sg.Button('Generate password', size=(30,1), key='-GENERATE-'), sg.Button('Copy password', size=(30,1), key='-COPY-')],
        [sg.Multiline(size=(72,3), autoscroll=True, no_scrollbar=True, key='-PASSWORD-')],
        [sg.Text('Check the password strength at:'), sg.Text('https://www.security.org/how-secure-is-my-password', enable_events=True, text_color='blue', key='-LINK-')]
    ]

    # Create window pattern
    window = sg.Window('DRH Health - Password Generator', layout)

    # Loop through event handlers
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == '-LINK-':
            webbrowser.open(r'https://www.security.org/how-secure-is-my-password')
        if event == '-GENERATE-' and values['-SLIDER-']:
            value = int(values['-SLIDER-'])
            pass_result = create_password(value)
            window['-PASSWORD-'].update(pass_result)
            window['-GENERATE-'].update('Generate another')              
        if event == '-COPY-':
            try:
                text = window['-PASSWORD-'].Widget.selection_get()
                window.TKroot.clipboard_clear()
                window.TKroot.clipboard_append(text)
                window['-COPY-'].update('Password copied to clipboard!')
            except:
                window['-COPY-'].update('No password selected!')
    # Kill the window instance        
    window.close()

# Set environment vars
if __name__ == '__main__':
    main()