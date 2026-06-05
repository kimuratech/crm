import React, { useEffect, useState, useRef } from 'react'
import client from '../api/client'
import { Modal } from 'bootstrap'

export default function Accounts() {
  const [accounts, setAccounts] = useState([])
  const [loading, setLoading] = useState(true)
  const [selected, setSelected] = useState(null)
  const modalRef = useRef(null)

  useEffect(() => {
    let mounted = true
    client
      .get('accounts/')
      .then((r) => {
        if (mounted) setAccounts(r.data || [])
      })
      .catch(() => {})
      .finally(() => mounted && setLoading(false))
    return () => {
      mounted = false
    }
  }, [])

  function openDetails(account) {
    setSelected(account)
    // show bootstrap modal
    const el = modalRef.current
    if (el) {
      const m = new Modal(el)
      m.show()
    }
  }

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h1>Accounts</h1>
      </div>

      {loading ? (
        <div>Loading…</div>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>Name</th>
                <th>Website</th>
                <th>Phone</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {accounts.map((a) => (
                <tr key={a.id}>
                  <td>{a.name}</td>
                  <td>{a.website}</td>
                  <td>{a.phone}</td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary" onClick={() => openDetails(a)}>
                      Details
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Modal */}
      <div className="modal fade" tabIndex="-1" ref={modalRef} id="accountModal" aria-hidden="true">
        <div className="modal-dialog modal-lg modal-dialog-centered">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title">{selected?.name || 'Account'}</h5>
              <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              {selected ? (
                <div>
                  <p><strong>Website:</strong> {selected.website}</p>
                  <p><strong>Phone:</strong> {selected.phone}</p>
                  <p><strong>Address:</strong> {selected.address || '—'}</p>
                  <p><strong>Notes:</strong> {selected.notes || '—'}</p>
                </div>
              ) : (
                <div>Loading…</div>
              )}
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">
                Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
