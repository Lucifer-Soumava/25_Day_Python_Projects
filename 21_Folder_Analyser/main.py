from tkinter import filedialog, Tk
from collections import Counter
import os
from dataclasses import dataclass

@dataclass
class Stats:
    folder : str
    num_files: int
    total_size_mb: float
    most_common_types: list[tuple[str, int]]

def select_folder() -> str | None:
    root: Tk = Tk()
    root.withdraw()

    folder_path: str = filedialog.askdirectory(
        title='Select a folder to analyse'
    )

    return folder_path if folder_path else None


def get_file_size(file_path: str) -> int:
    try:
        return os.path.getsize(file_path)
    except OSError:
        return 0


def process_file(
    filename: str,
    current_dir: str,
    extension_counter: Counter[str]
) -> int:
    
    if filename.startswith('.'):
        return 0

    full_path: str = os.path.join(current_dir, filename)

    file_size: int = get_file_size(full_path)

    _, extension = os.path.splitext(filename)

    if extension:
        extension_counter[extension.lower()] += 1

    return file_size


def scan_folder(folder_path: str) -> tuple[int, int, Counter[str]]:
    file_count: int = 0
    total_size: int = 0
    extension_counter: Counter[str] = Counter()

    for current_dir, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_size: int = process_file(
                filename,
                current_dir,
                extension_counter
            )

            if file_size == 0 and filename.startswith('.'):
                continue

            file_count += 1
            total_size += file_size

    return file_count, total_size, extension_counter


def build_stats(
    folder_path: str,
    file_count: int,
    total_size: int,
    extension_counter: Counter[str]
) -> Stats:

    total_size_mb: float = round(total_size / (1024 * 1024), 2)

    most_common_extensions: list[tuple[str, int]] = (
        extension_counter.most_common(5)
    )

    return Stats(
        folder=os.path.abspath(folder_path),
        num_files=file_count,
        total_size_mb=total_size_mb,
        most_common_types=most_common_extensions,
    )


def analyse_folder() -> Stats | None:
    folder_path: str | None = select_folder()

    if not folder_path:
        print('No folder selected.')
        return None

    file_count, total_size, extension_counter = scan_folder(folder_path)

    return build_stats(
        folder_path,
        file_count,
        total_size,
        extension_counter
    )
          
def main() -> None:
    stats: Stats | None = analyse_folder()

    if stats:
        print(f'Folder: {stats.folder}')
        print(f'Number of files: {stats.num_files}')
        print(f'Total size (MB): {stats.total_size_mb}')
        if stats.most_common_types:
            print('Most common file types:')
            for ext, count in stats.most_common_types:
                print(f'  {ext}: {count} files')

if __name__ == '__main__':
    main()