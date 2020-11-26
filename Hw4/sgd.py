import mxnet as mx
from mxnet import gluon


def load_data(self):
def transform(data, label):
return data.astype(np.float32) / 255., label.astype(np.float32)
train_data = DataLoader(MNIST(train=True, transform=transform),
self.batch_size, shuffle=True)
test_data = DataLoader(MNIST(train=False, transform=transform),
self.batch_size, shuffle=False)
return train_data, test_data

def model(self):
num_hidden = 64
net = gluon.nn.Sequential()
with net.name_scope():
net.add(gluon.nn.Dense(units=num_hidden, activation="relu"))
net.add(gluon.nn.Dense(units=num_hidden, activation="relu"))
net.add(gluon.nn.Dense(units=self.num_outputs))
net.collect_params().initialize(init=mx.init.Normal(sigma=.1), ctx=self.model_ctx)
return net

train_data, test_data = self.load_data()  
net = self.model()  

epochs = 200
smoothing_constant = 0.01
num_examples = 1000
softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss() 
trainer = gluon.Trainer(params=net.collect_params(),
optimizer='sgd',
optimizer_params={'learning_rate': smoothing_constant})

for e in range(epochs):
cumulative_loss = 0 
for i, (data, label) in enumerate(train_data):
data = data.as_in_context(self.model_ctx).reshape((-1, 784)) 
label = label.as_in_context(self.model_ctx)  
with autograd.record():  
output = net(data)  
loss = softmax_cross_entropy(output, label) 
loss.backward()  
trainer.step(data.shape[0]) 
cumulative_loss  = nd.sum(loss).asscalar()  
test_accuracy = self.__evaluate_accuracy(test_data, net)
train_accuracy = self.__evaluate_accuracy(train_data, net)
print("Epoch %s. Loss: %s, Train_accuracy %s, Test_accuracy %s" %
(e, cumulative_loss / num_examples, train_accuracy, test_accuracy))

def __evaluate_accuracy(self, data_itertor, net):
acc = mx.metric.Accuracy()  
for i, (data, label) in enumerate(data_iterator):
data = data.as_in_context(self.model_ctx).reshape((-1, 784))
label = label.as_in_context(self.model_ctx)
output = net(data)  
predictions = nd.argmax(output, axis=1) 
acc.update(preds=predictions, labels=label) 
return acc.get()[1]  