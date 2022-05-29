class Student:
    def __init__(self,name,age,tracks,score):
        pass

    def change_name(self, newname):
        self.name = newname
        print(self.name)

    def change_age(self, newage):
        self.age = int(newage)
        print(self.age)

    def add_track(self, newtrack):
        self.tracks = newtrack
        print(self.tracks)

    def get_score(self):
        pass
    

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
