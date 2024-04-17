using Microsoft.Data.Sqlite;
using Network;
using Simple_Neural_Network;
using System.Data.SQLite;

public class Program
{
    public static void Main(string[] args)
    {

        int arraysize = 10;
        // Define inputs
        //Product Number , Unit Cost ,  Unit Price , Unit Sale Price | output
        double[][] trainingInputs = new double[arraysize][];// = {
        //    new double[] { 0.99, 0.197, 0.494, 0.494},
        //    new double[] { 0.32, 0.1687, 0.2531, 0.2531 }
        //};
        double[] trainingOutputs = new double[arraysize];//= { 0.16, 0.28 }; // Corresponding desired outputs



        string path = "";
        switch (Environment.MachineName) 
        {
            case "KNIGHTANON-LAPT":
                path = "C:\\Users\\arcde\\Documents\\Haagse Hogeschool\\Jaar 2\\Semester 4\\DEDS\\DEDS_portfolio\\Week 10\\Simple_Neural_Network\\Simple_Neural_Network\\go_sales.sqlite";
                break;
            case "KNIGHTANON_DESK":
                path = "D:\\Documents\\Haagse_Hogeschool\\Jaar 2\\Semester 4\\DEDS\\DEDS_repository\\Week 10\\Simple_Neural_Network\\Simple_Neural_Network\\go_sales.sqlite";
                break;
        }

        //Console.WriteLine(Environment.MachineName);
        //Console.WriteLine(path);



        SQLiteConnection connection = new SQLiteConnection(@$"Data Source={path}; Version=3;");
        connection.Open();
        SQLiteCommand command = new SQLiteCommand(connection);
        
        
        var minList = new List<double>();
        var maxList = new List<double>();

        command.CommandText = @$"select min(product_number), max(product_number),
                                        min(Unit_Cost), max(Unit_Cost),
                                        min(Unit_Price), max(Unit_Price),
                                        min(Unit_Sale_Price), max(Unit_Sale_Price)
                                 from order_details";
        SQLiteDataReader reader = command.ExecuteReader();
        while (reader.Read()) 
        { 
            Console.WriteLine("Got min and max values"); 
            //Product Number
            minList.Add(Convert.ToDouble(reader.GetString(0)));
            maxList.Add(Convert.ToDouble(reader.GetString(1)));

            //Unit_Cost
            minList.Add(Convert.ToDouble(reader.GetString(2)));
            maxList.Add(Convert.ToDouble(reader.GetString(3)));
            
            //Unit_Price
            minList.Add(Convert.ToDouble(reader.GetString(4)));
            maxList.Add(Convert.ToDouble(reader.GetString(5)));
            
            //Unit_Sale_Price
            minList.Add(Convert.ToDouble(reader.GetString(6)));
            maxList.Add(Convert.ToDouble(reader.GetString(7)));
        }

        var minVal = minList.ToArray();
        var maxVal = maxList.ToArray();
        foreach ( var item in minVal ) { Console.Write($"{item},"); }
        foreach (var item in maxVal) { Console.Write($"{item},"); }
        Console.WriteLine();

        reader.Close();

        command.CommandText = @$"select distinct Product_Number , Unit_Cost ,  Unit_Price , Unit_Sale_Price, quantity from order_details limit {arraysize}";
        int arrayIndex = 0;
        reader = command.ExecuteReader();
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

            //foreach (var v in value)
            //{
            //    Console.Write($"{v}, ");
            //}
            //Console.WriteLine();
            arrayIndex++;
            //Console.WriteLine(arrayIndex);
        }
        Console.WriteLine();

        double[] normalizedOutputs = Normalizer.outputNormalize(trainingOutputs);

        double[][] normalizedInputs = Normalizer.normalizeInputs(trainingInputs, minVal, maxVal);

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
            Console.WriteLine("Input: " + string.Join(", ", normalizedInputs[i]) + " | Desired Output: " + normalizedOutputs[i] + " | Actual Output: " + actualOutput.ToString("F2"));
        }





        //HillClimb_Network climb_Network = new HillClimb_Network(4, 3, 1);

        //// Perform hill climbing optimization
        //climb_Network.HillClimbing(trainingData, iterations: 1000, stepSize: 0.1);

        //// Test the trained neural network
        //foreach (var data in trainingData)
        //{
        //    double[] inputs = new double[4];
        //    Array.Copy(data, inputs, 4);
        //    double[] outputs = climb_Network.Predict(inputs);
        //    Console.WriteLine($"Input: [{string.Join(", ", inputs)}], Output: [{string.Join(", ", outputs)}]");
        //}


    }
}