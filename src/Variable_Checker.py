import os

class Variable_Checker:

    def exists(self, variable_name: str) -> bool:
        if variable_name in os.environ:
            return True
        return False
