# YOLOv11 Segmentation Dataset Preparation

This repository contains scripts for preparing and augmenting image datasets for YOLOv11 segmentation tasks. It includes utilities for converting JSON annotations to YOLO format and performing data augmentation.

## Project Structure

- **prepare.py**: Converts JSON annotations from the `augmented/` directory into YOLOv11 segmentation format, saving the labels in `dataset/labels/`.
- **copy-matching-png.py**: Copies matching PNG files based on JSON annotations.
- **copy-frames.py**: Copies frame data for further processing.
- **script.py**: General utility script for dataset management.
- **augmentations/**: Contains scripts for data augmentation:
  - `main.py`: Main augmentation script.
  - `augmentations.py`: Defines augmentation functions.
  - `utils.py`: Utility functions for augmentation.
- **frames/**: Contains JSON files with frame annotations.

## Prerequisites

- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`):
  - json
  - os

## Usage

1. **Prepare Dataset**:
   - Place your JSON annotation files in the `augmented/` directory.
   - Run `prepare.py` to convert annotations to YOLOv11 format:
     ```bash
     python prepare.py
     ```
   - The converted labels will be saved in `dataset/labels/`.

2. **Data Augmentation**:
   - Navigate to the `augmentations/` directory.
   - Run the main augmentation script:
     ```bash
     python main.py
     ```

3. **Copy Matching PNGs**:
   - Use `copy-matching-png.py` to copy PNG files matching your JSON annotations:
     ```bash
     python copy-matching-png.py
     ```

4. **Copy Frames**:
   - Use `copy-frames.py` to copy frame data:
     ```bash
     python copy-frames.py
     ```

## Class Mapping

The `prepare.py` script uses a predefined class mapping to convert class names to numeric IDs. Modify the `class_map` dictionary in `prepare.py` if your classes differ.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes. 
