import snowflake.connector
from typing import Dict, List, Any
import os
from dotenv import load_dotenv

load_dotenv()

class SnowflakeConnector:
    def __init__(self):
        self.conn = snowflake.connector.connect(
            user=os.getenv('SNOWFLAKE_USER'),
            password=os.getenv('SNOWFLAKE_PASSWORD'),
            account=os.getenv('SNOWFLAKE_ACCOUNT'),
            warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
            database='tourism_insights'
        )
        self.cursor = self.conn.cursor()
    
    def get_state_statistics(self, state_name: str) -> Dict[str, Any]:
        """Get tourism statistics for a specific state"""
        query = """
        SELECT *
        FROM tourism_stats.visitor_statistics
        WHERE state_name = %s
        ORDER BY year DESC
        """
        self.cursor.execute(query, (state_name,))
        results = self.cursor.fetchall()
        return self._format_statistics(results)
    
    def get_cultural_info(self, state_name: str) -> Dict[str, List]:
        """Get cultural information for a specific state"""
        query = """
        SELECT art_forms, festivals, cuisines, heritage_sites
        FROM cultural_data.state_culture
        WHERE state_name = %s
        """
        self.cursor.execute(query, (state_name,))
        result = self.cursor.fetchone()
        return {
            'art_forms': result[0],
            'festivals': result[1],
            'cuisines': result[2],
            'heritage_sites': result[3]
        } if result else {}
    
    def get_destinations(self, state_name: str) -> List[Dict[str, Any]]:
        """Get tourist destinations for a specific state"""
        query = """
        SELECT place_name, description, best_time_to_visit, category, attractions
        FROM destination_info.places
        WHERE state_id = (
            SELECT state_id 
            FROM tourism_stats.visitor_statistics 
            WHERE state_name = %s 
            LIMIT 1
        )
        """
        self.cursor.execute(query, (state_name,))
        results = self.cursor.fetchall()
        return [
            {
                'name': r[0],
                'description': r[1],
                'best_time': r[2],
                'category': r[3],
                'attractions': r[4]
            }
            for r in results
        ]
    
    def _format_statistics(self, results: List[tuple]) -> Dict[str, Any]:
        """Format tourism statistics into a structured dictionary"""
        return {
            'yearly_stats': [
                {
                    'year': r[2],
                    'domestic': r[3],
                    'foreign': r[4],
                    'total': r[5],
                    'growth': r[6]
                }
                for r in results
            ],
            'latest': {
                'year': results[0][2],
                'domestic': results[0][3],
                'foreign': results[0][4],
                'total': results[0][5],
                'growth': results[0][6]
            } if results else {}
        }
    
    def close(self):
        """Close the Snowflake connection"""
        self.cursor.close()
        self.conn.close() 