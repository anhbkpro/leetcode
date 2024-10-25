class SolutionSet:
    def removeSubfolders(self, folder) -> list[str]:
        # Create a set to store all folder paths for fast lookup
        folder_set = set(folder)
        result = []

        # Iterate through each folder to check if it's a sub-folder
        for f in folder:
            is_sub_folder = False
            prefix = f

            # Check all prefixes of the current folder path
            while not prefix == "":
                pos = prefix.rfind("/")
                if pos == -1:
                    break

                # Reduce the prefix to its parent folder
                prefix = prefix[0:pos]

                # If the parent folder exists in the set, mark as sub-folder
                if prefix in folder_set:
                    is_sub_folder = True
                    break

            # If not a sub-folder, add it to the result
            if not is_sub_folder:
                result.append(f)
        return result


class SolutionSort:
    def removeSubfolders(self, folder):
        # Sort the folders alphabetically
        folder.sort()

        # Initialize the result list and add the first folder
        result = [folder[0]]

        # Iterate through each folder and check if it's a sub-folder of the last added folder in the result
        for i in range(1, len(folder)):
            last_folder = result[-1]
            last_folder += "/"

            # Check if the current folder starts with the last added folder path
            if not folder[i].startswith(last_folder):
                result.append(folder[i])

        # Return the result containing only non-sub-folders
        return result
