<h1>Ocular Disease Recognition</h1>

Project to explore ocular disease recognition with kaggle dataset of classified fundus images (https://www.kaggle.com/andrewmvd/ocular-disease-recognition-odir5k).

<b>IN PROGRESS</b><br>
<h2>To-Do</h2>
<ul>
<li>Explore whether it makes sense for each class to have a different threshold in multi-label classification</li>
<li>Re-run pretrained CNN using F1 score call to see if validation accuracy is increasing even when validation loss is not changing much</li>
<li>Re-run models using less classes - try to focus on predicting the 2-3 diseases that the models are performing best on. Reclassify the other diseases as other. </li>
<li>If accuracy is still limited, try model for singular disease (binary classification) </li>
</ul>

<h2>Contents</h2>
Notebooks/<br>
----- 1-data-exploration.ipynb: data structure, summary statistics, average images<br>
----- 2-simple-model.ipynb: Logistic regression and small MLP neutral net using multi-class classification using just the primary diagnostic<br>
----- 3-cnn-keras.ipynb: Try a few CNN architectures using keras. Multi-label classification using the pre-encoded diagnostic array that includes some images with multiple diseases <br>

src/<br>
---- __init__.py<br>
---- make_data.py: Download data from kaggle and unzip in data folder (not implemented)<br>
---- make_features.py: Helper functions for loading data, resizing images, plotting images, etc<br>

README.md<br>

tests.py: test functions in make features<br>
<br>
<h2>Requirements</h2>
Python 3.8.8<br>
pandas<br>
numpy<br>
matplotlib<br>
seaborn<br>
sklearn<br>
keras<br>
pytest