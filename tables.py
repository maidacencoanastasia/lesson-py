from prettytable import PrettyTable
import emoji

x = PrettyTable()
x.field_names = ["Country", "Capital", "is_russia"]
x.add_row(["Russia :blush:", "Moscow", True])
x.add_rows([["Argentina", "Buenos Aires", False], ["Jamaica", "Kingston", False]])
x.add_column("Starts with A", [False, True, False])

print(x)