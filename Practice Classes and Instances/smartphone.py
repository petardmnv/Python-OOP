class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = list()
        self.is_on = False
        self.used_memory = 0

    def power(self):
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int):
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        if (self.used_memory + app_memory) < self.memory:
            self.used_memory += app_memory
            self.apps.append(app)
            return f"Installing {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory - self.used_memory}"

smartphone = Smartphone(100)

print(smartphone.install("Facebook", 60))

smartphone.power()

print(smartphone.install("Facebook", 60))

print(smartphone.install("Messenger", 20))

print(smartphone.install("Instagram", 40))

print(smartphone.status())