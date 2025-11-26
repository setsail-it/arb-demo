# HTML Files for Blog Posts

This directory stores HTML files for blog post artifacts.

## File Naming Convention

HTML files should be named using the following pattern:

```
client_{client_id}_idea_{blog_idea_id}.html
```

Or for versioned HTML:

```
client_{client_id}_idea_{blog_idea_id}_v{version}.html
```

## Examples

- **Setsail (client_id=2)**:
  - `client_2_idea_1.html` - Blog idea ID 1
  - `client_2_idea_2.html` - Blog idea ID 2
  - `client_2_idea_3.html` - Blog idea ID 3

- **CleanDesign.ca (client_id=7)**:
  - `client_7_idea_1.html` - Blog idea ID 1

- **Versioned files**:
  - `client_2_idea_1_v1.html` - Setsail, blog idea ID 1, version 1
  - `client_7_idea_1_v2.html` - CleanDesign, blog idea ID 1, version 2

## How It Works

1. When a blog idea is processed and completed, the frontend will request HTML via `/clients/{client_id}/blog-ideas/{blog_idea_id}/html`
2. The backend will look for a file matching the naming pattern above
3. If a versioned file exists (e.g., `_v1.html`), it will be used
4. Otherwise, it will fall back to the non-versioned file (e.g., `.html`)
5. If no file exists, it will return a default placeholder HTML

## Adding HTML Files

Simply create a new `.html` file in this directory following the naming convention above. The file should contain the complete HTML content for the blog post.

