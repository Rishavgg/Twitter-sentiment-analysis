<h2>This project is a machine learning-based sentiment analysis of Twitter data. The goal of the project is to classify tweets as positive, negative, or neutral based on their content.</h2>

<h2>Installation and Setup</h2>
<p>To use this project, you will need to have Python 3 and the following libraries installed:</p>

<ul>
  <li>pandas</li>
  <li>numpy</li>
  <li>matplotlib</li>
  <li>scikit-learn</li>
  <li>nltk</li> 
 <li>seaborn</li>
 <li>string</li>
 <li>pickle</li>
</ul>
<h2>Data Collection and Preprocessing</h2>
<p>The data for this project was collected from Kaggle. We collected tweets on a specific topic using a set of search terms and filtered out any retweets or duplicate tweets.</p>

<p>The data was then preprocessed by removing any special characters and stop words.</p>
<h2>Feature Extraction and Selection</h2>
<p>We extracted features from the preprocessed data using a bag-of-words model. We also used TF-IDF to weight the features based on their importance.</p>
<div>
  <div>
  <h2>Machine Learning Model</h2>
  <p>We trained a Logistic regression, random forest classifier, Extra trees classifier, and Bagging classifiers. </p>
  <ul>
    <li>Logistic Regression</li>
    <li>Random Forest Classifier</li>
    <li>Extra Trees Classifier</li>
    <li>Bagging Classifiers</li>
    <li>Pipeline</li>
  </ul>
</div>
<div>
  <h3>Using a Pipeline for Best Accuracy</h3>
  <p>We utilized a pipeline to optimize our machine learning model and achieve the highest possible accuracy. The pipeline involved a series of data preprocessing and transformation steps, followed by fitting multiple models and selecting the best performing one.</p>
</div>
<h3>Using Streamlit</h3>
<p>Streamlit is a Python framework that allows you to quickly and easily create interactive web applications using only Python code. <br>Used in $app.py</p>



