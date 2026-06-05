import React from 'react'
import { NavLink } from 'react-router-dom'

export default function Sidebar() {
  return (
    <aside className="bg-primary text-white d-flex flex-column p-3" style={{ width: 250 }}>
      <h4 className="text-white mb-4">CRM</h4>
      <nav className="nav nav-pills flex-column">
        <NavLink to="/dashboard" className="nav-link text-white" activeclassname="active">Dashboard</NavLink>
        <NavLink to="/accounts" className="nav-link text-white" activeclassname="active">Accounts</NavLink>
        <NavLink to="/contacts" className="nav-link text-white" activeclassname="active">Contacts</NavLink>
      </nav>
      <div className="mt-auto small text-white-50">Built with Vite + React</div>
    </aside>
  )
}
