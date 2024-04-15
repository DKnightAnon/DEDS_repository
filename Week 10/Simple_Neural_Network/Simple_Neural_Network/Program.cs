using Network;

public class Program
{
    public static void Main(string[] args)
    {
        // Create neural network
        NeuralNetwork neuralNetwork = new NeuralNetwork(4,3,1);



        // Define inputs
        //Product Number , Unit Cost ,  Unit Price , Unit Sale Price | output
        double[][] trainingInputs = {
            new double[] { 0.99, 0.197, 0.494, 0.494},
            new double[] { 0.32, 0.1687, 0.2531, 0.2531 }
        };

        double[] trainingOutputs = { 0.16, 0.28 }; // Corresponding desired outputs

        // Train the neural network
        for (int epoch = 0; epoch < 1000; epoch++) // Training for 1000 epochs
        {
            for (int i = 0; i < trainingInputs.Length; i++)
            {
                neuralNetwork.Train(trainingInputs[i], trainingOutputs[i]);
            }
        }

        // Test the trained network
        for (int i = 0; i < trainingInputs.Length; i++)
        {
            double actualOutput = neuralNetwork.FeedForward(trainingInputs[i]);
            Console.WriteLine("Input: " + string.Join(", ", trainingInputs[i]) + " | Desired Output: " + trainingOutputs[i] + " | Actual Output: " + actualOutput);
        }
    }
}