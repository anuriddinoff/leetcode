class Solution(object):
    def convertDateToBinary(self, date):
        parts = date.split("-")
        year_str, month_str, day_str = parts[0], parts[1], parts[2]

        year = int(year_str)
        month = int(month_str)
        day = int(day_str)

        binary_year = bin(year)[2:]
        binary_month = bin(month)[2:]
        binary_day = bin(day)[2:]

        return "-".join([binary_year, binary_month, binary_day])
        