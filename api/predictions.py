from joblib import load

model = load('/home/alt9193/Documents/IA/IA_Backend/api/trainedModel.joblib')

def makePrediction(X):
    y_pred = model.predict(X)
    return y_pred