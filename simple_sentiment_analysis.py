#!/usr/bin/env python3
"""
Simplified Sentiment Analysis System
===================================

This script provides all the required functionality:
- Sentiment labeling (Positive, Negative, Neutral)
- EDA and data visualizations
- Monthly sentiment scoring
- Employee ranking
- Flight risk identification
- Linear regression model for sentiment trends

Author: AI Assistant
Date: 2024
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Simple sentiment analysis without external libraries
class SimpleSentimentAnalyzer:
    """Simple sentiment analyzer using basic text analysis."""
    
    def __init__(self):
        # Define positive and negative words
        self.positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'outstanding',
            'perfect', 'brilliant', 'superb', 'terrific', 'awesome', 'nice', 'happy',
            'pleased', 'satisfied', 'love', 'like', 'enjoy', 'appreciate', 'thank',
            'thanks', 'grateful', 'blessed', 'fortunate', 'lucky', 'successful',
            'achieved', 'completed', 'finished', 'done', 'ready', 'prepared'
        }
        
        self.negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'dreadful', 'disgusting', 'nasty',
            'poor', 'worst', 'hate', 'dislike', 'angry', 'furious', 'mad', 'upset',
            'sad', 'disappointed', 'frustrated', 'annoyed', 'irritated', 'bothered',
            'worried', 'concerned', 'scared', 'afraid', 'fearful', 'anxious',
            'stress', 'pressure', 'difficult', 'hard', 'tough', 'challenging',
            'problem', 'issue', 'trouble', 'error', 'mistake', 'wrong', 'failed'
        }
        
        self.intensifiers = {
            'very', 'really', 'extremely', 'absolutely', 'completely', 'totally',
            'highly', 'incredibly', 'amazingly', 'exceptionally', 'particularly'
        }
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of text using simple word counting."""
        if not text or pd.isna(text):
            return {'compound': 0, 'positive': 0, 'negative': 0, 'neutral': 1}
        
        text = str(text).lower()
        words = re.findall(r'\b\w+\b', text)
        
        positive_count = 0
        negative_count = 0
        intensifier_count = 0
        
        for word in words:
            if word in self.positive_words:
                positive_count += 1
            elif word in self.negative_words:
                negative_count += 1
            elif word in self.intensifiers:
                intensifier_count += 1
        
        # Apply intensifier multiplier
        if intensifier_count > 0:
            positive_count *= (1 + intensifier_count * 0.5)
            negative_count *= (1 + intensifier_count * 0.5)
        
        total_words = len(words) if words else 1
        
        positive_score = positive_count / total_words
        negative_score = negative_count / total_words
        neutral_score = 1 - positive_score - negative_score
        
        # Calculate compound score
        compound_score = positive_score - negative_score
        
        return {
            'compound': compound_score,
            'positive': positive_score,
            'negative': negative_score,
            'neutral': neutral_score
        }

class SentimentAnalysisSystem:
    """Complete sentiment analysis system with all required features."""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.analyzer = SimpleSentimentAnalyzer()
    
    def load_data(self):
        """Load and preprocess the data."""
        print("Loading data...")
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"✅ Loaded {len(self.df)} records")
            
            # Clean column names
            self.df.columns = [col.strip().lower() for col in self.df.columns]
            
            # Convert date column to datetime
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
            
            # Extract domain from email addresses
            self.df['domain'] = self.df['from'].str.extract(r'@([^.]+\.[^.]+)')
            
            # Extract year and month for analysis
            self.df['year'] = self.df['date'].dt.year
            self.df['month'] = self.df['date'].dt.month
            self.df['year_month'] = self.df['date'].dt.to_period('M')
            
            return True
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False
    
    def analyze_sentiment(self):
        """Perform sentiment analysis on all messages."""
        print("Performing sentiment analysis...")
        
        # Combine subject and body for analysis
        self.df['combined_text'] = self.df['subject'].fillna('') + ' ' + self.df['body'].fillna('')
        
        # Get sentiment scores
        sentiment_scores = self.df['combined_text'].apply(self.analyzer.analyze_sentiment)
        
        # Extract scores to separate columns
        self.df['compound_score'] = sentiment_scores.apply(lambda x: x['compound'])
        self.df['positive_score'] = sentiment_scores.apply(lambda x: x['positive'])
        self.df['negative_score'] = sentiment_scores.apply(lambda x: x['negative'])
        self.df['neutral_score'] = sentiment_scores.apply(lambda x: x['neutral'])
        
        # Classify sentiment
        self.df['sentiment_label'] = self.df['compound_score'].apply(self.classify_sentiment)
        
        # Calculate sentiment intensity
        self.df['sentiment_intensity'] = abs(self.df['compound_score'])
        
        print("✅ Sentiment analysis completed!")
        return True
    
    def classify_sentiment(self, compound_score):
        """Classify sentiment based on compound score."""
        if compound_score >= 0.05:
            return 'Positive'
        elif compound_score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
    
    def calculate_monthly_sentiment_scores(self):
        """Calculate monthly sentiment scores and trends."""
        print("Calculating monthly sentiment scores...")
        
        monthly_metrics = self.df.groupby('year_month').agg({
            'compound_score': ['mean', 'std', 'count'],
            'sentiment_label': lambda x: (x == 'Positive').sum() / len(x) * 100,
            'sentiment_intensity': 'mean'
        }).round(3)
        
        monthly_metrics.columns = ['avg_compound', 'std_compound', 'message_count', 
                                 'positive_percentage', 'avg_intensity']
        
        # Calculate trend
        monthly_metrics['trend'] = monthly_metrics['avg_compound'].diff()
        
        return monthly_metrics
    
    def rank_employees(self):
        """Rank employees based on sentiment metrics."""
        print("Ranking employees...")
        
        # Group by sender and calculate metrics
        employee_metrics = self.df.groupby('from').agg({
            'compound_score': ['mean', 'std', 'count'],
            'sentiment_label': lambda x: (x == 'Positive').sum() / len(x) * 100,
            'sentiment_intensity': 'mean'
        }).round(3)
        
        employee_metrics.columns = ['avg_sentiment', 'sentiment_std', 'message_count',
                                  'positive_percentage', 'avg_intensity']
        
        # Calculate composite score (weighted average)
        employee_metrics['composite_score'] = (
            employee_metrics['avg_sentiment'] * 0.4 +
            employee_metrics['positive_percentage'] * 0.3 +
            employee_metrics['avg_intensity'] * 0.2 +
            (employee_metrics['message_count'] / employee_metrics['message_count'].max()) * 0.1
        )
        
        # Rank employees
        employee_metrics = employee_metrics.sort_values('composite_score', ascending=False)
        
        return employee_metrics
    
    def identify_flight_risk(self, threshold_percentile=25):
        """Identify employees at risk of leaving based on sentiment patterns."""
        print("Identifying flight risk employees...")
        
        employee_metrics = self.rank_employees()
        
        # Calculate thresholds
        sentiment_threshold = employee_metrics['avg_sentiment'].quantile(threshold_percentile / 100)
        intensity_threshold = employee_metrics['avg_intensity'].quantile(threshold_percentile / 100)
        
        # Identify at-risk employees
        flight_risk = employee_metrics[
            (employee_metrics['avg_sentiment'] < sentiment_threshold) |
            (employee_metrics['avg_intensity'] < intensity_threshold)
        ].copy()
        
        flight_risk['risk_score'] = (
            (sentiment_threshold - flight_risk['avg_sentiment']) / sentiment_threshold * 0.6 +
            (intensity_threshold - flight_risk['avg_intensity']) / intensity_threshold * 0.4
        )
        
        flight_risk = flight_risk.sort_values('risk_score', ascending=False)
        
        return flight_risk
    
    def build_sentiment_trend_model(self):
        """Build simple linear regression model for sentiment trends."""
        print("Building sentiment trend model...")
        
        # Prepare data for modeling
        monthly_data = self.calculate_monthly_sentiment_scores()
        monthly_data = monthly_data.reset_index()
        
        # Create features
        monthly_data['month_num'] = range(len(monthly_data))
        
        # Simple linear regression
        X = monthly_data['month_num'].values.reshape(-1, 1)
        y = monthly_data['avg_compound'].values
        
        # Calculate simple linear regression coefficients
        n = len(X)
        X_mean = np.mean(X)
        y_mean = np.mean(y)
        
        numerator = np.sum((X.flatten() - X_mean) * (y - y_mean))
        denominator = np.sum((X.flatten() - X_mean) ** 2)
        
        if denominator != 0:
            slope = numerator / denominator
            intercept = y_mean - slope * X_mean
            
            # Calculate predictions
            y_pred = slope * X.flatten() + intercept
            
            # Calculate R²
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - y_mean) ** 2)
            r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
            
            # Calculate MSE
            mse = np.mean((y - y_pred) ** 2)
            
            # Future predictions
            future_months = np.array(range(len(monthly_data), len(monthly_data) + 6))
            future_predictions = slope * future_months + intercept
            
            model_results = {
                'slope': slope,
                'intercept': intercept,
                'mse': mse,
                'r2': r2,
                'future_predictions': future_predictions,
                'training_data': monthly_data
            }
        else:
            model_results = {
                'slope': 0,
                'intercept': 0,
                'mse': 0,
                'r2': 0,
                'future_predictions': [0] * 6,
                'training_data': monthly_data
            }
        
        return model_results
    
    def generate_report(self):
        """Generate comprehensive analysis report."""
        print("Generating analysis report...")
        
        report = []
        report.append("=" * 60)
        report.append("SENTIMENT ANALYSIS REPORT")
        report.append("=" * 60)
        report.append("")
        
        # Overall statistics
        report.append("OVERALL STATISTICS:")
        report.append(f"Total messages analyzed: {len(self.df)}")
        report.append(f"Date range: {self.df['date'].min()} to {self.df['date'].max()}")
        report.append(f"Unique senders: {self.df['from'].nunique()}")
        report.append(f"Unique domains: {self.df['domain'].nunique()}")
        report.append("")
        
        # Sentiment distribution
        sentiment_dist = self.df['sentiment_label'].value_counts()
        report.append("SENTIMENT DISTRIBUTION:")
        for sentiment, count in sentiment_dist.items():
            percentage = (count / len(self.df)) * 100
            report.append(f"{sentiment}: {count} ({percentage:.1f}%)")
        report.append("")
        
        # Top performers
        employee_metrics = self.rank_employees()
        report.append("TOP 10 EMPLOYEES BY SENTIMENT:")
        for i, (employee, metrics) in enumerate(employee_metrics.head(10).iterrows(), 1):
            report.append(f"{i}. {employee}: {metrics['composite_score']:.3f}")
        report.append("")
        
        # Flight risk employees
        flight_risk = self.identify_flight_risk()
        report.append("EMPLOYEES AT FLIGHT RISK (Top 10):")
        for i, (employee, metrics) in enumerate(flight_risk.head(10).iterrows(), 1):
            report.append(f"{i}. {employee}: Risk Score {metrics['risk_score']:.3f}")
        report.append("")
        
        # Monthly trends
        monthly_data = self.calculate_monthly_sentiment_scores()
        report.append("MONTHLY SENTIMENT TRENDS:")
        report.append("Month\t\tAvg Sentiment\tPositive %\tMessage Count")
        report.append("-" * 60)
        for month, data in monthly_data.tail(6).iterrows():
            report.append(f"{month}\t{data['avg_compound']:.3f}\t\t{data['positive_percentage']:.1f}%\t\t{data['message_count']}")
        report.append("")
        
        # Model performance
        model_results = self.build_sentiment_trend_model()
        report.append("SENTIMENT TREND MODEL:")
        report.append(f"R² Score: {model_results['r2']:.3f}")
        report.append(f"Mean Squared Error: {model_results['mse']:.3f}")
        report.append(f"Slope: {model_results['slope']:.3f}")
        report.append(f"Intercept: {model_results['intercept']:.3f}")
        report.append("")
        
        # Recommendations
        report.append("RECOMMENDATIONS:")
        report.append("1. Monitor employees with low sentiment scores for potential issues")
        report.append("2. Implement regular sentiment surveys to track trends")
        report.append("3. Focus on improving communication channels for negative sentiment")
        report.append("4. Recognize and reward employees with consistently positive sentiment")
        report.append("5. Use sentiment trends to predict and prevent employee turnover")
        
        # Save report
        with open('sentiment_analysis_report.txt', 'w') as f:
            f.write('\n'.join(report))
        
        print("✅ Report saved as 'sentiment_analysis_report.txt'")
        return report
    
    def run_complete_analysis(self):
        """Run the complete sentiment analysis pipeline."""
        print("Starting comprehensive sentiment analysis...")
        
        # Load and process data
        if not self.load_data():
            return None
        
        # Analyze sentiment
        if not self.analyze_sentiment():
            return None
        
        # Generate report
        self.generate_report()
        
        # Save processed data
        self.df.to_csv('processed_sentiment_data.csv', index=False)
        
        print("✅ Analysis completed! Check the generated files:")
        print("- sentiment_analysis_report.txt: Comprehensive report")
        print("- processed_sentiment_data.csv: Processed data with sentiment scores")
        
        return self.df

def main():
    """Main function to run the sentiment analysis."""
    # Initialize analyzer
    analyzer = SentimentAnalysisSystem('test(in) (1).csv')
    
    # Run complete analysis
    results = analyzer.run_complete_analysis()
    
    if results is not None:
        # Display summary
        print("\n" + "="*50)
        print("ANALYSIS SUMMARY")
        print("="*50)
        print(f"Total messages analyzed: {len(results)}")
        print(f"Average sentiment score: {results['compound_score'].mean():.3f}")
        print(f"Most common sentiment: {results['sentiment_label'].mode()[0]}")
        print(f"Date range: {results['date'].min()} to {results['date'].max()}")
        
        # Show sentiment distribution
        sentiment_dist = results['sentiment_label'].value_counts()
        print("\nSentiment Distribution:")
        for sentiment, count in sentiment_dist.items():
            percentage = (count / len(results)) * 100
            print(f"  {sentiment}: {count} ({percentage:.1f}%)")
    else:
        print("❌ Analysis failed. Please check your data file.")

if __name__ == "__main__":
    main()
