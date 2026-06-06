import React, { useEffect, useState } from 'react'

const STAGES = ['prospect', 'proposal', 'closed']

export default function Pipeline() {
  const [columns, setColumns] = useState({})

  useEffect(() => {
    fetch('/api/deals/')
      .then((r) => r.json())
      .then((data) => {
        const items = Array.isArray(data) ? data : data.results || []
        const cols = {}
        STAGES.forEach((s) => (cols[s] = items.filter((i) => (i.stage || 'prospect').toLowerCase() === s)))
        setColumns(cols)
      })
  }, [])

  return (
    <div>
      <h2>Pipeline</h2>
      <div className="row">
        {STAGES.map((s) => (
          <div key={s} className="col">
            <div className="card">
              <div className="card-header text-capitalize">{s}</div>
              <ul className="list-group list-group-flush">
                {(columns[s] || []).map((d) => (
                  <li key={d.id} className="list-group-item d-flex justify-content-between align-items-center">
                    <div>
                      <strong>{d.title}</strong>
                      <div className="small text-muted">${d.value}</div>
                    </div>
                    <div className="badge bg-secondary">{d.stage}</div>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
