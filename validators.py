from prompt_toolkit.validation import Validator,ValidationError
import regex

class PhoneNumberValidator(Validator):
    def validate(self,number):
        ok = regex.match('^\+?[0-9]{9,15}$',number.text)
        if not ok:
            raise ValidationError(
            message='Please enter a valid phone number',
            cursor_position=len(number.text)
        )

