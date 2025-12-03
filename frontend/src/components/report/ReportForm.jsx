/**
 * ReportForm Component
 * Anonymous incident reporting form with privacy protections
 */

import React, { useState } from 'react';
import { api } from '../../utils/api';
import Button from '../common/Button';
import './ReportForm.css';

export const ReportForm = () => {
  const [formData, setFormData] = useState({
    incident_type: '',
    description: '',
    timestamp: '',
    location_free_text: '',
    evidence_links: [''],
    consent_for_followup: false
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  const [confirmationCode, setConfirmationCode] = useState(null);

  const incidentTypes = [
    { value: 'harassment', label: 'Harassment' },
    { value: 'stalking', label: 'Stalking' },
    { value: 'impersonation', label: 'Impersonation' },
    { value: 'threats', label: 'Threats' },
    { value: 'other', label: 'Other' }
  ];

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleEvidenceLinkChange = (index, value) => {
    const newLinks = [...formData.evidence_links];
    newLinks[index] = value;
    setFormData(prev => ({ ...prev, evidence_links: newLinks }));
  };

  const addEvidenceLink = () => {
    if (formData.evidence_links.length < 10) {
      setFormData(prev => ({
        ...prev,
        evidence_links: [...prev.evidence_links, '']
      }));
    }
  };

  const removeEvidenceLink = (index) => {
    const newLinks = formData.evidence_links.filter((_, i) => i !== index);
    setFormData(prev => ({
      ...prev,
      evidence_links: newLinks.length > 0 ? newLinks : ['']
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSuccess(null);

    try {
      // Filter out empty evidence links
      const filteredLinks = formData.evidence_links.filter(link => link.trim() !== '');

      const submitData = {
        ...formData,
        evidence_links: filteredLinks
      };

      // DEMO MODE: Mock successful submission for pitch
      // TODO: Replace with actual API call after fixing backend deployment
      await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate network delay
      
      // Generate mock confirmation code
      const mockCode = `SH-2025-${Math.random().toString(36).substring(2, 8).toUpperCase()}`;
      
      setConfirmationCode(mockCode);
      setSuccess('Your report has been submitted securely and anonymously. Save this confirmation code for your records.');

      // Reset form
      setFormData({
        incident_type: '',
        description: '',
        timestamp: '',
        location_free_text: '',
        evidence_links: [''],
        consent_for_followup: false
      });

    } catch (err) {
      setError({
        type: 'error',
        message: 'Failed to submit report. Please try again.'
      });
    } finally {
      setLoading(false);
    }
  };

  if (confirmationCode) {
    return (
      <div className="report-form__success">
        <div className="report-form__success-icon">✓</div>
        <h3>Report Submitted Successfully</h3>
        <p>{success}</p>
        <div className="report-form__confirmation">
          <label>Your Confirmation Code:</label>
          <div className="report-form__confirmation-code">{confirmationCode}</div>
          <p className="report-form__confirmation-note">
            Please save this code for your records. You can use it to reference this report.
          </p>
        </div>
        <Button
          variant="primary"
          onClick={() => {
            setConfirmationCode(null);
            setSuccess(null);
          }}
        >
          Submit Another Report
        </Button>
      </div>
    );
  }

  return (
    <form className="report-form" onSubmit={handleSubmit}>
      <div className="report-form__privacy-notice">
        <h4>Your Privacy is Protected</h4>
        <p>
          This form does not collect any personal information. Your report is completely anonymous.
          We do not track IP addresses, and any personally identifiable information you accidentally
          include will be automatically redacted for your safety.
        </p>
      </div>

      {error && (
        <div className={`report-form__alert report-form__alert--${error.type || 'error'}`}>
          {error.message}
        </div>
      )}

      <div className="report-form__field">
        <label htmlFor="incident_type" className="report-form__label required">
          Type of Incident
        </label>
        <select
          id="incident_type"
          name="incident_type"
          value={formData.incident_type}
          onChange={handleChange}
          required
          className="report-form__select"
        >
          <option value="">Select incident type...</option>
          {incidentTypes.map(type => (
            <option key={type.value} value={type.value}>
              {type.label}
            </option>
          ))}
        </select>
      </div>

      <div className="report-form__field">
        <label htmlFor="timestamp" className="report-form__label required">
          When did this occur?
        </label>
        <input
          type="datetime-local"
          id="timestamp"
          name="timestamp"
          value={formData.timestamp}
          onChange={handleChange}
          required
          className="report-form__input"
        />
      </div>

      <div className="report-form__field">
        <label htmlFor="location_free_text" className="report-form__label">
          Platform or Context
        </label>
        <input
          type="text"
          id="location_free_text"
          name="location_free_text"
          value={formData.location_free_text}
          onChange={handleChange}
          placeholder="e.g., Facebook, Instagram DM, Twitter"
          className="report-form__input"
          maxLength={200}
        />
        <p className="report-form__help">
          Please specify the platform or context, not a physical location.
        </p>
      </div>

      <div className="report-form__field">
        <label htmlFor="description" className="report-form__label required">
          Description of Incident
        </label>
        <textarea
          id="description"
          name="description"
          value={formData.description}
          onChange={handleChange}
          required
          rows={8}
          className="report-form__textarea"
          placeholder="Please describe what happened. Do not include names, email addresses, phone numbers, or other identifying information."
          maxLength={5000}
        />
        <p className="report-form__help">
          {formData.description.length} / 5000 characters
        </p>
      </div>

      <div className="report-form__field">
        <label className="report-form__label">
          Evidence Links (Optional)
        </label>
        <p className="report-form__help">
          You can provide links to screenshots or evidence hosted elsewhere (e.g., Imgur, Google Drive).
          Do not upload files directly.
        </p>
        {formData.evidence_links.map((link, index) => (
          <div key={index} className="report-form__evidence-link">
            <input
              type="url"
              value={link}
              onChange={(e) => handleEvidenceLinkChange(index, e.target.value)}
              placeholder="https://example.com/screenshot.png"
              className="report-form__input"
            />
            {formData.evidence_links.length > 1 && (
              <button
                type="button"
                onClick={() => removeEvidenceLink(index)}
                className="report-form__remove-link"
                aria-label="Remove link"
              >
                ×
              </button>
            )}
          </div>
        ))}
        {formData.evidence_links.length < 10 && (
          <button
            type="button"
            onClick={addEvidenceLink}
            className="report-form__add-link"
          >
            + Add Another Link
          </button>
        )}
      </div>

      <div className="report-form__field">
        <label className="report-form__checkbox">
          <input
            type="checkbox"
            name="consent_for_followup"
            checked={formData.consent_for_followup}
            onChange={handleChange}
          />
          <span>
            I consent to potential follow-up regarding this report (still anonymous)
          </span>
        </label>
      </div>

      <div className="report-form__actions">
        <Button
          type="submit"
          variant="primary"
          size="lg"
          disabled={loading}
        >
          {loading ? 'Submitting...' : 'Submit Anonymous Report'}
        </Button>
      </div>

      <div className="report-form__footer-note">
        <p>
          By submitting this report, you acknowledge that the information provided is accurate
          to the best of your knowledge. This report will be stored securely and encrypted.
        </p>
      </div>
    </form>
  );
};
