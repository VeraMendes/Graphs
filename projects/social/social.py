import random

# use for BFS
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use add_user num_users time

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f'User {i}')

        # generate all friendship combinations
        possible_friendships = []

        # avoid dupes by making sure first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle all possible friendships
        random.shuffle(possible_friendships)

        # create for first x pairs - x is total //2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        ''' Hint 1: To create N random friendships,
        you could create a list with all possible
        friendship combinations, shuffle the list,
        then grab the first N elements from the list.
        You will need to `import random` to get shuffle.
        Hint 2: `add_friendship(1, 2)` is the same as
        `add_friendship(2, 1)`. You should avoid calling one
        after the other since it will do nothing but print a warning.
        You can avoid this by only creating friendships where user1 < user2.'''

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # implement BFS 
        # create a queue
        q = Queue()
        # enqueue user id on the queue
        q.enqueue([user_id])
        # create the dict of traversed vertices
        visited = {}
        # while queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            path = q.dequeue()

            # last friend on path is the new key
            new_key = path[-1]
            # if not in dict visited
            if not visited.get(new_key, None):
                # DO THE THING!!!
                # add key with respective shortest path in dict
                visited[new_key] = path
                

                # enqueue all friends of previous friend
                for next_friend in self.friendships[new_key]:
                    new_path = list(path)
                    new_path.append(next_friend)
                    q.enqueue(new_path)
                 


        return visited
    
    '''* Hint 1: What kind of graph search guarantees you a shortest path?
    * Hint 2: Instead of using a `set` to mark users as visited, you could use
    a `dictionary`. Similar to sets, checking if something is in a dictionary
    runs in O(1) time. If the visited user is the key, what would the value be?'''

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
