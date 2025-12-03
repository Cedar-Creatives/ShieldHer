# Static Data Migration

## Overview

ShieldHer has been simplified to use static JSON files for lessons, helplines, and resources instead of database storage. This reduces complexity and makes deployment easier while keeping the database only for user-generated content (reports and donations).

## What Changed

### Now Using Static JSON Files:
- **Lessons** (`frontend/src/data/lessons.json`)
- **Helplines** (`frontend/src/data/helplines.json`)
- **Resources** (`frontend/src/data/resources.json`)

### Still Using Database:
- **Reports** - Anonymous incident reports (encrypted)
- **Donations** - Donation tracking (when implemented)

## Benefits

1. **Simpler Deployment** - No need to populate database with content
2. **Faster Performance** - No API calls for static content
3. **Easier Updates** - Edit JSON files directly
4. **Reduced Database Load** - Only user-generated content in DB
5. **Better for Static Hosting** - Can deploy frontend independently

## How to Update Content

### Updating Lessons

Edit `frontend/src/data/lessons.json`:

```json
{
  "id": 1,
  "title": "Lesson Title",
  "description": "Brief description",
  "category": "privacy",
  "difficulty": "beginner",
  "duration_minutes": 15,
  "content": {
    "sections": [
      {
        "title": "Section Title",
        "paragraphs": ["Paragraph 1", "Paragraph 2"]
      }
    ]
  },
  "quiz": [],
  "thumbnail_url": "",
  "created_at": "2025-12-03T00:00:00Z"
}
```

### Updating Helplines

Edit `frontend/src/data/helplines.json`:

```json
{
  "id": 1,
  "name": "Helpline Name",
  "phone_number": "1-800-XXX-XXXX",
  "description": "Description",
  "category": "crisis",
  "availability": "24/7",
  "is_24_7": true,
  "languages": ["English", "Spanish"]
}
```

### Updating Resources

Edit `frontend/src/data/resources.json`:

```json
{
  "id": 1,
  "title": "Resource Title",
  "description": "Brief description",
  "content": "Full content here",
  "category": "legal_rights",
  "resource_type": "article",
  "external_url": "",
  "tags": ["tag1", "tag2"],
  "created_at": "2025-12-03T00:00:00Z"
}
```

## Database Models Kept

### Reports Model
- Stores anonymous incident reports
- Encrypted descriptions
- No PII collected
- Essential for the app's core functionality

### Donations Model
- Tracks donations (when frontend is implemented)
- Optional donor information
- Payment processor integration
- Needed for financial transparency

## Migration Script

If you need to export current database data to JSON files:

```bash
cd backend
python export_to_json.py
```

This will create/update the JSON files in `frontend/src/data/`.

## Deployment Notes

### Frontend Deployment
- No database connection needed
- Can deploy to static hosting (Netlify, Vercel, etc.)
- JSON files are bundled with the app

### Backend Deployment
- Only needs database for Reports and Donations
- Smaller database footprint
- Faster startup time

## Reverting to Database (If Needed)

If you need to move back to database storage:

1. Keep the models in `backend/apps/lessons`, `backend/apps/resources`
2. Restore the API endpoints in views
3. Update frontend hooks to use API calls instead of JSON imports
4. Run migrations to create tables
5. Import data from JSON files using Django management commands

## File Structure

```
frontend/src/
├── data/
│   ├── lessons.json      # Static lesson content
│   ├── helplines.json    # Static helpline data
│   └── resources.json    # Static resource data
├── hooks/
│   ├── useLessons.js     # Uses static JSON
│   ├── useHelplines.js   # Uses static JSON
│   └── useResources.js   # Uses static JSON
└── ...

backend/
├── apps/
│   ├── reports/          # Database model (kept)
│   ├── donations/        # Database model (kept)
│   ├── lessons/          # Models kept but not used
│   └── resources/        # Models kept but not used
└── export_to_json.py     # Export script
```

## Testing

After migration, test:

1. **Lessons Page** - http://localhost:3000/lessons
   - Should load lessons from JSON
   - Click on lesson to view details
   
2. **Helplines Page** - http://localhost:3000/emergency/helplines
   - Should load helplines from JSON
   - Search and filter should work
   
3. **Resources Page** - http://localhost:3000/emergency/resources
   - Should load resources from JSON
   - Category tabs should work
   
4. **Reports** - http://localhost:3000/report
   - Should still submit to database
   - Check backend logs for confirmation

## Performance Impact

- **Before**: 3 API calls on page load (lessons, helplines, resources)
- **After**: 0 API calls (data bundled with app)
- **Result**: Faster page loads, no loading spinners for static content
