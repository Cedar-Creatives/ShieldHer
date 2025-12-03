/**
 * PrivacyGuide Component
 * Provides comprehensive privacy and safety guides for users.
 */

import React from 'react';
import './PrivacyGuide.css';

export const PrivacyGuide = () => {
  const guides = [
    {
      title: 'Blocking & Filtering',
      description: 'Learn how to block users and filter content on social media platforms to protect yourself from harassment.',
      icon: '🚫'
    },
    {
      title: 'Reporting Abuse',
      description: 'Step-by-step instructions on how to report abuse online and to authorities.',
      icon: '📢'
    },
    {
      title: 'Privacy Settings',
      description: 'Tips for securing your browser and account privacy settings across different platforms.',
      icon: '🔐'
    },
    {
      title: 'Safety Planning',
      description: 'Create a digital and physical safety plan to protect yourself and your information.',
      icon: '📋'
    }
  ];

  return (
    <div className="privacy-guide">
      <div className="privacy-guide__header">
        <h3 className="privacy-guide__title">Privacy & Safety Guides</h3>
        <p className="privacy-guide__description">
          Comprehensive guides to help you stay safe online and protect your privacy
        </p>
      </div>

      <div className="privacy-guide__grid">
        {guides.map((guide, index) => (
          <div key={index} className="privacy-guide__card">
            <div className="privacy-guide__card-icon">{guide.icon}</div>
            <h4 className="privacy-guide__card-title">{guide.title}</h4>
            <p className="privacy-guide__card-description">{guide.description}</p>
          </div>
        ))}
      </div>

      <div className="privacy-guide__emergency">
        <p className="privacy-guide__emergency-text">
          <strong>In immediate danger?</strong> Call 911 or the National Domestic Violence Hotline: 1-800-799-7233
        </p>
      </div>
    </div>
  );
};
