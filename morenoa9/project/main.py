import os
import time
from library import MusicLibrary
from sorting import quick_sort, merge_sort
from playlist import Playlist

# Safe path handling for VS Code
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

    playlists = {}          # name -> Playlist
    current_playlist = None

    while True:
        display_menu()
        choice = input("Choice: ").strip()

        # 1. Browse library
        if choice == "1":
            library.display_library()

        # 2. Search songs
        elif choice == "2":
            query = input("Enter title keyword: ")
            results = library.search_by_title(query)
            if results:
                for song in results:
                    print(song)
            else:
                print("No songs found.")

        # 3. Sort library
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

            print(f"Top 5 songs by {key}:\n")
            top5 = sorted_songs[-5:]
            top5.reverse()
            for song in top5:
                print(song)

        # 4. Playlist manager (MULTIPLE PLAYLISTS)
        elif choice == "4":
            while True:
                print("\nPlaylist Manager:")
                print("1. New playlist")
                print("2. Select playlist")
                print("3. Add songs to playlist")
                print("4. View playlist")
                print("5. Remove next song")
                print("6. Back")

                sub = input("Select: ").strip()

                # Create playlist
                if sub == "1":
                    name = input("Playlist name: ")
                    if name in playlists:
                        print("Playlist already exists.")
                    else:
                        playlists[name] = Playlist(name)
                        current_playlist = playlists[name]
                        print(f'Playlist "{name}" created and selected.')

                # Select playlist
                elif sub == "2":
                    if not playlists:
                        print("No playlists available.")
                        continue

                    print("\nAvailable playlists:")
                    for name in playlists:
                        print("-", name)

                    selection = input("Select playlist: ")
                    if selection in playlists:
                        current_playlist = playlists[selection]
                        print(f'Playlist "{selection}" selected.')
                    else:
                        print("Playlist not found.")

                # Add songs
                elif sub == "3":
                    if not current_playlist:
                        print("No playlist selected.")
                        continue

                    print("\nEnter song titles (one per line, 'done' to finish):")
                    while True:
                        title = input()
                        if title.lower() == "done":
                            break
                        matches = library.search_by_title(title)
                        if matches:
                            current_playlist.add_song(matches[0])
                            print(f'Added: {matches[0]}')
                        else:
                            print("Song not found.")

                # View playlist
                elif sub == "4":
                    if not current_playlist:
                        print("No playlist selected.")
                    else:
                        current_playlist.play()

                # Remove song
                elif sub == "5":
                    if not current_playlist:
                        print("No playlist selected.")
                    else:
                        removed = current_playlist.remove_song()
                        if removed:
                            print(f"Removed: {removed}")
                        else:
                            print("Playlist is empty.")

                elif sub == "6":
                    break

                else:
                    print("Invalid option.")

        # 5. Compare sorting performance
        elif choice == "5":
            sizes = [10, 20, len(library.all_songs)]

            print("\nSorting performance comparison:\n")
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

        # 6. Exit
        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
