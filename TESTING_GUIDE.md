# ShieldHer - Local Testing Guide

## ✅ Development Environment Status

**Both servers are running successfully!**

- **Backend (Django)**: http://127.0.0.1:8000/
- **Frontend (React)**: http://localhost:3000/

## 🔐 Admin Credentials

- **Email**: admin@shieldher.com
- **Username**: admin
- **Password**: admin123

## 🧪 Testing Checklist

### 1. Frontend Homepage
**URL**: http://localhost:3000/

**What to test:**
- [ ] Page loads without errors
- [ ] Navigation menu is visible
- [ ] "Quick Exit" button appears (safety feature)
- [ ] Hero section displays correctly
- [ ] Feature cards are visible

### 2. Digital Literacy Lessons
**URL**: http://localhost:3000/lessons

**What to test:**
- [ ] Lessons page loads
- [ ] 3 sample lessons are displayed:
  - Understanding Digital Privacy (Beginner, 15 min)
  - Recognizing Online Harassment (Beginner, 20 min)
  - Securing Your Social Media (Intermediate, 25 min)
- [ ] Lesson cards show category, difficulty, and duration
- [ ] Click on a lesson card (should navigate to lesson detail)

### 3. Emergency Resources
**URL**: http://localhost:3000/resources

**What to test:**
- [ ] Resources page loads
- [ ] 3 sample resources are displayed:
  - National Domestic Violence Hotline
  - Cyber Civil Rights Initiative
  - RAINN - National Sexual Assault Hotline
- [ ] Resource cards show descriptions
- [ ] External links work (if implemented)

### 4. Anonymous Reporting
**URL**: http://localhost:3000/report

**What to test:**
- [ ] Report page loads
- [ ] "Quick Exit" button is prominently displayed
- [ ] "Hide from browser history" toggle is available
- [ ] Report form is visible with fields:
  - Incident type
  - Description
  - Date/time
  - Location (optional)
- [ ] Form submission works (creates anonymous report)
- [ ] No personal information is required

### 5. Backend API Endpoints

**Health Check**:
```bash
curl http://127.0.0.1:8000/api/health/
```
Expected: `{"status": "healthy"}`

**List Lessons**:
```bash
curl http://127.0.0.1:8000/api/lessons/
```
Expected: JSON array with 3 lessons

**List Resources**:
```bash
curl http://127.0.0.1:8000/api/resources/
```
Expected: JSON array with 3 resources

**List Helplines**:
```bash
curl http://127.0.0.1:8000/api/resources/helplines/
```
Expected: JSON array with 2 helplines

### 6. Admin Panel
**URL**: http://127.0.0.1:8000/admin/

**What to test:**
- [ ] Admin login page loads
- [ ] Login with credentials works
- [ ] Dashboard displays all models:
  - Admin Users
  - Lessons
  - Reports
  - Resources
  - Helplines
  - Donations
  - Audit Logs
- [ ] Can view sample lessons
- [ ] Can view sample resources
- [ ] Can view sample helplines

### 7. Privacy & Security Features

**Quick Exit Button**:
- [ ] Visible on all pages
- [ ] Clicking redirects to weather.com immediately
- [ ] Clears session storage

**History Hiding**:
- [ ] Toggle available on report page
- [ ] When enabled, prevents browser history tracking
- [ ] Shows confirmation message

**Anonymous Reporting**:
- [ ] No login required
- [ ] No email/name fields
- [ ] Generates confirmation code
- [ ] PII detection works (try entering email/phone in description)

## 🐛 Common Issues & Solutions

### Frontend won't load
- Check if frontend server is running on port 3000
- Check browser console for errors
- Verify `.env` file exists in `frontend/` directory

### Backend API errors
- Check if backend server is running on port 8000
- Verify database migrations completed
- Check backend console for error messages

### CORS errors in browser
- Verify `CORS_ALLOW_ALL_ORIGINS = True` in development settings
- Check backend is running on port 8000
- Check frontend `.env` has `VITE_API_URL=http://localhost:8000`

### Database errors
- Delete `backend/db.sqlite3` and run migrations again:
  ```bash
  cd backend
  .\venv\Scripts\activate
  python manage.py migrate
  python load_sample_data.py
  ```

## 📊 API Testing with Postman/Thunder Client

### Create Anonymous Report
**POST** `http://127.0.0.1:8000/api/reports/`

**Body** (JSON):
```json
{
  "incident_type": "cyberbullying",
  "description": "Someone is posting harmful content about me online",
  "incident_date": "2025-11-29",
  "location": "Social Media",
  "severity": "medium"
}
```

**Expected Response**: 201 Created with confirmation code

### Get Lesson Detail
**GET** `http://127.0.0.1:8000/api/lessons/1/`

**Expected Response**: 200 OK with lesson details

## 🎯 Key Features to Verify

### Privacy-First Design
- [ ] No user accounts required for public features
- [ ] Anonymous reporting works without login
- [ ] No tracking cookies
- [ ] PII detection in reports
- [ ] Field-level encryption (check admin panel)

### Accessibility
- [ ] Keyboard navigation works
- [ ] Screen reader compatible (test with NVDA/JAWS)
- [ ] Sufficient color contrast
- [ ] Touch targets are 44px minimum
- [ ] Alt text on images

### Mobile Responsiveness
- [ ] Test on mobile viewport (Chrome DevTools)
- [ ] Navigation menu adapts to mobile
- [ ] Forms are usable on small screens
- [ ] Quick Exit button accessible on mobile

## 📝 Test Results Template

```
Date: ___________
Tester: ___________

Frontend Tests:
- Homepage: ☐ Pass ☐ Fail
- Lessons: ☐ Pass ☐ Fail
- Resources: ☐ Pass ☐ Fail
- Reporting: ☐ Pass ☐ Fail

Backend Tests:
- API Health: ☐ Pass ☐ Fail
- Lessons API: ☐ Pass ☐ Fail
- Resources API: ☐ Pass ☐ Fail
- Admin Panel: ☐ Pass ☐ Fail

Privacy Features:
- Quick Exit: ☐ Pass ☐ Fail
- History Hiding: ☐ Pass ☐ Fail
- Anonymous Reporting: ☐ Pass ☐ Fail

Issues Found:
1. ___________
2. ___________
3. ___________
```

## 🚀 Next Steps After Testing

1. **Document Issues**: Note any bugs or problems found
2. **Test Edge Cases**: Try invalid inputs, long text, special characters
3. **Performance Testing**: Check page load times, API response times
4. **Security Testing**: Verify PII detection, encryption, rate limiting
5. **Accessibility Audit**: Use tools like axe DevTools, Lighthouse
6. **Cross-Browser Testing**: Test in Chrome, Firefox, Safari, Edge

## 📞 Support

If you encounter issues:
1. Check the browser console for errors
2. Check backend terminal for error messages
3. Review the `DEPLOYMENT_PLAN.md` for troubleshooting
4. Check Django logs in backend console

---

**Happy Testing! 🎉**

Remember: This platform serves survivors of digital violence. Every feature should prioritize their safety, privacy, and well-being.
