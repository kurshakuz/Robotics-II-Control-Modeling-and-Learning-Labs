% the data set size can be also tuned
data_size = 50000;
[XTrain, YTrain] = create_dataset(data_size);
XXy = XTrain;

%%
XTrain = reshape(XTrain', [1, 1, size(XTrain,2),size(XTrain,1)]);

%%

idx = randperm(size(XTrain, 4), 5000);
XValidation = XTrain(:,:,:,idx);
XTrain(:,:,:,idx) = [];
YValidation = YTrain(idx,:);
YTrain(idx,:) = [];

%%
nFeatures = 3;
numClasses = 5;

layers = [ ...
    imageInputLayer([1 1 nFeatures]);
    fullyConnectedLayer(512)
    leakyReluLayer
    fullyConnectedLayer(1024)
    leakyReluLayer
    fullyConnectedLayer(1024)
    leakyReluLayer
    fullyConnectedLayer(512)
    leakyReluLayer
    fullyConnectedLayer(numClasses)  
    regressionLayer
    ]

maxEpochs = 50;
miniBatchSize = 500;

options = trainingOptions('adam', ...
    'ExecutionEnvironment','cpu', ...
    'MaxEpochs',maxEpochs, ...
    'MiniBatchSize',miniBatchSize, ...
    'InitialLearnRate',3e-4, ...
    'SquaredGradientDecayFactor',0.99, ...
    'ValidationData',{XValidation,YValidation}, ...
    'ValidationFrequency',30, ...
    'Plots','training-progress');


net = trainNetwork(XTrain, YTrain,layers,options);


save net