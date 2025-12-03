/**
 * Custom hook for resources
 * Uses static JSON data instead of API calls
 */

import { useState, useEffect } from 'react';
import resourcesData from '../data/resources.json';

export const useResources = (filters = {}) => {
  const [resources, setResources] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    try {
      setLoading(true);
      setError(null);
      
      let filteredResources = [...resourcesData];
      
      // Apply filters
      if (filters.category) {
        filteredResources = filteredResources.filter(r => r.category === filters.category);
      }
      if (filters.resource_type) {
        filteredResources = filteredResources.filter(r => r.resource_type === filters.resource_type);
      }
      if (filters.search) {
        const searchLower = filters.search.toLowerCase();
        filteredResources = filteredResources.filter(r => 
          r.title.toLowerCase().includes(searchLower) ||
          r.description.toLowerCase().includes(searchLower) ||
          r.tags.some(tag => tag.toLowerCase().includes(searchLower))
        );
      }
      
      setResources(filteredResources);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [JSON.stringify(filters)]);

  return { resources, loading, error };
};

export const useResource = (id) => {
  const [resource, setResource] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (id) {
      try {
        setLoading(true);
        setError(null);
        const foundResource = resourcesData.find(r => r.id === parseInt(id));
        if (foundResource) {
          setResource(foundResource);
        } else {
          setError('Resource not found');
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
  }, [id]);

  return { resource, loading, error };
};
