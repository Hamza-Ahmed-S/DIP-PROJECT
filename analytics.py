"""
Analytics and Feedback System for Bioinformatics Web App
Handles usage tracking, ratings, and feedback collection
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class Analytics:
    """Manages analytics data and feedback collection"""
    
    def __init__(self, data_file: str = "data/analytics.json"):
        self.data_file = data_file
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """Load analytics data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._get_default_data()
        else:
            return self._get_default_data()
    
    def _get_default_data(self) -> Dict:
        """Get default analytics structure"""
        return {
            "total_visits": 0,
            "features": {
                "atp_hydrolysis": {"count": 0, "ratings": [], "feedback": []},
                "dna_analysis": {"count": 0, "ratings": [], "feedback": []},
                "advanced_analysis": {"count": 0, "ratings": [], "feedback": []},
                "n50_calculator": {"count": 0, "ratings": [], "feedback": []}
            },
            "general_feedback": [],
            "last_updated": None
        }
    
    def _save_data(self):
        """Save analytics data to JSON file"""
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        
        # Update timestamp
        self.data["last_updated"] = datetime.now().isoformat()
        
        # Save to file
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def increment_visit(self):
        """Increment total visit counter"""
        self.data["total_visits"] += 1
        self._save_data()
    
    def track_feature_usage(self, feature_name: str):
        """Track usage of a specific feature"""
        if feature_name in self.data["features"]:
            self.data["features"][feature_name]["count"] += 1
            self._save_data()
    
    def add_rating(self, feature_name: str, rating: int, feedback_text: str = ""):
        """Add a rating and optional feedback for a feature"""
        if feature_name in self.data["features"]:
            # Add rating (1-5 stars)
            self.data["features"][feature_name]["ratings"].append({
                "rating": rating,
                "timestamp": datetime.now().isoformat()
            })
            
            # Add feedback if provided
            if feedback_text.strip():
                self.data["features"][feature_name]["feedback"].append({
                    "text": feedback_text.strip(),
                    "rating": rating,
                    "timestamp": datetime.now().isoformat()
                })
            
            self._save_data()
    
    def add_general_feedback(self, feedback_text: str, rating: int = None):
        """Add general feedback about the app"""
        feedback_entry = {
            "text": feedback_text.strip(),
            "timestamp": datetime.now().isoformat()
        }
        if rating is not None:
            feedback_entry["rating"] = rating
        
        self.data["general_feedback"].append(feedback_entry)
        self._save_data()
    
    def get_total_analyses(self) -> int:
        """Get total number of analyses across all features"""
        return sum(feature["count"] for feature in self.data["features"].values())
    
    def get_feature_stats(self, feature_name: str) -> Dict:
        """Get statistics for a specific feature"""
        if feature_name not in self.data["features"]:
            return {}
        
        feature_data = self.data["features"][feature_name]
        ratings = [r["rating"] for r in feature_data["ratings"]]
        
        stats = {
            "count": feature_data["count"],
            "total_ratings": len(ratings),
            "average_rating": sum(ratings) / len(ratings) if ratings else 0,
            "feedback_count": len(feature_data["feedback"])
        }
        
        return stats
    
    def get_overall_stats(self) -> Dict:
        """Get overall statistics across all features"""
        all_ratings = []
        total_feedback = 0
        
        for feature_data in self.data["features"].values():
            all_ratings.extend([r["rating"] for r in feature_data["ratings"]])
            total_feedback += len(feature_data["feedback"])
        
        return {
            "total_visits": self.data["total_visits"],
            "total_analyses": self.get_total_analyses(),
            "total_ratings": len(all_ratings),
            "average_rating": sum(all_ratings) / len(all_ratings) if all_ratings else 0,
            "total_feedback": total_feedback
        }
    
    def get_most_popular_feature(self) -> str:
        """Get the name of the most used feature"""
        if not self.data["features"]:
            return "None"
        
        max_count = 0
        most_popular = "None"
        
        for feature_name, feature_data in self.data["features"].items():
            if feature_data["count"] > max_count:
                max_count = feature_data["count"]
                most_popular = feature_name
        
        return most_popular.replace("_", " ").title()
    
    def get_recent_feedback(self, limit: int = 5) -> List[Dict]:
        """Get recent feedback across all features"""
        all_feedback = []
        
        # Collect feedback from all features
        for feature_name, feature_data in self.data["features"].items():
            for fb in feature_data["feedback"]:
                fb_copy = fb.copy()
                fb_copy["feature"] = feature_name
                all_feedback.append(fb_copy)
        
        # Add general feedback
        for fb in self.data["general_feedback"]:
            fb_copy = fb.copy()
            fb_copy["feature"] = "general"
            all_feedback.append(fb_copy)
        
        # Sort by timestamp (most recent first)
        all_feedback.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return all_feedback[:limit]
    
    def get_feature_usage_distribution(self) -> Dict[str, int]:
        """Get usage count for each feature"""
        return {
            feature_name.replace("_", " ").title(): feature_data["count"]
            for feature_name, feature_data in self.data["features"].items()
        }
