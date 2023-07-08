using System;

namespace Hackerrank
{
        class Program
        {
                static void Main(string[] args)
                {

                        var listOfInteger = new List<int>() { 1, 2, 3, 4, 5, 90 };

                        var b = Solution.ReverseArray(listOfInteger);

                        Console.WriteLine(listOfInteger.Count);

                        Console.WriteLine(String.Join(',', b));

                        string ved  = 122.33455.ToString("F2");

                        Console.WriteLine(ved);


                }


        }

        public class Solution
        {
                //Solution 1
                public static List<int> ReverseArray(List<int> a)
                {

                        List<int> reverseList = new(a.Count);


                        for (int i = a.Count - 1; i >= 0; i--)
                        {

                                reverseList.Add(a[i]);
                        }

                        return reverseList;
                }

                //Solution 2
                // public static List<int> ReverseArray(List<int> a)
                // {

                        //a.Reverse();

                //         return a;
                // }

        }


}