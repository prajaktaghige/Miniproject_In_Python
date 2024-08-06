import pickle

def load_tasks():
    try:
        with open('tasks.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

def display_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)
        
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
            else:
                print("Invalid task number.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
