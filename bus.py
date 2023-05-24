class bus:
  # bus_id: 客運ID bus_capacity: 可上車人數
  def __init__(self, bus_id, bus_capacity):
    self.bus_id = bus_id
    self.bus_capacity = bus_capacity
  
  def set_bus_id(self, bus_id):
    self.bus_id = bus_id
  def set_bus_capacity(self, bus_capacity):
    self.bus_capacity = bus_capacity

  def get_bus_id(self):
    return str(self.bus_id)
  def get_bus_capacity(self):
    return str(self.bus_capacity)
  
  def __str__(self):
    return "客運ID: " + str(self.bus_id) + ", 可上車人數: " + str(self.bus_capacity) + "\n"
  
bus_1579 = bus("1579", 30)

def get_bus():
  return bus_1579