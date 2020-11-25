from PyInquirer import prompt, print_json, style_from_dict, Token   
from validators import PhoneNumberValidator

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})
questions =  [
            {
                'type': 'input',
                'name': 'country_code',
                'message': 'Enter country code without (+) sign',
            },
            {
                'type': 'input',
                'name': 'phone_number',
                'message': 'Enter phone number ',
                'validate': PhoneNumberValidator
            },
            {
                'type': 'input',
                'name': 'quantity',
                'message': 'Enter number of messages to send',
                'validate': lambda val: val.isnumeric() or 'Must be an integer'
            },
            {
                'type': 'input',
                'name': 'custom_msg',
                'message': 'Enter custom message'
            }
        ]

class Menu():
    def __init__(self):
        self.questions = questions
    def answers(self):
        return prompt(self.questions,style=style)

