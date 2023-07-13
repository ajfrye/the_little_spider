
class Option:
    processors = 0
    speed      = 0.0
    name       = None
    switches   = 0

    def set_processors(self, num_proc):
        self.processors = num_proc

    def set_speed(self, proc_speed):
        self.speed = proc_speed    
    
    def set_name(self, name):
        self.name = name
    
    def set_switches(self, num_switches):
        self.switches = num_switches
    