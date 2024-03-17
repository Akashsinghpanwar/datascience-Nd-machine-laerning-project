
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <img src="https://www.marktechpost.com/wp-content/uploads/2022/09/Screen-Shot-2022-09-05-at-9.37.26-AM.png" alt="Image">
</body>
</html>


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dataset Description</title>
</head>
<body>

<h1>Dataset Description</h1>

<p>In this dataset, you are presented pairs of phrases (an anchor and a target phrase) and asked to rate how similar they are on a scale from 0 (not at all similar) to 1 (identical in meaning). This challenge differs from a standard semantic similarity task in that similarity has been scored here within a patent's context, specifically its CPC classification (version 2021.05), which indicates the subject to which the patent relates. For example, while the phrases "bird" and "Cape Cod" may have low semantic similarity in normal language, the likeness of their meaning is much closer if considered in the context of "house".</p>

<h2>Score Meanings</h2>
<p>The scores are in the 0-1 range with increments of 0.25 with the following meanings:</p>
<ul>
  <li><strong>1.0</strong> - Very close match. This is typically an exact match except possibly for differences in conjugation, quantity (e.g. singular vs. plural), and addition or removal of stopwords (e.g. “the”, “and”, “or”).</li>
  <li><strong>0.75</strong> - Close synonym, e.g. “mobile phone” vs. “cellphone”. This also includes abbreviations, e.g. "TCP" -> "transmission control protocol".</li>
  <li><strong>0.5</strong> - Synonyms which don’t have the same meaning (same function, same properties). This includes broad-narrow (hyponym) and narrow-broad (hypernym) matches.</li>
  <li><strong>0.25</strong> - Somewhat related, e.g. the two phrases are in the same high level domain but are not synonyms. This also includes antonyms.</li>
  <li><strong>0.0</strong> - Unrelated.</li>
</ul>

<h2>Files</h2>
<ul>
  <li><strong>train.csv</strong> - the training set, containing phrases, contexts, and their similarity scores</li>
  <li><strong>test.csv</strong> - the test set, identical in structure to the training set but without the score</li>
  <li><strong>sample_submission.csv</strong> - a sample submission file in the correct format</li>
</ul>

<h2>Columns</h2>
<ul>
  <li><strong>id</strong> - a unique identifier for a pair of phrases</li>
  <li><strong>anchor</strong> - the first phrase</li>
  <li><strong>target</strong> - the second phrase</li>
  <li><strong>context</strong> - the CPC classification (version 2021.05), which indicates the subject within which the similarity is to be scored</li>
  <li><strong>score</strong> - the similarity score, sourced from a combination of one or more manual expert ratings</li>
</ul>

</body>
</html>
