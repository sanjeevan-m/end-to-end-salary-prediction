import sys 
def error_message_detail(what_error,error_detail:sys):
    exc_type, exc_value, exc_traceback =error_detail.exc_info()
    file_name=exc_traceback.tb_frame.f_code.co_filename 
    file_line=exc_traceback.tb_lineno
    error=str(what_error)
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,file_line,error)
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message