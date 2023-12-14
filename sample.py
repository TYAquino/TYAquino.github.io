class Appointment:
    def __init__(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    def reset(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = ''

    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self):
        return self.__appt_type

# Create an appointment object
appt = Appointment("John Doe", "123-456-7890", "Regular")
print(appt.get_client_name()) # Output: John Doe
print(appt.get_client_phone()) # Output: 123-456-7890
print(appt.get_appt_type()) # Output: Regular

# Reset the appointment object
appt.reset()
print(appt.get_client_name()) # Output: ''
print(appt.get_client_phone()) # Output: ''
print(appt.get_appt_type()) # Output: 0

class Appointment:
    def __init__(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    def reset(self):
        self.set_client_name("")
        self.set_client_phone("")
        self.set_appt_type(0)

    def get_client_name(self):
        return self.__client_name

    def set_client_name(self, client_name):
        if isinstance(client_name, str):
            self.__client_name = client_name
        else:
            raise ValueError("client_name must be a string")

    def get_client_phone(self):
        return self.__client_phone

    def set_client_phone(self, client_phone):
        if isinstance(client_phone, str):
            self.__client_phone = client_phone
        else:
            raise ValueError("client_phone must be a string")

    def get_appt_type(self):
        return self.__appt_type

    def set_appt_type(self, appt_type):
        if isinstance(appt_type, int):
            self.__appt_type = appt_type
        else:
            raise ValueError("appt_type must be an integer")

# Create an appointment object
appt = Appointment("John Doe", "123-456-7890", "Regular")
print(appt.get_client_name()) # Output: John Doe
print(appt.get_client_phone()) # Output: 123-456-7890
print(appt.get_appt_type()) # Output: Regular

# Reset the appointment object
appt.reset()
print(appt.get_client_name()) # Output: ''
print(appt.get_client_phone()) # Output: ''
print(appt.get_appt_type()) # Output: 0