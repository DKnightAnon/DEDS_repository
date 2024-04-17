using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Network;

namespace Network
{
    public class HillClimb_Network
    {
        private int inputNodes;
        private int hiddenNodes;
        private int outputNodes;
        private double[,] weightsInputHidden;
        private double[,] weightsHiddenOutput;
        private Random random;

        public HillClimb_Network(int inputNodes, int hiddenNodes, int outputNodes)
        {
            this.inputNodes = inputNodes;
            this.hiddenNodes = hiddenNodes;
            this.outputNodes = outputNodes;

            weightsInputHidden = new double[inputNodes, hiddenNodes];
            weightsHiddenOutput = new double[hiddenNodes, outputNodes];

            random = new Random();

            InitializeWeights();
        }

        private void InitializeWeights()
        {
            for (int i = 0; i < inputNodes; i++)
            {
                for (int j = 0; j < hiddenNodes; j++)
                {
                    weightsInputHidden[i, j] = random.NextDouble() * 2 - 1; // Random weights between -1 and 1
                }
            }

            for (int i = 0; i < hiddenNodes; i++)
            {
                for (int j = 0; j < outputNodes; j++)
                {
                    weightsHiddenOutput[i, j] = random.NextDouble() * 2 - 1; // Random weights between -1 and 1
                }
            }
        }

        public double[] Predict(double[] inputs)
        {
            double[] hiddenOutputs = new double[hiddenNodes];
            double[] finalOutputs = new double[outputNodes];

            // Calculate outputs of hidden layer
            for (int i = 0; i < hiddenNodes; i++)
            {
                double sum = 0;
                for (int j = 0; j < inputNodes; j++)
                {
                    sum += inputs[j] * weightsInputHidden[j, i];
                }
                hiddenOutputs[i] = Math.Tanh(sum);
            }

            // Calculate final outputs
            for (int i = 0; i < outputNodes; i++)
            {
                double sum = 0;
                for (int j = 0; j < hiddenNodes; j++)
                {
                    sum += hiddenOutputs[j] * weightsHiddenOutput[j, i];
                }
                finalOutputs[i] = Math.Tanh(sum);
            }

            //foreach(var row in weightsInputHidden)
            //{
            //    foreach (var col in weightsInputHidden)
            //    {
            //        Console.Write($"{col}|");
            //    }
            //    Console.WriteLine();
            //}

            return finalOutputs;
        }

        public void HillClimbing(double[][] trainingData, int iterations, double stepSize)
        {
            double currentError = double.MaxValue;
            double[] bestWeightsInputHidden = new double[inputNodes * hiddenNodes];
            double[] bestWeightsHiddenOutput = new double[hiddenNodes * outputNodes];

            // Flatten weights matrices into arrays for easier manipulation
            FlattenWeights(weightsInputHidden, bestWeightsInputHidden);
            FlattenWeights(weightsHiddenOutput, bestWeightsHiddenOutput);

            for (int iter = 0; iter < iterations; iter++)
            {
                // Perturb weights
                double[] newWeightsInputHidden = PerturbWeights(bestWeightsInputHidden, stepSize);
                double[] newWeightsHiddenOutput = PerturbWeights(bestWeightsHiddenOutput, stepSize);

                // Unflatten perturbed weights
                double[,] newWeightsInputHiddenMatrix = UnflattenWeights(newWeightsInputHidden, inputNodes, hiddenNodes);
                double[,] newWeightsHiddenOutputMatrix = UnflattenWeights(newWeightsHiddenOutput, hiddenNodes, outputNodes);

                // Evaluate perturbed weights
                double newError = CalculateTotalError(trainingData, newWeightsInputHiddenMatrix, newWeightsHiddenOutputMatrix);

                // If error improved, accept new weights
                if (newError < currentError)
                {
                    currentError = newError;
                    Array.Copy(newWeightsInputHidden, bestWeightsInputHidden, newWeightsInputHidden.Length);
                    Array.Copy(newWeightsHiddenOutput, bestWeightsHiddenOutput, newWeightsHiddenOutput.Length);
                }
            }

            // Update network weights with best found weights
            weightsInputHidden = UnflattenWeights(bestWeightsInputHidden, inputNodes, hiddenNodes);
            weightsHiddenOutput = UnflattenWeights(bestWeightsHiddenOutput, hiddenNodes, outputNodes);
        }

        private void FlattenWeights(double[,] weightsMatrix, double[] weightsArray)
        {
            int index = 0;
            for (int i = 0; i < weightsMatrix.GetLength(0); i++)
            {
                for (int j = 0; j < weightsMatrix.GetLength(1); j++)
                {
                    weightsArray[index++] = weightsMatrix[i, j];
                }
            }
        }

        private double[,] UnflattenWeights(double[] weightsArray, int rows, int columns)
        {
            double[,] weightsMatrix = new double[rows, columns];
            int index = 0;
            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    weightsMatrix[i, j] = weightsArray[index++];
                }
            }
            return weightsMatrix;
        }

        private double[] PerturbWeights(double[] weights, double stepSize)
        {
            double[] perturbedWeights = new double[weights.Length];
            for (int i = 0; i < weights.Length; i++)
            {
                perturbedWeights[i] = weights[i] + (random.NextDouble() * 2 - 1) * stepSize;
            }
            return perturbedWeights;
        }

        private double CalculateTotalError(double[][] trainingData, double[,] weightsInputHidden, double[,] weightsHiddenOutput)
        {
            double totalError = 0;
            foreach (var data in trainingData)
            {
                double[] inputs = new double[inputNodes];
                double[] targets = new double[outputNodes];
                Array.Copy(data, inputs, inputNodes);
                Array.Copy(data, inputNodes, targets, 0, outputNodes);

                double[] outputs = Predict(inputs);

                for (int i = 0; i < outputNodes; i++)
                {
                    totalError += Math.Pow(targets[i] - outputs[i], 2);
                }
            }
            return totalError;
        }
    }

}

