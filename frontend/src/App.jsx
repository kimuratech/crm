import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import Sidebar from './components/Sidebar'
import Dashboard from './pages/Dashboard'
import Accounts from './pages/Accounts'
import Contacts from './pages/Contacts'
import Deals from './pages/Deals'
import DealDetail from './pages/DealDetail'
import DealForm from './pages/DealForm'
import Pipeline from './pages/Pipeline'

export default function App() {
  return (
    <div className="d-flex" style={{ minHeight: '100vh' }}>
      <Sidebar />
      <main className="flex-fill p-4 bg-light">
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/accounts" element={<Accounts />} />
          <Route path="/contacts" element={<Contacts />} />
          <Route path="/deals" element={<Deals />} />
          <Route path="/deals/new" element={<DealForm />} />
          <Route path="/deals/:id" element={<DealDetail />} />
          <Route path="/pipeline" element={<Pipeline />} />
        </Routes>
      </main>
    </div>
  )
}
