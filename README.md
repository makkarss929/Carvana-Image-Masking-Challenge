<h2>References:</h2>
https://github.com/matterport/Mask_RCNN

<h2> Transfer learning - training only top layers </h2>

# Train a new model starting from pre-trained COCO weights
python car.py train --dataset=./datasets --weigths=coco

<h2> For generate predictions </h2>

python generate_predictions.py
