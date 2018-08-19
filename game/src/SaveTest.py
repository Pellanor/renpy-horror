from SaveTestNested import SaveTestNested


class SaveTest:
    def __init__(self, flag=False):
        self.nest = None
        self.flag = flag
        self.list = []

    def __str__(self):
        if self.nest:
            return "Nested " + str(self.nest)
        if self.flag:
            return "Modified save test\n" + '(%s)' % ', '.join(map(str, self.list))
        return "SaveTest String\n" + '(%s)' % ', '.join(map(str, self.list))

    def add(self, s):
        self.list.append(s)
        return self

    def nested(self, s):
        self.nest = SaveTestNested(s)
