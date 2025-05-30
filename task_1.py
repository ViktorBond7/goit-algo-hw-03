from pathlib import Path
import shutil
import argparse

def copy_and_sort_recursive(src: Path, dest: Path = Path("dist")):
    if not src.exists():
        print(f"Директорія '{src}' не існує або не є папкою.")
        return
   
    dest.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        if item.is_file():
            ext = item.suffix.lower().lstrip('.') or 'no_extension'
            target_subdir = dest / ext
            target_subdir.mkdir(exist_ok=True)
            target_file = target_subdir / item.name

            if item.resolve() != target_file.resolve():
                shutil.copy2(item, target_file)
                print(f"Скопійовано: {item} → {target_file}")

        elif item.is_dir():
            # Рекурсивний виклик для підпапки
            copy_and_sort_recursive(item, dest)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Команда, наприклад: copy")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")

    args = parser.parse_args()
    print("args", args)

    if args.command.lower() == "copy":
        source_path = Path(args.source)
        dest_path = Path(args.destination)
        copy_and_sort_recursive(source_path, dest_path)
    else:
        print(f"Невідома команда: {args.command}")
 



