class CarDoorsClass:
    def __init__(self):
        self._doors = 0

    def get_number_of_doors(self):
        return self._doors

    def set_number_of_doors(self, doors):
        if isinstance(doors, int) and doors > 0:
            self._doors = doors
        else:
            raise ValueError("Number of doors must be a positive integer.")
