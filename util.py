class vprinter:
    def __init__(self, verbose):
        self.verbose = verbose

    def vprint(self, obj):
        if self.verbose:
            print(obj)
