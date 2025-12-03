/**
 * LessonCard component
 * Displays lesson summary in card format
 */

import React from 'react';
import PropTypes from 'prop-types';
import Card from '../common/Card';
import './LessonCard.css';

const LessonCard = ({ lesson, progress, onClick }) => {
  const isCompleted = progress?.completed || false;
  const hasQuizScore = progress?.quizScore !== undefined;

  const getCategoryColor = (category) => {
    const colors = {
      privacy: '#ec4899',
      safety: '#a855f7',
      security: '#3b82f6',
      awareness: '#10b981',
    };
    return colors[category] || '#78716c';
  };

  const getDifficultyLabel = (difficulty) => {
    const labels = {
      beginner: 'Beginner',
      intermediate: 'Intermediate',
      advanced: 'Advanced',
    };
    return labels[difficulty] || difficulty;
  };

  return (
    <Card
      className="lesson-card"
      padding="md"
      shadow="md"
      hover
      onClick={onClick}
      as="article"
    >
      {lesson.thumbnail_url && (
        <div className="lesson-card__image">
          <img src={lesson.thumbnail_url} alt={lesson.title} />
        </div>
      )}
      
      <div className="lesson-card__content">
        <div className="lesson-card__header">
          <span
            className="lesson-card__category"
            style={{ backgroundColor: getCategoryColor(lesson.category) }}
          >
            {lesson.category}
          </span>
          {isCompleted && (
            <span className="lesson-card__badge lesson-card__badge--completed">
              ✓ Completed
            </span>
          )}
        </div>

        <h3 className="lesson-card__title">{lesson.title}</h3>
        <p className="lesson-card__description">{lesson.description}</p>

        {hasQuizScore && (
          <div className="lesson-card__quiz-score">
            Quiz Score: {progress.quizScore}/{progress.quizTotal}
          </div>
        )}
      </div>
    </Card>
  );
};

LessonCard.propTypes = {
  lesson: PropTypes.shape({
    id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    category: PropTypes.string.isRequired,
    difficulty: PropTypes.string.isRequired,
    duration_minutes: PropTypes.number.isRequired,
    thumbnail_url: PropTypes.string,
  }).isRequired,
  progress: PropTypes.object,
  onClick: PropTypes.func.isRequired,
};

export default LessonCard;
