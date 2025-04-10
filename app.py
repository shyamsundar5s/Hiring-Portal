import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [jobs, setJobs] = useState([]);
  const [filters, setFilters] = useState({ title: '', location: '', type: '' });

  const fetchJobs = async () => {
    const { data } = await axios.get('http://localhost:5000/jobs', { params: filters });
    setJobs(data);
  };

  useEffect(() => {
    fetchJobs();
  }, [filters]);

  return (
    <div>
      <h1>Hiring Portal</h1>
      <input placeholder="Job title" onChange={e => setFilters(f => ({ ...f, title: e.target.value }))} />
      <input placeholder="Location" onChange={e => setFilters(f => ({ ...f, location: e.target.value }))} />
      <select onChange={e => setFilters(f => ({ ...f, type: e.target.value }))}>
        <option value="">All Types</option>
        <option value="Full-Time">Full-Time</option>
        <option value="Part-Time">Part-Time</option>
      </select>

      <ul>
        {jobs.map(job => (
          <li key={job._id}>
            <h3>{job.title} - {job.company}</h3>
            <p>{job.location} | {job.type}</p>
            <p>{job.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
