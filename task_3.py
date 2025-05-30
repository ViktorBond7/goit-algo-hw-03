def hanoi(n: int):
    state = {
        'A': list(range(n, 0, -1)),  # Всі диски на стрижні A
        'B': [],
        'C': []
    }

    def move(n, source, target, auxiliary):
        if n == 1:
            disk = state[source].pop()
            
            state[target].append(disk)
            print(f"Перемістити диск з {source} на {target}: {disk}")
            print(f"Стан: {state}")
        else:
            move(n-1, source, auxiliary, target)
            move(1, source, target, auxiliary)
            move(n-1, auxiliary, target, source)

    print(f"Початковий стан: {state}")
    move(n, 'A', 'C', 'B')


if __name__ == "__main__":
    hanoi(3)