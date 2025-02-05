from train import train_model
from evaluate import evaluate_model

def main():
    choice = input("Enter 'train' to train the model or 'evaluate' to evaluate the model: ").strip().lower()
    if choice == 'train':
        train_model()
    elif choice == 'evaluate':
        evaluate_model()
    else:
        print("Invalid choice. Please enter 'train' or 'evaluate'.")

if __name__ == "__main__":
    main()