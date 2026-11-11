import joblib 

class PredictionService:
    def __init__(self,model_path):
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        print(self.model)
        return self.model.predict(input_data)[0]
