/**
 * Custom hook for handling donation submissions.
 */

import { useState } from 'react';
import { apiRequest } from '../utils/api';

export const useDonations = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [donation, setDonation] = useState(null);

  const submitDonation = async (donationData) => {
    setLoading(true);
    setError(null);
    setSuccess(false);
    setDonation(null);

    try {
      // DEMO MODE: Mock successful donation for pitch presentation
      // TODO: Replace with actual API call after backend deployment is stable
      
      // Simulate network delay
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      // Generate mock confirmation code
      const mockCode = `DON-${new Date().getFullYear()}-${Math.random().toString(36).substring(2, 10).toUpperCase()}`;
      
      // Create mock donation response
      const mockDonation = {
        id: Math.floor(Math.random() * 10000),
        confirmation_code: mockCode,
        amount: donationData.amount.toFixed(2),
        currency: donationData.currency || 'USD',
        status: 'completed',
        message: donationData.message || '',
        created_at: new Date().toISOString()
      };

      setDonation(mockDonation);
      setSuccess(true);
      
      return {
        success: true,
        message: 'Thank you for your donation!',
        donation: mockDonation
      };

      /* PRODUCTION CODE - Uncomment when backend is ready:
      const response = await apiRequest('/api/donations/', {
        method: 'POST',
        body: JSON.stringify(donationData)
      });

      setDonation(response.donation);
      setSuccess(true);
      return response;
      */
    } catch (err) {
      console.error('Error submitting donation:', err);
      setError(err.message || 'Failed to process donation');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setLoading(false);
    setError(null);
    setSuccess(false);
    setDonation(null);
  };

  return {
    submitDonation,
    loading,
    error,
    success,
    donation,
    reset
  };
};

/**
 * Hook for retrieving donation by confirmation code
 */
export const useDonationLookup = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [donation, setDonation] = useState(null);

  const lookupDonation = async (confirmationCode) => {
    setLoading(true);
    setError(null);
    setDonation(null);

    try {
      // DEMO MODE: Mock donation lookup
      await new Promise(resolve => setTimeout(resolve, 800));
      
      // Return mock donation data
      const mockDonation = {
        id: Math.floor(Math.random() * 10000),
        confirmation_code: confirmationCode,
        amount: '50.00',
        currency: 'USD',
        status: 'completed',
        message: 'Thank you for supporting ShieldHer!',
        created_at: new Date().toISOString()
      };
      
      setDonation(mockDonation);
      return mockDonation;

      /* PRODUCTION CODE - Uncomment when backend is ready:
      const data = await apiRequest(`/api/donations/${confirmationCode}/`);
      setDonation(data);
      return data;
      */
    } catch (err) {
      console.error('Error looking up donation:', err);
      setError(err.message || 'Donation not found');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return {
    lookupDonation,
    loading,
    error,
    donation
  };
};
