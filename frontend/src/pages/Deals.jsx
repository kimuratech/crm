import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

export default function Deals() {
  const [deals, setDeals] = useState([])

  useEffect(() => {
    fetch('/api/deals/')
      .then((r) => r.json())
      .then((data) => setDeals(Array.isArray(data) ? data : data.results || []))
      .catch(() => setDeals([]))
  }, [])

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h2>Deals</h2>
        <Link to="/deals/new" className="btn btn-primary">New Deal</Link>
      </div>
      <div className="list-group">
        {deals.map((d) => (
          <Link key={d.id} to={`/deals/${d.id}`} className="list-group-item list-group-item-action">
            <div className="d-flex justify-content-between">
              <div>
                <strong>{d.title}</strong>
                <div className="small text-muted">{d.account ? d.account : ''}</div>
              </div>
              <div className="text-end">
                <div>${d.value}</div>
                <div className="badge bg-secondary">{d.stage}</div>
              </div>
            </div>
          </Link>
        ))}
        {deals.length === 0 && <div className="text-muted">No deals found.</div>}
      </div>
    </div>
  )
}
