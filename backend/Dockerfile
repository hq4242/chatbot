FROM tensorflow/tensorflow

COPY . /usr/src

RUN pip install -r ./usr/src/requirements.txt
RUN python -c "exec(\"import nltk\nnltk.download('punkt')\")"

CMD ["python", "./usr/src/__main__.py"]