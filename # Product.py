# Product
class Computer:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show(self):
        return f"Computer Parts: {', '.join(self.parts)}"

# Builder Interface
class ComputerBuilder:
    def add_processor(self): pass
    def add_ram(self): pass
    def add_storage(self): pass
    def get_computer(self): pass

# Concrete Builder for Gaming Computer
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def add_processor(self):
        self.computer.add_part("High-end Processor")

    def add_ram(self):
        self.computer.add_part("32GB RAM")

    def add_storage(self):
        self.computer.add_part("1TB SSD")

    def get_computer(self):
        return self.computer

# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_computer(self):
        self.builder.add_processor()
        self.builder.add_ram()
        self.builder.add_storage()

# Client Code
builder = GamingComputerBuilder()
director = Director(builder)
director.build_computer()
computer = builder.get_computer()
print(computer.show())  # Output: Computer Parts: High-end Processor, 32GB RAM, 1TB SSD
