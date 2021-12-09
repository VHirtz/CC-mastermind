class turtle():
    @staticmethod
    def craft(quantity: int=1):
        """
        Craft items using ingredients anywhere in the turtle's inventory
        and place results in the active slot.
        If a quantity is specified,
        it will craft only up to that many items,
        otherwise, it will craft as many of the items as possible.
        """
        return f"turtle.craft({quantity})"
    @staticmethod
    def forward():
        """
        Try to move the turtle forward
        """
        return "turtle.forward()"
    @staticmethod
    def back():
        """
        Try to move the turtle back
        """
        return "turtle.back()"
    @staticmethod
    def up():
        """
        Try to move the turtle up
        """
        return "turtle.up()"
    @staticmethod
    def down():
        """
        Try to move the turtle down
        """
        return "turtle.down()"
    @staticmethod
    def turnLeft():
        """
        Turn the turtle Left
        """
        return "turtle.turnLeft()"
    @staticmethod
    def turnRight():
        """
        Turn the turtle Right
        """
        return "turtle.turnRight()"
    @staticmethod
    def select(slotNum: int):
        """
        Make the turtle select slot slotNum
        (1 is top left, 16 (9 in 1.33 and earlier) is bottom right)
        """
        return f"turtle.select({slotNum})"
    @staticmethod
    def getSelectedSlot():
        """
        Indicates the currently selected inventory slot
        """
        return "turtle.getSelectedSlot()"
    @staticmethod
    def getItemCount(slotNum: int=0):
        """
        Counts how many items are in the currently selected slot or,
        if specified, slotNum slot
        """
        return f"turtle.getItemCount({slotNum if slotNum else ''})"
    @staticmethod
    def getItemSpace(slotNum: int=0):
        """
        Counts how many remaining items you need to fill the stack
        in the currently selected slot or, if specified, slotNum slot
        """
        return f"turtle.getItemSpace({slotNum if slotNum else ''})"
    @staticmethod
    def getItemDetail(slotNum: int=0):
        """
        Returns the ID string,
        count and damage values of currently selected slot or,
        if specified, slotNum slot
        """
        return f"turtle.getItemDetail({slotNum if slotNum else ''})"
    @staticmethod
    def equipLeft():
        """
        Attempts to equip an item in the current slot to the turtle's left side,
        switching the previously equipped item back into the inventory
        """
        return "turtle.equipLeft()"
    @staticmethod
    def equipRight():
        """
        Attempts to equip an item in the current slot to the turtle's right side,
        switching the previously equipped item back into the inventory
        """
        return "turtle.equipRight()"
    @staticmethod
    def attack():
        """
        Attacks in front of the turtle.
        """
        return "turtle.attack()"
    @staticmethod
    def attackUp():
        """
        Attacks above the turtle.
        """
        return "turtle.attackUp()"
    @staticmethod
    def attackDown():
        """
        Attacks under the turtle.
        """
        return "turtle.attackDown()"
    @staticmethod
    def dig():
        """
        Breaks the block in front. With hoe: tills the dirt in front of it.
        """
        return "turtle.dig()"
    @staticmethod
    def digUp():
        """
        Breaks the block above.
        """
        return "turtle.digUp()"
    @staticmethod
    def digDown():
        """
        Breaks the block below. With hoe: tills the dirt beneath the space below it.
        """
        return "turtle.digDown()"
    @staticmethod
    def place(signText: str=''):
        """
        Places a block of the selected slot in front.
        Engrave signText on signs if provided.
        Collects water or lava if the currently selected slot is an empty bucket.
        """
        return "turtle.place({('\"'+ signText +'\"') if signText else ''})"
    @staticmethod
    def placeUp():
        """
        Places a block of the selected slot above.
        Collects water or lava if the currently selected slot is an empty bucket.
        """
        return "turtle.placeUp()"
    @staticmethod
    def placeDown():
        """
        Places a block of the selected slot below.
        Collects water or lava if the currently selected slot is an empty bucket.
        """
        return "turtle.placeDown()"
    @staticmethod
    def detect():
        """
        Detects if there is a block in front. Does not detect mobs.
        """
        return "turtle.detect()"
    @staticmethod
    def detectUp():
        """
        Detects if there is a block above
        """
        return "turtle.detectUp()"
    @staticmethod
    def detectDown():
        """
        Detects if there is a block below
        """
        return "turtle.detectDown()"
    @staticmethod
    def inspect():
        """
        Returns the ID string and metadata of the block in front of the Turtle
        """
        return "turtle.inspect()"
    @staticmethod
    def inspectUp():
        """
        Returns the ID string and metadata of the block above the Turtle
        """
        return "turtle.inspectUp()"
    @staticmethod
    def inspectDown():
        """
        Returns the ID string and metadata of the block below the Turtle
        """
        return "turtle.inspectDown()"

    @staticmethod
    def compare():
        """
        Detects if the block in front is the same as the one in the currently selected slot
        """
        return "turtle.compare()"
    @staticmethod
    def compareUp():
        """
        Detects if the block above is the same as the one in the currently selected slot
        """
        return "turtle.compareUp()"
    @staticmethod
    def compareDown():
        """
        Detects if the block below is the same as the one in the currently selected slot
        """
        return "turtle.compareDown()"
    @staticmethod
    def compareTo(slot: int):
        """
        Compare the current selected slot and the given slot to see if the items are the same.
        Returns true if they are the same, false if not.
        """
        return f"turtle.compareTo({slot})"
    @staticmethod
    def drop(count: int):
        """
        Drops all items in the selected slot,
        or specified, drops count items.
        [>= 1.4 only:] If there is a inventory on the side (i.e above the turtle) it will try to place into the inventory, returning false if the inventory is full.
        """
        return f"turtle.drop({count if count else ''})"
    @staticmethod
    def dropUp(count: int):
        """
        Drops all items in the selected slot,
        or specified, drops count items.
        [>= 1.4 only:] If there is a inventory on the side (i.e above the turtle) it will try to place into the inventory, returning false if the inventory is full.
        """
        return f"turtle.dropUp({count if count else ''})"
    @staticmethod
    def dropDown(count: int):
        """
        Drops all items in the selected slot,
        or specified, drops count items.
        [>= 1.4 only:] If there is a inventory on the side (i.e above the turtle) it will try to place into the inventory, returning false if the inventory is full.
        If above a furnace, will place item in the top slot.
        """
        return f"turtle.dropDown({count if count else ''})"
    @staticmethod
    def suck(amount: int=0):
        """
        Picks up an item stack of any number,
        from the ground or an inventory in front of the turtle,
        then places it in the selected slot.
        If the turtle can't pick up the item, the function returns false.
        amount parameter requires ComputerCraft 1.6 or later.
        """
        return f"turtle.suck({amount if amount else ''})"
    @staticmethod
    def suckUp(amount: int=0):
        """
        Picks up an item stack of any number,
        from the ground or an inventory above the turtle,
        then places it in the selected slot.
        If the turtle can't pick up the item, the function returns false.
        amount parameter requires ComputerCraft 1.6 or later.
        """
        return f"turtle.suckUp({amount if amount else ''})"
    @staticmethod
    def suckDown(amount: int=0):
        """
        Picks up an item stack of any number,
        from the ground or an inventory below the turtle,
        then places it in the selected slot.
        If the turtle can't pick up the item, the function returns false.
        amount parameter requires ComputerCraft 1.6 or later.
        """
        return f"turtle.suckDown({amount if amount else ''})"
    @staticmethod
    def refuel(quantity: int=0):
        """
        If the current selected slot contains a fuel item,
        it will consume it to give the turtle the ability to move.
        Added in 1.4 and is only needed in needfuel mode.
        If the current slot doesn't contain a fuel item,
        it returns false.
        Fuel values for different items can be found at
        Turtle.refuel#Fuel_Values. (https://www.computercraft.info/wiki/Turtle.refuel#Fuel_Values)
        If a quantity is specified,
        it will refuel only up to that many items,
        otherwise, it will consume all the items in the slot.
        """
        return f"turtle.refuel({quantity if quantity else ''})"
    @staticmethod
    def getFuelLevel():
        """
        Returns the current fuel level of the turtle,
        this is the number of blocks the turtle can move.
        If turtleNeedFuel = 0 then it returns "unlimited".
        """
        return "turtle.getFuelLevel()"
    @staticmethod
    def getFuelLimit():
        """
        Returns the maximum amount of fuel a turtle can store
        - by default, 20,000 for regular turtles, 100,000 for advanced.
        If turtleNeedFuel = 0 then it returns "unlimited".
        """
        return "turtle.getFuelLimit()"
    @staticmethod
    def transferTo(slot: int, quantity: int=0):
        """
        Transfers quantity items from the selected slot to slot.
        If quantity isn't specified,
        will attempt to transfer everything in the selected slot to slot.
        """
        return f"turtle.transferTo({slot}{(',' + str(quantity)) if quantity else ''})"

def Print(msg):
    return 'print("{msg}")'.format(msg = msg)