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

### ⚠️ Important Considerations & Best Practices

#### 1. Sentiment Thresholds: Domain-Specific Justification
- **Do not use arbitrary cutoffs!** Sentiment thresholds (e.g., what counts as "neutral") should be validated for your data. The default (compound >= 0.05: Positive, <= -0.05: Negative) is a starting point, but you must check if it fits your domain (e.g., emails vs. tweets). Use labeled data or domain expert review to tune these values.

#### 2. Model & Tool Limitations
- **This tool uses a simple, rule-based sentiment analyzer.** It may not capture sarcasm, formal tone, or domain-specific language. Relying on a single tool (like TextBlob, VADER, or this script) can lead to bias. For critical applications, compare outputs from multiple models and validate against a sample of your data.

#### 3. Always Interpret Outputs
- **Charts and metrics are not self-explanatory.** Every visualization or metric (e.g., time series, employee ranking) should be accompanied by an explanation: What does it show? Why does it matter? What could cause the observed trend?

#### 4. Metric Design: Avoid Arbitrary Formulas
- **All new metrics (e.g., composite score, risk score) are explained in the code and report.** Do not invent metrics without a clear rationale. If you change or add metrics, document your reasoning and test if they reflect real-world outcomes.

#### 5. Human-in-the-Loop: Validate AI Outputs
- **Never copy AI results blindly.** Always cross-check outputs (charts, predictions, classifications) with raw data and domain knowledge. Look for mismatches or errors (e.g., all neutral reviews marked negative due to sarcasm).

#### 6. Thoughtful Feature Selection
- **Only use features that logically affect your target.** Avoid including irrelevant data (e.g., email font size) in predictive models. Use domain knowledge and feature importance tools to guide selection.

#### 7. Model Evaluation: Context Matters
- **R² and MSE tell different stories.** High R² with high MSE may mean your model fits the trend but misses the scale. Always interpret metrics in the context of your data and business goals.

#### 8. Cross-Verification is Essential
- **Validate all AI-generated outputs.** If a chart or prediction contradicts known data, investigate. Use multiple sources and manual checks.

#### 9. Cohesive Narrative
- **Analysis is more than numbers.** Connect your findings: How do sentiment trends, employee rankings, and risk scores relate? What story does the data tell?

#### 10. Use AI as a Tool, Not a Decision-Maker
- **Break down tasks, experiment, and interpret.** Don’t treat the AI as a black box. Ask questions, try variations, and use your judgment to guide the analysis.
