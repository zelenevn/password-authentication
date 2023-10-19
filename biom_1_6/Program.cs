using System.Text;
using OxyPlot;
using OxyPlot.Axes;
using OxyPlot.Series;
using OxyPlot.WindowsForms;

public class PasswordGenerator
{
    public int Length { get; }
    public string Alphabet { get; }

    public PasswordGenerator(int length, string alphabet)
    {
        Length = length;
        Alphabet = alphabet;
    }

    public string GeneratePassword()
    {
        Random rand = new Random();
        StringBuilder password = new StringBuilder();
        for (int i = 0; i < Length; i++)
        {
            int randIndex = rand.Next(0, Alphabet.Length);
            password.Append(Alphabet[randIndex]);
        }
        return password.ToString();
    }
}

class Program
{
    static TextBox lenTextBox;
    static TextBox iterTextBox;
    static Form mainForm;
    static List<int> errorFreq;

    static void Main()
    {
        mainForm = new Form
        {
            Width = 300,
            Height = 200,
            Text = "Генератор пароля"
        };

        lenTextBox = new TextBox
        {
            Location = new Point(170, 30),
            Size = new Size(100, 20),
            Text = "10" 
        };

        iterTextBox = new TextBox
        {
            Location = new Point(170, 60),
            Size = new Size(100, 20),
            Text = "5" 
        };

        Label lenLabel = new Label
        {
            Location = new Point(10, 30),
            Size = new Size(150, 20),
            Text = "Длина пароля"
        };

        Label iterLabel = new Label
        {
            Location = new Point(10, 60),
            Size = new Size(150, 20),
            Text = "Количество итераций"
        };

        Button generateButton = new Button
        {
            Location = new Point(80, 120),
            Size = new Size(120, 23),
            Text = "Генерировать",
            UseVisualStyleBackColor = true
        };

        generateButton.Click += (sender, e) => GeneratePasswordAndOpenGraphForm();

        mainForm.Controls.Add(lenLabel);
        mainForm.Controls.Add(iterLabel);
        mainForm.Controls.Add(lenTextBox);
        mainForm.Controls.Add(iterTextBox);
        mainForm.Controls.Add(generateButton);

        Application.Run(mainForm);
    }

    static void GeneratePasswordAndOpenGraphForm()
    {
        int len = Convert.ToInt32(lenTextBox.Text);
        string alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        PasswordGenerator gen = new PasswordGenerator(len, alph);
        string password = gen.GeneratePassword();

        int iter = Convert.ToInt32(iterTextBox.Text);
        errorFreq = new List<int>();

        for (int i = 0; i < iter; i++)
        {
            string pass = Microsoft.VisualBasic.Interaction.InputBox($"Введите пароль {i + 1}\n{password}", "Ввод пароля");

            if (pass.Length > len)
            {
                MessageBox.Show($"Длина пароля не должна превышать {len} символов.");
                i--; 
                continue;
            }

            int sum_err = 0;
            for (int j = 0; j < pass.Length; j++)
            {
                if (pass[j] != password[j])
                    sum_err++;
            }
            errorFreq.Add(sum_err);
        }

        OpenGraphForm();
    }

    static void OpenGraphForm()
    {
        Form graphForm = new Form
        {
            Width = 600,
            Height = 400,
            Text = "График ошибок"
        };

        PlotModel plotModel = BuildPlotModel(errorFreq);

        PlotView plotView = new PlotView
        {
            Model = plotModel,
            Dock = DockStyle.Fill
        };

        graphForm.Controls.Add(plotView);

        graphForm.ShowDialog();
    }

    static PlotModel BuildPlotModel(List<int> errorFreq)
    {
        PlotModel plotModel = new PlotModel();

        LineSeries lineSeries = new LineSeries
        {
            MarkerType = MarkerType.Circle,
            MarkerSize = 4,
            MarkerStroke = OxyColors.White,
            MarkerFill = OxyColors.Blue
        };

        for (int i = 0; i < errorFreq.Count; i++)
        {
            lineSeries.Points.Add(new DataPoint(i + 1, errorFreq[i]));
        }

        plotModel.Series.Add(lineSeries);

        plotModel.Axes.Add(new LinearAxis
        {
            Position = AxisPosition.Bottom,
            Key = "IndexAxis",
            Title = "Index",
            //Minimum = 0,
            //Maximum = 10
        });

        plotModel.Axes.Add(new LinearAxis
        {
            Position = AxisPosition.Left,
            Key = "ValueAxis",
            Title = "Value",
            //Minimum = 0,
            //Maximum = 10
        });

        return plotModel;
    }
}


