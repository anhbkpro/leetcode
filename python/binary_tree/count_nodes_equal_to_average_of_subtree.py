class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def averageOfSubtree(self, root: 'TreeNode') -> int:
        self.count = 0  # Khởi tạo lại biến đếm
        self.postOrder(root)
        return self.count

    def postOrder(self, root: 'TreeNode') -> tuple[int, int]:
        if root is None:
            return (0, 0)

        # Duyệt cây theo thứ tự sau (Post-order): Trái -> Phải -> Gốc
        left_sum, left_count = self.postOrder(root.left)
        right_sum, right_count = self.postOrder(root.right)

        # Tính tổng giá trị và số lượng nút của cây con hiện tại
        node_sum = left_sum + right_sum + root.val
        node_count = left_count + right_count + 1

        # Kiểm tra nếu giá trị nút gốc bằng trung bình cộng của cây con
        # Sử dụng // để chia lấy phần nguyên giống C++
        if root.val == node_sum // node_count:
            self.count += 1

        # Trả về (tổng_giá_trị, số_lượng_nút)
        return (node_sum, node_count)
