import numpy as np
import scipy.special

class Brain:
    def __init__(self, inputnodes, hiddennodes, outputnodes):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.wih = np.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        self.activation_function = lambda x: scipy.special.expit(x) * 2 - 1
        
    def predict(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs

    def breed(self, b):
        c = Brain(self.inodes, self.hnodes, self.onodes)
        c.wih = (self.wih + b.wih) / 2
        c.who = (self.who + b.who) / 2
        return c
        
    def mutate(self):
        wih_mask = np.random.normal(0, 1, size=self.wih.shape)
        who_mask = np.random.normal(0, 1, size=self.who.shape)
        self.wih *= wih_mask * 0.1
        self.who *= who_mask * 0.1
