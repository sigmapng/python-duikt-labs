class CollisionCheck():

    @staticmethod
    def x_axis(co1, co2):
        if (co2.x1 < co1.x1 < co2.x2) \
                or (co2.x1 < co1.x2 < co2.x2) \
                or (co1.x1 < co2.x1 < co1.x2) \
                or (co1.x1 < co2.x2 < co1.x2):
            return True
        else:
            return False

    @staticmethod
    def y_axis(co1, co2):
        if (co2.y1 < co1.y1 < co2.y2) \
                or (co2.y1 < co1.y2 < co2.y2) \
                or (co1.y1 < co2.y1 < co1.y2) \
                or (co1.y1 < co2.y2 < co1.y2):
            return True
        else:
            return False

    @staticmethod
    def left_side_collide(co1, co2):
        if CollisionCheck.y_axis(co1, co2):
            if co2.x2 >= co1.x1 >= co2.x1:
                return True
        return False

    @staticmethod
    def right_side_collide(co1, co2):
        if CollisionCheck.y_axis(co1, co2):
            if co2.x1 <= co1.x2 <= co2.x2:
                return True
        return False

    @staticmethod
    def top_part_collide(co1, co2):
        if CollisionCheck.x_axis(co1, co2):
            if co2.y2 >= co1.y1 >= co2.y1:
                return True
        return False

    @staticmethod
    def bottom_part_collide(y, co1, co2):
        if CollisionCheck.x_axis(co1, co2):
            y_calc = co1.y2 + y
            if y_calc >= co2.y1 >= co1.y2:
                return True
        return False
