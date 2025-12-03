/**
 * Custom hook for lessons
 * Uses static JSON data instead of API calls
 */

import { useState, useEffect } from 'react';
import lessonsData from '../data/lessons.json';

export const useLessons = (filters = {}) => {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    try {
      setLoading(true);
      setError(null);
      
      let filteredLessons = [...lessonsData];
      
      // Apply filters
      if (filters.category) {
        filteredLessons = filteredLessons.filter(l => l.category === filters.category);
      }
      if (filters.difficulty) {
        filteredLessons = filteredLessons.filter(l => l.difficulty === filters.difficulty);
      }
      if (filters.search) {
        const searchLower = filters.search.toLowerCase();
        filteredLessons = filteredLessons.filter(l => 
          l.title.toLowerCase().includes(searchLower) ||
          l.description.toLowerCase().includes(searchLower)
        );
      }
      
      setLessons(filteredLessons);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [JSON.stringify(filters)]);

  return { lessons, loading, error };
};

export const useLesson = (id) => {
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (id) {
      try {
        setLoading(true);
        setError(null);
        const foundLesson = lessonsData.find(l => l.id === parseInt(id));
        if (foundLesson) {
          setLesson(foundLesson);
        } else {
          setError('Lesson not found');
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
  }, [id]);

  return { lesson, loading, error };
};
