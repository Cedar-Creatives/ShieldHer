/**
 * Home Page
 * Main dashboard with hero section, quick links, and feature highlights.
 */

import React from 'react';
import { Link } from 'react-router-dom';
import { Card } from '../components/common/Card';
import { Button } from '../components/common/Button';
import './Home.css';

export const Home = () => {
  const quickLinks = [
    {
      title: 'Emergency Helplines',
      description: '24/7 crisis support numbers',
      icon: '📞',
      link: '/emergency/helplines',
      color: 'danger'
    },
    {
      title: 'Digital Literacy',
      description: 'Learn to stay safe online',
      icon: '📚',
      link: '/lessons',
      color: 'primary'
    },
    {
      title: 'Anonymous Reporting',
      description: 'Report abuse privately',
      icon: '📝',
      link: '/report',
      color: 'secondary'
    },
    {
      title: 'Safety Settings',
      description: 'Configure your privacy',
      icon: '🛡️',
      link: '/settings/safety',
      color: 'success'
    }
  ];

  const safetyTips = [
    'Use private browsing mode when accessing sensitive information',
    'Enable panic exit shortcut in Settings for quick site exit',
    'Clear your browsing history regularly',
    'Create a safety plan and keep it updated',
    'Trust your instincts - if something feels wrong, seek help'
  ];

  return (
    <div className="home">
      {/* Hero Section */}
      <section className="home__hero">
        <div className="home__hero-content">
          <h1 className="home__hero-title">
            You Are Not Alone
          </h1>
          <p className="home__hero-subtitle">
            ShieldHer provides safe, anonymous support and resources for survivors of domestic violence.
          </p>
          <div className="home__hero-actions">
            <Link to="/emergency/helplines">
              <Button variant="primary" size="lg">
                Get Help Now
              </Button>
            </Link>
            <Link to="/lessons">
              <Button variant="secondary" size="lg">
                Learn More
              </Button>
            </Link>
          </div>
          <div className="home__hero-emergency">
            <p className="home__hero-emergency-text">
              <strong>In immediate danger?</strong> Call 911 or the National Domestic Violence Hotline
            </p>
            <a href="tel:1-800-799-7233" className="home__hero-emergency-number">
              📞 1-800-799-7233
            </a>
          </div>
        </div>
      </section>

      {/* Quick Links */}
      <section className="home__section">
        <div className="home__container">
          <h2 className="home__section-title">Quick Access</h2>
          <div className="home__quick-links">
            {quickLinks.map((link, index) => (
              <Link key={index} to={link.link} className="home__quick-link">
                <Card className={`home__quick-link-card home__quick-link-card--${link.color}`}>
                  <span className="home__quick-link-icon">{link.icon}</span>
                  <h3 className="home__quick-link-title">{link.title}</h3>
                  <p className="home__quick-link-description">{link.description}</p>
                </Card>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Safety Tips */}
      <section className="home__section home__section--alt">
        <div className="home__container">
          <h2 className="home__section-title">Safety Tips</h2>
          <Card>
            <ul className="home__tips-list">
              {safetyTips.map((tip, index) => (
                <li key={index} className="home__tip-item">
                  <span className="home__tip-icon">💡</span>
                  <span className="home__tip-text">{tip}</span>
                </li>
              ))}
            </ul>
          </Card>
        </div>
      </section>

      {/* Features Overview */}
      <section className="home__section">
        <div className="home__container">
          <h2 className="home__section-title">How ShieldHer Helps</h2>
          <div className="home__features">
            <div className="home__feature">
              <div className="home__feature-icon">🔒</div>
              <h3 className="home__feature-title">100% Private</h3>
              <p className="home__feature-text">
                All settings stored locally. No tracking, no data collection.
              </p>
            </div>
            <div className="home__feature">
              <div className="home__feature-icon">🆘</div>
              <h3 className="home__feature-title">Emergency Access</h3>
              <p className="home__feature-text">
                Quick access to helplines and resources when you need them most.
              </p>
            </div>
            <div className="home__feature">
              <div className="home__feature-icon">📚</div>
              <h3 className="home__feature-title">Education</h3>
              <p className="home__feature-text">
                Learn digital safety skills to protect yourself online.
              </p>
            </div>
            <div className="home__feature">
              <div className="home__feature-icon">💜</div>
              <h3 className="home__feature-title">Support</h3>
              <p className="home__feature-text">
                Connect with resources and support organizations.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Donation CTA */}
      <section className="home__section home__section--donate">
        <div className="home__container">
          <Card className="home__donate-card">
            <div className="home__donate-content">
              <div className="home__donate-icon">💝</div>
              <h2 className="home__donate-title">Help Us Help Others</h2>
              <p className="home__donate-description">
                Your donation helps us provide free, safe resources to survivors of domestic violence. 
                Every contribution makes a difference in someone's life.
              </p>
              <div className="home__donate-impact">
                <div className="home__donate-impact-item">
                  <strong>$10</strong> provides digital literacy resources
                </div>
                <div className="home__donate-impact-item">
                  <strong>$25</strong> supports helpline directory maintenance
                </div>
                <div className="home__donate-impact-item">
                  <strong>$50</strong> helps develop new safety tools
                </div>
              </div>
              <Link to="/emergency/donations">
                <Button variant="primary" size="lg" className="home__donate-button">
                  Make a Donation
                </Button>
              </Link>
              <p className="home__donate-note">
                100% secure • Anonymous option available • No payment details stored
              </p>
            </div>
          </Card>
        </div>
      </section>
    </div>
  );
};
