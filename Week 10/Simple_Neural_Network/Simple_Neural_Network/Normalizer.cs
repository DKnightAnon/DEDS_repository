using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simple_Neural_Network
{
    public static class Normalizer
    {



        public static double[] outputNormalize(double[] outputs) 
        {
            //double max = outputs.Max();
            //double min = outputs.Min();

            double[] normalizedOutputs = new double[outputs.Length];

            int arrayIndex = 0; 
            foreach (var output in outputs) 
            {
                string value = output.ToString().Trim(new Char[] { ' ', '*', '.' });
                value = $"0,{value}";
                double normalizeValue = Convert.ToDouble(value);
                //Console.WriteLine(normalizeValue);
                normalizedOutputs[arrayIndex] = normalizeValue;
                arrayIndex++;
            }
            foreach (var value in normalizedOutputs) { Console.WriteLine(value); }

            arrayIndex = 0;

            return normalizedOutputs;

        }


        public static double[][] normalizeInputs(double[][] inputs) 
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
                    double normalizeValue = Convert.ToDouble(value);
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


    }
}
