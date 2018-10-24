class Four_format:
    """ A tool for formatting number of N size padding with 0.
    Designed to make binary and hex values more readable."""
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError
        self.number = number
        self.styles = ["x", "b"]

    def __format__(self, form):
        """ pad is the character used to pad the string.
        length is the desired amount of characters to print.
        style is the type of the representation; supports
        binary and hex."""
        if len(form) < 3:
            raise ValueError
        pad = form[0]
        type = form[-1]
        length = form.partition(type)[0]
        length = int(length.partition(pad)[-1])
        string = ("{:0{length}{type}}"
                  .format(self.number, length = length, type = type))
        step = 4
        words = [string[i:i + step] for i in range(0, len(string), step)]
        output = pad + type
        output += " ".join(words)
        return output.rstrip()
