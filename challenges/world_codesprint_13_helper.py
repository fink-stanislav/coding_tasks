class Group(object):
    
    def __init__(self, name, grade):
        self.names = set()
        self.names.add(name)
        self.grades = {}
        self.grades[grade] = 1
        self.number = 0
    
    def get_grades_count(self, grade):
        return self.grades.get(grade, 0)

    def merge(self, group):
        self.names |= group.names
        for grade, count in group.grades.iteritems():
            g = self.grades.get(grade, 0)
            if g != 0:
                self.grades[grade] += count
            else:
                self.grades[grade] = count

    def get_size(self):
        return len(self.names)
    
    def is_valid(self, restrictions):
        if self.get_size() < restrictions['min']:
            return False
        return True

class Groups(object):
    
    def __init__(self, groups, restrictions):
        self.restrictions = restrictions
        #self.groups = groups
        self.groups = {}
        self.name_group = {}
        for i, g in enumerate(groups):
            self.groups[i] = g
            g.number = i
            self.name_group[next(iter(g.names))] = i

    def can_merge(self, group1, group2):
        gs1 = group1.get_size()
        gs2 = group2.get_size()
        
        if gs1 + gs2 > self.restrictions['max']:
            return False
        
        if group1.get_grades_count(1) + group2.get_grades_count(1) > self.restrictions['fg']:
            return False
        
        if group1.get_grades_count(2) + group2.get_grades_count(2) > self.restrictions['sg']:
            return False
        
        if group1.get_grades_count(3) + group2.get_grades_count(3) > self.restrictions['tg']:
            return False
    
        return True
    
    def get_group(self, name):
        """
        for group in self.groups:
            if name in group.names:
                return group
        return None
        """
        number = self.name_group[name]
        return self.groups[number]
    
    def merge(self, name1, name2):
        group1 = self.get_group(name1)
        group2 = self.get_group(name2)
        if group1 == group2:
            return
        if self.can_merge(group1, group2):
            group1.merge(group2)
            self.groups.pop(group2.number)

            for name in group2.names:
                self.name_group[name] = group1.number

    def print_largest(self):
        _max = -1
        for _, group in self.groups.iteritems():
            if group.is_valid(self.restrictions):
                gs = group.get_size()
                if gs > _max:
                    _max = gs

        if _max == -1:
            print 'no groups'
            return

        names = set()
        for _, group in self.groups.iteritems():
            if group.get_size() == _max:
                names |= group.names

        result = sorted(list(names))
        for r in result:
            print r

# Complete the membersInTheLargestGroups function below.
def membersInTheLargestGroups(a, b, f, s, t, students, requests):
    # Print the names of the students in all largest groups or determine if there are no valid groups.
    
    restrictions = {'fg': f, 'sg': s, 'tg': t, 'min': a, 'max': b}
    students = [student.split(' ') for student in students]
    groups = [Group(student[0], int(student[1])) for student in students]
    
    groups = Groups(groups, restrictions)
    
    for request in requests:
        r = request.split(' ')
        name1 = r[0]
        name2 = r[1]
        groups.merge(name1, name2)
    
    groups.print_largest()
