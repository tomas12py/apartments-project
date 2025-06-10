from rest_framework import serializers

def number_greater_than_zero(value):
    if value == 0:
        raise serializers.ValidationError("The number must be greater than zero")
    
def is_letter_and_spaces(string_param):
    if not all(valid_param.isalpha() or valid_param.isspace() for valid_param in string_param) and string_param != '':
        raise serializers.ValidationError("The value only allowed letters or spaces")