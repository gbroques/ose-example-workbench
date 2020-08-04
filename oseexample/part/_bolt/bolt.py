import Part


class Bolt:

    @staticmethod
    def make() -> Part.Shape:
        return Part.makeBox(10, 10, 10)
