class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        self.file = open(file=self.file_path)
        return self

    def __next__(self):
        data = self.file.read()
        if not data:
            self.file.close()
            raise StopIteration
        return data.strip()


if __name__ == '__main__':
    fruits = []
    for file in os.listdir("descriptions"):
        data = {}
        file_data = []
        for line in FileManager(f"descriptions/{file}"):
            file_data = line.split("\n")
            data["name"] = file_data[0]
            data["price"] = int(file_data[1].split()[0])
            data["description"] = file_data[2]
            fruits.append(data)
            with open(f"Response {file} 200.txt", "w") as f:
                f.write(f'name:{data['name']}\n price:{data["price"]}\n description:{data["description"]}')
