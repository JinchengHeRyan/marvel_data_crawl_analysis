from marvel.requester import Requester


class Base:
    def __init__(self, PUBLIC_KEY, PRIVATE_KEY, LIMIT):
        self.requester = Requester(PUBLIC_KEY, PRIVATE_KEY, LIMIT)
