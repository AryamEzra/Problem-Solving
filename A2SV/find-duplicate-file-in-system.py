class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        track = defaultdict(list)

        for path in paths:
            path = path.split(" ")
            folder = path[0]

            for string in path[1:]:
                string = string.split(".txt")
                name = string[0]
                content = string[1]

                track[content].append((folder, name))

        output = []
        for key, val in track.items():
            if len(val) > 1:
                tmp = []
                for path, name in val:
                    tmp.append(path + "/" + name + ".txt")
                output.append(tmp)
        return output
        