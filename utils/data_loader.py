import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
from typing import List, Dict
import json
import os

class DataLoader:
    def __init__(self, snowflake_connector):
        self.sf = snowflake_connector
    
    def load_tourism_statistics(self, csv_file: str):
        """Load tourism statistics from CSV file"""
        df = pd.read_csv(csv_file)
        # Perform necessary data cleaning and transformations
        df = self._clean_tourism_data(df)
        
        # Write to Snowflake
        write_pandas(
            self.sf.conn,
            df,
            'visitor_statistics',
            'tourism_stats'
        )
    
    def load_cultural_data(self, json_file: str):
        """Load cultural data from JSON file"""
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Write to Snowflake
        write_pandas(
            self.sf.conn,
            df,
            'state_culture',
            'cultural_data'
        )
    
    def load_destination_data(self, json_file: str):
        """Load destination data from JSON file"""
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Write to Snowflake
        write_pandas(
            self.sf.conn,
            df,
            'places',
            'destination_info'
        )
    
    def _clean_tourism_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and prepare tourism data"""
        # Remove any missing values
        df = df.dropna()
        
        # Convert numeric columns
        numeric_cols = ['domestic_visitors', 'foreign_visitors', 'total_visitors']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Calculate growth rate
        df['growth_rate'] = df.groupby('state_name')['total_visitors'].pct_change() * 100
        
        return df 

def load_state_overview(state_name=None):
    """Load state overview data from CSV"""
    df = pd.read_csv('data/states_overview.csv')
    if state_name:
        return df[df['state_name'] == state_name].to_dict('records')[0]
    return df.to_dict('records')

def load_tourism_stats(state_name=None):
    """Load tourism statistics from CSV"""
    df = pd.read_csv('data/tourism_stats.csv')
    if state_name:
        return {
            'yearly_stats': df[df['state_name'] == state_name].to_dict('records'),
            'monthly_distribution': load_monthly_stats(state_name),
            'impact_metrics': df[df['state_name'] == state_name].iloc[0].to_dict()
        }
    return df.to_dict('records')

def load_monthly_stats(state_name=None):
    """Load monthly statistics from CSV"""
    df = pd.read_csv('data/monthly_stats.csv')
    if state_name:
        state_data = df[df['state_name'] == state_name]
        return {
            'months': state_data['month'].to_list(),
            'visitors': state_data['visitors'].to_list(),
            'occupancy_rate': state_data['occupancy_rate'].to_list()
        }
    return df.to_dict('records')

def load_cultural_info(state_name=None):
    """Load cultural information from CSV"""
    df = pd.read_csv('data/cultural_info.csv')
    if state_name:
        state_data = df[df['state_name'] == state_name]
        
        # Get art forms
        art_forms = state_data[state_data['category'] == 'art_form'].apply(
            lambda x: {
                'name': x['name'],
                'description': x['description']
            }, axis=1
        ).to_list()
        
        # Get festivals
        festivals = state_data[state_data['category'] == 'festival'].apply(
            lambda x: {
                'name': x['name'],
                'description': x['description'],
                'month': x['month']
            }, axis=1
        ).to_list()
        
        # Get cuisines
        cuisines = state_data[state_data['category'] == 'cuisine'].apply(
            lambda x: {
                'name': x['name'],
                'description': x['description']
            }, axis=1
        ).to_list()
        
        return {
            'art_forms': art_forms,
            'festivals': festivals,
            'cuisines': cuisines
        }
    return df.to_dict('records')

def load_destinations(state_name=None):
    """Load destination information from CSV"""
    df = pd.read_csv('data/destinations.csv')
    if state_name:
        state_data = df[df['state_name'] == state_name]
        
        # Get popular destinations
        popular_data = state_data[state_data['category'] == 'popular']
        popular = [
            {
                'name': row['name'],
                'description': row['description'],
                'attractions': str(row['attractions']).split('|'),
                'best_time': row['best_time']
            }
            for _, row in popular_data.iterrows()
        ]
        
        # Get hidden gems
        hidden_data = state_data[state_data['category'] == 'hidden_gem']
        hidden_gems = [
            {
                'name': row['name'],
                'description': row['description'],
                'attractions': str(row['attractions']).split('|'),
                'best_time': row['best_time']
            }
            for _, row in hidden_data.iterrows()
        ]
        
        return {
            'popular': popular,
            'hidden_gems': hidden_gems
        }
    return df.to_dict('records')

def get_all_states():
    """Get list of all available states"""
    df = pd.read_csv('data/states_overview.csv')
    return df['state_name'].tolist()

def get_state_data(state_name):
    """Get all data for a specific state"""
    if not state_name:
        return {}
    
    return {
        'banner_image': load_state_overview(state_name).get('banner_image', ''),
        'overview': load_state_overview(state_name),
        'tourism_stats': load_tourism_stats(state_name),
        'cultural_info': load_cultural_info(state_name),
        'destinations': load_destinations(state_name)
    } 