import math
import logging

logging.basicConfig(filename='line_comparison.log', filemode='a', level=logging.DEBUG)


class Line:
    def __init__(self, point_dict):

        self.x1 = point_dict.get('x1')
        self.x2 = point_dict.get('x2')
        self.y1 = point_dict.get('y1')
        self.y2 = point_dict.get('y2')

    def length_of_line(self):
        """
        Function to calculate the length of the line by taking user input
        """
        logging.debug("Program started running")
        try:
            length = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
            # print(length)
            return length
        except Exception as e:
            logging.warning("Recheck the code")
            logging.exception(e)


if __name__ == "__main__":
    x1 = int(input("Enter value for first point on X axis"))
    x2 = int(input("Enter value for second point on X axis"))
    y1 = int(input("Enter value for first point on Y axis"))
    y2 = int(input("Enter value for second point on Y axis"))
    l1 = Line({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})
    length1 = l1.length_of_line()
    print(length1)
    x1 = int(input("Enter value for first point on X axis : "))
    x2 = int(input("Enter value for second point on X axis : "))
    y1 = int(input("Enter value for first point on Y axis : "))
    y2 = int(input("Enter value for second point on Y axis : "))
    l2 = Line({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})
    length2 = l2.length_of_line()
    print(length2)
    l1.line_equality(l2)
