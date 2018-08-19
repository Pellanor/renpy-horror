# Not actually functional...
class SaveTestFunctional:
    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self.lst = lst

    def __str__(self):
        return "FunctionalSaveTest String\n" + '(%s)' % ', '.join(map(str, self.lst))

    def add(self, s):
        lst = list(self.lst)
        lst.append(s)
        return SaveTestFunctional(lst)
