import enum


class OrderStatus(enum.Enum):
    ACCEPTED = 1
    EXECUTED = 2
    OVERDUE = 3
