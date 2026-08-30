class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        height_index_stack = []
        result = []

        for i in range(len(heights)):

            # Current bar is smaller → close taller rectangles
            while height_index_stack and heights[height_index_stack[-1]] > heights[i]:

                popped_index = height_index_stack.pop()

                if height_index_stack:
                    left_boundary = height_index_stack[-1]
                else:
                    left_boundary = -1

                right_boundary = i

                width = right_boundary - left_boundary - 1
                area = heights[popped_index] * width

                result.append(area)

            # Current bar can potentially extend to the right
            height_index_stack.append(i)

        # Process rectangles that extend to the end
        while height_index_stack:

            popped_index = height_index_stack.pop()

            if height_index_stack:
                left_boundary = height_index_stack[-1]
            else:
                left_boundary = -1

            right_boundary = len(heights)

            width = right_boundary - left_boundary - 1
            area = heights[popped_index] * width

            result.append(area)

        return max(result)