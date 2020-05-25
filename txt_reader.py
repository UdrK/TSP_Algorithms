from graph import Graph
import math

def to_radians(convertee):
    deg = int(convertee)
    min = convertee - deg
    return math.pi * (deg + 5.0 * min/3.0) / 180.0

def geographical_distance(latitude1, latitude2, longitude1, longitude2):
    rrr = 6378.388

    q1 = math.cos(longitude1 - longitude2)
    q2 = math.cos(latitude1 - latitude2)
    q3 = math.cos(latitude1 + latitude2)

    return int(rrr * math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)

def euclidean_distance(x1, x2, y1, y2):
    q1 = x1 - x2
    q2 = y1 - y2
    q1 = q1**2
    q2 = q2**2
    return round(math.sqrt(q1 + q2))

def distance(x1, x2, y1, y2, format):
    if format == "GEO":
        x1 = to_radians(x1)
        x2 = to_radians(x2)
        y1 = to_radians(y1)
        y2 = to_radians(y2)
        return geographical_distance(x1, x2, y1, y2)
    elif format == "EUC_2D":
        return euclidean_distance(x1, x2, y1, y2)

def file_to_graph(file_path):

    format = ""
    size = -1
    vertices = []
    adjacency_matrix = []
    coordinates = []

    f = open(file_path, 'r')
    file_lines = f.readlines()
    line = file_lines.pop(0)
    while not "NODE_COORD_SECTION" in line:
        values = line.split()
        if "DIMENSION" in values[0]:
            size = int(values[-1])
        elif "EDGE_WEIGHT_TYPE" in values[0]:
            format = values[-1]
        line = file_lines.pop(0)

    if format == "" or size == -1:
        print("Something went wrong")

    vertices = [None for i in range(size)]
    adjacency_matrix = [[None for i in range(size)] for j in range(size)]
    coordinates = [[None for i in range(2)] for j in range(size)]

    line = file_lines.pop(0)
    while not "EOF" in line:
        values = line.split()
        vertex = int(values[0])
        x = float(values[1])
        y = float(values[2])

        vertices[vertex-1] = vertex - 1
        coordinates[vertex - 1][0] = x
        coordinates[vertex - 1][1] = y

        adjacency_matrix[vertex - 1][vertex - 1] = 0
        for i in range(0, vertex-1):
            dist = distance(x, coordinates[i][0], y, coordinates[i][1], format)
            adjacency_matrix[i][vertex-1] = dist
            adjacency_matrix[vertex-1][i] = dist

        line = file_lines.pop(0)

    return Graph(adjacency_matrix, vertices)