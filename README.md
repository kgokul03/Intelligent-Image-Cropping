# Thumbnail enhancer

Run the code by:

For whole folder
```bash
python command.py --rgb_folder=./test
```
For single image
```bash
python command.py --rgb=sample.jpg
```

# MAE:

For a folder:
```bash
python command.py --rgb_folder=./eval
```

Paste the generated ouput in generated_sal folder and run the below command. This is
because, we would find MAE only if Ground Truth image is available.
```bash
python mae.py --rgb_folder=./generated_sal
```
For a file:
```bash
python command.py --rgb=sample.jpg
python mae.py --rgb=sample_out.jpg
```
