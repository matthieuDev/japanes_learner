
# japanese_learner_site

## japanese2latin

You have a list of words written with Hiragana, and you have to find the original word.

Fill the input under the words :

![Alt text](README_img/fill_j2l.png)

And next press the Submit button. The good answers will be displayed next to the hiragana words and the result will be shown at the bottom.

![Alt text](README_img/answer_j2l.png)

Click on the "New Test" button or refresh the page to have the next question


## latin2japanese

You have a Hiragana in Latin letters, and you have to draw the corresponding Hiragana. If you made a mistake, click on the reset button to clean the canvas.

![Alt text](README_img/draw_l2j.png)

Once you draw the letter, click on the check button to see the letter that was detected. If the letter is not the expected one, redraw it.


![Alt text](README_img/check_l2j.png)

Once you have your expected letter, click on Answer to see if you had the good answer.

![Alt text](README_img/answer_l2j.png)

Click on the "New Question" button or refresh the page to have the next question

## Init data

run generate_datasets.py at the base of the project :

```
generate_datasets.py
```

and then run :

```
python manage.py loaddata japanese2latin/data_init.json
python manage.py loaddata latin2japanese/data_init.json
```

in japanese_learner_site/ folder



