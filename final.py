import os
def final_model():

	# training top layers( transfer learning ) 
	os.system('python car.py train --dataset=./datasets --weights=coco')
	# prediction of test dataset and making submission file
	os.system('python generate_predictions.py')
final_model()