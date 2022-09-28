# Returns the steps required to solve a Rubrics Cube
# Couper Smith

# Cube Class accepts six faces as paramaters and creates a "cube" using these faces
class Cube:

    # assigns the faces and then creates a list containing each face used to iterate through
    def __init__(self, top, bottom, front, back, right, left):
        _registry = []
        self.faces = _registry
        self.bottom = self.Face(bottom)
        self.faces.append(self.bottom)
        self.top = self.Face(top)
        self.faces.append(self.top)
        self.front = self.Face(front)
        self.faces.append(self.front)
        self.back = self.Face(back)
        self.faces.append(self.back)
        self.left = self.Face(left)
        self.faces.append(self.left)
        self.right = self.Face(right)
        self.faces.append(self.right)

    # moves required to perform a clockwise rotation of the top face (Face 2)
    def topCW(self):
        temp = self.back.pieces[0].copy()
        self.back.pieces[0] = self.left.pieces[0].copy()
        self.left.pieces[0] = self.front.pieces[0].copy()
        self.front.pieces[0] = self.right.pieces[0].copy()
        self.right.pieces[0] = temp
        self.top.resetCW()
        print("Top (Face 2) Clockwise")

    # moves required to perform a counter-clockwise rotation of the top face (Face 2)
    def topCCW(self):
        temp = self.back.pieces[0].copy()
        self.back.pieces[0] = self.right.pieces[0].copy()
        self.right.pieces[0] = self.front.pieces[0].copy()
        self.front.pieces[0] = self.left.pieces[0].copy()
        self.left.pieces[0] = temp
        self.top.resetCCW()
        print("Top (Face 2) Counter-Clockwise")

    # moves required to perform a clockwise rotation of the bottom face (Face 1)
    def bottomCW(self):
        temp = self.front.pieces[2].copy()
        self.front.pieces[2] = self.left.pieces[2].copy()
        self.left.pieces[2] = self.back.pieces[2].copy()
        self.back.pieces[2] = self.right.pieces[2].copy()
        self.right.pieces[2] = temp
        self.bottom.resetCW()
        print("Bottom (Face 1) Clockwise")

    # moves required to perform a counter-clockwise rotation of the bottom face (Face 1)
    def bottomCCW(self):
        temp = self.front.pieces[2].copy()
        self.front.pieces[2] = self.right.pieces[2].copy()
        self.right.pieces[2] = self.back.pieces[2].copy()
        self.back.pieces[2] = self.left.pieces[2].copy()
        self.left.pieces[2] = temp
        self.bottom.resetCCW()
        print("Bottom (Face 1) Counter-Clockwise")

    # moves required to perform a clockwise rotation of the front face (Face 3)
    def frontCW(self):
        temp = self.top.pieces[2].copy()
        self.top.pieces[2] = [self.left.pieces[2][2], self.left.pieces[1][2], self.left.pieces[0][2]]
        self.left.pieces[0][2] = self.bottom.pieces[0][0]
        self.left.pieces[1][2] = self.bottom.pieces[0][1]
        self.left.pieces[2][2] = self.bottom.pieces[0][2]
        self.bottom.pieces[0] = [self.right.pieces[2][0], self.right.pieces[1][0], self.right.pieces[0][0]]
        self.right.pieces[0][0] = temp[0]
        self.right.pieces[1][0] = temp[1]
        self.right.pieces[2][0] = temp[2]
        self.front.resetCW()
        print("Front (Face 3) Clockwise")
    
    # moves required to perform a counter-clockwise rotation of the front face (Face 3)
    def frontCCW(self):
        temp = self.top.pieces[2].copy()
        self.top.pieces[2] = [self.right.pieces[0][0], self.right.pieces[1][0], self.right.pieces[2][0]]
        self.right.pieces[0][0] = self.bottom.pieces[0][2]
        self.right.pieces[1][0] = self.bottom.pieces[0][1]
        self.right.pieces[2][0] = self.bottom.pieces[0][0]
        self.bottom.pieces[0] = [self.left.pieces[0][2], self.left.pieces[1][2], self.left.pieces[2][2]]
        self.left.pieces[0][2] = temp[2]
        self.left.pieces[1][2] = temp[1]
        self.left.pieces[2][2] = temp[0]
        self.front.resetCCW()
        print("Front (Face 3) Counter-Clockwise")

    # moves required to perform a clockwise rotation of the back face (Face 4)
    def backCW(self):
        temp = self.top.pieces[0].copy()
        self.top.pieces[0] = [self.right.pieces[0][2], self.right.pieces[1][2], self.right.pieces[2][2]]
        self.right.pieces[0][2] = self.bottom.pieces[2][2]
        self.right.pieces[1][2] = self.bottom.pieces[2][1]
        self.right.pieces[2][2] = self.bottom.pieces[2][0]
        self.bottom.pieces[2] = [self.left.pieces[0][0], self.left.pieces[1][0], self.left.pieces[2][0]]
        self.left.pieces[0][0] = temp[2]
        self.left.pieces[1][0] = temp[1]
        self.left.pieces[2][0] = temp[0]
        self.back.resetCW()
        print("Back (Face 4) Clockwise")

    # moves required to perform a counter-clockwise rotation of the back face (Face 4)
    def backCCW(self):
        temp = self.top.pieces[0].copy()
        self.top.pieces[0] = [self.left.pieces[2][0], self.left.pieces[1][0], self.left.pieces[0][0]]
        self.left.pieces[0][0] = self.bottom.pieces[2][0]
        self.left.pieces[1][0] = self.bottom.pieces[2][1]
        self.left.pieces[2][0] = self.bottom.pieces[2][2]
        self.bottom.pieces[2] = [self.right.pieces[2][2], self.right.pieces[1][2], self.right.pieces[0][2]]
        self.right.pieces[0][2] = temp[0]
        self.right.pieces[1][2] = temp[1]
        self.right.pieces[2][2] = temp[2]
        self.back.resetCCW()
        print("Back (Face 4) Counter-Clockwise")

    # moves required to perform a clockwise rotation of the right face (Face 6)
    def rightCW(self):
        temp = [self.top.pieces[0][2],self.top.pieces[1][2],self.top.pieces[2][2]]
        self.top.pieces[0][2] = self.front.pieces[0][2]
        self.top.pieces[1][2] = self.front.pieces[1][2]
        self.top.pieces[2][2] = self.front.pieces[2][2]
        self.front.pieces[0][2] = self.bottom.pieces[0][2]
        self.front.pieces[1][2] = self.bottom.pieces[1][2]
        self.front.pieces[2][2] = self.bottom.pieces[2][2]
        self.bottom.pieces[0][2] = self.back.pieces[2][0]
        self.bottom.pieces[1][2] = self.back.pieces[1][0]
        self.bottom.pieces[2][2] = self.back.pieces[0][0]
        self.back.pieces[2][0] = temp[0]
        self.back.pieces[1][0] = temp[1]
        self.back.pieces[0][0] = temp[2]
        self.right.resetCW()
        print("Right (Face 6) Clockwise")

    # moves required to perform a counter-clockwise rotation of the right face (Face 6)
    def rightCCW(self):
        temp = [self.top.pieces[0][2],self.top.pieces[1][2],self.top.pieces[2][2]]
        self.top.pieces[0][2] = self.back.pieces[2][0]
        self.top.pieces[1][2] = self.back.pieces[1][0]
        self.top.pieces[2][2] = self.back.pieces[0][0]
        self.back.pieces[2][0] = self.bottom.pieces[0][2]
        self.back.pieces[1][0] = self.bottom.pieces[1][2]
        self.back.pieces[0][0] = self.bottom.pieces[2][2]
        self.bottom.pieces[0][2] = self.front.pieces[0][2]
        self.bottom.pieces[1][2] = self.front.pieces[1][2]
        self.bottom.pieces[2][2] = self.front.pieces[2][2]
        self.front.pieces[0][2] = temp[0]
        self.front.pieces[1][2] = temp[1]
        self.front.pieces[2][2] = temp[2]
        self.right.resetCCW()
        print("Right (Face 6) Counter-Clockwise")

    # moves required to perform a clockwise rotation of the left face (Face 5)
    def leftCW(self):
        temp = [self.top.pieces[2][0],self.top.pieces[1][0],self.top.pieces[0][0]]
        self.top.pieces[2][0] = self.back.pieces[0][2]
        self.top.pieces[1][0] = self.back.pieces[1][2]
        self.top.pieces[0][0] = self.back.pieces[2][2]
        self.back.pieces[0][2] = self.bottom.pieces[2][0]
        self.back.pieces[1][2] = self.bottom.pieces[1][0]
        self.back.pieces[2][2] = self.bottom.pieces[0][0]
        self.bottom.pieces[2][0] = self.front.pieces[2][0]
        self.bottom.pieces[1][0] = self.front.pieces[1][0]
        self.bottom.pieces[0][0] = self.front.pieces[0][0]
        self.front.pieces[2][0] = temp[0]
        self.front.pieces[1][0] = temp[1]
        self.front.pieces[0][0] = temp[2]
        self.left.resetCW()
        print("Left (Face 5) Clockwise")

    # moves required to perform a counter-clockwise rotation of the left face (Face 5)
    def leftCCW(self):
        temp = [self.top.pieces[2][0],self.top.pieces[1][0],self.top.pieces[0][0]]
        self.top.pieces[2][0] = self.front.pieces[2][0]
        self.top.pieces[1][0] = self.front.pieces[1][0]
        self.top.pieces[0][0] = self.front.pieces[0][0]
        self.front.pieces[2][0] = self.bottom.pieces[2][0]
        self.front.pieces[1][0] = self.bottom.pieces[1][0]
        self.front.pieces[0][0] = self.bottom.pieces[0][0]
        self.bottom.pieces[2][0] = self.back.pieces[0][2]
        self.bottom.pieces[1][0] = self.back.pieces[1][2]
        self.bottom.pieces[0][0] = self.back.pieces[2][2]
        self.back.pieces[0][2] = temp[0]
        self.back.pieces[1][2] = temp[1]
        self.back.pieces[2][2] = temp[2]
        self.left.resetCCW()
        print("Left (Face 5) Counter-Clockwise")

    def rightTrigger(self,face):
        # trigger dictionary looks for which face the right trigger is being performed on
        # checks the colour of the center piece to determine which face it is

        trigger = dict([
            ('O', [self.rightCW,self.topCW,self.rightCCW]), # if performing right trigger on Front (3), face to the right is the Right (6)
            ('G', [self.backCW,self.topCW,self.backCCW]), # if performing right trigger on Right (6), face to the right is the Back (4)
            ('B', [self.leftCW,self.topCW,self.leftCCW]), # if performing right trigger on Back (4), face to the right is the Left (5)
            ('Y', [self.frontCW,self.topCW,self.frontCCW]) # if performing right trigger on Left (5), face to the right is the Front (3)
        ])

        # perform the corresponding right trigger (perform moves in dictionary list returned)
        for i in range(3):
            trigger[face][i]()

    def leftTrigger(self,face):
        # trigger dictionary looks for which face the left trigger is being performed on
        # checks the colour of the center piece to determine which face it is

        trigger = dict([
            ('O', [self.leftCCW,self.topCCW,self.leftCW]), # if performing left trigger on Front (3), face to the left is the Left (5)
            ('G', [self.frontCCW,self.topCCW,self.frontCW]), # if performing left trigger on Right (6), face to the left is the Front (3)
            ('B', [self.rightCCW,self.topCCW,self.rightCW]), # if performing left trigger on Back (4), face to the left is the Right (6)
            ('Y', [self.backCCW,self.topCCW,self.backCW]) # if performing left trigger on Left (5), face to the left is the Back (4)
        ])

        # perform the corresponding left trigger (perform moves in dictionary list returned)
        for i in range(3):
            trigger[face][i]()
    
    # prints the whole cube using the print function for the Face Class
    def printCube(self):
        self.bottom.printFace()
        print("\n")
        self.top.printFace()
        print("\n")
        self.front.printFace()
        print("\n")
        self.back.printFace()
        print("\n")
        self.left.printFace()
        print("\n")
        self.right.printFace()

    # Step 1) make a daisy using the white pieces on the top face
    def make_the_daisy(self):
        print("Step #1: Making the Daisy")
        count = 0   # keeps track of how many white edge pieces are in the correct location
        # checks if there are already white pieces on the top face in place
        if self.top.pieces[0][1] == 'W':
            count += 1
        if self.top.pieces[1][0] == 'W':
            count += 1
        if self.top.pieces[1][2] == 'W':
            count += 1
        if self.top.pieces[2][1] == 'W':
            count += 1
        # keeps iterating through the faces until all white edge pieces are in place
        while count != 4:
            for face in self.faces:
                # skips the top face because these are already in place and do not need to be moved
                if face == self.top:
                    continue
                elif face.checkEdges('W'):
                    # saves the location when it finds a white edge piece to move
                    location = face.checkEdges('W')
                    # determines which face the white edge piece is located on and depending on the location on the face, performs the correct moves
                    if (face == self.bottom):
                        if location == 4:
                            # checks if there is a white piece already in place where trying to put the new piece and moves it out of the way
                            while (self.top.getColour(4) == 'W'):
                                self.topCW()
                            self.leftCW()
                            self.leftCW()
                            count += 1
                            break
                        elif location == 2:
                            while (self.top.getColour(8) == 'W'):
                                self.topCW()
                            self.frontCW()
                            self.frontCW()
                            count += 1
                            break
                        elif location == 6:
                            while (self.top.getColour(6) == 'W'):
                                self.topCW()
                            self.rightCW()
                            self.rightCW()
                            count += 1
                            break
                        elif location == 8:
                            while (self.top.getColour(2) == 'W'):
                                self.topCW()
                            self.frontCW()
                            self.frontCW()
                            count += 1
                            break
                    elif (face == self.front):
                        if location == 2:
                            self.frontCW()
                            while (self.top.getColour(6) == 'W'):
                                self.topCW()
                            self.rightCW()
                            # self.frontCCW() taking out because of mistake, delete later
                            count += 1
                            break
                        elif location == 4:
                            while (self.top.getColour(4) == 'W'):
                                self.topCW()
                            self.leftCCW()
                            count += 1
                            break
                        elif location == 6:
                            while (self.top.getColour(6) == 'W'):
                                self.topCW()
                            self.rightCW()
                            count += 1
                            break
                        elif location == 8:
                            while (self.top.getColour(6) == 'W'):
                                self.topCW()
                            self.frontCCW()
                            self.rightCW()
                            self.frontCW()
                            count += 1
                            break
                    elif (face == self.back):
                        if location == 2:
                            self.backCW() # this comes first here otherwise it moves the piece along with the top
                            while (self.top.getColour(4) == 'W'):
                                self.topCW()
                            self.leftCW()
                            # self.backCCW() taking out because of mistake, delete later
                            count += 1
                            break
                        elif location == 4:
                            while (self.top.getColour(6) == 'W'):
                                self.topCW()
                            self.rightCCW()
                            count += 1
                            break
                        elif location == 6:
                            while (self.top.getColour(4) == 'W'):
                                self.topCW()
                            self.leftCW()
                            count += 1
                            break
                        elif location == 8:
                            while (self.top.getColour(4) == 'W'):
                                self.topCW()
                            self.backCCW()
                            self.leftCW()
                            self.backCW()
                            count += 1
                            break
                    elif (face == self.left):
                        if location == 2:
                            self.leftCW()
                            while (self.top.getColour(8) == 'W'):
                                self.topCW()
                            self.frontCW()
                            # self.leftCCW() taking out because of mistake, delete later
                            count += 1
                            break
                        elif location == 4:
                            while (self.top.getColour(2) == 'W'):
                                self.topCW()
                            self.backCCW()
                            count += 1
                            break
                        elif location == 6:
                            while (self.top.getColour(8) == 'W'):
                                self.topCW()
                            self.frontCW()
                            count += 1
                            break
                        elif location == 8:
                            while (self.top.getColour(8) == 'W'):
                                self.topCW()
                            self.leftCCW()
                            self.frontCW()
                            self.leftCW()
                            count += 1
                            break
                    elif (face == self.right):
                        if location == 2:
                            self.rightCW()
                            while (self.top.getColour(2) == 'W'):
                                self.topCW()
                            self.backCW()
                            # self.rightCCW() taking out because of mistake, delete later
                            count += 1
                            break
                        elif location == 4:
                            while (self.top.getColour(8) == 'W'):
                                self.topCW()
                            self.frontCCW()
                            count += 1
                            break
                        elif location == 6:
                            while (self.top.getColour(2) == 'W'):
                                self.topCW()
                            self.backCW()
                            count += 1
                            break
                        elif location == 8:
                            while (self.top.getColour(2) == 'W'):
                                self.topCW()
                            self.rightCCW()
                            self.backCW()
                            self.rightCW()
                            count += 1
                            break
    
    # Step 2) takes the white daisy and moves those pieces to bottom and makes a cross
    def make_the_cross(self):
        print("Step #2: Making the Cross")
        times = 0
        edges = [2,4,6,8]   # locations of edge pieces
        faces = [self.back,self.right,self.front,self.left]
        faces2 = [self.back,self.right,self.front,self.left]
        # dictionary relating the colour with the corresponding face to rotate
        face_colours = dict([
            ('W',self.bottomCW),
            ('R',self.topCW),
            ('O',self.frontCW),
            ('B',self.backCW),
            ('Y',self.leftCW),
            ('G',self.rightCW)
        ])
        # for each edge, matches the other side of the square to the corresponding middle colour on the face
        for edge in range(4):
            j = 0 + times
            count = 0
            square_colour = faces[edge].getColour(2)
            while square_colour != faces2[j].getColour(5):
                self.topCW()
                j += 1
                count += 1
            face_colours[square_colour]()
            face_colours[square_colour]()
            for num in range(count):
                self.topCCW()
            faces2.append(faces2[times])
            times += 1
        # for square 2,4,6,8 match the other edge colour to the middle
        # create a dictionary for the colours
        # rotate the face twice clockwise to get it into position
    
    # Step 3: solving the bottom layer
    def solve_bottom_layer(self):
        print("Step #3: Solving the Bottom Face")

        count = 0 # to use as counter for corner pieces in place

        toLeft = dict([
            ('O', self.left.getColour),
            ('B', self.right.getColour),
            ('Y', self.back.getColour),
            ('G', self.front.getColour),
        ])

        toRight = dict([
            ('O', self.right.getColour),
            ('B', self.left.getColour),
            ('Y', self.front.getColour),
            ('G', self.back.getColour),
        ])

        # location_piece_7 = dict([
        #     ('O', 9),
        #     ('B', 1),
        #     ('Y', 7),
        #     ('G', 3)
        # ])

        # location_piece_9 = dict([
        #     ('O', 7),
        #     ('B', 3),
        #     ('Y', 1),
        #     ('G', 9)
        # ])

        # define list of the faces 3,4,5,6 and check the top two corner pieces for white (loop until the end or a white is found)
        faces = [self.front,self.right,self.back,self.left] # list of faces to check
        pieces_to_check = [1,3]
        while count != 1:
            to_break = False
            found_piece = False
            for face in faces:
                if to_break:
                    break # breaks out of second for loop if to_break is set to true
                for piece in pieces_to_check:
                    if face.getColour(piece) == 'W':
                        found_piece = True
                        if piece == 1:
                            print("Colour to match: ", toLeft[face.getColour(5)](3)) # if the white piece is in spot 1, checks the piece on the opposite side (face to the left) and returns the colour
                            colour = toLeft[face.getColour(5)](3)
                            middle = toLeft[face.getColour(5)](5)
                            # while colour doesn't match the center piece, turn top face clockwise
                            while middle != colour: #while the colour doesn't match the middle, keep turning top face clockwise
                                self.topCW()
                                middle = toLeft[middle](5)
                            self.rightTrigger(colour)
                            print("Completed Right Trigger")
                        elif piece == 3:
                            print("Colour to match: ", toRight[face.getColour(5)](1))
                            colour = toRight[face.getColour(5)](1)
                            middle = toRight[face.getColour(5)](5)
                            # while colour doesn't match the center piece, turn top face clockwise
                            while middle != colour: #while the colour doesn't match the middle, keep turning top face clockwise
                                self.topCW()
                                middle = toLeft[middle](5)
                            self.leftTrigger(colour)
                            print("Completed Left Trigger")
                        else:
                            print("Error")
                        to_break = True
                        count += 1
                        break # breaks out of first for loop if it finds a white piece
            if found_piece == False: # No more white pieces in the top row, check for white pieces on the bottom row
                print("Checking bottom row")
                check_top = False
                pieces_to_check = [7,9]
                for face in faces:
                    if check_top:
                        break
                    for piece in pieces_to_check:
                        if check_top:
                            break
                        print(piece)
                        if face.getColour(piece) == 'W':
                            check_top = True
                            if piece == 7:
                                # perform left trigger to put piece on top
                                self.leftTrigger(face.getColour(5))
                                count += 1
                            elif piece == 9:
                                # perform right trigger to put piece on top
                                self.rightTrigger(face.getColour(5))
                                count += 1
                            else:
                                print("Error")
                # code to check top
                print("Checking top row")
                corners = [1,3,7,9]
                bottom_corners = dict([ #corresponding bottom piece
                    (1,7),
                    (3,9),
                    (7,1),
                    (9,3)
                ])

                for corner in corners:
                    if self.top.getColour(corner) == 'W':
                        if self.bottom.getColour(bottom_corners[corner]) == 'W':
                            self.topCW()
                        else:
                            print("IDK")
                break

# Working Here
# Just finished moving bottom row pieces to the top face
# Next Steps: move the white corner pieces on the top face to the top row and cycle through the previous code to move them to the bottom face

    class Face:
        def __init__(self,pieces):
            self.pieces = [ [pieces[i][j] for j in range(3)] for i in range(3) ]

        def resetCW(self):
            temp = self.pieces[0].copy()
            self.pieces[0][0] = self.pieces[2][0]
            self.pieces[0][1] = self.pieces[1][0]
            self.pieces[0][2] = temp[0]
            self.pieces[1][0] = self.pieces[2][1]
            self.pieces[2][0] = self.pieces[2][2]
            self.pieces[2][1] = self.pieces[1][2]
            self.pieces[2][2] = temp[2]
            self.pieces[1][2] = temp[1]

        def resetCCW(self):
            temp = self.pieces[0].copy()
            self.pieces[0][0] = temp[2]
            self.pieces[0][1] = self.pieces[1][2]
            self.pieces[0][2] = self.pieces[2][2] 
            self.pieces[1][2] = self.pieces[2][1]
            self.pieces[2][2] = self.pieces[2][0]
            self.pieces[2][1] = self.pieces[1][0]
            self.pieces[2][0] = temp[0]
            self.pieces[1][0] = temp[1]

        def checkEdges(self, colour):
            if self.pieces[0][1] == colour:
                return 2
            elif self.pieces[1][0] == colour:
                return 4
            elif self.pieces[1][2] == colour:
                return 6
            elif self.pieces[2][1] == colour:
                return 8
            else:
                return 0

        def printFace(self):
            print(self.pieces[0])
            print(self.pieces[1])
            print(self.pieces[2])

        # returns the colour at a specified location (1-9)
        def getColour(self, square):
            colours = dict([
                (1,self.pieces[0][0]),
                (2,self.pieces[0][1]),
                (3,self.pieces[0][2]),
                (4,self.pieces[1][0]),
                (5,self.pieces[1][1]),
                (6,self.pieces[1][2]),
                (7,self.pieces[2][0]),
                (8,self.pieces[2][1]),
                (9,self.pieces[2][2]),
                ])
            return colours[square]

# topFace = [['G', 'Y', 'W'], ['B', 'R', 'W'], ['Y', 'G', 'R']]
# bottomFace = [['Y', 'O', 'B'], ['Y', 'W', 'Y'], ['B', 'G', 'W']]
# frontFace = [['O', 'R', 'Y'], ['R', 'O', 'B'], ['R', 'G', 'W']]
# backFace = [['B', 'R', 'R'], ['W', 'B', 'W'], ['G', 'W', 'G']]
# rightFace = [['O', 'O', 'Y'], ['R', 'G', 'B'], ['G', 'B', 'O']]
# leftFace = [['O', 'G', 'W'], ['Y', 'Y', 'O'], ['R', 'O', 'B']]

bottomFace = [['G', 'O', 'O'], ['W', 'W', 'O'], ['R', 'G', 'G']]
topFace = [['Y', 'O', 'O'], ['O', 'R', 'R'], ['W', 'Y', 'R']]
frontFace = [['O', 'W', 'Y'], ['R', 'O', 'B'], ['W', 'Y', 'R']]
backFace = [['W', 'G', 'B'], ['R', 'B', 'B'], ['B', 'W', 'Y']]
leftFace = [['W', 'R', 'G'], ['Y', 'Y', 'Y'], ['B', 'B', 'B']]
rightFace = [['O', 'B', 'Y'], ['G', 'G', 'G'], ['G', 'W', 'R']]

rubriksCube = Cube(topFace, bottomFace, frontFace, backFace, rightFace, leftFace)

rubriksCube.make_the_daisy()
rubriksCube.make_the_cross()
rubriksCube.solve_bottom_layer()
rubriksCube.printCube()