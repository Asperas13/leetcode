class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.children = {}


class File:
    def __init__(self, name, content=''):
        self.content = content
        self.name = name


class FileSystem:

    def __init__(self):
        self.path_trie = DirectoryNode("/")

    def ls(self, path: str) -> List[str]:
        path = path.split('/')
        path_trie = self.path_trie
        for part in path:
            if part and part in path_trie.children:
                path_trie = path_trie.children[part]

        if isinstance(path_trie, DirectoryNode):
            return sorted(path_trie.children.keys())
        elif isinstance(path_trie, File):
            return [path_trie.name]

    def mkdir(self, path: str) -> None:
        path_trie = self.path_trie
        path = path.split('/')
        for part in path:
            if part:
                if part not in path_trie.children:
                    path_trie.children[part] = DirectoryNode(part)
                path_trie = path_trie.children[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        *path_to_file, filename = filePath.split('/')
        path_trie = self.path_trie
        for part in path_to_file:
            if part and part in path_trie.children:
                path_trie = path_trie.children[part]

        _file = path_trie.children.get(filename)
        if isinstance(_file, File):
            _file.content += content
        else:
            path_trie.children[filename] = File(filename, content)

    def readContentFromFile(self, filePath: str) -> str:
        *path_to_file, filename = filePath.split('/')
        path_trie = self.path_trie
        for part in path_to_file:
            if part and part in path_trie.children:
                path_trie = path_trie.children[part]
        if isinstance(path_trie.children[filename], File):
            return path_trie.children[filename].content

        return ''

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)