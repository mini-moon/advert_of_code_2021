import logging


class Datapoint:
    def __init__(self, row, col):
        self.row = int(row)
        self.col = int(col)

    def value(self, data_frame):
        return int(data_frame.iat[self.row, self.col])

    def up(self, data_frame):
        try:
            if not self.row - 1 < 0:
                return int(data_frame.iat[self.row - 1, self.col])
        except Exception as e:
            pass

    def down(self, data_frame):
        try:
            return int(data_frame.iat[self.row + 1, self.col])
        except Exception as e:
            pass

    def before(self, data_frame):
        try:
            if not self.col - 1 < 0:
                return int(data_frame.iat[self.row, self.col - 1])
        except Exception as e:
            pass

    def after(self, data_frame):
        try:
            return int(data_frame.iat[self.row, self.col + 1])
        except Exception as e:
            pass

    def neighbors(self, data_frame):
        all = {"up": self.up(data_frame), "down": self.down(data_frame), "before": self.before(data_frame),
                    "after": self.after(data_frame)}
        return [int(v) for v in all.values() if v is not None]
