"""
Data Cache Module
Provides in-memory caching for frequently accessed data
"""
import time
from typing import Any, Optional
import pandas as pd

class DataCache:
    """Simple in-memory cache with TTL support"""
    _cache = {}
    _cache_ttl = 300  # 5 minutes default
    
    @classmethod
    def get(cls, key: str) -> Optional[Any]:
        """Get cached data if not expired"""
        if key in cls._cache:
            data, timestamp = cls._cache[key]
            if time.time() - timestamp < cls._cache_ttl:
                return data
            else:
                # Remove expired entry
                del cls._cache[key]
        return None
    
    @classmethod
    def set(cls, key: str, data: Any, ttl: Optional[int] = None):
        """Set cached data with optional custom TTL"""
        cache_ttl = ttl if ttl is not None else cls._cache_ttl
        cls._cache[key] = (data, time.time())
    
    @classmethod
    def clear(cls):
        """Clear all cached data"""
        cls._cache.clear()
    
    @classmethod
    def set_ttl(cls, ttl: int):
        """Set default TTL in seconds"""
        cls._cache_ttl = ttl
    
    @classmethod
    def get_stats(cls):
        """Get cache statistics"""
        total_entries = len(cls._cache)
        valid_entries = sum(
            1 for _, (_, ts) in cls._cache.items() 
            if time.time() - ts < cls._cache_ttl
        )
        return {
            'total': total_entries,
            'valid': valid_entries,
            'expired': total_entries - valid_entries
        }
