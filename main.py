import os
from generators import generate_data, generate_train_data

def main():
    print("Generating controlled dataset...")
    generate_data.generate_dataset(
        digits=['6', '7', '8', '9'],
        rotations=[0, 90, 180, 270],
        output_dir="controlled_digits"
    )

    print("\nGenerating training dataset...")
    generate_train_data.generate_training_data()

    print("\nAll datasets successfully generated.")

if __name__ == "__main__":
    main()
