
def final(top_right, position):
    coord = ["N", "E", "S", "W"]
    for key, value in position.items():
        current_coord, coord_index = key[-1], 
        x, y = key[0], key[1]
        
        


top_right = "55"
position = {
    "12N": "LMLMLMLMM",
    "33E": "MMRMMRMRRM"
}
print(final(top_right, position))