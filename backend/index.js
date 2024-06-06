import express from 'express';
import * as db from './db/index.js'
import cors from 'cors'

const app = express();
const port = 3000;

app.use(cors())

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.get('/api/v1/utvikling', (req, res) => {
  const position = 'IT-Utvikling';
  db.pool.query('SELECT * FROM job_listings WHERE position = $1',[position] ,(err, result) => {
    if (err) {
      console.error('Error executing query', err.stack);
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    res.status(200).json(result.rows);
  });
});

app.get('/api/v1/drift', (req, res) => {
  const position = 'IT-Drift';
  db.pool.query('SELECT * FROM job_listings WHERE position = $1',[position] ,(err, result) => {
    if (err) {
      console.error('Error executing query', err.stack);
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    res.status(200).json(result.rows);
  });
});




app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});