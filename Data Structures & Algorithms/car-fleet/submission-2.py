class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a stack, hold (start position, speed to reach target)
        # Create a map for the postions->speed
        # Sort the position array
        # loop from the back
        # for each value in the position
        # calculate time for the current to reach end
        # if stack is empty:
        # add (position, time)
        # else: 
        # if the time for item on top of the stack takes <= we dont add (position, time)
        # else: we add positon time
        # return len(stack)

        stack = []
        sm = {}
        for i in range(len(speed)):
            sm[position[i]] = speed[i]
        # sm = {6:3, 8:2}

        position.sort()

        # [6, 8]
        # [1, ]


        for i in range(len(speed) - 1, -1, -1):
            pos = position[i]
            spe = sm[position[i]]
            time = (target - pos) / spe

            if not stack or stack[-1] < time:
                stack.append(time)


        return len(stack)

        

