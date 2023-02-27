import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.utils.data_utils import pad_sequences
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
# add data set
df=pd.read_csv('text_dataset.csv')

# Text snippets
texts = df.text

# Labels (positive or negative sentiment)
labels = df.label

# Tokenize the text snippets
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Convert the words to numerical representations
word_index = tokenizer.word_index
vocab_size = len(word_index) + 1

# Pad the sequences to the same length
max_length = max([len(seq) for seq in sequences])
padded_sequences = pad_sequences(sequences, maxlen=max_length)
# Split the data into training and validation sets
train_data, val_data, train_labels, val_labels = train_test_split(padded_sequences, labels, test_size=0.2)


# Define the model
model = Sequential()
model.add(Embedding(vocab_size, 8, input_length=max_length))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(train_data, train_labels, epochs=15, batch_size=32, validation_data=(val_data, val_labels))
# Save the model in TensorFlow format
model.save('model.h5')