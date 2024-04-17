using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System;

namespace Network
{


    public class NeuralNetwork
    {
        private double[,] inputToHiddenWeights = {
        {0.8, 0.7, 0.8},
        {0.4, 0.1, 0.6},
        {0.7, 0.8, 0.3},
        {0.2, 1.1, 1.2}
    };


        private double[] hiddenToOutputWeights = { 0.4, 0.6, 0.7 };
        private double[] hiddenLayer = new double[3];
        private double output;

        private double learningRate = 0.1; // Learning rate


        private double[] inputLayer;
        private double[][] weights;
        private double[] biases;


        // Initialize the neural network with random weights and biases
        public NeuralNetwork(int inputSize, int hiddenSize, int outputSize)
        {
            inputLayer = new double[inputSize];
            weights = new double[inputSize][];
            biases = new double[hiddenSize];

            // Initialize weights with random values
            Random rand = new Random();
            for (int i = 0; i < inputSize; i++)
            {
                weights[i] = new double[hiddenSize];
                for (int j = 0; j < hiddenSize; j++)
                {
                    weights[i][j] = rand.NextDouble();
                }
            }

            // Initialize biases with random values
            for (int i = 0; i < hiddenSize; i++)
            {
                biases[i] = rand.NextDouble();
            }
        }

        private double Sigmoid(double x)
        {
            return 1.0 / (1.0 + Math.Exp(-x));
        }

        public double FeedForward(double[] inputs)
        {
            for (int i = 0; i < hiddenLayer.Length; i++)
            {
                double sum = 0;
                for (int j = 0; j < inputs.Length; j++)
                {
                    sum += inputs[j] * inputToHiddenWeights[j, i];
                }
                hiddenLayer[i] = Sigmoid(sum);
            }

            double outputSum = 0;
            for (int i = 0; i < hiddenLayer.Length; i++)
            {
                outputSum += hiddenLayer[i] * hiddenToOutputWeights[i];
            }
            output = Sigmoid(outputSum);

            return output;
        }

        public void Train(double[] inputs, double targetOutput)
        {
            // Perform feedforward to get the actual output
            double actualOutput = FeedForward(inputs);

            // Calculate the error
            double error = targetOutput - actualOutput;

            // Adjust the weights of the hidden to output connections
            for (int i = 0; i < hiddenToOutputWeights.Length; i++)
            {
                double deltaOutputWeight = error * actualOutput * (1 - actualOutput) * hiddenLayer[i];
                hiddenToOutputWeights[i] += learningRate * deltaOutputWeight;
            }

            // Adjust the weights of the input to hidden connections
            for (int i = 0; i < inputToHiddenWeights.GetLength(0); i++)
            {
                for (int j = 0; j < inputToHiddenWeights.GetLength(1); j++)
                {
                    //this used to indirectly use backpropagation
                    double deltaHiddenWeight = error * inputs[i] * hiddenToOutputWeights[j];
                    inputToHiddenWeights[i, j] += learningRate * deltaHiddenWeight;
                }
            }
        }
    }
}