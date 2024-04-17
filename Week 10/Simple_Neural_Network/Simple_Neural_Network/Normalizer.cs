using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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

        public static double[][] normalizeTraining(double[][] inputs, double[]outputs, double[] minOutput, double[]maxOutput) 
        {






            throw new NotImplementedException();
        }


    }
}
