
# https://www.lintcode.com/problem/load-balancer/description?_from=ladder&&fromId=75
# https://www.jiuzhang.com/solution/load-balancer/
# pick(): 数组中随机选取一个元素可以直接使用随机函数得到一个 [0, 数组大小-1] 的整数即可.
# add(server_id): 在数组末尾添加这个server_id, 并在哈希表中添加 server_id -> 数组下标 的键值映射
# remove(server_id): 利用哈希表得到 server_id 的数组下标, 在数组中将它和最末尾的元素交换位置, 然后删除, 并将修改同步到哈希表
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.servers = []
        self.server2idx = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id):
        # write your code here
        if server_id in self.servers:
            return

        self.servers.append(server_id)
        self.server2idx[server_id] = len(self.servers) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id):
        # write your code here
        if server_id not in self.server2idx:
            return

        idx = self.server2idx.get(server_id)
        del self.server2idx[server_id]

        last_server = self.servers[-1]
        self.server2idx[last_server] = idx
        self.servers[idx] = last_server
        self.servers.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self):
        # write your code here
        from random import randint

        rand_server = randint(0, len(self.servers) - 1)

        return self.servers[rand_server]
