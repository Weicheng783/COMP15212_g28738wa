from memory import Memory

# Your implementations of the classes below should not include any additional print statements. 


class CyclicCache(Memory):
    def name(self):
        return "Cyclic"

    # Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with a cache size of 4. You can
    # use additional methods and variables as you see fit as long as you
    # provide a suitable overridding of the lookup method.

    def __init__(self):
        super().__init__()


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
        self.cache_area_2 = None
        self.cache_area_2_at = None
        self.cache_area_3 = None
        self.cache_area_3_at = None
        self.cache_area_4 = None
        self.cache_area_4_at = None

        super().__init__()
#        location = sys.stdin.readline().strip()
#        print(super().lookup(self))

    def lookup(self, address):


        if(self.cache_area_1!=None and self.cache_area_2!=None and self.cache_area_3!=None and self.cache_area_4!=None):
#            print(self.cache_area_1_at, self.cache_area_2_at, self.cache_area_3_at, self.cache_area_4_at)
        elif (self.cache_area_1 == None):
            self.cache_area_1 = super().lookup(address)
            self.cache_area_1_at = super().get_hit_count()
            return self.cache_area_1

        elif(self.cache_area_2 == None):
            self.cache_area_2 = super().lookup(address)
            self.cache_area_2_at = super().get_hit_count()
            return self.cache_area_2
        elif(self.cache_area_3 == None):
            self.cache_area_3 = super().lookup(address)
            self.cache_area_3_at = super().get_hit_count()
            return self.cache_area_3
        elif(self.cache_area_4 == None):
            self.cache_area_4 = super().lookup(address)
            self.cache_area_4_at = super().get_hit_count()
            return self.cache_area_4
