Image : sample2.jpg
Pre Procedure:
1. Create 3 new folders before processing the project:
	1) images
	2) line
	3) word
The above named directories are used to store processed data
2. Delete the sample2.jpg file, which is already given for testing.
3. Add the sample image with name 'sample2' and file should be of jpg format.


1. For Skew correction, Run : SkewCorrection.py by python using cmd command: 
	a. First reach location of image
	b. run code - SkewCorrection.py --image sample2.jpg 
2. For preprocessing, Run preprocessing.py
 
3. For line segmentation, Run lineseg.py
 
4. For word segmentation, Run wordseg.py
 
5. For character segment run TrainAndTest.py
5. Change image number at line no. 64
6. Run GenData.py file to train the machine for characters.
	press left arrow key until the window closes
