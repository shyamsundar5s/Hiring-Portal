const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();

mongoose.connect('mongodb://localhost:27017/hiring-portal', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const JobSchema = new mongoose.Schema({
  title: String,
  company: String,
  location: String,
  type: String,
  description: String,
});

const Job = mongoose.model('Job', JobSchema);

app.use(cors());
app.use(express.json());

app.post('/jobs', async (req, res) => {
  const job = new Job(req.body);
  await job.save();
  res.status(201).send(job);
});

app.get('/jobs', async (req, res) => {
  const { title, location, type } = req.query;
  const filters = {};
  if (title) filters.title = new RegExp(title, 'i');
  if (location) filters.location = new RegExp(location, 'i');
  if (type) filters.type = type;

  const jobs = await Job.find(filters);
  res.send(jobs);
});

app.listen(5000, () => {
  console.log('Server running on port 5000');
});
