using Microsoft.Data.Sqlite;
using Network;
using Simple_Neural_Network;
using System.Data.SQLite;

public class Program
{
    public static void Main(string[] args)
    {

        int arraysize = 5;
        // Define inputs
        //Product Number , Unit Cost ,  Unit Price , Unit Sale Price | output
        double[][] trainingInputs = new double[arraysize][];// = {
        //    new double[] { 0.99, 0.197, 0.494, 0.494},
        //    new double[] { 0.32, 0.1687, 0.2531, 0.2531 }
        //};
        double[] trainingOutputs = new double[arraysize];//= { 0.16, 0.28 }; // Corresponding desired outputs

        string path = "D:\\Documents\\Haagse_Hogeschool\\Jaar 2\\Semester 4\\DEDS\\DEDS_repository\\Week 10\\Simple_Neural_Network\\Simple_Neural_Network\\go_sales.sqlite";

        SQLiteConnection connection = new SQLiteConnection(@$"Data Source={path}; Version=3;");
        connection.Open();
        SQLiteCommand command = new SQLiteCommand(connection);
        command.CommandText = @$"select distinct Product_Number , Unit_Cost ,  Unit_Price , Unit_Sale_Price, quantity from order_details limit {arraysize}";
        int arrayIndex = 0;
        SQLiteDataReader reader = command.ExecuteReader();
        while (reader.Read())
        {
            //Console.WriteLine("succeeded");
            var Product_number = Convert.ToDouble(reader.GetString(0));
            var Unit_Cost = Convert.ToDouble(reader.GetString(1));
            var Unit_Price = Convert.ToDouble(reader.GetString(2));
            var Unit_Sale_Price = Convert.ToDouble(reader.GetString(3));
            var quantity = reader.GetInt32(4);
            Console.WriteLine($"{Product_number} {Unit_Cost} {Unit_Price} {Unit_Sale_Price} | Expected Output : {quantity}");
            
            double[] value = { Product_number, Unit_Cost, Unit_Price, Unit_Sale_Price };
            trainingInputs[arrayIndex] = value;
            trainingOutputs[arrayIndex] = quantity;

            foreach (var v in value)
            {
                Console.Write($"{v}, ");
            }    
            Console.WriteLine();
            arrayIndex++;
            //Console.WriteLine(arrayIndex);
        }
        Console.WriteLine();

        double[] normalizedOutputs = Normalizer.outputNormalize(trainingOutputs);

        double[][] normalizedInputs = Normalizer.normalizeInputs(trainingInputs);

        Console.WriteLine("Connection succeeded");

        reader.Close();

        //Console.WriteLine($"TrainingInputs length : {trainingInputs.Length}");

        //for (int i = 0; i < trainingInputs.Length; i++)
        //{
        //    Console.WriteLine($"trainingInputs element {i} length: {trainingInputs[i].Length}");
        //}



        // Create neural network
        NeuralNetwork neuralNetwork = new NeuralNetwork(4, 3, 1);






        // Train the neural network
        for (int epoch = 0; epoch < 1000; epoch++) // Training for 1000 epochs
        {
            for (int i = 0; i < normalizedInputs.Length; i++)
            {
                neuralNetwork.Train(normalizedInputs[i], normalizedOutputs[i]);
            }
        }

        // Test the trained network
        for (int i = 0; i < normalizedInputs.Length; i++)
        {
            double actualOutput = neuralNetwork.FeedForward(normalizedInputs[i]);
            Console.WriteLine("Input: " + string.Join(", ", normalizedInputs[i]) + " | Desired Output: " + normalizedOutputs[i] + " | Actual Output: " + actualOutput);
        }
    }
}