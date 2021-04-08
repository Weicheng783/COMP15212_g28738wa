from memory import Memory

# Your implementations of the classes below
# should not include any additional print statements.


class CyclicCache(Memory):
    def name(self):
        return "Cyclic"

    # Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with a cache size of 4. You can
    # use additional methods and variables as you see fit as long as you
    # provide a suitable overridding of the lookup method.

    def __init__(self):
        self.cache_area_1 = None
        self.cache_area_2 = None
        self.cache_area_3 = None
        self.cache_area_4 = None
        self.cache_area_1_addr = None
        self.cache_area_2_addr = None
        self.cache_area_3_addr = None
        self.cache_area_4_addr = None
        self.next = 1

        super().__init__()

    def lookup(self, address):

        if(self.cache_area_1 == address):

            return "Memory Access "+self.cache_area_1_addr

        elif (self.cache_area_2 == address):

            return "Memory Access "+self.cache_area_2_addr

        elif(self.cache_area_3 == address):

            return "Memory Access "+self.cache_area_3_addr

        elif(self.cache_area_4 == address):

            return "Memory Access "+self.cache_area_4_addr

        else:
            if self.next == 1:
                self.cache_area_1 = address
                self.next = 2
                self.cache_area_1_addr = super().lookup(address)
                return self.cache_area_1_addr

            elif self.next == 2:
                self.cache_area_2 = address
                self.next = 3
                self.cache_area_2_addr = super().lookup(address)
                return self.cache_area_2_addr

            elif self.next == 3:
                self.cache_area_3 = address
                self.next = 4
                self.cache_area_3_addr = super().lookup(address)
                return self.cache_area_3_addr

            elif self.next == 4:
                self.cache_area_4 = address
                self.next = 1
                self.cache_area_4_addr = super().lookup(address)
                return self.cache_area_4_addr


class LRUCache(Memory):

    def name(self):
        return "LRU"

    # Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with a cache size of
    # 4. You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.

    def __init__(self):
        self.cache_area_1 = None
        self.cache_area_1_at = None
        self.cache_area_1_addr = None
        self.cache_area_2 = None
        self.cache_area_2_at = None
        self.cache_area_2_addr = None
        self.cache_area_3 = None
        self.cache_area_3_at = None
        self.cache_area_3_addr = None
        self.cache_area_4 = None
        self.cache_area_4_at = None
        self.cache_area_4_addr = None
        self.time = 0

        super().__init__()

    def lookup(self, address):
        self.time += 1

        if(self.cache_area_1 == address):

            self.cache_area_1_at = self.time
            return "Memory Access "+self.cache_area_1_addr

        elif (self.cache_area_2 == address):

            self.cache_area_2_at = self.time
            return "Memory Access "+self.cache_area_2_addr

        elif(self.cache_area_3 == address):

            self.cache_area_3_at = self.time
            return "Memory Access "+self.cache_area_3_addr

        elif(self.cache_area_4 == address):

            self.cache_area_4_at = self.time
            return "Memory Access "+self.cache_area_4_addr

        else:
            if(self.cache_area_1 is not None
               and self.cache_area_2 is not None
               and self.cache_area_3 is not None
               and self.cache_area_4 is not None):
                list = [self.cache_area_1_at, self.cache_area_2_at,
                        self.cache_area_3_at, self.cache_area_4_at]

                for i in range(0, len(list)):
                    if list[i] == min(list):
                        minimal_index = i
                        break

                if minimal_index == 0:
                    self.cache_area_1 = address
                    self.cache_area_1_at = self.time
                    self.cache_area_1_addr = super().lookup(address)
                    return self.cache_area_1_addr
                elif minimal_index == 1:
                    self.cache_area_2 = address
                    self.cache_area_2_at = self.time
                    self.cache_area_2_addr = super().lookup(address)
                    return self.cache_area_2_addr
                elif minimal_index == 2:
                    self.cache_area_3 = address
                    self.cache_area_3_at = self.time
                    self.cache_area_3_addr = super().lookup(address)
                    return self.cache_area_3_addr
                elif minimal_index == 3:
                    self.cache_area_4 = address
                    self.cache_area_4_at = self.time
                    self.cache_area_4_addr = super().lookup(address)
                    return self.cache_area_4_addr

            elif (self.cache_area_1 is None):
                self.cache_area_1 = address
                self.cache_area_1_at = self.time
                self.cache_area_1_addr = super().lookup(address)
                return self.cache_area_1_addr
            elif (self.cache_area_2 is None):
                self.cache_area_2 = address
                self.cache_area_2_at = self.time
                self.cache_area_2_addr = super().lookup(address)
                return self.cache_area_2_addr
            elif (self.cache_area_3 is None):
                self.cache_area_3 = address
                self.cache_area_3_at = self.time
                self.cache_area_3_addr = super().lookup(address)
                return self.cache_area_3_addr
            elif (self.cache_area_4 is None):
                self.cache_area_4 = address
                self.cache_area_4_at = self.time
                self.cache_area_4_addr = super().lookup(address)
                return self.cache_area_4_addr
