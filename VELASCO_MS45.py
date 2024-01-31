class chess:
    def __init__(self, vertical, horizontal, blocks):
        self.vertical = vertical
        self.horizontal = horizontal
        self.vertices = self.vertical * self.horizontal
        self.coords = [(x, y) for x in range(self.vertical) for y in range(self.horizontal)]
        self.floyd = FloydWarshall(self.vertices)
        self.blocks = blocks
        self.index_coords = [False for i in range(len(self.coords))]

    def pawn(self,x1,y1):
        source = (x1,y1)
        for x in range(x1+1,self.vertical):
            dest = (x, y1)
            if dest in self.blocks:
                break
            else:
                vertex_source = self.coords.index(source)
                vertex_dest = self.coords.index(dest)
                edge = Edge(int(vertex_source), int(vertex_dest), int(1))
                self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                source = dest

    def rook(self,x1, y1):

        index_coords_rook = [False for i in range(len(self.coords))]

        def recurse(x,y):
            source1 = (x,y)
            vertex_source = self.coords.index(source1)
            if index_coords_rook[vertex_source] == False:

                for left in range(y-1, -1, -1):
                    dest_left = (x, left)
                    if dest_left in self.blocks:
                        break
                    else:
                        vertex_dest_left = self.coords.index(dest_left)
                        edge = Edge(int(vertex_source), int(vertex_dest_left), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_rook[self.coords.index(source1)] = True
                        recurse(dest_left[0], dest_left[1])

                for right in range(y+1, self.horizontal):
                    dest_right = (x, right)
                    if dest_right in self.blocks:
                        break
                    else:
                        vertex_dest_right = self.coords.index(dest_right)
                        edge = Edge(int(vertex_source), int(vertex_dest_right), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_rook[self.coords.index(source1)] = True
                        recurse(dest_right[0], dest_right[1])

                for up in range(x+1, self.vertical):
                    dest_up = (up, y)
                    if dest_up in self.blocks:
                        break
                    else:
                        vertex_dest_up = self.coords.index(dest_up)
                        edge = Edge(int(vertex_source), int(vertex_dest_up), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_rook[self.coords.index(source1)] = True
                        recurse(dest_up[0], dest_up[1])

                for down in range(x-1, -1, -1):
                    dest_down = (down, y)
                    if dest_down in self.blocks:
                        break
                    else:
                        vertex_dest_down = self.coords.index(dest_down)
                        edge = Edge(int(vertex_source), int(vertex_dest_down), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_rook[self.coords.index(source1)] = True
                        recurse(dest_down[0], dest_down[1])

        recurse(x1,y1)

    def bishop(self, x1,y1):

        index_coords_bishop = [False for i in range(len(self.coords))]

        def recurse(x,y):
            source1 = (x,y)
            vertex_source = self.coords.index(source1)
            if index_coords_bishop[vertex_source] == False:
                upper_left = (x+1, y-1)
                upper_right = (x+1, y+1)
                lower_left = (x-1, y-1)
                lower_right = (x-1, y+1)

                while upper_left in self.coords:
                    if upper_left in self.blocks:
                        break
                    else:
                        vertex_uleft = self.coords.index(upper_left)
                        edge = Edge(int(vertex_source), int(vertex_uleft), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_bishop[self.coords.index(source1)] = True
                        recurse(upper_left[0], upper_left[1])
                        upper_left = (upper_left[0]+1, upper_left[1]-1)

                while upper_right in self.coords:
                    if upper_right in self.blocks:
                        break
                    else:
                        vertex_uright = self.coords.index(upper_right)
                        edge = Edge(int(vertex_source), int(vertex_uright), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_bishop[self.coords.index(source1)] = True
                        recurse(upper_right[0], upper_right[1])
                        upper_right = (upper_right[0]+1, upper_right[1]+1)

                while lower_left in self.coords:
                    if lower_left in self.blocks:
                        break
                    else:
                        vertex_lleft = self.coords.index(lower_left)
                        edge = Edge(int(vertex_source), int(vertex_lleft), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_bishop[self.coords.index(source1)] = True
                        recurse(lower_left[0], lower_left[1])
                        lower_left = (lower_left[0]-1, lower_left[1]-1)

                while lower_right in self.coords:
                    if lower_right in self.blocks:
                        break
                    else:
                        vertex_lright = self.coords.index(lower_right)
                        edge = Edge(int(vertex_source), int(vertex_lright), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_bishop[self.coords.index(source1)] = True
                        recurse(lower_right[0], lower_right[1])
                        lower_right = (lower_right[0]-1, lower_right[1]+1)
        recurse(x1,y1)

    def queen(self, x,y):

        index_coords_queen = [False for i in range(len(self.coords))]
        source1 = (x,y)
        vertex_source = self.coords.index(source1)
        if index_coords_queen[vertex_source] == False:

            for left in range(y-1, -1, -1):
                dest_left = (x, left)
                if dest_left in self.blocks:
                    break
                else:
                    vertex_dest_left = self.coords.index(dest_left)
                    edge = Edge(int(vertex_source), int(vertex_dest_left), int(1))
                    self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                    index_coords_queen[self.coords.index(source1)] = True
                    self.rook(dest_left[0], dest_left[1])
                    self.bishop(dest_left[0], dest_left[1])

            for right in range(y+1, self.horizontal):
                dest_right = (x, right)
                if dest_right in self.blocks:
                    break
                else:
                    vertex_dest_right = self.coords.index(dest_right)
                    edge = Edge(int(vertex_source), int(vertex_dest_right), int(1))
                    self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                    index_coords_queen[self.coords.index(source1)] = True
                    self.rook(dest_right[0], dest_right[1])
                    self.bishop(dest_right[0], dest_right[1])

            for up in range(x+1, self.vertical):
                dest_up = (up, y)
                if dest_up in self.blocks:
                    break
                else:
                    vertex_dest_up = self.coords.index(dest_up)
                    edge = Edge(int(vertex_source), int(vertex_dest_up), int(1))
                    self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                    index_coords_queen[self.coords.index(source1)] = True
                    self.rook(dest_up[0], dest_up[1])
                    self.bishop(dest_up[0], dest_up[1])

            for down in range(x-1, -1, -1):
                dest_down = (down, y)
                if dest_down in self.blocks:
                    break
                else:
                    vertex_dest_down = self.coords.index(dest_down)
                    edge = Edge(int(vertex_source), int(vertex_dest_down), int(1))
                    self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                    index_coords_queen[self.coords.index(source1)] = True
                    self.rook(dest_down[0], dest_down[1])
                    self.bishop(dest_down[0], dest_down[1])

            upper_left = (x+1, y-1)
            upper_right = (x+1, y+1)
            lower_left = (x-1, y-1)
            lower_right = (x-1, y+1)

            while upper_left in self.coords:
                if upper_left in self.blocks:
                    break
                else:
                    vertex_uleft = self.coords.index(upper_left)
                    edge = Edge(int(vertex_source), int(vertex_uleft), int(1))
                    self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                    index_coords_queen[self.coords.index(source1)] = True
                    self.rook(upper_left[0], upper_left[1])
                    self.bishop(upper_left[0], upper_left[1])
                    upper_left = (upper_left[0]+1, upper_left[1]-1)

            while upper_right in self.coords:
                if upper_right in self.blocks:
                    break
                else:
                    vertex_uright = self.coords.index(upper_right)
                    edge = Edge(int(vertex_source), int(vertex_uright), int(1))
                    self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                    index_coords_queen[self.coords.index(source1)] = True
                    self.rook(upper_right[0], upper_right[1])
                    self.bishop(upper_right[0], upper_right[1])
                    upper_right = (upper_right[0]+1, upper_right[1]+1)

            while lower_left in self.coords:
                if lower_left in self.blocks:
                    break
                else:
                    vertex_lleft = self.coords.index(lower_left)
                    edge = Edge(int(vertex_source), int(vertex_lleft), int(1))
                    self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                    index_coords_queen[self.coords.index(source1)] = True
                    self.rook(lower_left[0], lower_left[1])
                    self.bishop(lower_left[0], lower_left[1])
                    lower_left = (lower_left[0]-1, lower_left[1]-1)

            while lower_right in self.coords:
                if lower_right in self.blocks:
                    break
                else:
                    vertex_lright = self.coords.index(lower_right)
                    edge = Edge(int(vertex_source), int(vertex_lright), int(1))
                    self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                    index_coords_queen[self.coords.index(source1)] = True
                    self.rook(lower_right[0], lower_right[1])
                    self.bishop(lower_right[0], lower_right[1])
                    lower_right = (lower_right[0]-1, lower_right[1]+1)

    def king(self, x1, y1):

        index_coords_king = [False for i in range(len(self.coords))]

        def recurse(x,y):
            source1 = (x,y)
            vertex_source = self.coords.index(source1)
            if index_coords_king[vertex_source] == False:

                upper_left = (x+1, y-1)
                if upper_left in self.coords:
                    if upper_left not in self.blocks:
                        vertex_uleft = self.coords.index(upper_left)
                        edge = Edge(int(vertex_source), int(vertex_uleft), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_king[self.coords.index(source1)] = True
                        recurse(upper_left[0], upper_left[1])

                upper_right = (x+1, y+1)
                if upper_right in self.coords:
                    if upper_right not in self.blocks:
                        vertex_uright = self.coords.index(upper_right)
                        edge = Edge(int(vertex_source), int(vertex_uright), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_king[self.coords.index(source1)] = True
                        recurse(upper_right[0], upper_right[1])

                lower_left = (x-1, y-1)
                if lower_left in self.coords:
                    if lower_left not in self.blocks:
                        vertex_lleft = self.coords.index(lower_left)
                        edge = Edge(int(vertex_source), int(vertex_lleft), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_king[self.coords.index(source1)] = True
                        recurse(lower_left[0], lower_left[1])

                lower_right = (x-1, y+1)
                if lower_right in self.coords:
                    if lower_right not in self.blocks:
                        vertex_lright = self.coords.index(lower_right)
                        edge = Edge(int(vertex_source), int(vertex_lright), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_king[self.coords.index(source1)] = True
                        recurse(lower_right[0], lower_right[1])

                up = (x+1, y)
                if up in self.coords:
                    if up not in self.blocks:
                        vertex_up = self.coords.index(up)
                        edge = Edge(int(vertex_source), int(vertex_up), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_king[self.coords.index(source1)] = True
                        recurse(up[0], up[1])

                down = (x-1, y)
                if down in self.coords:
                    if down not in self.blocks:
                        vertex_down = self.coords.index(down)
                        edge = Edge(int(vertex_source), int(vertex_down), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_king[self.coords.index(source1)] = True
                        recurse(down[0], down[1])

                left = (x, y-1)
                if left in self.coords:
                    if left not in self.blocks:
                        vertex_left = self.coords.index(left)
                        edge = Edge(int(vertex_source), int(vertex_left), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_king[self.coords.index(source1)] = True
                        recurse(left[0], left[1])

                right = (x, y+1)
                if right in self.coords:
                    if right not in self.blocks:
                        vertex_right = self.coords.index(right)
                        edge = Edge(int(vertex_source), int(vertex_right), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_king[self.coords.index(source1)] = True
                        recurse(right[0], right[1])
        recurse(x1,y1)

    def knight(self, x1, y1):

        index_coords_knight = [False for i in range(len(self.coords))]

        def recurse(x,y):
            source1 = (x,y)
            vertex_source = self.coords.index(source1)
            if index_coords_knight[vertex_source] == False:

                upper_left1 = (x+1, y-2)
                if upper_left1 in self.coords:
                    if upper_left1 not in self.blocks:
                        vertex_uleft1 = self.coords.index(upper_left1)
                        edge = Edge(int(vertex_source), int(vertex_uleft1), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_knight[self.coords.index(source1)] = True
                        recurse(upper_left1[0], upper_left1[1])

                upper_left2 = (x+2, y-1)
                if upper_left2 in self.coords:
                    if upper_left2 not in self.blocks:
                        vertex_uleft2 = self.coords.index(upper_left2)
                        edge = Edge(int(vertex_source), int(vertex_uleft2), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_knight[self.coords.index(source1)] = True
                        recurse(upper_left2[0], upper_left2[1])

                upper_right1 = (x+2, y+1)
                if upper_right1 in self.coords:
                    if upper_right1 not in self.blocks:
                        vertex_uright1 = self.coords.index(upper_right1)
                        edge = Edge(int(vertex_source), int(vertex_uright1), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_knight[self.coords.index(source1)] = True
                        recurse(upper_right1[0], upper_right1[1])

                upper_right2 = (x+1, y+2)
                if upper_right2 in self.coords:
                    if upper_right2 not in self.blocks:
                        vertex_uright2 = self.coords.index(upper_right2)
                        edge = Edge(int(vertex_source), int(vertex_uright2), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_knight[self.coords.index(source1)] = True
                        recurse(upper_right2[0], upper_right2[1])

                lower_right1 = (x-1, y+2)
                if lower_right1 in self.coords:
                    if lower_right1 not in self.blocks:
                        vertex_lright1 = self.coords.index(lower_right1)
                        edge = Edge(int(vertex_source), int(vertex_lright1), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_knight[self.coords.index(source1)] = True
                        recurse(lower_right1[0], lower_right1[1])

                lower_right2 = (x-2, y+1)
                if lower_right2 in self.coords:
                    if lower_right2 not in self.blocks:
                        vertex_lright2 = self.coords.index(lower_right2)
                        edge = Edge(int(vertex_source), int(vertex_lright2), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_knight[self.coords.index(source1)] = True
                        recurse(lower_right2[0], lower_right2[1])

                lower_left1 = (x-2, y-1)
                if lower_left1 in self.coords:
                    if lower_left1 not in self.blocks:
                        vertex_lleft1 = self.coords.index(lower_left1)
                        edge = Edge(int(vertex_source), int(vertex_lleft1), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_knight[self.coords.index(source1)] = True
                        recurse(lower_left1[0], lower_left1[1])

                lower_left2 = (x-1, y-2)
                if lower_left2 in self.coords:
                    if lower_left2 not in self.blocks:
                        vertex_lleft2 = self.coords.index(lower_left2)
                        edge = Edge(int(vertex_source), int(vertex_lleft2), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_knight[self.coords.index(source1)] = True
                        recurse(lower_left2[0], lower_left2[1])

        recurse(x1,y1)

    def app567(self, x1, y1):

        index_coords_app = [False for i in range(len(self.coords))]

        def recurse(x,y):
            source1 = (x,y)
            vertex_source = self.coords.index(source1)
            if index_coords_app[vertex_source] == False:

                up = (x, y-1)
                if up in self.coords:
                    if up not in self.blocks:
                        vertex_up = self.coords.index(up)
                        edge = Edge(int(vertex_source), int(vertex_up), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_app[self.coords.index(source1)] = True
                        recurse(up[0], up[1])

                down = (x-2, y-1)
                if down in self.coords:
                    if down not in self.blocks:
                        vertex_down = self.coords.index(down)
                        edge = Edge(int(vertex_source), int(vertex_down), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_app[self.coords.index(source1)] = True
                        recurse(down[0], down[1])

                left = (x-1, y-2)
                if left in self.coords:
                    if left not in self.blocks:
                        vertex_left = self.coords.index(left)
                        edge = Edge(int(vertex_source), int(vertex_left), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_app[self.coords.index(source1)] = True
                        recurse(left[0], left[1])

                right = (x-1, y)
                if right in self.coords:
                    if right not in self.blocks:
                        vertex_right = self.coords.index(right)
                        edge = Edge(int(vertex_source), int(vertex_right), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_app[self.coords.index(source1)] = True
                        recurse(right[0], right[1])

                middle = (x-1, y-1)
                if middle in self.coords:
                    if middle not in self.blocks:
                        vertex_middle = self.coords.index(middle)
                        edge = Edge(int(vertex_source), int(vertex_middle), int(1))
                        self.floyd.add_undirected_edge(edge.src, edge.dest, edge.cost)
                        index_coords_app[self.coords.index(source1)] = True
                        recurse(middle[0], middle[1])
        recurse(x1,y1)

    def print(self, x1, y1, endpts = None, piece = None):

        self.floyd.compute_shortest_path()
        true = []
        source = (x1,y1)
        vertex_src = self.coords.index(source)
        if endpts == None and piece == None:
            for dest in range(self.vertices):
                dist = self.floyd.get_shortest_path(vertex_src, dest)
                true.append(dist)
            for x in true:
                print(x)
        else:
            if piece == " pawn":
                dest = (self.vertical-1, y1)
                vertex_dest = self.coords.index(dest)
                dist =  self.floyd.get_shortest_path(vertex_src, vertex_dest)
                return dist, dest
            else:
                vertex_dest = self.coords.index(endpts)
                dist =  self.floyd.get_shortest_path(vertex_src, vertex_dest)
                return dist


class FloydWarshall: # from module
    def __init__(self, V):
        self.V = V
        self.dist = [ [float('inf') for i in range(self.V)] for j in range(self.V)]
        self.pred = [ [None for i in range(self.V)] for j in range(self.V)]

    def add_undirected_edge(self, src, dest, cost):
        self.add_directed_edge(src, dest, cost)
        self.add_directed_edge(dest, src, cost)

    def add_directed_edge(self, src, dest, cost):
        self.dist[src][dest] = cost
        self.pred[src][dest] = src

    def compute_shortest_path(self):
        for k in range(0, self.V):
              for i in range(0, self.V):
                for j in range(0, self.V):
                      if (self.dist[i][k]+self.dist[k][j] < self.dist[i][j]):
                        self.dist[i][j] = self.dist[i][k]+self.dist[k][j]
                        self.pred[i][j] = self.pred[k][j]

    def get_shortest_path(self, src, dest):
        start = src
        end = dest
        path = []
        if end == start:
            return 0
        while end != start:
            path.append(end)
            end = self.pred[start][end]
            if end == None:
                return "-1"
        path.append(start)
        path.reverse()
        return self.dist[src][dest]

class Edge:
      def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = cost

if __name__ == '__main__':
    first_line = input().split(",")
    if len(first_line) == 5: #milestone4
        s1, s2, x1, y1, piece = first_line
        s1, s2, x1, y1 = int(s1), int(s2), int(x1), int(y1)
        n = int(input())
        blocks = []
        for block in range(n):
            block_1, block_2 = input().split(",")
            blocks.append((int(block_2), int(block_1)))
        chess_game = chess(s2, s1, blocks)
        exec('chess_game.' + piece[1:] + str((y1, x1)))
        chess_game.print(y1, x1)

    if len(first_line) == 7:
        s1, s2, x1, y1, x2, y2, piece = first_line
        s1, s2, x1, y1, x2, y2 = int(s1), int(s2), int(x1), int(y1), int(x2), int(y2)
        n = int(input())
        blocks = []
        for block in range(n):
            block_1, block_2 = input().split(",")
            blocks.append((int(block_2), int(block_1)))
        chess_pawn = chess(s2, s1, blocks)
        chess_queen = chess(s2, s1, blocks)
        chess_knight = chess(s2, s1, blocks)
        ending = (y2, x2)
        if piece[1:] == "pawn":
            chess_pawn.pawn(y1, x1)
            pawn_dist, pawn_dest = chess_pawn.print(y1, x1, ending, piece)
            min_paths = []
            if int(pawn_dist) != -1:
                chess_queen.queen(pawn_dest[0], pawn_dest[1])
                queen_dist = chess_queen.print(pawn_dest[0], pawn_dest[1], ending, "queen")
                if int(queen_dist) != -1:
                    min_paths.append(queen_dist)
                chess_knight.knight(pawn_dest[0], pawn_dest[1])
                knight_dist = chess_knight.print(pawn_dest[0], pawn_dest[1], ending, "knight")
                if int(knight_dist) != -1:
                    min_paths.append(knight_dist)

                if min_paths:
                    total = pawn_dist + min(min_paths)
                    print (total)
                else:
                    print ("-1")
            else:
                print ("-1")



