class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("Cannot dynamically create new instance attributes")
        super().__setattr__(name, value)
