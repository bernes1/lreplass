import express from 'express';
import * as db from './db/index.js';
import cors from 'cors';

const app = express();
const port = 3000;

app.use(cors());

// Helper function to get pagination parameters
const getPagination = (page, limit) => {
  const offset = (page - 1) * limit;
  return { limit, offset };
};

// Helper function to get total items count
const getTotalItems = async (position) => {
  const result = await db.pool.query('SELECT COUNT(*) FROM job_listings WHERE position = $1', [position]);
  return parseInt(result.rows[0].count, 10);
};

// Public route
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Protected route with pagination
app.get('/api/v1/utvikling', async (req, res) => {
  const position = 'IT-Utvikling';
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const { limit: queryLimit, offset } = getPagination(page, limit);

  try {
    const totalItems = await getTotalItems(position);
    const result = await db.pool.query('SELECT * FROM job_listings WHERE position = $1 LIMIT $2 OFFSET $3', [position, queryLimit, offset]);
    const totalPages = Math.ceil(totalItems / limit);

    res.status(200).json({
      data: result.rows,
      pagination: {
        totalItems,
        totalPages,
        currentPage: page,
        itemsPerPage: limit
      }
    });
  } catch (err) {
    console.error('Error executing query', err.stack);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Another protected route with pagination
app.get('/api/v1/drift', async (req, res) => {
  const position = 'IT-Drift';
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const { limit: queryLimit, offset } = getPagination(page, limit);

  try {
    const totalItems = await getTotalItems(position);
    const result = await db.pool.query('SELECT * FROM job_listings WHERE position = $1 LIMIT $2 OFFSET $3', [position, queryLimit, offset]);
    const totalPages = Math.ceil(totalItems / limit);

    res.status(200).json({
      data: result.rows,
      pagination: {
        totalItems,
        totalPages,
        currentPage: page,
        itemsPerPage: limit
      }
    });
  } catch (err) {
    console.error('Error executing query', err.stack);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});