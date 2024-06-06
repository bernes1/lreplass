import pg from 'pg'
import { dirname } from 'path';
import { fileURLToPath } from 'url';
import { resolve } from 'path';
import dotenv from 'dotenv';

// Get the directory name of the current module
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Resolve the path to two directories up and then into 'vars/.env'
const envPath = resolve(__dirname, '../../vars/.env');

//decaling that i want to use the pool module from pg
const { Pool } = pg

dotenv.config({path: envPath})

export const pool = new Pool({
  user: process.env.POSTGRES_USER, 
  password: process.env.POSTGRES_PASSWORD, 
  host: process.env.POSTGRES_SERVER,
  database: process.env.POSTGRES_DB,
  port: process.env.POSTGRES_PORT
})
