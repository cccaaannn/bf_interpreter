class bf_interpreter():
    def __init__(self, wrapping = False):
        self.program_array = [0]
        self.cursor = 0
        self.program_steps = []
        self.step_index = 0

        self.wrapping = wrapping


    def __strip_code(self, steps):
        """splits bf program code into list elements and adds terminator character"""

        lines = steps.split("\n")
        lines = [line.split(";") for line in lines]
        striped_code = [line[0].strip() for line in lines]
        striped_code = list(filter(None, striped_code))

        stript_str = ""
        for c in striped_code:
            stript_str += c

        for step in stript_str:
            self.program_steps.append(step)

        if(self.program_steps[-1] != "#"):
            self.program_steps.append("#")

        print(self.program_steps)



    def __program_loop(self, loop_start_index):
        loop_counter_index = self.cursor
        
        # loop until loop counter ends
        while True:
            # if(self.program_array[loop_counter_index] == 0 and not loop_start_index == -1):
            #     return

            # set the loop at the begining of the '['
            self.step_index = loop_start_index + 1

            # loop until ']'
            while True:
                # terminate
                if(self.program_steps[self.step_index] == "#"):
                    break
                         
                # add 1 to current index
                if(self.program_steps[self.step_index] == "+"):
                    if(self.wrapping):
                        if(self.program_array[self.cursor] == 255):
                            self.program_array[self.cursor] = 0
                        else:
                            self.program_array[self.cursor] += 1
                    else:
                        self.program_array[self.cursor] += 1        
                
                # subtract 1 from the current index
                if(self.program_steps[self.step_index] == "-"):
                    if(self.wrapping):
                        if(self.program_array[self.cursor] == 0):
                            self.program_array[self.cursor] = 255
                        else:
                            self.program_array[self.cursor] -= 1
                    else:
                        self.program_array[self.cursor] -= 1

                # go right
                if(self.program_steps[self.step_index] == ">"):
                    if(self.cursor == len(self.program_array) - 1):
                        self.program_array.append(0)
                        self.cursor += 1
                    else:
                        self.cursor += 1

                # go left
                if(self.program_steps[self.step_index] == "<"):
                    if(self.cursor == 0):
                        self.program_array.insert(0,0)
                        loop_counter_index += 1
                    else:
                        self.cursor -= 1

                # starting of a loop recursive call
                if(self.program_steps[self.step_index] == "["):
                    
                    self.__program_loop(self.step_index)
                    
                    self.step_index += 1
                    continue
                
                # end of a loop
                if(self.program_steps[self.step_index] == "]"):
                    if(loop_start_index != -1):
                        break 
                
                # get input
                if(self.program_steps[self.step_index] == ","):
                    self.program_array[self.cursor] = int(input("input:"))

                # print output
                if(self.program_steps[self.step_index] == "."):
                    print(chr(self.program_array[self.cursor]), end="")

                # print(self.program_steps[self.step_index])
                # print(self.program_array)
                self.step_index += 1
                
            # if loop_start_index == -1 it is the starting of the program kind of like base case else it is a recursive call
            if(self.program_array[self.cursor] == 0 or loop_start_index == -1):
                return


    
    def print_program_array(self):
        print("")
        print(self.program_array)


    def interpret(self, bf_code):
        self.__strip_code(bf_code)
        self.__program_loop(-1)























