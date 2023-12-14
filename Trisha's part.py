# For cancel() part that resets the client's info properties to zero/empty
day_cancellation = input('What day: ')
start_hour = input('Enter start hour (24 hour clock): ')


def reset(self):
    self.__client_name = ''
    self.__client_phone = ''
    self.__appt_type = ''

def get_client_name(self):
    return self.__client_name

def get_client_phone(self):
    return self.__client_phone

def get_appt_type(self):
    return self.__appt_types
appt.reset()