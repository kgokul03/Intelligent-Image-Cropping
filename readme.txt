Paste the model folder from below link in this folder
 

Run the code by:
================
For whole folder -> python command.py --rgb_folder=./test
For single image -> python command.py --rgb=sample.jpg

MAE:
====
For a folder:
python command.py --rgb_folder=./eval

Paste the generated ouput in generated_sal folder and run the below command. This is
because, we would find MAE only if Ground Truth image is available.

python mae.py --rgb_folder=./generated_sal

For a file:
python command.py --rgb=sample.jpg
python mae.py --rgb=sample_out.jpg



