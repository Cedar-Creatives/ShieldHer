/**
 * LessonDetailPage - Display individual lesson content
 */

import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useLesson } from '../../hooks/useLessons';
import Card from '../../components/common/Card';
import Button from '../../components/common/Button';
import './LessonDetailPage.css';

export const LessonDetailPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { lesson, loading, error } = useLesson(id);

  if (loading) {
    return (
      <div className="lesson-detail">
        <div className="lesson-detail__loading">Loading lesson...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="lesson-detail">
        <div className="lesson-detail__error">
          <p>Error loading lesson: {error}</p>
          <Button onClick={() => navigate('/lessons')}>Back to Lessons</Button>
        </div>
      </div>
    );
  }

  if (!lesson) {
    return (
      <div className="lesson-detail">
        <div className="lesson-detail__error">
          <p>Lesson not found</p>
          <Button onClick={() => navigate('/lessons')}>Back to Lessons</Button>
        </div>
      </div>
    );
  }

  return (
    <div className="lesson-detail">
      <div className="lesson-detail__container">
        <Button 
          onClick={() => navigate('/lessons')} 
          className="lesson-detail__back"
        >
          ← Back to Lessons
        </Button>

        <Card className="lesson-detail__card">
          <header className="lesson-detail__header">
            <span className="lesson-detail__category">{lesson.category}</span>
            <h1 className="lesson-detail__title">{lesson.title}</h1>
            <p className="lesson-detail__description">{lesson.description}</p>
            
            <div className="lesson-detail__meta">
              <span>⏱️ {lesson.duration_minutes} minutes</span>
              <span>📊 {lesson.difficulty}</span>
            </div>
          </header>

          <div className="lesson-detail__content">
            {lesson.content && typeof lesson.content === 'object' && lesson.content.sections ? (
              lesson.content.sections.map((section, index) => (
                <section key={index} className="lesson-detail__section">
                  <h2>{section.title}</h2>
                  <p>{section.text}</p>
                </section>
              ))
            ) : (
              <p>{lesson.content || 'Lesson content coming soon...'}</p>
            )}
          </div>

          {lesson.quiz && lesson.quiz.length > 0 && (
            <div className="lesson-detail__quiz">
              <h2>Quiz</h2>
              <p>Quiz feature coming soon...</p>
            </div>
          )}
        </Card>
      </div>
    </div>
  );
};
