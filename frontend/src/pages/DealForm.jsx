import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

export default function DealForm() {
  const [title, setTitle] = useState('')
  const [value, setValue] = useState('0')
  const [stage, setStage] = useState('prospect')
  const navigate = useNavigate()

  const handleSubmit = (e) => {
    e.preventDefault()
    fetch('/api/deals/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, value, stage }),
    })
      .then((r) => r.json())
      .then((data) => navigate(`/deals/${data.id}`))
      .catch(() => alert('Failed to create deal'))
  }

  return (
    <div>
      <h2>New Deal</h2>
      <form onSubmit={handleSubmit} className="mt-3">
        <div className="mb-3">
          <label className="form-label">Title</label>
          <input className="form-control" value={title} onChange={(e) => setTitle(e.target.value)} required />
        </div>
        <div className="mb-3">
          <label className="form-label">Value</label>
          <input className="form-control" value={value} onChange={(e) => setValue(e.target.value)} type="number" />
        </div>
        <div className="mb-3">
          <label className="form-label">Stage</label>
          <select className="form-select" value={stage} onChange={(e) => setStage(e.target.value)}>
            <option value="prospect">Prospect</option>
            <option value="proposal">Proposal</option>
            <option value="closed">Closed</option>
          </select>
        </div>
        <button className="btn btn-primary" type="submit">Create</button>
      </form>
    </div>
  )
}
