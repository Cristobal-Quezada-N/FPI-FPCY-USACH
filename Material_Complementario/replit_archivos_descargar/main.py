from sys import exit
from definitions import ReplitData

def main():
    replit  = ReplitData()
    replit.init()

    err     = replit.login()
    if err != None:
        exit(f"[!] Failed to Login: {err}")

    print("\n[i] Access\n")
    guides  = replit.guides_data()
    print(guides)
<<<<<<< HEAD
    #replit.download_guides(guides)
=======
    #replit.get_guides(guides)
>>>>>>> b050fc1 (feat(ReplitData): add `get_guides(self, guides: List[Guide])`.)

    replit.close()


if __name__ == "__main__":
    main()
