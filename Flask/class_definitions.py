import pickle 

class BOTTLE:
#  'Common base class for BOTTLE object'
  bottleCount = 0

  def __init__(self,spirit,name,size,amount_left,ABV, price):
    self.spirit_type=spirit
    self.name_of_bottle=name
    self.size_of_bottle=size
    self.amount_left=amount_left
    self.ABV=ABV
    self.price_shot=price

  def __str__(self):
    return self.__dict__ 

  def __repr__(self): # this gets called when __dict__ of pump is called
    return str(self.__dict__)

class PUMP:
#  'Defines a Pump. Each Pump has a bottle, a pin, and an amount of time to prime.
#   priming_time is a derived quantity, based on the size of the bottle and how much is left'
  number=4 #This is constant; depends on the machine

  def __init__(self, BOTTLE, pin, priming_time):
    self.BOTTLE = BOTTLE
    self.pin=pin
    self.priming_time=priming_time

  def __repr__(self):
    return str(self.__dict__)

test_bottle = BOTTLE('Vodka','Svedka',750,750,35,0)
test_bottle2= BOTTLE('Rum, Generic', 'Capt. Morgan',1500,1500,25,0)
test_pump = PUMP(test_bottle,16,200)
test_pump2= PUMP(test_bottle2,14,250)
#pump_list = [test_pump,test_pump2]


def save_pumps(pump_list):
#test writing it to a file
  file_pump=open('./lists/pumps.cfg','w')
  with file_pump as output:
    pickle.dump(pump_list,output, -1)
  file_pump.close()

##Usage for load_pumps
## read_pump_list = load_pumps()
#  `print read_pump_list[1]` prints the second pump object
#  `print read_pump_list[0].BOTTLE.spirit_type` you get it

def load_pumps():
  file_pump=open('./lists/pumps.cfg','r')
  with file_pump as input:
    read_pump_list = pickle.load(input)
  file_pump.close()
  return read_pump_list

def create_pumps_list():
  #A list, with pin assignments
  pins=range(2,26)
  NUM_PUMPS=16
  pump_list=[]
  for idx in range(0,NUM_PUMPS):
    pump_list.append(PUMP (BOTTLE('','',0,0,0,0),pins[idx],200))
  return pump_list
  
#save_pumps(pump_list)
#print(load_pumps())

#print create_pumps_list()
