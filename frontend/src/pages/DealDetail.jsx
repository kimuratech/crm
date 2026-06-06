import React, { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'

export default function DealDetail() {
  const { id } = useParams()
  const [deal, setDeal] = useState(null)

  useEffect(() => {
    fetch(`/api/deals/${id}/`)
      .then((r) => r.json())
      .then((data) => setDeal(data))
      .catch(() => setDeal(null))
  }, [id])

  if (!deal) return <div>Loading...</div>

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h2>{deal.title}</h2>
        <Link to="/deals" className="btn btn-secondary">Back</Link>
      </div>
      <dl className="row">
        <dt className="col-sm-3">Account</dt>
        <dd className="col-sm-9">{deal.account || '-'}</dd>

        <dt className="col-sm-3">Value</dt>
        <dd className="col-sm-9">${deal.value}</dd>

        <dt className="col-sm-3">Stage</dt>
        <dd className="col-sm-9"><span className="badge bg-info">{deal.stage}</span></dd>

        <dt className="col-sm-3">ID</dt>
        <dd className="col-sm-9">{deal.id}</dd>
      </dl>
    </div>
  )
}
