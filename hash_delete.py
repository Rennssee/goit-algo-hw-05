class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][i]
                    return True
        return False


# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)


while True:
    user_input = input("Введіть ключ для видалення (або 'exit' для виходу): ")

    if user_input.lower() == "exit":
        break

    result = H.delete(user_input)

    if result:
        print(f"Запис з ключем '{user_input}' видалено успішно.")
    else:
        print(f"Запис з ключем '{user_input}' не знайдено.")

print(H.get("apple"))  # Виведе: None, оскільки "apple" було видалено
print(H.get("orange"))  # Виведе: None, оскільки "orange" було видалено
print(H.get("banana"))  # Виведе: None, оскільки "banana" було видалено
