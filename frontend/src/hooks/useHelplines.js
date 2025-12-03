/**
 * Custom hook for helplines
 * Uses static JSON data instead of API calls
 */

import { useState, useEffect } from 'react';
import helplinesData from '../data/helplines.json';

export const useHelplines = (filters = {}) => {
  const [helplines, setHelplines] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    try {
      setLoading(true);
      setError(null);
      
      let filteredHelplines = [...helplinesData];
      
      // Apply filters
      if (filters.category) {
        filteredHelplines = filteredHelplines.filter(h => h.category === filters.category);
      }
      if (filters.is_24_7 !== undefined) {
        filteredHelplines = filteredHelplines.filter(h => h.is_24_7 === filters.is_24_7);
      }
      
      setHelplines(filteredHelplines);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [JSON.stringify(filters)]);

  return { helplines, loading, error };
};
