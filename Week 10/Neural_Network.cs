namespace Simple_Neural_Network
{
    public static class Normalizer
    {

        private static double scaler(double val, double min, double max)
        => min + val * (max - min);
        static double Map(double a1, double a2, double b1, double b2, double s) 
            => b1 + (s - a1) * (b2 - b1) / (a2 - a1);




        public static double[] outputNormalize(double[] outputs) 
        {
            double max = outputs.Max();
            double min = outputs.Min();

            Console.WriteLine($"Max output : {max} | Min Output : {min}");
            Console.WriteLine($"example map : {Map(2,224,0,1,224)}");

            double[] normalizedOutputs = new double[outputs.Length];

            int arrayIndex = 0; 
            foreach (var output in outputs) 
            {
                string value = output.ToString().Trim(new Char[] { ' ', '*', '.' });
                value = $"0,{value}";
                double normalizeValue =
                /*scaler(output, min, max);*/
                //Convert.ToDouble(value);
                Map(min, max, 0, 1, output);


                //Console.WriteLine(normalizeValue);
                normalizedOutputs[arrayIndex] = normalizeValue;
                arrayIndex++;
            }
            foreach (var value in normalizedOutputs) { Console.WriteLine(value); }

            arrayIndex = 0;

            return normalizedOutputs;

        }


        public static double[][] normalizeInputs(double[][] inputs, double[] min, double[] max) 
        {

            int arrayIndex = 0;

            double[][] normalizedInputs = new double[inputs.Length][];

            foreach (var input in inputs) 
            {

                int recordIndex = 0;
                double[] normalizedRecord = new double[input.Length];
                foreach (var record in input)
                {
                    string value = record.ToString().Trim(new Char[] { ' ', '*', '.' });
                    value = $"0,{value}";
                    double normalizeValue = Map(min[recordIndex], max[recordIndex], 0, 1, record);//Convert.ToDouble(value);
                    normalizedRecord[recordIndex] = normalizeValue;
                    recordIndex++;
                }

                normalizedInputs[arrayIndex] = normalizedRecord;
                arrayIndex++;
            }


            foreach (var record in normalizedInputs)
            {
                foreach (var value in record)
                {
                    Console.Write($"{value}, ");
                }
                Console.WriteLine();
            }


            return normalizedInputs;


        }

        public static double[][] normalizeTraining(double[][] inputs, double[]outputs, double[] minInputs, double[] maxOutputs) 
        {


            double[][] normalizedInputs = normalizeInputs(inputs, minInputs, maxOutputs);
            double[] normalizedOutputs = outputNormalize(outputs);

            
            for (int i = 0; i<normalizedInputs.Length; i++ )
            {

                double[] outputValue = new double[] { normalizedOutputs[i] };
                normalizedInputs[i] = normalizedInputs[i].Concat(outputValue).ToArray();
               
            }

            Console.WriteLine("Normalized inputs with normalized output:");
            foreach (var record in normalizedInputs) 
            { 
                foreach (var value in record) 
                {
                    Console.Write($"{value}| "); 
                }
                Console.WriteLine();
            }

            return normalizedInputs;
        }


    }
}

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

        private double learningRate = 0.1; 


        private double[] inputLayer;
        private double[][] weights;
        private double[] biases;


        public NeuralNetwork(int inputSize, int hiddenSize, int outputSize)
        {
            inputLayer = new double[inputSize];
            weights = new double[inputSize][];
            biases = new double[hiddenSize];

            Random rand = new Random();
            for (int i = 0; i < inputSize; i++)
            {
                weights[i] = new double[hiddenSize];
                for (int j = 0; j < hiddenSize; j++)
                {
                    weights[i][j] = rand.NextDouble();
                }
            }

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
            double actualOutput = FeedForward(inputs);

            double error = targetOutput - actualOutput;

            for (int i = 0; i < hiddenToOutputWeights.Length; i++)
            {
                double deltaOutputWeight = error * actualOutput * (1 - actualOutput) * hiddenLayer[i];
                hiddenToOutputWeights[i] += learningRate * deltaOutputWeight;
            }

            for (int i = 0; i < inputToHiddenWeights.GetLength(0); i++)
            {
                for (int j = 0; j < inputToHiddenWeights.GetLength(1); j++)
                {
                    double deltaHiddenWeight = error * inputs[i] * hiddenToOutputWeights[j];
                    inputToHiddenWeights[i, j] += learningRate * deltaHiddenWeight;
                }
            }
        }
    }
}

public class Program
{
    public static void Main(string[] args)
    {

        int arraysize = 10;
        double[][] trainingInputs = new double[arraysize][];// = {
        //    new double[] { 0.99, 0.197, 0.494, 0.494},
        //    new double[] { 0.32, 0.1687, 0.2531, 0.2531 }
        //};
        double[] trainingOutputs = new double[arraysize];//= { 0.16, 0.28 }; 



        string path = "";
        switch (Environment.MachineName) 
        {
            case "KNIGHTANON-LAPT":
                path = "C:\\Users\\arcde\\Documents\\Haagse Hogeschool\\Jaar 2\\Semester 4\\DEDS\\DEDS_portfolio\\Week 10\\Simple_Neural_Network\\Simple_Neural_Network\\go_sales.sqlite";
                break;
            case "KNIGHTANON-DESK":
                path = "D:\\Documents\\Haagse_Hogeschool\\Jaar 2\\Semester 4\\DEDS\\DEDS_repository\\Week 10\\Simple_Neural_Network\\Simple_Neural_Network\\go_sales.sqlite";
                break;
        }




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
            var Product_number = Convert.ToDouble(reader.GetString(0));
            var Unit_Cost = Convert.ToDouble(reader.GetString(1));
            var Unit_Price = Convert.ToDouble(reader.GetString(2));
            var Unit_Sale_Price = Convert.ToDouble(reader.GetString(3));
            var quantity = reader.GetInt32(4);
            Console.WriteLine($"{Product_number} {Unit_Cost} {Unit_Price} {Unit_Sale_Price} | Expected Output : {quantity}");

            double[] value = { Product_number, Unit_Cost, Unit_Price, Unit_Sale_Price };
            trainingInputs[arrayIndex] = value;
            trainingOutputs[arrayIndex] = quantity;

  
            arrayIndex++;
        }
        Console.WriteLine();

        double[] normalizedOutputs = Normalizer.outputNormalize(trainingOutputs);

        double[][] normalizedInputs = Normalizer.normalizeInputs(trainingInputs, minVal, maxVal);

        Console.WriteLine("Connection succeeded");

        reader.Close();

       





        NeuralNetwork neuralNetwork = new NeuralNetwork(4, 3, 1);


        //for (int epoch = 0; epoch < 1000; epoch++) // Training for 1000 epochs
        //{
        //    for (int i = 0; i < normalizedInputs.Length; i++)
        //    {
        //        neuralNetwork.Train(normalizedInputs[i], normalizedOutputs[i]);
        //    }
        //}

        //for (int i = 0; i < normalizedInputs.Length; i++)
        //{
        //    double actualOutput = neuralNetwork.FeedForward(normalizedInputs[i]);
        //    Console.WriteLine("Input: " + string.Join(", ", normalizedInputs[i]) + " | Desired Output: " + normalizedOutputs[i] + " | Actual Output: " + actualOutput.ToString("F2"));
        //}


        double[][] inputOutput = Normalizer.normalizeTraining(trainingInputs,trainingOutputs,minVal,maxVal);


        HillClimb_Network climb_Network = new HillClimb_Network(4, 3, 1);

        climb_Network.HillClimbing(inputOutput, iterations: 1000, stepSize: 0.1);


        foreach (var data in inputOutput)
        {
            double[] inputs = new double[4];
            Array.Copy(data, inputs, 4);
            double[] outputs = climb_Network.Predict(inputs);
            Console.WriteLine($"Input: [{string.Join(", ", inputs)}], Output: [{string.Join(", ", outputs)}]");
        }


    }
}