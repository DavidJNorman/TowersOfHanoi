class Tower(object):

    def __init__(self, given_name):
        self.name = given_name
        self.discs = []

class TowersOfHanoi(object):

    def output_message(self, t1, t2, disc):
        print(str(self.step) + ": Move disc " + str(disc) + " from " + t1.name + " to " + t2.name)

    def solve(self, tower1, tower2, tower3, disc):
        if disc == 1:
            moved_disc = tower1.discs.pop()
            tower2.discs.append(moved_disc)
            self.output_message(tower1, tower2, moved_disc)
            self.step += 1
        else:
            self.solve(tower1, tower3, tower2, disc - 1)
            moved_disc = tower1.discs.pop()
            tower2.discs.append(moved_disc)
            self.output_message(tower1, tower2, moved_disc)
            self.step += 1
            self.solve(tower3, tower2, tower1, disc - 1)

    def __init__(self, source_name, dest_name, aux_name, height):
        self.source = Tower(source_name)
        self.destination = Tower(dest_name)
        self.auxillary = Tower(aux_name)
        self.step = 1
        for i in range(height, 0, -1):
            self.source.discs.append(i)
        self.solve(self.source, self.destination, self.auxillary, len(self.source.discs))