import os
import time
from library import MusicLibrary
from sorting import quick_sort, merge_sort
from playlist import Playlist

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "songs.csv")


def display_menu():
    print("\n=== Smart Playlist Generator ===\n")
    print("Main Menu:")
    print("1. Browse library")
    print("2. Search songs")
    print("3. Sort library")
    print("4. Create/edit playlist")
    print("5. Compare sorting performance")
    print("6. Exit")


def sort_menu():
    print("\nSort library by:")
    print("1. Title (A-Z)")
    print("2. Artist")
    print("3. Duration")
    print("4. Rating")
    print("5. Play count")


def algorithm_menu():
    print("\nChoose sorting algorithm:")
    print("1. Quick Sort")
    print("2. Merge Sort")


def main():
    library = MusicLibrary()
    library.load_from_file(DATA_PATH)

    print(f"\nMusic library loaded: {len(library.all_songs)} songs")

    playlist = None

    while True:
        display_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            library.display_library()

        elif choice == "2":
            query = input("Enter title keyword: ")
            results = library.search_by_title(query)
            for song in results:
                print(song)

        elif choice == "3":
            sort_menu()
            sort_choice = input("Select: ").strip()

            keys = {
                "1": "title",
                "2": "artist",
                "3": "duration",
                "4": "rating",
                "5": "play_count"
            }

            key = keys.get(sort_choice)
            if not key:
                print("Invalid sort option.")
                continue

            algorithm_menu()
            algo_choice = input("Select: ").strip()

            start = time.perf_counter()

            if algo_choice == "1":
                sorted_songs = quick_sort(library.all_songs, key)
                algo_name = "Quick Sort"
            elif algo_choice == "2":
                sorted_songs = merge_sort(library.all_songs, key)
                algo_name = "Merge Sort"
            else:
                print("Invalid algorithm choice.")
                continue

            end = time.perf_counter()

            print(
                f"\nSorting {len(sorted_songs)} songs by {key} "
                f"using {algo_name}... "
                f"Completed in {end - start:.4f} seconds.\n"
            )

            print("Top 5 songs:\n")
            for song in reversed(sorted_songs[-5:]):
                print(song)

        elif choice == "4":
            print("\nPlaylist Manager:")
            print("1. New playlist")
            print("2. Add songs")
            print("3. View playlist")
            print("4. Back")

            sub = input("Select: ").strip()

            if sub == "1":
                name = input("Playlist name: ")
                playlist = Playlist(name)
                print(f'Playlist "{name}" created.')

            elif sub == "2" and playlist:
                print("\nEnter song titles (one per line, 'done' to finish):")
                while True:
                    title = input()
                    if title.lower() == "done":
                        break
                    matches = library.search_by_title(title)
                    if matches:
                        playlist.add_song(matches[0])
                        print(f'Added: {matches[0]}')
                    else:
                        print("Song not found.")

            elif sub == "3" and playlist:
                playlist.play()

        elif choice == "5":
            sizes = [10, 20, len(library.all_songs)]
            for size in sizes:
                sample = library.all_songs[:size]

                start = time.perf_counter()
                quick_sort(sample, "rating")
                quick_time = time.perf_counter() - start

                start = time.perf_counter()
                merge_sort(sample, "rating")
                merge_time = time.perf_counter() - start

                print(
                    f"{size} songs → "
                    f"Quick Sort: {quick_time:.4f}s, "
                    f"Merge Sort: {merge_time:.4f}s"
                )

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
