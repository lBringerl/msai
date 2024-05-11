import numpy as np


class SimplifiedBaggingRegressor:
    def __init__(self, num_bags, oob=False):
        self.num_bags = num_bags
        self.oob = oob
        
    def _generate_splits(self, data: np.ndarray):
        '''
        Generate indices for every bag and store in self.indices_list list
        '''
        self.indices_list = []
        data_length = len(data)
        for _ in range(self.num_bags):
            self.indices_list.append(np.random.randint(0, data_length, data_length))

    def fit(self, model_constructor, data, target):
        '''
        Fit model on every bag.
        Model constructor with no parameters (and with no ()) is passed to this function.
        
        example:
        
        bagging_regressor = SimplifiedBaggingRegressor(num_bags=10, oob=True)
        bagging_regressor.fit(LinearRegression, X, y)
        '''
        self.data = None
        self.target = None
        self._generate_splits(data)
        assert len(set(list(map(len, self.indices_list)))) == 1, 'All bags should be of the same length!'
        assert list(map(len, self.indices_list))[0] == len(data), 'All bags should contain `len(data)` number of elements!'
        self.models_list = []
        for bag in range(self.num_bags):
            model = model_constructor()
            data_bag, target_bag = data[self.indices_list[bag]], target[self.indices_list[bag]]
            self.models_list.append(model.fit(data_bag, target_bag)) # store fitted models here
        if self.oob:
            self.data = data
            self.target = target
        
    def predict(self, data):
        '''
        Get average prediction for every object from passed dataset
        '''
        predictions = []
        for model in self.models_list:
            predictions.append(model.predict(data))
        return np.mean(predictions, axis=0)

    def _get_oob_predictions_from_every_model(self):
        '''
        Generates list of lists, where list i contains predictions for self.data[i] object
        from all models, which have not seen this object during training phase
        '''
        list_of_predictions_lists = [[] for _ in range(len(self.data))]
        for i, _object in enumerate(self.data):
            for j, model in enumerate(self.models_list):
                if i not in self.indices_list[j]:
                    list_of_predictions_lists[i].append(model.predict(_object.reshape(1, -1))[0])
            list_of_predictions_lists[i] = np.array(list_of_predictions_lists[i])
        self.list_of_predictions_lists = np.array(list_of_predictions_lists, dtype=object)

    def _get_averaged_oob_predictions(self):
        '''
        Compute average prediction for every object from training set.
        If object has been used in all bags on training phase, return None instead of prediction
        '''
        self._get_oob_predictions_from_every_model()
        self.oob_predictions = []
        oob_predictions = []
        for pred in self.list_of_predictions_lists:
            if len(pred) == 0:
                oob_predictions.append(np.nan)
                continue
            np_pred = np.array(pred, dtype=float)
            oob_predictions.append(np.mean(pred[~np.isnan(np_pred)]))
        self.oob_predictions = np.array(oob_predictions, dtype=float)

    def OOB_score(self):
        '''
        Compute mean square error for all objects, which have at least one prediction
        '''
        self._get_averaged_oob_predictions()
        predictions = self.oob_predictions[~np.isnan(self.oob_predictions)]
        targets = self.target[~np.isnan(self.oob_predictions)]
        return np.mean((predictions - targets) ** 2)
