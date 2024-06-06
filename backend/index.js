import express from 'express';
import * as db from './db/index.js'
    
const app = express();
const port = 3000;


app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.get('/api/v1/utvikling', (req, res) => {
    res.send('utvikling');
});

app.get('/api/v1/drift', (req, res) => {
    res.send('drift');
});


app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});