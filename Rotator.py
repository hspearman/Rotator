__author__ = 'Hannah'
from enum import Enum
import copy

# Used to signal whether we want to rotate the array clockwise or counter-clockwise
class Direction(Enum):
	CLOCKWISE = 0
	COUNTER_CLOCKWISE = 1


# Returns a 90 degree rotated version of an array
def rotate_array(array, direction):
	# Create a new array that will be rotated
	rotated_array = copy.deepcopy(array)

	columns = len(array)
	# Iterate through each cell in the 2d array and insert it into the rotated array
	for column in range(0, columns):
		# Keeps track of the size of each sub-array; Used to error-check for asymmetric arrays (ex.3x4)
		max_row = 0

		# The max index of the array (ex. 1 would be the max index of a 2x2 array)
		max_array_index = len(array) - 1

		# Get the length of this sub-array
		rows = len(array[column])

		# Used to error-check for asymmetrical arrays
		max_row_index = rows - 1

		# Make sure this sub-array is not too big
		not_too_many_rows = not (max_row_index > max_array_index)
		assert not_too_many_rows, "There are too many rows! The array must be symmetrical. (ex. 5x5)"

		# Make sure this sub-array is not too small
		not_too_few_rows = not (max_row_index < max_array_index)
		assert not_too_few_rows, "There are too few rows! The array must be symmetrical. (ex. 5x5)"

		for row in range(0, rows):
			current_element = array[column][row]

			# Calculate the new rotate position of this element (depends if we're rotating clockwise or counter-clockwise
			new_column = -1
			new_row = -1
			if direction == Direction.CLOCKWISE:
				new_column = row
				new_row = max_array_index - column
			else:
				new_column = max_array_index - row
				new_row = column

			# Sanity check. Make sure the new row and column were calculated successfully
			successfully_calculated = (new_column != -1) and (new_row != -1)
			assert successfully_calculated, "Failed to calculate the new rotated position for a cell."

			rotated_array[new_column][new_row] = current_element

	return rotated_array


def print_array(array):
	columns = len(array)
	rows = len(array[0])

	output = ''
	max_array_index = len(array) - 1

	for column in range(0, columns):
		for row in range(0, rows):
			assert row <= columns, "The array must be symmetrical! (ex. 5x5)"

			current_element = array[column][row]
			output += "[{}]".format(current_element)

			# If we've reached the end of a row, start a new line for the next row
			if row == max_array_index:
				output += "\n"

	print(output)

column_one = [1, 2, 3]
column_two = [4, 5, 6]
column_three = [7, 8, 9]

array_dimension = len(column_one)

array = [column_one, column_two, column_three]
print("Array: \n")
print_array(array)

array_clockwise_0 = rotate_array(array, Direction.CLOCKWISE)
print("Array rotated clockwise: \n")
print_array(array_clockwise_0)

array_clockwise_1 = rotate_array(array_clockwise_0, Direction.CLOCKWISE)
print("Array rotated clockwise again: \n")
print_array(array_clockwise_1)

array_counter_clockwise_0 = rotate_array(array, Direction.COUNTER_CLOCKWISE)
print("Array rotated counter-clockwise: \n")
print_array(array_counter_clockwise_0)

array_counter_clockwise_1 = rotate_array(array_counter_clockwise_0, Direction.COUNTER_CLOCKWISE)
print("Array rotated counter-clockwise again: \n")
print_array(array_counter_clockwise_1)











