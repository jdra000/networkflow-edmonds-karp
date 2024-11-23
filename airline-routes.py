print('--- MAXIMIZE FLIGHTS FROM BOG(Colombia) TO JFK(USA) ---')
airplanes_available = int(input('Please type number of airplanes available: '))

print('--- BOG(Bogotá) ---')

BOG_MIA = int(input('Availability BOG - MIA: '))
BOG_PTY = int(input('Availability BOG - PTY: '))
BOG_LIM = int(input('Availability BOG - LIM: '))
BOG_EWR = int(input('Availability BOG - EWR: '))

print()

print('--- MIA(Miami) ---')

MIA_JFK = int(input('Availability MIA - JKF: '))

print()

print('--- LIM(Lima) ---')

LIM_EWR = int(input('Availability LIM - EWR: '))
LIM_JFK = int(input('Availability LIM - JFK: '))

print()

print('--- PTY(Panamá) ---')

PTY_EWR = int(input('Availability PTY - EWR: '))
PTY_JFK = int(input('Availability PTY - JFK: '))

print()

print('--- EWR(Mexico) ---')

EWR_JFK = int(input('Availability EWR - JFK: '))

print()

from graph import Graph
from ford_fulkerson import FordFulkerson

graph = Graph()
graph.add_nodes(['BOG', 'MIA', 'PTY', 'LIM', 'EWR', 'JFK'])
# BOGOTA
graph.add_edge('BOG', 'MIA', BOG_MIA)
graph.add_edge('BOG', 'PTY', BOG_PTY)
graph.add_edge('BOG', 'LIM', BOG_LIM)
graph.add_edge('BOG', 'EWR', BOG_EWR)
# MIAMI
graph.add_edge('MIA', 'JFK', MIA_JFK)
# LIMA
graph.add_edge('LIM', 'EWR', LIM_EWR)
graph.add_edge('LIM', 'JFK', LIM_JFK)
# PANAMA
graph.add_edge('PTY', 'EWR', PTY_EWR)
graph.add_edge('PTY', 'JFK', PTY_JFK)
# MEXICO
graph.add_edge('EWR', 'JFK', EWR_JFK)


starting_node = 'BOG'
ending_node = 'JFK'
method = FordFulkerson(graph, starting_node, ending_node)

print('ROUTES AVAILABLE: \n')
max_amount = method.initiate()

print(f"\n !!! {max_amount} PLANES AUTHORIZED FOR THE ROUTE !!!")

if max_amount > airplanes_available:
    print(f'FROM {airplanes_available} AVAILABLE YOU CAN START OPERATION WITH {airplanes_available}')
else:
    print(f'FROM {airplanes_available} AVAILABLE YOU CAN START OPERATION WITH {max_amount}')
