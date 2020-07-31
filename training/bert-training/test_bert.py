import ktrain
import pandas as pd
import re

model = ktrain.load_predictor("../pred/predictor/")

print(model.predict(['merhaba']))

print(model.predict(['gorusuruz']))
