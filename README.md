# 📊 Customer Sentiment Analysis System

A comprehensive sentiment analysis tool that analyzes customer feedback data to provide insights on employee performance, identify flight risks, and predict sentiment trends.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation
1. **Install Python** (if not already installed):
   ```bash
   # Windows
   winget install Python.Python.3.11
   
   # macOS
   brew install python
   
   # Linux
   sudo apt-get install python3 python3-pip
   ```

2. **Install required packages**:
   ```bash
   pip install pandas numpy
   ```

3. **Run the analysis**:
   ```bash
   python simple_sentiment_analysis.py
   ```

## 📁 Project Structure

```
customer-sentiment-analysis/
├── simple_sentiment_analysis.py    # Main analysis script
├── requirements.txt                # Python dependencies
├── test(in) (1).csv               # Sample data file
├── sentiment_analysis_report.txt   # Generated analysis report
└── processed_sentiment_data.csv    # Processed data with scores
```

## 🎯 Features

### ✅ Sentiment Analysis
- **Sentiment Classification**: Positive, Negative, Neutral
- **Score Calculation**: Compound, positive, negative, neutral scores
- **Intensity Analysis**: Sentiment strength measurement

### 📈 Analytics & Insights
- **Employee Ranking**: Top performers based on sentiment metrics
- **Flight Risk Detection**: Identify employees at risk of leaving
- **Monthly Trends**: Sentiment patterns over time
- **Predictive Modeling**: Linear regression for trend forecasting

### 📊 Output Files
- **Analysis Report**: Comprehensive insights and recommendations
- **Processed Data**: CSV with sentiment scores for further analysis

## 📋 Data Format

Your CSV file should contain these columns:
- `Subject`: Email subject line
- `body`: Email content
- `date`: Date of communication
- `from`: Sender email address

## 📊 What You'll Get

### Analysis Outputs
- **Sentiment Distribution**: Percentage breakdown of positive/negative/neutral messages
- **Employee Rankings**: Top performers based on sentiment metrics
- **Flight Risk Analysis**: Employees identified as potential retention risks
- **Monthly Trends**: Sentiment patterns over time
- **Predictive Insights**: Future sentiment forecasting

## 🛠️ Customization

### Modify Sentiment Thresholds
Edit the `classify_sentiment` method in `simple_sentiment_analysis.py`:
```python
def classify_sentiment(self, compound_score):
    if compound_score >= 0.05:      # Adjust threshold
        return 'Positive'
    elif compound_score <= -0.05:   # Adjust threshold
        return 'Negative'
    else:
        return 'Neutral'
```

### Add Custom Words
Extend the sentiment dictionaries in `SimpleSentimentAnalyzer`:
```python
self.positive_words.update(['your', 'custom', 'words'])
self.negative_words.update(['your', 'custom', 'words'])
```

## 📈 Key Metrics Explained

- **Compound Score**: Overall sentiment (-1 to +1)
- **Positive Percentage**: % of positive messages per employee
- **Sentiment Intensity**: Strength of sentiment expression
- **Risk Score**: Likelihood of employee leaving (higher = more risk)

## 🎯 Use Cases

1. **HR Analytics**: Monitor employee satisfaction and engagement
2. **Customer Service**: Track customer sentiment trends
3. **Performance Management**: Identify top performers and areas for improvement
4. **Retention Strategy**: Proactively address flight risk employees

## 🔧 Troubleshooting

### Common Issues
- **Python not found**: Install Python and add to PATH
- **Missing packages**: Run `pip install pandas numpy`
- **Data format error**: Ensure CSV has required columns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

**Ready to analyze your customer sentiment?** Just run `python simple_sentiment_analysis.py` and get instant insights! 🚀
