import pg from 'pg'
import dotenv from 'dotenv'
const { Pool } = pg

dotenv.config({path: '../../vars/.env'})
console.log(process.env)

export const pool = new Pool({
  user: process.env.POSTGRES_USER, 
  password: process.env.POSTGRES_PASSWORD, 
  host: process.env.POSTGRES_SERVER,
  database: process.env.POSTGRES_DB,
  port: process.env.POSTGRES_PORT
})
