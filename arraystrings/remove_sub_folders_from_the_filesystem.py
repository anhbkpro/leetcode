from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)

        parent_set = set()
        sub_folders = set()
        for f in folder:
            splited_folders = f.split("/")
            for i in range(1, len(f)):
                prefix = "/".join(splited_folders[:i])
                if prefix in parent_set:
                    sub_folders.add(f)
                    break
            if f not in sub_folders:
                parent_set.add(f)

        return list(parent_set)
